# Video Cleaning - Quick Start

Transcribe and remove pauses/filler words from videos with a single command. Handles long videos automatically.

## Setup

```bash
# Install FFmpeg
# macOS: brew install ffmpeg
# Linux: sudo apt install ffmpeg
# Windows: Download from ffmpeg.org

# Install Python dependencies
pip install openai

# Set OpenAI API key
export OPENAI_API_KEY="your-key-here"
```

## Unified Workflow (New)

The process is now a single step. The script will automatically run transcription if needed.

```bash
# Transcribe and edit in one go
python edit_video_remove_pauses.py "my_video.mp4" --transcribe --no-fillers --pause-threshold 0.5
```

This command will:
1.  Check for `my_video - transcript.json`.
2.  If not found, it runs the transcription automatically.
3.  It then removes pauses longer than 0.5 seconds.

## Long Video Support

- ✅ **Automatic Chunking**: Videos longer than the `chunk-duration` are automatically split, processed, and merged.
- **Transcription**: Defaults to 20-minute chunks to avoid API limits.
- **Editing**: Defaults to 30-minute chunks for better performance.

## Common Options

```bash
# Run transcription and edit with a 0.8s pause threshold
python edit_video_remove_pauses.py "video.mp4" --transcribe --pause-threshold 0.8

# Change chunk size to 10 mins (600s) for potentially faster API responses
python edit_video_remove_pauses.py "long_video.mp4" --transcribe --chunk-duration 600

# Specify a different language for transcription
python edit_video_remove_pauses.py "video_en.mp4" --transcribe --lang "en"

# Just run editing (if transcript already exists)
python edit_video_remove_pauses.py "video.mp4" --no-fillers

# Custom output path
python edit_video_remove_pauses.py "video.mp4" --transcribe --output "cleaned.mp4"
```

## What Gets Removed

- ✅ Pauses longer than the `--pause-threshold`
- ✅ Korean filler words: 어, 음, 아, 이, 오, 저 (unless `--no-fillers` is used)

## Output Files

**After running the full pipeline**:
- `video - transcript.json` (complete data)
- `video - transcript.md` (formatted)
- `video - word_timings.txt` (reference)
- `video_edited.mkv` (cleaned video)
- `video_edited_edit_report.txt` (detailed report)

---

**New Workflow**: Run one command → Done!
