# Video Cleaning Skill v3.0

Automated video transcription and editing workflow that removes pauses and filler words. It uses the OpenAI Whisper API for transcription and a high-performance FFmpeg pipeline for editing.

**New in v3.0**:
- **Unified Pipeline**: Run transcription and editing with a single command.
- **Automatic Chunking**: Automatically handles long videos for both transcription and editing.

## When to Use This Skill

Use this skill when you need to:
- Clean up recorded presentations or talks by removing dead air and filler words.
- Process long videos (e.g., 1-2 hours) without manual splitting.
- Create polished videos from raw recordings.
- Process Korean language videos (default) or other languages.

## Requirements

- **FFmpeg**: Must be installed and accessible in your system's PATH.
- **Python 3.7+**: With `openai` package installed (`pip install openai`).
- **OpenAI API Key**: Set as an environment variable `OPENAI_API_KEY`.

## How It Works

This skill now uses a **unified pipeline model**.

### The Pipeline (`edit_video_remove_pauses.py`)
1.  **Transcript Check**: When run with `--transcribe`, it checks if a transcript file (`<video_name> - transcript.json`) exists.
2.  **Automatic Transcription (Optional)**: If the transcript is missing, it automatically calls the transcription logic (`transcribe_video.py`).
    - **Chunking**: If the video is long, it's split into temporary audio chunks (default: 20 mins) which are sent to the Whisper API individually to avoid file size limits.
    - **Timestamp Correction**: Timestamps from each chunk are adjusted to absolute time.
    - **Combination**: The results are combined into a single, complete JSON transcript file.
3.  **Video Editing**:
    - **Analysis**: The script loads the full transcript and identifies pauses and filler words.
    - **Chunking**: If the video is long, it's split into video chunks (default: 30 mins) for efficient processing.
    - **Segmenting**: For each chunk, it calculates which segments to *keep*.
    - **High-Performance Editing**: It uses pure FFmpeg to losslessly extract all "keep" segments into temporary files and then concatenates them. This is much faster than re-encoding.
    - **Final Assembly**: The edited chunks are concatenated to create the final video.

## Usage Guide

### Unified Workflow (Recommended)

The easiest way to use the skill is with the `--transcribe` flag, which handles everything.

```bash
# Transcribe and edit a video in one command, removing pauses > 0.5s
python edit_video_remove_pauses.py "my_presentation.mp4" --transcribe --no-fillers --pause-threshold 0.5
```

### Manual Two-Step Workflow

You can still run the steps separately if you need more control.

```bash
# Step 1: Transcribe the video (handles long videos automatically)
python transcribe_video.py "my_presentation.mp4"

# Step 2: Preview the edits
python edit_video_remove_pauses.py "my_presentation.mp4" --preview

# Step 3: Run the edit
python edit_video_remove_pauses.py "my_presentation.mp4"
```

## Command-Line Options

### `edit_video_remove_pauses.py` (Main Pipeline)

| Argument | Description | Default |
|---|---|---|
| `video_file` | Path to the video file to process. | (required) |
| `--transcribe`| If present, runs transcription automatically if the `.json` file is missing. | `False` |
| `--transcript` | Manually specify the path to the transcript JSON file. | Auto-detect |
| `--output` | Path for the final edited video. | `<video>_edited.mkv` |
| `--pause-threshold` | Minimum duration of a pause (in seconds) to be removed. | `1.0` |
| `--no-fillers`| Disables the removal of filler words. | `False` |
| `--padding` | Padding (in seconds) to add around cuts to avoid abrupt transitions. | `0.1` |
| `--chunk-duration`| Chunk size in seconds for editing long videos. | `1800` (30 mins) |
| `--lang` | Language code (e.g., "en", "ja") to pass to the transcription step. | `ko` |
| `--preview` | Show a report of what would be cut without creating a video. | `False` |

### `transcribe_video.py`

| Argument | Description | Default |
|---|---|---|
| `video_file` | Path to the video file to transcribe. | (required) |
| `--output-dir`| Directory to save transcript files. | Same as video |
| `--language` | Language code for transcription. | `ko` |
| `--chunk-duration` | Chunk size in seconds for transcribing long videos. | `1200` (20 mins) |
| `--keep-audio` | Prevents deletion of the temporary audio chunk files. | `False` |


## Technical Details

### High-Performance FFmpeg Editing

This version uses a pure `ffmpeg` implementation for maximum speed and quality.
- ✅ **Fast**: Instead of re-encoding the whole video, it performs two fast operations:
  1.  **Segment Extraction**: Uses `-c copy` to losslessly and quickly extract every "keep" segment into its own temporary file.
  2.  **Concatenation**: Uses the `concat` demuxer to combine all temporary segment files. This is also extremely fast as it doesn't re-encode.
- ✅ **No Quality Loss**: Because no re-encoding happens, the output quality is identical to the input.
- ✅ **Reliable**: Avoids complex library dependencies like MoviePy and potential version conflicts.

## Version History
- **v3.0 (2026-01)**
  - **Unified Pipeline**: Introduced `--transcribe` flag in `edit_video_remove_pauses.py` for a one-command workflow.
  - **Automatic Chunking**: Added robust, automatic handling of long videos for both transcription (to meet API limits) and editing (for performance).
  - **High-Performance Editing**: Replaced MoviePy with a pure `ffmpeg` (extract + concat) workflow, resulting in significant speed improvements and no quality loss.
  - **New Arguments**: Added `--chunk-duration` to both scripts and `--lang` to the editing script to control the pipeline.
- **v2.0** (2026-01): MoviePy migration for frame accuracy.
- **v1.0** (2024): Initial conservative mode release.

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│ VIDEO CLEANING WORKFLOW v3.0 - QUICK REFERENCE          │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ UNIFIED WORKFLOW (RECOMMENDED)                          │
│   python edit_video_remove_pauses.py "video.mp4" \      │
│     --transcribe --pause-threshold 0.5                   │
│   → Transcribes and edits in one step.                  │
│                                                          │
│ MANUAL WORKFLOW                                         │
│   1. python transcribe_video.py "video.mp4"             │
│   2. python edit_video_remove_pauses.py "video.mp4"     │
│                                                          │
│ KEY ARGUMENTS:                                          │
│   --transcribe             Run transcription if needed  │
│   --pause-threshold 0.8    Remove pauses > 0.8s         │
│   --no-fillers             Keep filler words            │
│   --chunk-duration 600     Process in 10-min chunks     │
│                                                          │
│ WHAT GETS REMOVED:                                      │
│   ✓ Pauses > threshold                                  │
│   ✓ Filler words (어,음,아...) unless --no-fillers is on │
│                                                          │
└─────────────────────────────────────────────────────────┘
```
