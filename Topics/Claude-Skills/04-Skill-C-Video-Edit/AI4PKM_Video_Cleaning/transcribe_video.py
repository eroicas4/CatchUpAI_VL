#!/usr/bin/env python3
"""
Video Transcription Tool with Word-Level Timestamps

Extracts audio from video files and transcribes them using OpenAI Whisper API
with word-level and segment-level timestamps for video editing.

Now supports chunking for long videos to bypass API file size limits.

Usage:
    python transcribe_video.py <video_file> [options]

Options:
    --output-dir <dir>     Output directory (default: same as video)
    --keep-audio           Keep extracted audio file(s)
    --language <lang>      Language code for transcription (default: ko)
    --chunk-duration <sec> Chunk duration in seconds for long videos (default: 1200)
"""

import argparse
import json
import os
import subprocess
import sys
import math
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
from openai import OpenAI


def get_video_duration(video_path: str) -> float:
    """Get video duration in seconds using ffprobe."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(result.stdout)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error getting video duration with ffprobe: {e}", file=sys.stderr)
        return 0.0


def extract_audio_chunk(video_path: str, output_path: str, start: float, duration: float) -> bool:
    """Extract a chunk of audio from a video file."""
    try:
        cmd = [
            'ffmpeg', '-y',
            '-ss', str(start),
            '-i', video_path,
            '-t', str(duration),
            '-vn',
            '-acodec', 'aac',
            '-ab', '64k',
            output_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error extracting audio chunk: {result.stderr}", file=sys.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False


def transcribe_audio(audio_path: str, language: str = "ko") -> dict:
    """Transcribe audio using OpenAI Whisper API with word-level timestamps."""
    try:
        client = OpenAI()
        print(f"Transcribing audio with Whisper API (language: {language})...")
        with open(audio_path, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",
                timestamp_granularities=["word", "segment"],
                language=language
            )
        print("Transcription successful for chunk.")
        return response.model_dump()
    except Exception as e:
        print(f"Error during transcription: {e}", file=sys.stderr)
        return None


def format_timestamp(seconds: float) -> str:
    """Format seconds to HH:MM:SS.mmm"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"


def create_markdown_transcript(transcript_data: dict, video_name: str, video_path: str) -> str:
    # This function remains the same as before
    lines = []
    date = datetime.now().strftime("%Y-%m-%d")
    lines.append("---")
    lines.append(f"title: {video_name}")
    lines.append(f"date: {date}")
    lines.append(f"source: {video_path}")
    lines.append("tags:\n  - transcription\n  - video")
    lines.append("---\n")
    lines.append(f"# {video_name}\n")
    duration = transcript_data.get('duration', 0)
    lines.append(f"**Duration**: {format_timestamp(duration)}")
    lines.append(f"**Language**: {transcript_data.get('language', 'unknown')}\n")
    lines.append("## Transcript\n")
    segments = transcript_data.get('segments', [])
    for i, segment in enumerate(segments, 1):
        start = segment.get('start', 0)
        end = segment.get('end', 0)
        text = segment.get('text', '').strip()
        lines.append(f"### Segment {i} [{format_timestamp(start)} - {format_timestamp(end)}]\n")
        lines.append(text + "\n")
    lines.append("## Word-Level Timing Data\n")
    lines.append("For video editing reference, see the raw JSON file with word-level timestamps.\n")
    return "\n".join(lines)

def create_word_timing_text(transcript_data: dict) -> str:
    # This function remains the same as before
    lines = []
    lines.append("# Word-Level Timing\n# Format: [start-end] word\n")
    words = transcript_data.get('words', [])
    for word_data in words:
        word = word_data.get('word', '')
        start = word_data.get('start', 0)
        end = word_data.get('end', 0)
        lines.append(f"[{format_timestamp(start)}-{format_timestamp(end)}] {word}")
    return "\n".join(lines)


def main():
    start_time = datetime.now()
    print(f"Transcription process started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    parser = argparse.ArgumentParser(description="Transcribe video with word-level timestamps and chunking.")
    parser.add_argument("video_file", help="Path to video file")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: same as video)")
    parser.add_argument("--language", default="ko", help="Language code (default: ko)")
    parser.add_argument("--keep-audio", action="store_true", help="Keep extracted audio files")
    parser.add_argument("--chunk-duration", type=int, default=1200, help="Chunk duration for long videos (seconds)")

    args = parser.parse_args()

    video_path = Path(args.video_file)
    if not video_path.exists():
        print(f"Error: Video file not found: {args.video_file}", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir) if args.output_dir else video_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    video_name = video_path.stem

    json_path = output_dir / f"{video_name} - transcript.json"
    md_path = output_dir / f"{video_name} - transcript.md"
    words_path = output_dir / f"{video_name} - word_timings.txt"

    total_duration = get_video_duration(str(video_path))
    if total_duration == 0: return 1

    print(f"Total video duration: {format_timestamp(total_duration)}")
    
    # --- Chunking Logic ---
    chunk_duration = args.chunk_duration
    if total_duration <= chunk_duration:
        print("Video is short. Processing as a single file.")
        audio_path = output_dir / f"{video_name}_audio.m4a"
        if not extract_audio_chunk(str(video_path), str(audio_path), 0, total_duration):
            return 1
        
        transcript_data = transcribe_audio(str(audio_path), args.language)
        if not transcript_data: return 1
        
        if not args.keep_audio:
            audio_path.unlink()
    else:
        print(f"Video is long, processing in chunks of {chunk_duration}s...")
        num_chunks = math.ceil(total_duration / chunk_duration)
        chunk_temp_dir = tempfile.mkdtemp(prefix="audio_chunks_")
        
        all_words = []
        all_segments = []
        full_text = ""

        try:
            for i in range(num_chunks):
                chunk_start = i * chunk_duration
                current_chunk_duration = min(chunk_duration, total_duration - chunk_start)
                print(f"\n--- Processing Chunk {i+1}/{num_chunks} ({format_timestamp(chunk_start)}) ---")
                
                chunk_audio_path = os.path.join(chunk_temp_dir, f"chunk_{i}.m4a")
                
                if not extract_audio_chunk(str(video_path), chunk_audio_path, chunk_start, current_chunk_duration):
                    continue

                chunk_transcript = transcribe_audio(chunk_audio_path, args.language)
                if not chunk_transcript:
                    print(f"Skipping chunk {i+1} due to transcription error.")
                    continue

                # Adjust timestamps and collect results
                if 'words' in chunk_transcript:
                    for word in chunk_transcript['words']:
                        word['start'] += chunk_start
                        word['end'] += chunk_start
                        all_words.append(word)
                
                if 'segments' in chunk_transcript:
                    for segment in chunk_transcript['segments']:
                        segment['start'] += chunk_start
                        segment['end'] += chunk_start
                        all_segments.append(segment)
                
                full_text += chunk_transcript.get('text', '')

            # Combine results into a single transcript dictionary
            transcript_data = {
                "text": full_text,
                "language": args.language,
                "duration": total_duration,
                "words": all_words,
                "segments": all_segments
            }

        finally:
            if os.path.exists(chunk_temp_dir):
                shutil.rmtree(chunk_temp_dir)
                print("\nCleaned up temporary audio chunks.")

    if not transcript_data:
        print("Transcription failed for all chunks.", file=sys.stderr)
        return 1

    # --- Save all outputs ---
    print(f"\nSaving combined transcript to {json_path}...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(transcript_data, f, ensure_ascii=False, indent=2)

    print("Creating formatted transcript...")
    markdown = create_markdown_transcript(transcript_data, video_name, str(video_path))
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

    word_timings = create_word_timing_text(transcript_data)
    with open(words_path, 'w', encoding='utf-8') as f:
        f.write(word_timings)

    print("\nTranscription complete!")
    print(f"  JSON: {json_path}")
    print(f"  Markdown: {md_path}")
    print(f"  Word timings: {words_path}")

    end_time = datetime.now()
    total_duration = end_time - start_time
    print("="*60)
    print(f"Transcription finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total processing time: {total_duration}")
    print("="*60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
