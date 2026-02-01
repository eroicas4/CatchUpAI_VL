# Video Edit Skill

영상 또는 오디오 파일에서 무음 구간과 필러 단어를 자동으로 제거하여 편집된 파일을 생성합니다.

## Description

이 Skill은 영상/오디오 편집을 자동화합니다:
- **무음 구간 제거**: 지정된 임계값 이하의 무음 구간을 자동 감지하고 제거
- **필러 단어 제거**: "um", "uh", "음", "어" 등의 필러 단어를 AI 음성 인식으로 감지하고 제거
- **통합 편집**: 무음과 필러를 동시에 제거하여 깔끔한 결과물 생성
- **편집 보고서**: 원본 대비 단축 시간, 제거 내역 등 상세 보고서 생성

## When to Use

- YouTube 영상 제작 시 불필요한 무음 구간 제거
- 팟캐스트나 강의 녹음에서 필러 단어 정리
- 인터뷰 영상의 빠른 편집
- 영상 편집 시간을 크게 단축하고 싶을 때

## Prerequisites

이 Skill을 사용하기 전에 다음이 설치되어 있어야 합니다:

1. **FFmpeg**: 영상 처리용
   - Windows: `choco install ffmpeg` 또는 https://ffmpeg.org/download.html
   - Mac: `brew install ffmpeg`
   - Linux: `apt install ffmpeg`

2. **Python 라이브러리**:
   ```bash
   pip install pydub ffmpeg-python openai-whisper
   ```

3. **Whisper 모델** (필러 단어 감지 시):
   - 첫 실행 시 자동 다운로드됨
   - 모델 크기: tiny (~1GB), base (~1GB), small (~2GB)

## Usage

### 기본 사용법

사용자가 다음과 같이 요청하면 이 Skill을 실행합니다:
- "영상에서 무음 구간 제거해줘"
- "이 오디오 파일의 필러 단어 정리해줘"
- "video.mp4 파일 편집해줘"

### 실행 단계

#### Step 1: 파일 확인

사용자가 제공한 파일 경로를 확인합니다.

```
지원 형식:
- 영상: .mp4, .mkv, .avi, .mov, .webm
- 오디오: .mp3, .wav, .m4a, .ogg, .flac
```

#### Step 2: 편집 옵션 확인

사용자에게 편집 옵션을 확인합니다:

1. **무음 구간 제거** (기본 권장)
   - 임계값: -40dB (조용한 구간 기준)
   - 최소 무음 길이: 500ms

2. **필러 단어 제거** (Whisper 필요)
   - 모델: base (권장), tiny (빠름), small (정확)
   - 언어: 자동 감지 또는 지정 (en, ko)

3. **모두 제거** (권장)
   - 무음 + 필러 동시 제거

#### Step 3: 스크립트 실행

`video-editor.py` 스크립트를 실행합니다.

**무음만 제거:**
```bash
python video-editor.py "파일경로" --remove-silence
```

**필러만 제거:**
```bash
python video-editor.py "파일경로" --remove-fillers --model base
```

**모두 제거 (권장):**
```bash
python video-editor.py "파일경로" --all --model base
```

**옵션 설명:**
- `--remove-silence`: 무음 구간 제거
- `--remove-fillers`: 필러 단어 제거
- `--all`: 무음 + 필러 모두 제거
- `--threshold -40`: 무음 판단 임계값 (dB)
- `--min-silence 500`: 최소 무음 길이 (ms)
- `--model base`: Whisper 모델 (tiny/base/small)
- `--output "출력경로"`: 출력 파일 경로 지정

#### Step 4: 결과 확인

편집 완료 후:
1. 편집된 파일: `원본파일명_edited.확장자`
2. 편집 보고서: `원본파일명_edited_report.md`

보고서에는 다음 정보가 포함됩니다:
- 원본 길이 vs 편집 후 길이
- 단축 시간 및 비율
- 제거된 무음 구간 수
- 제거된 필러 단어 수

## Examples

### 예시 1: 무음 구간만 제거

```
사용자: video.mp4 파일에서 무음 구간 제거해줘

Claude: 영상 편집을 시작하겠습니다.

[실행]
python video-editor.py "video.mp4" --remove-silence

[결과]
- 원본: 10분 30초
- 편집 후: 8분 45초
- 단축: 1분 45초 (16.7%)
- 제거된 무음: 12개 구간
```

### 예시 2: 필러 단어만 제거

```
사용자: 이 오디오에서 "음", "어" 같은 필러 단어 정리해줘

Claude: 필러 단어 제거를 시작하겠습니다. Whisper로 음성 인식 후 처리합니다.

[실행]
python video-editor.py "audio.mp3" --remove-fillers --model base --language ko

[결과]
- 원본: 5분 20초
- 편집 후: 4분 50초
- 단축: 30초 (9.4%)
- 제거된 필러: 28개 단어
```


### 예시 3: 모두 제거 (권장)

```
사용자: YouTube 영상 올리기 전에 깔끔하게 편집해줘

Claude: 무음 구간과 필러 단어를 모두 제거하여 깔끔한 영상을 만들겠습니다.

[실행]
python video-editor.py "youtube_raw.mp4" --all --model base

[결과]
- 원본: 15분 00초
- 편집 후: 11분 30초
- 단축: 3분 30초 (23.3%)
- 제거된 무음: 18개 구간
- 제거된 필러: 45개 단어

편집된 파일: youtube_raw_edited.mp4
보고서: youtube_raw_edited_report.md
```

## Troubleshooting

### 문제 1: FFmpeg를 찾을 수 없음

```
[Error] FFmpeg가 설치되지 않았습니다.
```

**해결**: FFmpeg를 설치하고 PATH에 추가
- Windows: `choco install ffmpeg`
- Mac: `brew install ffmpeg`

### 문제 2: pydub 모듈 없음

```
[Error] pydub 라이브러리가 설치되지 않았습니다.
```

**해결**:
```bash
pip install pydub
```

### 문제 3: Whisper 모델 다운로드 실패

```
[Error] 모델 로드 실패
```

**해결**: 인터넷 연결 확인 후 다시 시도. 모델은 `~/.cache/whisper/`에 저장됨

### 문제 4: 영상 편집 시간이 너무 오래 걸림

**해결**:
- 더 작은 Whisper 모델 사용: `--model tiny`
- 필러 감지 없이 무음만 제거: `--remove-silence`
- 긴 영상은 분할하여 처리

### 문제 5: 편집 결과가 부자연스러움

**해결**: 파라미터 조정
- 무음 임계값 조정: `--threshold -35` (더 민감하게)
- 최소 무음 길이 증가: `--min-silence 800` (짧은 무음 유지)

## Script Location

스크립트 위치:
```
04-Skill-C-Video-Edit/
├── examples/
│   ├── video-editor.py          # 통합 편집 스크립트 (메인)
│   ├── silence-detection.py     # 무음 감지 (분석용)
│   ├── silence-remover.py       # 무음 제거 (단독)
│   ├── filler-detection.py      # 필러 감지 (분석용)
│   └── video-edit-skill/
│       └── SKILL.md             # 이 파일
└── outputs/
    └── (편집된 파일들)
```

## Notes

1. **처리 시간**: 영상 길이와 Whisper 모델에 따라 다름
   - 무음만: 빠름 (실시간의 1/10)
   - 필러 포함: 느림 (실시간의 1~3배)

2. **품질**: FFmpeg로 재인코딩되므로 약간의 품질 손실 가능
   - 원본 보존이 필요하면 백업 권장

3. **언어**: 필러 감지는 영어와 한국어 최적화
   - 다른 언어는 범용 필러 단어만 감지

4. **GPU 가속**: Whisper는 CUDA GPU가 있으면 자동 활용
   - CPU만 있어도 동작하나 느림

---

**작성일**: 2026-01-18
**모듈**: M4 - Skill C: 영상 편집 자동화 Skill
**방법론**: CUA_VL (Catch Up AI Vibe Learning)
