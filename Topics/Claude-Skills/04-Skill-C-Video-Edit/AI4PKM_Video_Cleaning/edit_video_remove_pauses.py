#!/usr/bin/env python3
"""
Video Editor & Transcriber Pipeline

Analyzes word-level transcript to remove long pauses and Korean filler words
from video using FFmpeg for precise cuts. Can optionally run transcription first.

Usage:
    python edit_video_remove_pauses.py <video_file> [options]

Options:
    --transcribe               Run transcription first if JSON is missing.
    --transcript <path>        Path to transcript JSON (default: auto-detect)
    --pause-threshold <sec>    Minimum pause length to remove (default: 1.0)
    --padding <sec>            Padding around cuts (default: 0.1)
    --preview                  Show what would be removed without editing
    --output <path>            Output file path (default: <input>_edited.mov)
    --no-fillers               Skip filler word removal (only remove pauses)
    --chunk-duration <sec>     Chunk duration for long videos (default: 1800)
"""

import argparse
import json
import sys
import os
import subprocess
import math
import shutil
import tempfile
from pathlib import Path
from typing import List, Tuple, Dict
from datetime import datetime

# Import the main function from the transcription script
try:
    from transcribe_video import main as run_transcription
except ImportError:
    print("Error: transcribe_video.py not found. Make sure it's in the same directory.", file=sys.stderr)
    run_transcription = None


# Korean clear filler words (unambiguous)
CLEAR_FILLERS = ['어', '음', '아', '이', '오', '저']


def get_video_duration(video_path: str) -> float:
    # ... (function remains the same)
    cmd = [ "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(result.stdout)
    except Exception as e:
        print(f"Error getting video duration: {e}", file=sys.stderr)
        return 0.0

def load_transcript(json_path: str) -> dict:
    # ... (function remains the same)
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def identify_pauses(words: List[dict], threshold: float) -> List[Tuple[float, float, float]]:
    # ... (function remains the same)
    pauses = []
    for i in range(len(words) - 1):
        current_end = words[i]['end']
        next_start = words[i + 1]['start']
        pause_duration = next_start - current_end
        if pause_duration >= threshold:
            pauses.append((current_end, next_start, pause_duration))
    return pauses

def identify_filler_words(words: List[dict]) -> List[Dict]:
    # ... (function remains the same)
    filler_instances = []
    for i, word_data in enumerate(words):
        word = word_data['word'].strip()
        if word in CLEAR_FILLERS:
            filler_instances.append({'index': i, 'word': word, 'start': word_data['start'], 'end': word_data['end']})
    return filler_instances

def generate_keep_segments(
    words: List[dict],
    pauses: List[Tuple[float, float, float]],
    fillers: List[Dict],
    padding: float = 0.1,
    tail_buffer: float = 0.15
) -> List[Tuple[float, float, float]]:
    # ... (function is correct now)
    if not words: return []
    remove_ranges = []
    for pause_start, pause_end, pause_duration in pauses:
        remove_ranges.append((pause_start, pause_end, 'pause', pause_duration))
    for filler in fillers:
        remove_ranges.append((filler['start'], filler['end'], 'filler', 0))
    remove_ranges.sort(key=lambda x: x[0])
    merged_removes = []
    if remove_ranges:
        for start, end, rtype, duration in remove_ranges:
            if merged_removes and start <= merged_removes[-1][1]:
                prev_start, prev_end, prev_type, prev_duration = merged_removes[-1]
                new_type = 'filler' if (prev_type == 'filler' or rtype == 'filler') else 'pause'
                new_duration = max(prev_duration, duration) if new_type == 'pause' else 0
                merged_removes[-1] = (prev_start, max(prev_end, end), new_type, new_duration)
            else:
                merged_removes.append((start, end, rtype, duration))
    keep_segments = []
    current_time = 0.0
    preceding_pause = 0
    for remove_start, remove_end, remove_type, remove_duration in merged_removes:
        if current_time < remove_start:
            segment_end = remove_start if remove_type != 'pause' else remove_start + tail_buffer
            keep_segments.append((current_time, segment_end, preceding_pause))
        preceding_pause = remove_duration if remove_type == 'pause' else 0
        current_time = remove_end + padding
    video_end = words[-1]['end'] if words else 0
    if current_time < video_end:
        keep_segments.append((current_time, video_end, preceding_pause))
    return [(s, e, p) for s, e, p in keep_segments if e - s >= 0.1]

def format_time(seconds: float) -> str:
    # ... (function remains the same)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"

def edit_video_with_ffmpeg(video_path: str, keep_segments: List[Tuple[float, float, float]], output_path: str, skip_indicator: float = 5.0) -> bool:
    # ... (function remains the same)
    temp_dir = tempfile.mkdtemp(prefix="video_edit_segments_")
    success = False
    try:
        segment_files = []
        for i, (start, end, pause_duration) in enumerate(keep_segments):
            segment_file = os.path.join(temp_dir, f"segment_{i:04d}.mp4")
            duration = end - start
            cmd = ["ffmpeg", "-y", "-ss", str(start), "-i", video_path, "-t", str(duration), "-c:v", "libx264", "-preset", "superfast", "-c:a", "aac", "-avoid_negative_ts", "make_zero", segment_file]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0: raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)
            segment_files.append(segment_file)
        concat_file = os.path.join(temp_dir, "concat_list.txt")
        with open(concat_file, 'w') as f:
            for seg_file in segment_files: f.write(f"file '{os.path.basename(seg_file)}'\n")
        concat_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_file, "-c", "copy", output_path]
        result = subprocess.run(concat_cmd, capture_output=True, text=True, cwd=temp_dir)
        if result.returncode != 0: raise subprocess.CalledProcessError(result.returncode, concat_cmd, output=result.stdout, stderr=result.stderr)
        success = True
    except Exception as e:
        print(f"An error occurred during FFmpeg processing: {e}", file=sys.stderr)
    finally:
        if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
    return success

def generate_report(pauses: List[Tuple[float, float, float]], fillers: List[Dict], keep_segments: List[Tuple[float, float, float]], original_duration: float, output_path: str):
    # ... (function remains the same)
    edited_duration = sum(end - start for start, end, _ in keep_segments)
    time_saved = original_duration - edited_duration if original_duration > 0 else 0
    lines = ["="*60, "VIDEO EDIT REPORT", "="*60, "", "SUMMARY", "-"*60]
    lines.append(f"Original Duration:  {format_time(original_duration)}")
    lines.append(f"Edited Duration:    {format_time(edited_duration)}")
    if original_duration > 0: lines.append(f"Time Saved:         {format_time(time_saved)} ({time_saved/original_duration*100:.1f}%)")
    lines.append(f"Segments Kept:      {len(keep_segments)}\n")
    report_text = "\n".join(lines)
    print("\n" + report_text)
    report_file = str(Path(output_path).with_name(f"{Path(output_path).stem}_edit_report.txt"))
    with open(report_file, 'w', encoding='utf-8') as f: f.write(report_text)
    print(f"\nReport saved to: {report_file}")

def process_chunk(chunk_video_path: str, chunk_words: List[dict], args: argparse.Namespace, chunk_index: int, chunk_start_time: float) -> str:
    # ... (function remains the same)
    print(f"\n--- Processing Chunk {chunk_index+1} ({format_time(chunk_start_time)}) ---")
    relative_words = [{'word': w['word'], 'start': w['start'] - chunk_start_time, 'end': w['end'] - chunk_start_time} for w in chunk_words]
    pauses = identify_pauses(relative_words, args.pause_threshold)
    fillers = [] if args.no_fillers else identify_filler_words(relative_words)
    keep_segments = generate_keep_segments(relative_words, pauses, fillers, args.padding)
    if not keep_segments:
        print("No content to keep in this chunk.")
        return None
    chunk_output_path = chunk_video_path.replace(".mp4", "_edited.mp4")
    print(f"Editing chunk {chunk_index + 1}...")
    success = edit_video_with_ffmpeg(chunk_video_path, keep_segments, chunk_output_path, args.skip_indicator)
    if success:
        print(f"Chunk {chunk_index + 1} processed successfully.")
        return chunk_output_path
    else:
        print(f"Failed to process chunk {chunk_index + 1}.", file=sys.stderr)
        return None

def main():
    start_time = datetime.now()
    print(f"Pipeline started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    parser = argparse.ArgumentParser(description="Full pipeline for video transcription and editing.")
    parser.add_argument("video_file", help="Path to video file")
    parser.add_argument("--transcribe", action="store_true", help="Run transcription first if JSON is missing.")
    parser.add_argument("--transcript", help="Path to transcript JSON (default: <video_name> - transcript.json)")
    parser.add_argument("--pause-threshold", type=float, default=1.0, help="Min pause length (seconds)")
    parser.add_argument("--padding", type=float, default=0.1, help="Padding around cuts (seconds)")
    parser.add_argument("--preview", action="store_true", help="Preview edits without saving video")
    parser.add_argument("--output", help="Output file path (default: <video_name>_edited.mkv)")
    parser.add_argument("--no-fillers", action="store_true", help="Skip filler word removal")
    parser.add_argument("--skip-indicator", type=float, default=5.0, help="Show 'Skipping X secs' overlay (0 to disable)")
    parser.add_argument("--chunk-duration", type=int, default=1800, help="Chunk duration for long videos (seconds)")
    parser.add_argument("--lang", default="ko", help="Language for transcription (default: ko)")

    args = parser.parse_args()

    video_path = Path(args.video_file)
    if not video_path.exists():
        print(f"Error: Video file not found: {args.video_file}", file=sys.stderr)
        return 1

    # Define transcript path
    if args.transcript:
        transcript_path = Path(args.transcript)
    else:
        # Auto-detect path consistent with transcribe_video.py
        transcript_path = video_path.parent / f"{video_path.stem} - transcript.json"

    # --- Transcription Step ---
    if args.transcribe:
        if not run_transcription:
            return 1 # Error already printed
        if not transcript_path.exists():
            print("="*60)
            print(f"Transcript not found. Running transcription for '{video_path.name}'...")
            print("="*60)
            # Simulate command-line args for the transcription script
            transcribe_args = [str(video_path), "--language", args.lang, "--output-dir", str(video_path.parent)]
            sys.argv = [sys.argv[0]] + transcribe_args
            try:
                if run_transcription() != 0:
                    print("Transcription failed. Aborting edit.", file=sys.stderr)
                    return 1
                print("\nTranscription complete. Proceeding to video editing...")
            finally:
                # Restore original sys.argv
                sys.argv = [sys.argv[0]] + sys.argv[1:]
        else:
            print("Transcript already exists. Skipping transcription.")

    # --- Editing Step ---
    if not transcript_path.exists():
        print(f"Error: Transcript not found at {transcript_path}", file=sys.stderr)
        print("Please provide a transcript or use the --transcribe flag.", file=sys.stderr)
        return 1
        
    print("\n" + "="*60)
    print("Starting video editing process...")
    print("="*60)

    output_path = args.output if args.output else str(video_path.with_name(f"{video_path.stem}_edited{video_path.suffix}"))
    total_duration = get_video_duration(str(video_path))
    if total_duration == 0: return 1

    print(f"Total video duration: {format_time(total_duration)}")
    all_words = load_transcript(str(transcript_path)).get('words', [])
    if not all_words:
        print("Error: No words in transcript.", file=sys.stderr)
        return 1

    if args.preview:
        pauses = identify_pauses(all_words, args.pause_threshold)
        fillers = [] if args.no_fillers else identify_filler_words(all_words)
        keep_segments = generate_keep_segments(all_words, pauses, fillers, args.padding)
        generate_report(pauses, fillers, keep_segments, total_duration, output_path)
        print("\n[PREVIEW MODE] No video was edited. Remove --preview to proceed.")
        return 0

    chunk_duration = args.chunk_duration
    if total_duration <= chunk_duration:
        print("Video is short. Processing as a single file.")
        pauses = identify_pauses(all_words, args.pause_threshold)
        fillers = [] if args.no_fillers else identify_filler_words(all_words)
        keep_segments = generate_keep_segments(all_words, pauses, fillers, args.padding)
        if not keep_segments:
            print("No content worth keeping after analysis.", file=sys.stderr)
            return 1
        success = edit_video_with_ffmpeg(str(video_path), keep_segments, output_path, args.skip_indicator)
        if success:
            generate_report(pauses, fillers, keep_segments, total_duration, output_path)
            print(f"\n✅ Success! Edited video saved to: {output_path}")
        else:
            print("\n❌ Failed to edit video.", file=sys.stderr)
        return 0 if success else 1

    print(f"\nVideo is longer than {chunk_duration}s, processing in chunks...")
    num_chunks = math.ceil(total_duration / chunk_duration)
    chunk_temp_dir = tempfile.mkdtemp(prefix="video_chunks_")
    edited_chunk_files = []

    try:
        for i in range(num_chunks):
            chunk_start = i * chunk_duration
            chunk_end = min((i + 1) * chunk_duration, total_duration)
            current_chunk_duration = chunk_end - chunk_start
            chunk_video_path = os.path.join(chunk_temp_dir, f"chunk_{i}.mp4")
            
            print(f"\nSplitting chunk {i+1}/{num_chunks}...")
            split_cmd = ["ffmpeg", "-y", "-ss", str(chunk_start), "-i", str(video_path), "-t", str(current_chunk_duration), "-c", "copy", chunk_video_path]
            subprocess.run(split_cmd, check=True, capture_output=True)

            chunk_words = [w for w in all_words if chunk_start <= w['start'] < chunk_end]
            if not chunk_words:
                print(f"No words in chunk {i+1}, skipping.")
                continue

            edited_chunk_path = process_chunk(chunk_video_path, chunk_words, args, i, chunk_start)
            if edited_chunk_path:
                edited_chunk_files.append(edited_chunk_path)

        if not edited_chunk_files:
            print("No chunks were successfully processed.", file=sys.stderr)
            return 1

        print(f"\nConcatenating {len(edited_chunk_files)} edited chunks...")
        concat_list_path = os.path.join(chunk_temp_dir, "edited_concat_list.txt")
        with open(concat_list_path, 'w', encoding='utf-8') as f:
            for path in edited_chunk_files:
                f.write(f"file '{path}'\n")

        concat_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list_path, "-c", "copy", output_path]
        result = subprocess.run(concat_cmd, check=True, capture_output=True, text=True)
        
        print("\n--- FINAL REPORT (CHUNKED) ---")
        edited_duration = get_video_duration(output_path)
        print(f"Original duration: {format_time(total_duration)}")
        print(f"Edited duration:   {format_time(edited_duration)}")
        if total_duration > 0:
            saved = total_duration - edited_duration
            print(f"Time saved:        {format_time(saved)} ({saved/total_duration*100:.1f}%)")

        print(f"\n✅ Success! Final video saved to: {output_path}")

    except Exception as e:
        print(f"\nAn error occurred during chunk processing: {e}", file=sys.stderr)
        return 1
    finally:
        if os.path.exists(chunk_temp_dir):
            shutil.rmtree(chunk_temp_dir)
            print("Cleaned up chunk temporary directory.")

    end_time = datetime.now()
    total_duration = end_time - start_time
    print("="*60)
    print(f"Pipeline finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total processing time: {total_duration}")
    print("="*60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
