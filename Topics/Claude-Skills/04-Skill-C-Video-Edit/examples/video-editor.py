#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
통합 영상 편집 스크립트 (Video Editor)

이 스크립트는 영상/오디오 파일에서 무음 구간과 필러 단어를 자동으로 제거합니다.
- 무음 구간 감지 및 제거 (pydub)
- 필러 단어 감지 및 제거 (Whisper + FFmpeg)
- 통합 편집 및 보고서 생성

사용법:
    python video-editor.py <파일경로> [옵션]

예시:
    python video-editor.py video.mp4 --remove-silence
    python video-editor.py video.mp4 --remove-fillers --model base
    python video-editor.py video.mp4 --remove-silence --remove-fillers
    python video-editor.py video.mp4 --all --output edited.mp4

옵션:
    --remove-silence: 무음 구간 제거
    --remove-fillers: 필러 단어 제거 (Whisper 필요)
    --all: 무음 + 필러 모두 제거
    --threshold: 무음 판단 임계값 (dB), 기본값: -40
    --min-silence: 최소 무음 길이 (ms), 기본값: 500
    --model: Whisper 모델 (tiny, base, small), 기본값: base
    --output: 출력 파일 경로 (선택)

작성일: 2026-01-18
모듈: M4 - Skill C: 영상 편집 자동화 Skill
"""

import sys
import os
import io
import argparse
import tempfile
import subprocess
import json
from datetime import datetime, timedelta

# Windows UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    from pydub import AudioSegment
    from pydub.silence import detect_nonsilent, detect_silence
except ImportError:
    print("[Error] pydub 라이브러리가 설치되지 않았습니다.")
    print("        pip install pydub 명령어로 설치해주세요.")
    sys.exit(1)

# 필러 단어 목록
FILLER_WORDS = {
    'en': ['um', 'uh', 'er', 'ah', 'eh', 'hmm', 'mm', 'like', 'you know', 'i mean', 'so', 'well', 'basically', 'actually', 'literally', 'right'],
    'ko': ['음', '어', '아', '그', '저', '이제', '뭐', '근데', '그래서', '그러니까', '막', '좀', '진짜', '약간', '되게'],
    'universal': ['um', 'uh', 'er', 'ah', 'mm', 'hmm']
}


def format_timestamp(milliseconds):
    """밀리초를 HH:MM:SS.mmm 형식으로 변환"""
    td = timedelta(milliseconds=milliseconds)
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    ms = int(milliseconds % 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:03d}"


def format_duration(milliseconds):
    """밀리초를 읽기 쉬운 형식으로 변환"""
    if milliseconds < 1000:
        return f"{int(milliseconds)}ms"
    elif milliseconds < 60000:
        return f"{milliseconds/1000:.1f}s"
    else:
        return f"{milliseconds/60000:.1f}m"


def is_video_file(file_path):
    """파일이 영상인지 확인"""
    ext = os.path.splitext(file_path)[1].lower()
    return ext in ['.mp4', '.mkv', '.avi', '.mov', '.webm', '.flv', '.wmv']


def print_header():
    """헤더 출력"""
    print("=" * 70)
    print("  통합 영상 편집 스크립트 (Video Editor)")
    print("  - 무음 구간 제거")
    print("  - 필러 단어 제거")
    print("=" * 70)


def load_audio(file_path):
    """오디오 파일 로드"""
    print(f"\n[1/5] 파일 로드 중...")
    print(f"      파일: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    audio = AudioSegment.from_file(file_path)
    duration = len(audio)

    print(f"      [OK] 로드 완료!")
    print(f"      - 길이: {format_timestamp(duration)} ({format_duration(duration)})")
    print(f"      - 채널: {audio.channels}, 샘플레이트: {audio.frame_rate}Hz")

    return audio


def detect_silence_ranges(audio, threshold_db=-40, min_silence_ms=500):
    """무음 구간 감지"""
    print(f"\n[2/5] 무음 구간 감지 중...")
    print(f"      임계값: {threshold_db}dB, 최소 길이: {min_silence_ms}ms")

    silence_ranges = detect_silence(
        audio,
        min_silence_len=min_silence_ms,
        silence_thresh=threshold_db
    )

    total_silence = sum(end - start for start, end in silence_ranges)
    print(f"      [OK] {len(silence_ranges)}개 무음 구간 발견 ({format_duration(total_silence)})")

    return silence_ranges


def detect_filler_ranges(file_path, model_name="base", language=None):
    """Whisper를 사용하여 필러 단어 구간 감지"""
    print(f"\n[3/5] 필러 단어 감지 중...")
    print(f"      Whisper 모델: {model_name}")

    try:
        import whisper
    except ImportError:
        print("      [Skip] whisper 미설치 - 필러 감지 건너뜀")
        return []

    # 모델 로드
    print(f"      모델 로드 중...")
    model = whisper.load_model(model_name)

    # 음성 인식
    print(f"      음성 인식 중... (시간이 걸릴 수 있습니다)")
    options = {"word_timestamps": True, "verbose": False}
    if language:
        options["language"] = language

    result = model.transcribe(file_path, **options)
    detected_language = result.get("language", "en")

    # 필러 단어 목록
    filler_list = FILLER_WORDS.get(detected_language, []) + FILLER_WORDS['universal']
    filler_list = list(set(word.lower() for word in filler_list))

    # 필러 단어 감지
    filler_ranges = []
    segments = result.get('segments', [])

    for segment in segments:
        words = segment.get('words', [])
        for word_info in words:
            word = word_info.get('word', '').strip().lower()
            word_clean = ''.join(c for c in word if c.isalnum() or c in ['\'', '-'])

            if word_clean in filler_list:
                start_ms = int(word_info.get('start', 0) * 1000)
                end_ms = int(word_info.get('end', 0) * 1000)
                filler_ranges.append((start_ms, end_ms, word_info.get('word', '')))

    total_filler = sum(end - start for start, end, _ in filler_ranges)
    print(f"      [OK] {len(filler_ranges)}개 필러 단어 발견 ({format_duration(total_filler)})")

    return filler_ranges


def merge_removal_ranges(silence_ranges, filler_ranges, audio_duration, padding_ms=100):
    """제거할 구간들을 병합하여 유지할 구간 계산"""
    print(f"\n[4/5] 편집 구간 계산 중...")

    # 모든 제거 구간 수집 (밀리초 단위)
    remove_ranges = []

    # 무음 구간 추가
    for start, end in silence_ranges:
        # 패딩 적용 (무음의 시작/끝 부분은 약간 유지)
        adjusted_start = start + padding_ms
        adjusted_end = end - padding_ms
        if adjusted_start < adjusted_end:
            remove_ranges.append((adjusted_start, adjusted_end))

    # 필러 구간 추가
    for start, end, _ in filler_ranges:
        remove_ranges.append((start, end))

    if not remove_ranges:
        print(f"      [Info] 제거할 구간 없음 - 원본 유지")
        return [(0, audio_duration)]

    # 정렬 및 병합
    remove_ranges.sort(key=lambda x: x[0])

    merged_remove = []
    for start, end in remove_ranges:
        if merged_remove and start <= merged_remove[-1][1] + padding_ms:
            merged_remove[-1] = (merged_remove[-1][0], max(merged_remove[-1][1], end))
        else:
            merged_remove.append((start, end))

    # 유지할 구간 계산 (제거 구간의 보완)
    keep_ranges = []
    prev_end = 0

    for start, end in merged_remove:
        if prev_end < start:
            keep_ranges.append((prev_end, start))
        prev_end = end

    if prev_end < audio_duration:
        keep_ranges.append((prev_end, audio_duration))

    total_keep = sum(end - start for start, end in keep_ranges)
    total_remove = audio_duration - total_keep

    print(f"      [OK] {len(keep_ranges)}개 유지 구간 계산 완료")
    print(f"      - 제거: {format_duration(total_remove)} ({total_remove/audio_duration*100:.1f}%)")
    print(f"      - 유지: {format_duration(total_keep)} ({total_keep/audio_duration*100:.1f}%)")

    return keep_ranges


def edit_audio(audio, keep_ranges):
    """오디오 편집 (유지 구간만 연결)"""
    edited = AudioSegment.empty()

    for start, end in keep_ranges:
        edited += audio[start:end]

    return edited


def extract_ffmpeg_error(stderr_text):
    """FFmpeg stderr에서 핵심 에러 메시지만 추출"""
    error_keywords = ['error', 'invalid', 'failed', 'cannot', 'no such', 'not found', 'unable']
    error_lines = []

    for line in stderr_text.split('\n'):
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in error_keywords):
            error_lines.append(line.strip())

    if error_lines:
        return '\n'.join(error_lines[-5:])  # 마지막 5개 에러만 표시
    return stderr_text[-500:] if len(stderr_text) > 500 else stderr_text


def edit_video_ffmpeg(input_path, output_path, keep_ranges):
    """FFmpeg를 사용하여 영상 편집 (구간 분할 처리 및 병합으로 안정성/효율성 개선)"""
    import re
    import math
    import shutil

    print(f"\n[5/5] 영상 편집 중 (FFmpeg)...")

    if not keep_ranges:
        print("      [Info] 유지할 구간이 없어 편집을 건너뜁니다.")
        return False

    # 임시 디렉터리 생성
    temp_dir = tempfile.mkdtemp(prefix="ffmpeg_chunks_")
    print(f"      임시 폴더 생성: {temp_dir}")

    try:
        # 1. 구간 분할 처리
        CHUNK_SIZE = 100  # 한 번에 처리할 구간 수
        num_chunks = math.ceil(len(keep_ranges) / CHUNK_SIZE)
        temp_video_files = []

        # 각 청크의 예상 시간 계산 (진행률 표시용)
        chunk_durations = []
        for i in range(num_chunks):
            chunk_start = i * CHUNK_SIZE
            chunk_end = min(chunk_start + CHUNK_SIZE, len(keep_ranges))
            chunk_ranges = keep_ranges[chunk_start:chunk_end]
            chunk_duration = sum(end - start for start, end in chunk_ranges) / 1000  # 초 단위
            chunk_durations.append(chunk_duration)

        print(f"      {len(keep_ranges)}개 구간을 {num_chunks}개 묶음으로 분할 처리합니다.")

        for i in range(num_chunks):
            chunk_start = i * CHUNK_SIZE
            chunk_end = min(chunk_start + CHUNK_SIZE, len(keep_ranges))
            chunk_ranges = keep_ranges[chunk_start:chunk_end]
            chunk_duration = chunk_durations[i]

            temp_part_path = os.path.join(temp_dir, f"part_{i:04d}.mkv")
            print(f"\n      - 묶음 {i+1}/{num_chunks}: {len(chunk_ranges)}개 구간 ({chunk_duration:.1f}초)")

            select_expr = "+".join([f"between(t,{start/1000},{end/1000})" for start, end in chunk_ranges])
            filter_complex = f"[0:v]select='{select_expr}',setpts=N/FRAME_RATE/TB[v];[0:a]aselect='{select_expr}',asetpts=N/SR/TB[a]"

            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as filter_file:
                filter_file.write(filter_complex)
                filter_file_name = filter_file.name

            cmd = [
                "ffmpeg", "-y", "-i", input_path,
                "-filter_complex_script", filter_file_name,
                "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-preset", "fast", "-crf", "23",
                "-c:a", "aac", "-b:a", "128k",
                temp_part_path
            ]

            # 진행 상황 실시간 표시
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='ignore'
            )

            stderr_output = []
            last_progress = ""

            # stderr를 실시간으로 읽어서 진행 상황 표시
            while True:
                line = process.stderr.readline()
                if not line and process.poll() is not None:
                    break
                stderr_output.append(line)

                # FFmpeg 진행 상황 파싱 (time=00:00:00.00 형식)
                time_match = re.search(r'time=(\d{2}:\d{2}:\d{2}\.\d{2})', line)
                if time_match:
                    current_time = time_match.group(1)
                    # 시간을 초로 변환
                    parts = current_time.split(':')
                    current_seconds = float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])

                    if chunk_duration > 0:
                        progress_pct = min(100, (current_seconds / chunk_duration) * 100)
                        progress_str = f"        진행: {current_time} / {chunk_duration:.1f}초 ({progress_pct:.1f}%)"

                        # 같은 줄에 업데이트 (carriage return)
                        if progress_str != last_progress:
                            print(f"\r{progress_str}", end='', flush=True)
                            last_progress = progress_str

            # 줄바꿈으로 진행 상황 표시 마무리
            if last_progress:
                print()  # 새 줄로 이동

            os.unlink(filter_file_name)
            stderr_text = ''.join(stderr_output)

            if process.returncode != 0:
                print(f"        [Error] 묶음 {i+1} 처리 실패:")
                print(f"        {extract_ffmpeg_error(stderr_text)}")
                raise RuntimeError(f"FFmpeg 묶음 {i+1} 처리 중 오류 발생")

            print(f"        [OK] 묶음 {i+1} 완료")
            temp_video_files.append(temp_part_path)

        # 2. 최종 병합
        print("\n      모든 묶음 처리 완료. 최종 파일로 병합합니다...")
        concat_list_path = os.path.join(temp_dir, "concat_list.txt")
        with open(concat_list_path, 'w', encoding='utf-8') as f:
            for video_file in temp_video_files:
                # FFmpeg concat demuxer는 경로에 역슬래시가 있으면 오류 발생 가능
                f.write(f"file '{video_file.replace(os.sep, '/')}'\n")

        concat_cmd = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list_path,
            "-c", "copy",  # 재인코딩 없이 빠른 속도로 복사
            output_path
        ]

        process = subprocess.Popen(
            concat_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        _, stderr = process.communicate()

        if process.returncode != 0:
            print("        [Error] 최종 파일 병합 실패:")
            print(f"        {extract_ffmpeg_error(stderr)}")
            raise RuntimeError("FFmpeg 최종 병합 중 오류 발생")

        print(f"      [OK] 영상 편집 완료!")
        return True

    except KeyboardInterrupt:
        print("\n[Info] 사용자에 의해 작업이 중단되었습니다.")
        raise
    finally:
        # 3. 자동 정리
        print(f"      임시 폴더 및 파일 정리: {temp_dir}")
        shutil.rmtree(temp_dir, ignore_errors=True)


def save_audio(audio, output_path):
    """오디오 저장"""
    print(f"\n[5/5] 오디오 저장 중...")
    print(f"      파일: {output_path}")

    ext = os.path.splitext(output_path)[1].lower().lstrip('.')
    format_map = {'mp3': 'mp3', 'wav': 'wav', 'ogg': 'ogg', 'flac': 'flac', 'm4a': 'mp4'}
    audio_format = format_map.get(ext, 'mp3')

    audio.export(output_path, format=audio_format)
    print(f"      [OK] 저장 완료!")


def generate_report(input_path, output_path, original_duration, edited_duration,
                   silence_ranges, filler_ranges, keep_ranges,
                   start_time=None, end_time=None, elapsed_time=None):
    """편집 결과 보고서 생성"""
    saved_time = original_duration - edited_duration
    saved_ratio = (saved_time / original_duration * 100) if original_duration > 0 else 0

    silence_time = sum(end - start for start, end in silence_ranges)
    filler_time = sum(end - start for start, end, _ in filler_ranges)

    print("\n")
    print("=" * 70)
    print("  편집 결과 보고서")
    print("=" * 70)

    print(f"\n  [파일 정보]")
    print(f"  - 입력: {os.path.basename(input_path)}")
    print(f"  - 출력: {os.path.basename(output_path)}")

    print(f"\n  [시간 분석]")
    print(f"  - 원본 길이:    {format_timestamp(original_duration):>15} ({format_duration(original_duration)})")
    print(f"  - 편집 후:      {format_timestamp(edited_duration):>15} ({format_duration(edited_duration)})")
    print(f"  - 단축 시간:    {format_timestamp(saved_time):>15} ({format_duration(saved_time)})")
    print(f"  - 단축 비율:    {saved_ratio:>15.1f}%")

    print(f"\n  [제거 내역]")
    print(f"  - 무음 구간:    {len(silence_ranges):>10}개 ({format_duration(silence_time)})")
    print(f"  - 필러 단어:    {len(filler_ranges):>10}개 ({format_duration(filler_time)})")
    print(f"  - 유지 구간:    {len(keep_ranges):>10}개")

    if os.path.exists(output_path):
        original_size = os.path.getsize(input_path)
        edited_size = os.path.getsize(output_path)
        size_ratio = (edited_size / original_size * 100) if original_size > 0 else 0

        print(f"\n  [파일 크기]")
        print(f"  - 원본:         {original_size/1024/1024:>10.1f} MB")
        print(f"  - 편집 후:      {edited_size/1024/1024:>10.1f} MB")
        print(f"  - 크기 비율:    {size_ratio:>10.1f}%")

    # 작업 시간 정보 출력
    if start_time and end_time and elapsed_time:
        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        elapsed_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        print(f"\n  [작업 시간]")
        print(f"  - 시작:         {start_time.strftime('%Y-%m-%d %H:%M:%S'):>19}")
        print(f"  - 종료:         {end_time.strftime('%Y-%m-%d %H:%M:%S'):>19}")
        print(f"  - 소요 시간:    {elapsed_str:>19}")

    print("\n" + "=" * 70)

    # 마크다운 보고서 생성
    report_path = output_path.rsplit('.', 1)[0] + '_report.md'
    report_lines = [
        f"# 영상 편집 보고서",
        f"",
        f"**생성일**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        f"## 파일 정보",
        f"",
        f"| 항목 | 값 |",
        f"|------|------|",
        f"| 입력 파일 | {os.path.basename(input_path)} |",
        f"| 출력 파일 | {os.path.basename(output_path)} |",
        f"",
        f"## 시간 분석",
        f"",
        f"| 항목 | 값 |",
        f"|------|------|",
        f"| 원본 길이 | {format_timestamp(original_duration)} |",
        f"| 편집 후 | {format_timestamp(edited_duration)} |",
        f"| 단축 시간 | {format_timestamp(saved_time)} |",
        f"| 단축 비율 | {saved_ratio:.1f}% |",
        f"",
        f"## 제거 내역",
        f"",
        f"| 항목 | 개수 | 총 시간 |",
        f"|------|------|------|",
        f"| 무음 구간 | {len(silence_ranges)} | {format_duration(silence_time)} |",
        f"| 필러 단어 | {len(filler_ranges)} | {format_duration(filler_time)} |",
        f"",
    ]

    # 작업 시간 정보 추가
    if start_time and end_time and elapsed_time:
        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        elapsed_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        report_lines.extend([
            f"## 작업 시간",
            f"",
            f"| 항목 | 값 |",
            f"|------|------|",
            f"| 시작 시각 | {start_time.strftime('%Y-%m-%d %H:%M:%S')} |",
            f"| 종료 시각 | {end_time.strftime('%Y-%m-%d %H:%M:%S')} |",
            f"| 소요 시간 | {elapsed_str} |",
            f"",
        ])

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"\n  [보고서 저장] {report_path}")

    return {
        'original_duration': original_duration,
        'edited_duration': edited_duration,
        'saved_time': saved_time,
        'saved_ratio': saved_ratio,
        'silence_count': len(silence_ranges),
        'filler_count': len(filler_ranges),
    }


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="영상/오디오 파일에서 무음 구간과 필러 단어를 제거합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python video-editor.py video.mp4 --remove-silence
  python video-editor.py video.mp4 --remove-fillers --model base
  python video-editor.py video.mp4 --all --output edited.mp4
        """
    )
    parser.add_argument("file", help="편집할 파일 경로")
    parser.add_argument("--remove-silence", action="store_true", help="무음 구간 제거")
    parser.add_argument("--remove-fillers", action="store_true", help="필러 단어 제거")
    parser.add_argument("--all", action="store_true", help="무음 + 필러 모두 제거")
    parser.add_argument("--threshold", type=int, default=-40, help="무음 임계값 (dB)")
    parser.add_argument("--min-silence", type=int, default=500, help="최소 무음 길이 (ms)")
    parser.add_argument("--model", type=str, default="base", choices=["tiny", "base", "small", "medium"], help="Whisper 모델")
    parser.add_argument("--language", type=str, default=None, help="언어 코드 (en, ko)")
    parser.add_argument("--output", "-o", type=str, default=None, help="출력 파일 경로")

    args = parser.parse_args()

    # --all 옵션 처리
    if args.all:
        args.remove_silence = True
        args.remove_fillers = True

    # 최소 하나의 옵션 필요
    if not args.remove_silence and not args.remove_fillers:
        print("[Error] --remove-silence, --remove-fillers, 또는 --all 옵션을 지정하세요.")
        return 1

    print_header()

    # 작업 시작 시간 기록
    start_time = datetime.now()
    print(f"\n  [작업 시작] {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # 1. 오디오 로드
        audio = load_audio(args.file)
        original_duration = len(audio)

        # 2. 무음 구간 감지
        silence_ranges = []
        if args.remove_silence:
            silence_ranges = detect_silence_ranges(
                audio,
                threshold_db=args.threshold,
                min_silence_ms=args.min_silence
            )
        else:
            print(f"\n[2/5] 무음 구간 감지... [Skip]")

        # 3. 필러 단어 감지
        filler_ranges = []
        if args.remove_fillers:
            filler_ranges = detect_filler_ranges(
                args.file,
                model_name=args.model,
                language=args.language
            )
        else:
            print(f"\n[3/5] 필러 단어 감지... [Skip]")

        # 4. 유지 구간 계산
        keep_ranges = merge_removal_ranges(
            silence_ranges,
            filler_ranges,
            original_duration
        )

        # 5. 출력 파일 경로
        if args.output:
            output_path = args.output
        else:
            base, ext = os.path.splitext(args.file)
            output_path = f"{base}_edited{ext}"

        # 6. 편집 및 저장
        if is_video_file(args.file):
            edit_video_ffmpeg(args.file, output_path, keep_ranges)
        else:
            edited_audio = edit_audio(audio, keep_ranges)
            save_audio(edited_audio, output_path)

        # 7. 작업 종료 시간 기록
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        # 소요 시간을 읽기 쉬운 형식으로 변환
        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        elapsed_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        # 8. 결과 보고서
        edited_duration = sum(end - start for start, end in keep_ranges)
        generate_report(
            args.file, output_path,
            original_duration, edited_duration,
            silence_ranges, filler_ranges, keep_ranges,
            start_time, end_time, elapsed_time
        )

        print(f"\n  [완료] 편집이 완료되었습니다!")
        print("=" * 70)

        return 0

    except Exception as e:
        print(f"\n[Error] {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
