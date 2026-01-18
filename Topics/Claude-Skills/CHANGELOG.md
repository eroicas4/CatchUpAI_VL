# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-18

### Added

#### CUA_VL Skill (M2)
- Topic 시작 기능 (`/cua-vl start`)
- Roadmap 생성 기능 (`/cua-vl roadmap`)
- Daily 학습 계획 기능 (`/cua-vl daily`)
- SKILL.md 완성

#### YouTube→MD Skill (M3)
- YouTube 자막 추출 (`youtube-transcript-api`)
- Claude API를 사용한 AI 요약 생성
- 구조화된 마크다운 문서 생성
- 5분 간격 타임라인 생성
- AI Memory 360 Tour 14개 영상 변환 완료 (463KB)
- SKILL.md, README.md, user-guide.md 완성

#### Video Edit Skill (M4)
- 무음 구간 감지 (`silence-detection.py`)
- 무음 구간 제거 (`silence-remover.py`)
- 필러 단어 감지 (`filler-detection.py`) - Whisper 사용
- 통합 편집 스크립트 (`video-editor.py`)
- 실제 영상 테스트: 30.9% 시간 단축
- SKILL.md, README.md 완성

#### Integration (M5)
- 통합 README.md 작성
- CHANGELOG.md 작성
- LICENSE (MIT) 추가
- Final Retrospective 작성

### Technical Details

- Python 3.10+ 지원
- FFmpeg 필수
- Windows UTF-8 인코딩 지원
- Claude API (claude-sonnet-4-5-20250929)
- Whisper base 모델 기본 사용

---

## [0.3.0] - 2026-01-18

### Added
- M4: Video Edit Skill 개발 완료
- 무음 구간 감지/제거 기능
- 필러 단어 감지/제거 기능 (Whisper)
- 통합 편집 스크립트
- 실제 영상 테스트 (3분 34초 → 2분 28초)

---

## [0.2.0] - 2026-01-11

### Added
- M3: YouTube→MD Skill 개발 완료
- AI Memory 360 Tour 14개 영상 MD 변환
- vl_materials 폴더 구조 (Silicon Valley, Seattle)

---

## [0.1.0] - 2026-01-10

### Added
- M1: Claude Skills 기본 개념 학습 완료
- M2: CUA_VL Skill 개발 완료
- Hello Skill 예제
- CUA_VL Skill vs Repository 비교 분석

---

## [0.0.1] - 2026-01-04

### Added
- 프로젝트 초기화
- Topic 정보 및 Roadmap 생성
- CUA_VL 방법론 프롬프트 템플릿
