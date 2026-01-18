#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
무음 구간 제거 스크립트 (Silence Remover)

이 스크립트는 영상 또는 오디오 파일에서 무음 구간을 자동으로 제거합니다.
pydub 라이브러리를 사용하여 오디오를 분석하고,
FFmpeg를 사용하여 영상을 편집합니다.

사용법:
    python silence-remover.py <파일경로> [옵션]

예시:
    python silence-remover.py video.mp4
    python silence-remover.py audio.mp3 --threshold -40 --min-silence 500
    python silence-remover.py video.mp4 --output edited_video.mp4 --keep-padding 100

옵션:
    --threshold: 무음 판단 임계값 (dB), 기본값: -40
    --min-silence: 최소 무음 길이 (ms), 기본값: 500
    --keep-padding: 무음 구간 앞뒤 유지할 패딩 (ms), 기본값: 100
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
from datetime import timedelta

# Windows UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    from pydub import AudioSegment
    from pydub.silence import detect_nonsilent
except ImportError:
    print("[Error] pydub 라이브러리가 설치되지 않았습니다.")
    print("        pip install pydub 명령어로 설치해주세요.")
    sys.exit(1)


def format_timestamp(milliseconds):
    """밀리초를 HH:MM:SS.mmm 형식으로 변환"""
    td = timedelta(milliseconds=milliseconds)
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    ms = milliseconds % 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:03d}"


def format_duration(milliseconds):
    """밀리초를 읽기 쉬운 형식으로 변환"""
    if milliseconds < 1000:
        return f"{milliseconds}ms"
    elif milliseconds < 60000:
        return f"{milliseconds/1000:.1f}s"
    else:
        return f"{milliseconds/60000:.1f}m"


def is_video_file(file_path):
    """파일이 영상인지 확인"""
    ext = os.path.splitext(file_path)[1].lower()
    return ext in ['.mp4', '.mkv', '.avi', '.mov', '.webm', '.flv', '.wmv']


def load_audio(file_path):
    """오디오 파일 로드 (영상 파일도 지원)"""
    print(f"\n[Load] 파일 로드 중: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    try:
        audio = AudioSegment.from_file(file_path)
        duration = len(audio)
        print(f"[OK] 파일 로드 완료!")
        print(f"     - 길이: {format_timestamp(duration)} ({format_duration(duration)})")
        print(f"     - 채널: {audio.channels}")
        print(f"     - 샘플레이트: {audio.frame_rate}Hz")

        return audio

    except Exception as e:
        raise RuntimeError(f"파일 로드 실패: {e}")


def detect_speech_segments(audio, threshold_db=-40, min_silence_ms=500, padding_ms=100):
    """음성(비무음) 구간 감지 및 패딩 추가"""
    print(f"\n[Detect] 음성 구간 감지 중...")
    print(f"         - 임계값: {threshold_db}dB")
    print(f"         - 최소 무음 길이: {min_silence_ms}ms")
    print(f"         - 패딩: {padding_ms}ms")

    # 비무음(음성) 구간 감지
    nonsilent_ranges = detect_nonsilent(
        audio,
        min_silence_len=min_silence_ms,
        silence_thresh=threshold_db
    )

    # 패딩 적용 (앞뒤로 약간의 여유 추가)
    total_duration = len(audio)
    padded_ranges = []

    for start, end in nonsilent_ranges:
        padded_start = max(0, start - padding_ms)
        padded_end = min(total_duration, end + padding_ms)
        padded_ranges.append((padded_start, padded_end))

    # 겹치는 구간 병합
    merged_ranges = []
    for start, end in sorted(padded_ranges):
        if merged_ranges and start <= merged_ranges[-1][1]:
            # 이전 구간과 겹침 - 병합
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
        else:
            merged_ranges.append((start, end))

    print(f"[OK] 감지 완료! - {len(merged_ranges)}개 음성 구간")

    return merged_ranges


def remove_silence_audio(audio, speech_ranges):
    """오디오에서 무음 구간 제거"""
    print(f"\n[Edit] 무음 구간 제거 중...")

    # 음성 구간만 연결
    edited_audio = AudioSegment.empty()

    for i, (start, end) in enumerate(speech_ranges):
        segment = audio[start:end]
        edited_audio += segment
        print(f"  [{i+1:3d}/{len(speech_ranges)}] {format_timestamp(start)} - {format_timestamp(end)}")

    return edited_audio


def remove_silence_video_ffmpeg(input_path, output_path, speech_ranges):
    """FFmpeg를 사용하여 영상에서 무음 구간 제거"""
    print(f"\n[Edit] FFmpeg로 영상 편집 중...")

    # FFmpeg filter_complex를 사용한 구간 추출 및 연결
    filter_parts = []
    concat_parts = []

    for i, (start, end) in enumerate(speech_ranges):
        start_sec = start / 1000
        end_sec = end / 1000
        # 각 구간 추출
        filter_parts.append(f"[0:v]trim=start={start_sec}:end={end_sec},setpts=PTS-STARTPTS[v{i}];")
        filter_parts.append(f"[0:a]atrim=start={start_sec}:end={end_sec},asetpts=PTS-STARTPTS[a{i}];")
        concat_parts.append(f"[v{i}][a{i}]")

    # 모든 구간 연결
    filter_complex = "".join(filter_parts)
    filter_complex += "".join(concat_parts)
    filter_complex += f"concat=n={len(speech_ranges)}:v=1:a=1[outv][outa]"

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-filter_complex", filter_complex,
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        output_path
    ]

    print(f"[Run] FFmpeg 명령어 실행 중...")
    print(f"      (구간 수: {len(speech_ranges)}개)")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10분 타임아웃
        )

        if result.returncode != 0:
            print(f"[Warning] FFmpeg 경고/오류:\n{result.stderr[:500]}")
            # 경고는 무시하고 파일이 생성되었는지 확인
            if not os.path.exists(output_path):
                raise RuntimeError(f"FFmpeg 실패: {result.stderr}")

        print(f"[OK] 영상 편집 완료!")
        return True

    except subprocess.TimeoutExpired:
        raise RuntimeError("FFmpeg 실행 시간 초과 (10분)")
    except FileNotFoundError:
        raise RuntimeError("FFmpeg가 설치되지 않았거나 PATH에 없습니다.")


def save_audio(audio, output_path):
    """오디오 파일 저장"""
    print(f"\n[Save] 저장 중: {output_path}")

    ext = os.path.splitext(output_path)[1].lower().lstrip('.')
    format_map = {
        'mp3': 'mp3',
        'wav': 'wav',
        'ogg': 'ogg',
        'flac': 'flac',
        'm4a': 'mp4',
        'aac': 'adts',
    }

    audio_format = format_map.get(ext, 'mp3')

    try:
        audio.export(output_path, format=audio_format)
        print(f"[OK] 저장 완료!")
        return True
    except Exception as e:
        raise RuntimeError(f"저장 실패: {e}")


def generate_edit_report(input_path, output_path, original_duration, edited_duration, speech_ranges):
    """편집 결과 보고서 출력"""
    saved_time = original_duration - edited_duration
    saved_ratio = (saved_time / original_duration * 100) if original_duration > 0 else 0

    print("\n" + "=" * 60)
    print("편집 결과 보고서")
    print("=" * 60)

    print(f"\n[Files]")
    print(f"  - 입력: {input_path}")
    print(f"  - 출력: {output_path}")

    print(f"\n[Duration]")
    print(f"  - 원본 길이: {format_timestamp(original_duration)} ({format_duration(original_duration)})")
    print(f"  - 편집 후: {format_timestamp(edited_duration)} ({format_duration(edited_duration)})")
    print(f"  - 단축 시간: {format_timestamp(saved_time)} ({format_duration(saved_time)})")
    print(f"  - 단축 비율: {saved_ratio:.1f}%")

    print(f"\n[Segments]")
    print(f"  - 유지된 음성 구간: {len(speech_ranges)}개")

    if os.path.exists(output_path):
        original_size = os.path.getsize(input_path)
        edited_size = os.path.getsize(output_path)
        size_ratio = (edited_size / original_size * 100) if original_size > 0 else 0

        print(f"\n[File Size]")
        print(f"  - 원본: {original_size / 1024 / 1024:.1f} MB")
        print(f"  - 편집 후: {edited_size / 1024 / 1024:.1f} MB")
        print(f"  - 크기 비율: {size_ratio:.1f}%")

    print("\n" + "=" * 60)

    return {
        'original_duration': original_duration,
        'edited_duration': edited_duration,
        'saved_time': saved_time,
        'saved_ratio': saved_ratio,
        'segment_count': len(speech_ranges),
    }


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="영상/오디오 파일에서 무음 구간을 제거합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python silence-remover.py video.mp4
  python silence-remover.py audio.mp3 --threshold -35 --min-silence 300
  python silence-remover.py video.mp4 --output edited.mp4 --keep-padding 200
        """
    )
    parser.add_argument("file", help="편집할 파일 경로 (영상 또는 오디오)")
    parser.add_argument("--threshold", type=int, default=-40,
                        help="무음 판단 임계값 (dB), 기본값: -40")
    parser.add_argument("--min-silence", type=int, default=500,
                        help="최소 무음 길이 (ms), 기본값: 500")
    parser.add_argument("--keep-padding", type=int, default=100,
                        help="음성 구간 앞뒤 유지할 패딩 (ms), 기본값: 100")
    parser.add_argument("--output", "-o", type=str, default=None,
                        help="출력 파일 경로 (선택, 기본값: 원본파일_edited.확장자)")

    args = parser.parse_args()

    print("=" * 60)
    print("무음 구간 제거 스크립트 (Silence Remover)")
    print("=" * 60)

    try:
        # 1. 오디오 로드
        audio = load_audio(args.file)
        original_duration = len(audio)

        # 2. 음성 구간 감지
        speech_ranges = detect_speech_segments(
            audio,
            threshold_db=args.threshold,
            min_silence_ms=args.min_silence,
            padding_ms=args.keep_padding
        )

        if not speech_ranges:
            print("\n[Warning] 음성 구간이 감지되지 않았습니다.")
            print("          임계값(--threshold)을 낮춰보세요.")
            return 1

        # 3. 출력 파일 경로 설정
        if args.output:
            output_path = args.output
        else:
            base, ext = os.path.splitext(args.file)
            output_path = f"{base}_edited{ext}"

        # 4. 무음 제거 및 저장
        if is_video_file(args.file):
            # 영상 파일 - FFmpeg 사용
            remove_silence_video_ffmpeg(args.file, output_path, speech_ranges)
            # 편집된 영상 길이 계산
            edited_duration = sum(end - start for start, end in speech_ranges)
        else:
            # 오디오 파일 - pydub 사용
            edited_audio = remove_silence_audio(audio, speech_ranges)
            edited_duration = len(edited_audio)
            save_audio(edited_audio, output_path)

        # 5. 결과 보고서
        generate_edit_report(
            args.file, output_path,
            original_duration, edited_duration,
            speech_ranges
        )

        print("\n[OK] 편집 완료!")
        print("=" * 60)

        return 0

    except FileNotFoundError as e:
        print(f"\n[Error] {e}")
        return 1
    except RuntimeError as e:
        print(f"\n[Error] {e}")
        return 1
    except KeyboardInterrupt:
        print("\n\n[Cancel] 사용자에 의해 취소되었습니다.")
        return 1
    except Exception as e:
        print(f"\n[Error] 예상치 못한 오류: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
