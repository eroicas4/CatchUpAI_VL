#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
무음 구간 감지 스크립트 (Silence Detection)

이 스크립트는 영상 또는 오디오 파일에서 무음 구간을 자동으로 감지합니다.
pydub 라이브러리를 사용하여 오디오 레벨을 분석하고,
지정된 임계값 이하의 구간을 무음으로 판단합니다.

사용법:
    python silence-detection.py <파일경로> [옵션]

예시:
    python silence-detection.py video.mp4
    python silence-detection.py audio.mp3 --threshold -40 --min-silence 500
    python silence-detection.py video.mp4 --output report.txt

옵션:
    --threshold: 무음 판단 임계값 (dB), 기본값: -40
    --min-silence: 최소 무음 길이 (ms), 기본값: 500
    --output: 결과 저장 파일 경로 (선택)

작성일: 2026-01-18
모듈: M4 - Skill C: 영상 편집 자동화 Skill
"""

import sys
import os
import io
import argparse
from datetime import timedelta

# Windows UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    from pydub import AudioSegment
    from pydub.silence import detect_silence, detect_nonsilent
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


def load_audio(file_path):
    """오디오 파일 로드 (영상 파일도 지원)"""
    print(f"\n[Load] 파일 로드 중: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    # 파일 확장자 확인
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext in ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac']:
            audio = AudioSegment.from_file(file_path)
        elif ext in ['.mp4', '.mkv', '.avi', '.mov', '.webm']:
            # 영상 파일에서 오디오 추출 (FFmpeg 필요)
            print("[Info] 영상 파일에서 오디오 추출 중...")
            audio = AudioSegment.from_file(file_path)
        else:
            # 알 수 없는 확장자 - FFmpeg에 맡김
            audio = AudioSegment.from_file(file_path)

        duration = len(audio)
        print(f"[OK] 파일 로드 완료!")
        print(f"     - 길이: {format_timestamp(duration)} ({format_duration(duration)})")
        print(f"     - 채널: {audio.channels}")
        print(f"     - 샘플레이트: {audio.frame_rate}Hz")
        print(f"     - 비트: {audio.sample_width * 8}bit")

        return audio

    except Exception as e:
        raise RuntimeError(f"파일 로드 실패: {e}")


def detect_silence_segments(audio, threshold_db=-40, min_silence_ms=500):
    """무음 구간 감지"""
    print(f"\n[Detect] 무음 구간 감지 중...")
    print(f"         - 임계값: {threshold_db}dB")
    print(f"         - 최소 무음 길이: {min_silence_ms}ms")

    # 무음 구간 감지
    silence_ranges = detect_silence(
        audio,
        min_silence_len=min_silence_ms,
        silence_thresh=threshold_db
    )

    # 비무음(음성) 구간 감지
    nonsilent_ranges = detect_nonsilent(
        audio,
        min_silence_len=min_silence_ms,
        silence_thresh=threshold_db
    )

    return silence_ranges, nonsilent_ranges


def analyze_results(audio, silence_ranges, nonsilent_ranges):
    """분석 결과 계산"""
    total_duration = len(audio)

    # 무음 총 시간 계산
    total_silence = sum(end - start for start, end in silence_ranges)

    # 비무음 총 시간 계산
    total_nonsilent = sum(end - start for start, end in nonsilent_ranges)

    # 비율 계산
    silence_ratio = (total_silence / total_duration * 100) if total_duration > 0 else 0
    nonsilent_ratio = (total_nonsilent / total_duration * 100) if total_duration > 0 else 0

    return {
        'total_duration': total_duration,
        'total_silence': total_silence,
        'total_nonsilent': total_nonsilent,
        'silence_ratio': silence_ratio,
        'nonsilent_ratio': nonsilent_ratio,
        'silence_count': len(silence_ranges),
        'potential_savings': total_silence
    }


def print_results(silence_ranges, nonsilent_ranges, stats, show_details=True):
    """결과 출력"""
    print("\n" + "=" * 60)
    print("무음 구간 감지 결과")
    print("=" * 60)

    print(f"\n[Summary] 요약:")
    print(f"  - 전체 길이: {format_timestamp(stats['total_duration'])} ({format_duration(stats['total_duration'])})")
    print(f"  - 무음 총 시간: {format_timestamp(stats['total_silence'])} ({format_duration(stats['total_silence'])})")
    print(f"  - 음성 총 시간: {format_timestamp(stats['total_nonsilent'])} ({format_duration(stats['total_nonsilent'])})")
    print(f"  - 무음 비율: {stats['silence_ratio']:.1f}%")
    print(f"  - 음성 비율: {stats['nonsilent_ratio']:.1f}%")
    print(f"  - 무음 구간 수: {stats['silence_count']}개")
    print(f"  - 예상 단축 시간: {format_duration(stats['potential_savings'])}")

    if show_details and len(silence_ranges) > 0:
        print(f"\n[Details] 무음 구간 상세 (상위 10개):")
        print("-" * 50)
        print(f"{'번호':>4} | {'시작':>12} | {'종료':>12} | {'길이':>10}")
        print("-" * 50)

        # 길이 순으로 정렬하여 상위 10개 표시
        sorted_ranges = sorted(silence_ranges, key=lambda x: x[1] - x[0], reverse=True)
        for i, (start, end) in enumerate(sorted_ranges[:10], 1):
            duration = end - start
            print(f"{i:>4} | {format_timestamp(start):>12} | {format_timestamp(end):>12} | {format_duration(duration):>10}")

    print("\n" + "=" * 60)


def generate_report(file_path, silence_ranges, nonsilent_ranges, stats, output_path=None):
    """분석 보고서 생성"""
    report = []
    report.append("# 무음 구간 감지 보고서")
    report.append("")
    report.append(f"**파일**: {file_path}")
    report.append(f"**분석일**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("## 요약")
    report.append("")
    report.append(f"| 항목 | 값 |")
    report.append(f"|------|------|")
    report.append(f"| 전체 길이 | {format_timestamp(stats['total_duration'])} |")
    report.append(f"| 무음 총 시간 | {format_timestamp(stats['total_silence'])} |")
    report.append(f"| 음성 총 시간 | {format_timestamp(stats['total_nonsilent'])} |")
    report.append(f"| 무음 비율 | {stats['silence_ratio']:.1f}% |")
    report.append(f"| 무음 구간 수 | {stats['silence_count']}개 |")
    report.append(f"| 예상 단축 시간 | {format_duration(stats['potential_savings'])} |")
    report.append("")
    report.append("## 무음 구간 상세")
    report.append("")
    report.append(f"| 번호 | 시작 | 종료 | 길이 |")
    report.append(f"|------|------|------|------|")

    for i, (start, end) in enumerate(silence_ranges, 1):
        duration = end - start
        report.append(f"| {i} | {format_timestamp(start)} | {format_timestamp(end)} | {format_duration(duration)} |")

    report_text = "\n".join(report)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"\n[OK] 보고서 저장: {output_path}")

    return report_text


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="영상/오디오 파일에서 무음 구간을 감지합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python silence-detection.py video.mp4
  python silence-detection.py audio.mp3 --threshold -35 --min-silence 300
  python silence-detection.py video.mp4 --output report.md
        """
    )
    parser.add_argument("file", help="분석할 파일 경로 (영상 또는 오디오)")
    parser.add_argument("--threshold", type=int, default=-40,
                        help="무음 판단 임계값 (dB), 기본값: -40")
    parser.add_argument("--min-silence", type=int, default=500,
                        help="최소 무음 길이 (ms), 기본값: 500")
    parser.add_argument("--output", "-o", type=str, default=None,
                        help="결과 보고서 저장 경로 (선택)")
    parser.add_argument("--no-details", action="store_true",
                        help="상세 목록 출력 생략")

    args = parser.parse_args()

    print("=" * 60)
    print("무음 구간 감지 스크립트 (Silence Detection)")
    print("=" * 60)

    try:
        # 1. 오디오 로드
        audio = load_audio(args.file)

        # 2. 무음 구간 감지
        silence_ranges, nonsilent_ranges = detect_silence_segments(
            audio,
            threshold_db=args.threshold,
            min_silence_ms=args.min_silence
        )

        # 3. 결과 분석
        stats = analyze_results(audio, silence_ranges, nonsilent_ranges)

        # 4. 결과 출력
        print_results(silence_ranges, nonsilent_ranges, stats,
                     show_details=not args.no_details)

        # 5. 보고서 생성 (선택)
        if args.output:
            generate_report(args.file, silence_ranges, nonsilent_ranges,
                          stats, args.output)

        print("\n[OK] 분석 완료!")
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
