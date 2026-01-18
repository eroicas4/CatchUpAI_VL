#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
필러 단어 감지 스크립트 (Filler Word Detection)

이 스크립트는 OpenAI Whisper를 사용하여 음성을 인식하고,
필러 단어 (um, uh, 음, 어 등)를 감지합니다.

사용법:
    python filler-detection.py <파일경로> [옵션]

예시:
    python filler-detection.py video.mp4
    python filler-detection.py audio.mp3 --model base --language en
    python filler-detection.py video.mp4 --output report.md

옵션:
    --model: Whisper 모델 (tiny, base, small, medium, large), 기본값: base
    --language: 언어 코드 (en, ko 등), 기본값: 자동 감지
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
    import whisper
except ImportError:
    print("[Error] whisper 라이브러리가 설치되지 않았습니다.")
    print("        pip install openai-whisper 명령어로 설치해주세요.")
    sys.exit(1)

# 필러 단어 목록 (언어별)
FILLER_WORDS = {
    'en': [
        'um', 'uh', 'er', 'ah', 'eh', 'hmm', 'mm',
        'like', 'you know', 'i mean', 'so', 'well',
        'basically', 'actually', 'literally', 'right',
    ],
    'ko': [
        '음', '어', '아', '그', '저', '이제', '뭐',
        '근데', '그래서', '그러니까', '막', '좀',
        '진짜', '약간', '되게',
    ],
    'universal': [
        'um', 'uh', 'er', 'ah', 'mm', 'hmm',
    ]
}


def format_timestamp(seconds):
    """초를 HH:MM:SS.mmm 형식으로 변환"""
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    ms = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{ms:03d}"


def format_duration(seconds):
    """초를 읽기 쉬운 형식으로 변환"""
    if seconds < 1:
        return f"{int(seconds * 1000)}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    else:
        return f"{seconds/60:.1f}m"


def load_whisper_model(model_name="base"):
    """Whisper 모델 로드"""
    print(f"\n[Load] Whisper 모델 로드 중: {model_name}")
    print("       (첫 실행 시 모델 다운로드가 필요할 수 있습니다)")

    try:
        model = whisper.load_model(model_name)
        print(f"[OK] 모델 로드 완료!")
        return model
    except Exception as e:
        raise RuntimeError(f"모델 로드 실패: {e}")


def transcribe_audio(model, file_path, language=None):
    """오디오 파일 음성 인식"""
    print(f"\n[Transcribe] 음성 인식 중: {file_path}")
    print("             (파일 크기에 따라 시간이 걸릴 수 있습니다)")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    try:
        # 음성 인식 실행
        options = {
            "word_timestamps": True,  # 단어별 타임스탬프 활성화
            "verbose": False,
        }
        if language:
            options["language"] = language

        result = model.transcribe(file_path, **options)

        detected_language = result.get("language", "unknown")
        print(f"[OK] 음성 인식 완료!")
        print(f"     - 감지된 언어: {detected_language}")
        print(f"     - 세그먼트 수: {len(result.get('segments', []))}")

        return result, detected_language

    except Exception as e:
        raise RuntimeError(f"음성 인식 실패: {e}")


def detect_filler_words(transcription_result, detected_language):
    """필러 단어 감지"""
    print(f"\n[Detect] 필러 단어 감지 중...")

    # 언어에 맞는 필러 단어 목록 선택
    filler_list = FILLER_WORDS.get(detected_language, []) + FILLER_WORDS['universal']
    filler_list = list(set(word.lower() for word in filler_list))

    print(f"         - 검색 대상 필러 단어: {len(filler_list)}개")

    filler_instances = []
    segments = transcription_result.get('segments', [])

    for segment in segments:
        words = segment.get('words', [])

        for word_info in words:
            word = word_info.get('word', '').strip().lower()
            # 문장 부호 제거
            word_clean = ''.join(c for c in word if c.isalnum() or c in ['\'', '-'])

            if word_clean in filler_list:
                filler_instances.append({
                    'word': word_info.get('word', '').strip(),
                    'start': word_info.get('start', 0),
                    'end': word_info.get('end', 0),
                    'duration': word_info.get('end', 0) - word_info.get('start', 0),
                    'segment_text': segment.get('text', '').strip(),
                })

    print(f"[OK] 감지 완료! - {len(filler_instances)}개 발견")

    return filler_instances


def analyze_results(filler_instances, total_duration=None):
    """분석 결과 계산"""
    if not filler_instances:
        return {
            'total_fillers': 0,
            'total_filler_duration': 0,
            'filler_ratio': 0,
            'filler_frequency': {},
            'avg_filler_duration': 0,
        }

    total_filler_duration = sum(f['duration'] for f in filler_instances)

    # 필러 단어별 빈도 계산
    filler_frequency = {}
    for f in filler_instances:
        word = f['word'].lower().strip()
        filler_frequency[word] = filler_frequency.get(word, 0) + 1

    # 비율 계산 (총 시간 대비)
    filler_ratio = 0
    if total_duration and total_duration > 0:
        filler_ratio = (total_filler_duration / total_duration * 100)

    return {
        'total_fillers': len(filler_instances),
        'total_filler_duration': total_filler_duration,
        'filler_ratio': filler_ratio,
        'filler_frequency': filler_frequency,
        'avg_filler_duration': total_filler_duration / len(filler_instances) if filler_instances else 0,
    }


def print_results(filler_instances, stats, show_details=True):
    """결과 출력"""
    print("\n" + "=" * 60)
    print("필러 단어 감지 결과")
    print("=" * 60)

    print(f"\n[Summary] 요약:")
    print(f"  - 총 필러 단어 수: {stats['total_fillers']}개")
    print(f"  - 필러 총 시간: {format_duration(stats['total_filler_duration'])}")
    print(f"  - 평균 필러 길이: {format_duration(stats['avg_filler_duration'])}")

    if stats['filler_frequency']:
        print(f"\n[Frequency] 필러 단어별 빈도:")
        sorted_freq = sorted(stats['filler_frequency'].items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_freq[:10]:
            print(f"  - \"{word}\": {count}회")

    if show_details and filler_instances:
        print(f"\n[Details] 필러 단어 상세 (상위 15개):")
        print("-" * 70)
        print(f"{'번호':>4} | {'시작':>12} | {'종료':>12} | {'단어':>10} | 문맥")
        print("-" * 70)

        for i, f in enumerate(filler_instances[:15], 1):
            context = f['segment_text'][:30] + "..." if len(f['segment_text']) > 30 else f['segment_text']
            print(f"{i:>4} | {format_timestamp(f['start']):>12} | {format_timestamp(f['end']):>12} | {f['word']:>10} | {context}")

    print("\n" + "=" * 60)


def generate_report(file_path, filler_instances, stats, output_path=None):
    """분석 보고서 생성"""
    report = []
    report.append("# 필러 단어 감지 보고서")
    report.append("")
    report.append(f"**파일**: {file_path}")
    report.append(f"**분석일**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("## 요약")
    report.append("")
    report.append(f"| 항목 | 값 |")
    report.append(f"|------|------|")
    report.append(f"| 총 필러 단어 수 | {stats['total_fillers']}개 |")
    report.append(f"| 필러 총 시간 | {format_duration(stats['total_filler_duration'])} |")
    report.append(f"| 평균 필러 길이 | {format_duration(stats['avg_filler_duration'])} |")
    report.append("")

    if stats['filler_frequency']:
        report.append("## 필러 단어별 빈도")
        report.append("")
        report.append(f"| 단어 | 횟수 |")
        report.append(f"|------|------|")
        sorted_freq = sorted(stats['filler_frequency'].items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_freq:
            report.append(f"| {word} | {count} |")
        report.append("")

    report.append("## 필러 단어 상세")
    report.append("")
    report.append(f"| 번호 | 시작 | 종료 | 단어 | 문맥 |")
    report.append(f"|------|------|------|------|------|")

    for i, f in enumerate(filler_instances, 1):
        context = f['segment_text'][:40].replace("|", "\\|")
        report.append(f"| {i} | {format_timestamp(f['start'])} | {format_timestamp(f['end'])} | {f['word']} | {context} |")

    report_text = "\n".join(report)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"\n[OK] 보고서 저장: {output_path}")

    return report_text


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="영상/오디오 파일에서 필러 단어를 감지합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python filler-detection.py video.mp4
  python filler-detection.py audio.mp3 --model small --language en
  python filler-detection.py video.mp4 --output report.md

모델 크기:
  tiny   - 가장 빠름, 정확도 낮음 (~1GB VRAM)
  base   - 빠름, 기본 정확도 (~1GB VRAM) [기본값]
  small  - 중간, 좋은 정확도 (~2GB VRAM)
  medium - 느림, 높은 정확도 (~5GB VRAM)
  large  - 가장 느림, 최고 정확도 (~10GB VRAM)
        """
    )
    parser.add_argument("file", help="분석할 파일 경로 (영상 또는 오디오)")
    parser.add_argument("--model", type=str, default="base",
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper 모델 크기, 기본값: base")
    parser.add_argument("--language", type=str, default=None,
                        help="언어 코드 (en, ko 등), 기본값: 자동 감지")
    parser.add_argument("--output", "-o", type=str, default=None,
                        help="결과 보고서 저장 경로 (선택)")
    parser.add_argument("--no-details", action="store_true",
                        help="상세 목록 출력 생략")

    args = parser.parse_args()

    print("=" * 60)
    print("필러 단어 감지 스크립트 (Filler Word Detection)")
    print("=" * 60)

    try:
        # 1. Whisper 모델 로드
        model = load_whisper_model(args.model)

        # 2. 음성 인식
        result, detected_language = transcribe_audio(model, args.file, args.language)

        # 3. 필러 단어 감지
        filler_instances = detect_filler_words(result, detected_language)

        # 4. 결과 분석
        # 총 시간 계산 (마지막 세그먼트의 종료 시간)
        segments = result.get('segments', [])
        total_duration = segments[-1].get('end', 0) if segments else 0

        stats = analyze_results(filler_instances, total_duration)

        # 5. 결과 출력
        print_results(filler_instances, stats, show_details=not args.no_details)

        # 6. 보고서 생성 (선택)
        if args.output:
            generate_report(args.file, filler_instances, stats, args.output)

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
