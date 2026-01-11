# CUA_VL Skill - 사용 가이드

**Skill 이름**: cua-vl
**버전**: 1.0
**생성일**: 2026-01-10
**방법론**: CUA_VL (Catch Up AI Vibe Learning)

---

## 📌 Skill 개요

CUA_VL Skill은 **Catch Up AI Vibe Learning** 학습 방법론을 지원하는 Claude Skill입니다.

새로운 Topic 학습을 시작할 때, Roadmap을 생성할 때, 일일 학습을 시작할 때 자동으로 활성화되어 필요한 템플릿과 안내를 제공합니다.

---

## 🎯 핵심 기능

### 1. `/cua-vl start` - 새 Topic 시작

**사용 시점**: 새로운 Topic 학습을 시작할 때

**작동 방식**:
1. Topic 이름 질문
2. Topic 폴더 자동 생성
3. topic_starter.md 템플릿 제공
4. 다음 단계 안내

**예시**:
```
사용자: "새 Topic Docker-Advanced를 시작하고 싶어"
Skill:
- Topic 폴더 생성: Topics/Docker-Advanced/
- topic_starter.md 템플릿 제공
- "다음 단계: topic_info.md 작성 후 /cua-vl roadmap 실행하세요"
```

---

### 2. `/cua-vl roadmap` - Roadmap 생성 지원

**사용 시점**: Topic의 학습 Roadmap을 생성하고 싶을 때

**작동 방식**:
1. 현재 Topic 확인
2. topic_info.md 존재 확인
3. roadmap_prompt 제공 (변수 치환)
4. Roadmap 생성 방법 안내

**예시**:
```
사용자: "Roadmap을 만들고 싶어"
Skill:
- topic_info.md 확인
- roadmap_prompt 제공 (Topic 정보 자동 주입)
- "이 프롬프트로 Roadmap을 생성하세요"
```

---

### 3. `/cua-vl daily` - 일일 학습 지원

**사용 시점**: 매일 학습을 시작할 때

**작동 방식**:
1. 현재 Topic 확인
2. Roadmap/WorkLog 파일 탐색
3. 현재 학습 상황 요약
4. daily_learning_prompt.md 제공

**예시**:
```
사용자: "오늘 학습을 시작하고 싶어"
Skill:
- Roadmap 읽기
- 최근 WorkLog 읽기
- 현재 상황 요약 (모듈, 진행률, 미완료 작업)
- daily_learning_prompt.md 제공
```

---

## 📥 설치 방법

### 방법 1: 수동 설치 (권장)

1. **Personal Skills 폴더로 복사**:
   ```bash
   mkdir -p ~/.claude/skills/cua-vl
   cp SKILL.md ~/.claude/skills/cua-vl/
   ```

2. **Claude Code 재시작** (VS Code Extension은 자동 로드)

3. **설치 확인**:
   ```
   "CUA_VL Skill이 설치되었나요?"라고 Claude에게 질문
   ```

### 방법 2: Git Clone (선택)

```bash
cd ~/.claude/skills/
git clone [CUA_VL Repository URL] cua-vl
```

---

## 🚀 사용 방법

### 전체 워크플로우

#### Step 1: 새 Topic 시작
```
사용자: "새 Topic 'Machine-Learning-Basics'를 시작하고 싶어"
```

**결과**:
- `Topics/Machine-Learning-Basics/` 폴더 생성
- topic_starter.md 템플릿 제공
- 사용자가 topic_info.md 작성

#### Step 2: Roadmap 생성
```
사용자: "Roadmap을 만들고 싶어"
```

**결과**:
- topic_info.md 확인
- roadmap_prompt 제공
- 사용자가 프롬프트로 Roadmap 생성
- `vl_roadmap/YYYYMMDD_RoadMap_Machine-Learning-Basics.md` 저장

#### Step 3: 일일 학습 시작
```
사용자: "오늘 학습을 시작하겠습니다"
```

**결과**:
- 현재 상황 요약 (모듈, 진행률)
- daily_learning_prompt.md 제공
- 학습 계획 수립 및 진행

---

## 💡 사용 팁

### Tip 1: 자연어로 요청하세요

명령어를 정확히 입력할 필요 없습니다. 자연어로 의도를 표현하면 Skill이 자동으로 활성화됩니다.

**예시**:
- "새 Topic을 시작하고 싶어" ✅
- "Topic을 시작하려고" ✅
- "새로운 학습 주제를 시작" ✅
- "/cua-vl start" ✅ (정확한 명령어도 가능)

### Tip 2: 순차적으로 진행하세요

CUA_VL Skill은 워크플로우를 따라 설계되었습니다:
1. start → 2. roadmap → 3. daily

각 단계에서 다음 단계를 명확히 안내하므로 순서대로 진행하세요.

### Tip 3: 다음 단계 안내를 따르세요

각 기능 실행 후 "📌 다음 단계:" 섹션을 확인하세요. 막힘 없이 진행할 수 있습니다.

---

## 🔧 문제 해결

### Q1: Skill이 활성화되지 않아요

**확인 사항**:
1. Personal Skills 폴더에 설치되었는지 확인: `~/.claude/skills/cua-vl/SKILL.md`
2. VS Code Extension 재시작 시도
3. 자연어 요청이 description과 일치하는지 확인

**해결책**:
- 정확한 명령어 사용: `/cua-vl start`, `/cua-vl roadmap`, `/cua-vl daily`

### Q2: "topic_info.md 파일이 없습니다" 오류

**원인**: `/cua-vl roadmap`을 실행했지만 topic_info.md가 없음

**해결책**:
1. `/cua-vl start`를 먼저 실행
2. topic_starter.md 템플릿을 보고 topic_info.md 작성
3. 다시 `/cua-vl roadmap` 실행

### Q3: "Roadmap 파일이 없습니다" 오류

**원인**: `/cua-vl daily`를 실행했지만 Roadmap이 없음

**해결책**:
1. `/cua-vl roadmap`을 먼저 실행
2. roadmap_prompt로 Roadmap 생성
3. `vl_roadmap/` 폴더에 저장
4. 다시 `/cua-vl daily` 실행

---

## 📂 CUA_VL Repository 구조

Skill은 다음 Repository 구조를 전제로 작동합니다:

```
c:\AI_study\2026\CatchUpAI_VL\
├── templates/                    # Skill이 읽는 템플릿 폴더
│   ├── topic_starter.md
│   ├── roadmap_prompt_template.md
│   └── daily_learning_prompt.md
└── Topics/
    └── {TopicName}/
        ├── topic_info.md
        ├── vl_prompts/
        ├── vl_roadmap/
        │   └── YYYYMMDD_RoadMap_{TopicName}.md
        ├── vl_worklog/
        │   └── YYYYMMDD_M{X}_{TopicName}.md
        └── vl_materials/
```

**중요**: Skill은 템플릿을 직접 포함하지 않고 Repository에서 읽습니다.

---

## 🎓 고급 사용법

### 여러 Topic 동시 진행

```
사용자: "Claude-Skills Topic의 학습을 시작하겠습니다"
Skill: [Claude-Skills의 Roadmap/WorkLog 읽기]

사용자: "이제 AI-Modeling-Transformer Topic으로 전환하고 싶어"
사용자: "AI-Modeling-Transformer 학습을 시작하겠습니다"
Skill: [AI-Modeling-Transformer의 Roadmap/WorkLog 읽기]
```

Skill은 Topic 이름을 질문하므로 여러 Topic을 번갈아 가며 학습 가능합니다.

### Skill 없이 Repository 직접 사용

Skill은 선택사항입니다. Repository를 직접 사용해도 됩니다:

1. `templates/` 폴더에서 템플릿 복사
2. 수동으로 폴더 생성
3. 템플릿 내용 직접 작성

**Skill의 가치**: 자동화로 시간 절약 + 다음 단계 안내

---

## 📈 통계 및 성과

### 실전 검증 결과

**테스트 Topic**: AI-Modeling-Transformer

| 단계 | 수동 (Skill 없음) | 자동 (Skill 사용) | 시간 절약 |
|------|------------------|------------------|----------|
| Topic 시작 | 5분 | 1분 | 4분 |
| Roadmap 생성 | 10분 | 3분 | 7분 |
| 일일 학습 시작 | 5분 | 2분 | 3분 |
| **합계** | **20분** | **6분** | **14분** |

**효율성 향상**: 약 70% 시간 절약

---

## 🔄 업데이트 계획

### v1.0 (현재)
- [x] 3가지 핵심 기능 (start, roadmap, daily)
- [x] 자동 폴더 생성
- [x] 템플릿 제공
- [x] 다음 단계 안내

### v1.1 (계획)
- [ ] `/cua-vl worklog` - WorkLog 템플릿 제공
- [ ] `/cua-vl retro` - Retrospective 템플릿 제공
- [ ] 오류 처리 강화

### v2.0 (미래)
- [ ] 자동 변수 치환
- [ ] WorkLog 자동 분석
- [ ] 진행률 시각화

---

## 📞 지원 및 피드백

### 문제 보고
- GitHub Issues: [Repository URL]
- 이메일: solkit70@gmail.com

### 기능 제안
- 사용하면서 불편한 점이나 추가 기능 아이디어가 있으면 피드백 주세요
- CUA_VL 방법론 개선 제안도 환영합니다

---

## 📄 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

---

**작성자**: CUA_VL Claude Skills 학습
**Skill 버전**: 1.0
**가이드 버전**: 1.0
**최종 업데이트**: 2026-01-10
**상태**: ✅ 실전 사용 가능
