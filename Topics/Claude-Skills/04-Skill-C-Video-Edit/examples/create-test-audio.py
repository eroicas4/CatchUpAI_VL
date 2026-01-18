#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
테스트용 오디오 파일 생성 스크립트

무음 구간 감지 테스트를 위한 샘플 오디오를 생성합니다.
- 음성 구간 (톤 신호)과 무음 구간이 번갈아 나타나는 오디오
- 총 30초 길이

사용법:
    python create-test-audio.py

작성일: 2026-01-18
"""

import sys
import io
import os

# Windows UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    from pydub import AudioSegment
    from pydub.generators import Sine
except ImportError:
    print("[Error] pydub 라이브러리가 설치되지 않았습니다.")
    print("        pip install pydub 명령어로 설치해주세요.")
    sys.exit(1)


def create_test_audio(output_path="test_audio.mp3"):
    """테스트용 오디오 파일 생성"""
    print("=" * 60)
    print("테스트용 오디오 파일 생성")
    print("=" * 60)

    # 오디오 세그먼트 정의 (밀리초 단위)
    segments = [
        ("tone", 3000),     # 3초 톤
        ("silence", 1000),  # 1초 무음
        ("tone", 5000),     # 5초 톤
        ("silence", 2000),  # 2초 무음
        ("tone", 2000),     # 2초 톤
        ("silence", 500),   # 0.5초 무음 (짧음)
        ("tone", 4000),     # 4초 톤
        ("silence", 3000),  # 3초 무음
        ("tone", 3000),     # 3초 톤
        ("silence", 1500),  # 1.5초 무음
        ("tone", 4000),     # 4초 톤
    ]

    print("\n[Create] 오디오 구간 생성 중...")

    combined = AudioSegment.empty()

    for i, (seg_type, duration) in enumerate(segments):
        if seg_type == "tone":
            # 440Hz 사인파 생성 (A4 음)
            segment = Sine(440).to_audio_segment(duration=duration)
            segment = segment - 10  # 볼륨 낮추기 (-10dB)
            print(f"  [{i+1:2d}] 톤: {duration/1000:.1f}초")
        else:
            # 무음 생성
            segment = AudioSegment.silent(duration=duration)
            print(f"  [{i+1:2d}] 무음: {duration/1000:.1f}초")

        combined += segment

    print(f"\n[Info] 총 길이: {len(combined)/1000:.1f}초")

    # 예상 무음 구간 계산
    expected_silence = sum(d for t, d in segments if t == "silence")
    expected_silence_count = sum(1 for t, d in segments if t == "silence" and d >= 500)
    print(f"[Info] 예상 무음 총 시간: {expected_silence/1000:.1f}초")
    print(f"[Info] 예상 무음 구간 수 (500ms 이상): {expected_silence_count}개")

    # 파일 저장
    print(f"\n[Save] 저장 중: {output_path}")
    combined.export(output_path, format="mp3")
    print(f"[OK] 저장 완료!")

    # 파일 크기 확인
    file_size = os.path.getsize(output_path)
    print(f"[Info] 파일 크기: {file_size / 1024:.1f} KB")

    print("\n" + "=" * 60)
    print("테스트 명령어:")
    print(f"  python silence-detection.py {output_path}")
    print("=" * 60)

    return output_path


if __name__ == "__main__":
    # 현재 스크립트 디렉토리에 테스트 파일 생성
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "test_audio.mp3")

    create_test_audio(output_path)
