#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
빠른 무음 제거 스크립트 (Fast Silence Remover)

FFmpeg의 silencedetect 필터를 사용하여 무음 구간을 빠르게 감지하고 제거합니다.
긴 영상도 효율적으로 처리할 수 있습니다.

사용법:
    python fast-silence-remover.py <파일경로> [옵션]

예시:
    python fast-silence-remover.py video.mp4
    python fast-silence-remover.py video.mp4 --threshold -40 --min-duration 0.3

옵션:
    --threshold: 무음 판단 임계값 (dB), 기본값: -40
    --min-duration: 최소 무음 길이 (초), 기본값: 0.3
    --output: 출력 파일 경로 (기본: 원본_edited.확장자)

작성일: 2026-01-19
"""

import sys
import os
import io
import re
import subprocess
import argparse
import tempfile
from datetime import timedelta

# Windows UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_time(seconds):
    """초를 HH:MM:SS.mmm 형식으로 변환"""
    td = timedelta(seconds=seconds)
    total_secs = int(td.total_seconds())
    hours, remainder = divmod(total_secs, 3600)
    minutes, secs = divmod(remainder, 60)
    ms = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{ms:03d}"


def get_video_duration(input_path):
    """영상 길이 가져오기"""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        input_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return float(result.stdout.strip())
    except:
        return 0


def detect_silence_ffmpeg(input_path, threshold_db=-40, min_duration=0.3):
    """FFmpeg를 사용하여 무음 구간 감지"""
    print(f"\n[1/3] 무음 구간 감지 중 (FFmpeg silencedetect)...")
    print(f"      임계값: {threshold_db}dB, 최소 길이: {min_duration}초")

    cmd = [
        "ffmpeg", "-i", input_path,
        "-af", f"silencedetect=noise={threshold_db}dB:d={min_duration}",
        "-f", "null", "-"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=600)
        output = result.stderr

        if output is None:
            output = ""

        # 무음 구간 파싱
        silence_starts = []
        silence_ends = []

        for line in output.split('\n'):
            if 'silence_start' in line:
                match = re.search(r'silence_start: ([\d.]+)', line)
                if match:
                    silence_starts.append(float(match.group(1)))
            elif 'silence_end' in line:
                match = re.search(r'silence_end: ([\d.]+)', line)
                if match:
                    silence_ends.append(float(match.group(1)))

        # 시작과 끝을 매칭
        silence_ranges = []
        for i, start in enumerate(silence_starts):
            if i < len(silence_ends):
                silence_ranges.append((start, silence_ends[i]))

        print(f"      [OK] {len(silence_ranges)}개 무음 구간 발견")
        return silence_ranges

    except subprocess.TimeoutExpired:
        raise RuntimeError("무음 감지 시간 초과 (10분)")
    except FileNotFoundError:
        raise RuntimeError("FFmpeg가 설치되지 않았습니다.")


def calculate_keep_ranges(duration, silence_ranges, padding=0.05):
    """유지할 구간 계산"""
    if not silence_ranges:
        return [(0, duration * 1000)]

    # 무음 구간에 패딩 적용
    padded_silence = []
    for start, end in silence_ranges:
        padded_start = max(0, start + padding)
        padded_end = max(padded_start, end - padding)
        if padded_end > padded_start:
            padded_silence.append((padded_start, padded_end))

    # 유지 구간 계산 (무음이 아닌 부분)
    keep_ranges = []
    current_pos = 0

    for silence_start, silence_end in sorted(padded_silence):
        if current_pos < silence_start:
            keep_ranges.append((current_pos, silence_start))
        current_pos = max(current_pos, silence_end)

    if current_pos < duration:
        keep_ranges.append((current_pos, duration))

    return keep_ranges


def edit_video_ffmpeg(input_path, output_path, keep_ranges):
    """FFmpeg를 사용하여 영상 편집"""
    print(f"\n[3/3] 영상 편집 중...")
    print(f"      구간 수: {len(keep_ranges)}개")

    if len(keep_ranges) == 0:
        raise RuntimeError("유지할 구간이 없습니다.")

    # FFmpeg filter_complex 생성
    filter_parts = []
    concat_parts = []

    for i, (start, end) in enumerate(keep_ranges):
        filter_parts.append(f"[0:v]trim=start={start}:end={end},setpts=PTS-STARTPTS[v{i}];")
        filter_parts.append(f"[0:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS[a{i}];")
        concat_parts.append(f"[v{i}][a{i}]")

    filter_complex = "".join(filter_parts)
    filter_complex += "".join(concat_parts)
    filter_complex += f"concat=n={len(keep_ranges)}:v=1:a=1[outv][outa]"

    # 필터를 파일로 저장 (명령어 길이 제한 우회)
    filter_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8')
    filter_file.write(filter_complex)
    filter_file.close()

    print(f"      필터 파일: {filter_file.name}")

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-filter_complex_script", filter_file.name,
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        output_path
    ]

    print(f"      FFmpeg 실행 중... (이 작업은 오래 걸릴 수 있습니다)")

    try:
        # FFmpeg 실행 (진행 상황 출력)
        process = subprocess.Popen(
            cmd,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # 진행 상황 모니터링
        last_time = ""
        for line in process.stderr:
            if 'time=' in line:
                match = re.search(r'time=(\S+)', line)
                if match and match.group(1) != last_time:
                    last_time = match.group(1)
                    print(f"\r      진행: {last_time}", end='', flush=True)

        process.wait()
        print()  # 줄바꿈

        # 임시 파일 정리
        if os.path.exists(filter_file.name):
            os.unlink(filter_file.name)

        if process.returncode != 0:
            raise RuntimeError("FFmpeg 실행 실패")

        if not os.path.exists(output_path):
            raise RuntimeError("출력 파일이 생성되지 않았습니다.")

        print(f"      [OK] 편집 완료!")
        return True

    except Exception as e:
        if os.path.exists(filter_file.name):
            os.unlink(filter_file.name)
        raise


def main():
    parser = argparse.ArgumentParser(description="FFmpeg를 사용한 빠른 무음 제거")
    parser.add_argument("file", help="입력 파일 경로")
    parser.add_argument("--threshold", type=int, default=-40,
                        help="무음 임계값 (dB), 기본값: -40")
    parser.add_argument("--min-duration", type=float, default=0.3,
                        help="최소 무음 길이 (초), 기본값: 0.3")
    parser.add_argument("--output", "-o", type=str, default=None,
                        help="출력 파일 경로")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[Error] 파일을 찾을 수 없습니다: {args.file}")
        return 1

    print("=" * 60)
    print("  빠른 무음 제거 (Fast Silence Remover)")
    print("=" * 60)

    try:
        # 영상 정보
        duration = get_video_duration(args.file)
        print(f"\n[Info] 입력 파일: {os.path.basename(args.file)}")
        print(f"       길이: {format_time(duration)} ({duration/60:.1f}분)")

        # 1. 무음 감지
        silence_ranges = detect_silence_ffmpeg(
            args.file,
            threshold_db=args.threshold,
            min_duration=args.min_duration
        )

        if not silence_ranges:
            print("\n[Info] 무음 구간이 발견되지 않았습니다.")
            return 0

        # 2. 유지 구간 계산
        print(f"\n[2/3] 편집 구간 계산 중...")
        keep_ranges = calculate_keep_ranges(duration, silence_ranges)

        silence_total = sum(end - start for start, end in silence_ranges)
        keep_total = sum(end - start for start, end in keep_ranges)

        print(f"      무음 총 시간: {format_time(silence_total)} ({silence_total/60:.1f}분)")
        print(f"      유지 시간: {format_time(keep_total)} ({keep_total/60:.1f}분)")
        print(f"      예상 단축률: {(silence_total/duration*100):.1f}%")

        # 3. 출력 경로 설정
        if args.output:
            output_path = args.output
        else:
            base, ext = os.path.splitext(args.file)
            output_path = f"{base}_edited{ext}"

        print(f"\n      출력 파일: {os.path.basename(output_path)}")

        # 4. 영상 편집
        edit_video_ffmpeg(args.file, output_path, keep_ranges)

        # 결과 출력
        output_size = os.path.getsize(output_path) / (1024 * 1024)
        input_size = os.path.getsize(args.file) / (1024 * 1024)

        print("\n" + "=" * 60)
        print("  결과 요약")
        print("=" * 60)
        print(f"  원본 길이: {format_time(duration)}")
        print(f"  편집 길이: {format_time(keep_total)}")
        print(f"  단축 시간: {format_time(silence_total)} ({silence_total/duration*100:.1f}%)")
        print(f"  원본 크기: {input_size:.1f}MB")
        print(f"  편집 크기: {output_size:.1f}MB ({output_size/input_size*100:.1f}%)")
        print(f"  출력 파일: {output_path}")
        print("=" * 60)

        return 0

    except Exception as e:
        print(f"\n[Error] {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
