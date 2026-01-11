# CUA_VL Skill MVP 설계 문서

**버전**: 1.0
**작성일**: 2026-01-10
**모듈**: M2 - Skill A: CUA_VL Skill 개발
**방법론**: CUA_VL (Catch Up AI Vibe Learning)

---

## 📌 설계 철학

### 핵심 원칙

**1. Repository 우선, Skill은 보조 도구**
- CUA_VL의 본질: "학습 방법론 + 교과서"
- Repository가 메인, Skill은 사용자 경험 개선용
- 모든 템플릿과 문서는 Repository에 유지

**2. 간단함의 힘**
- SKILL.md 하나로 충분
- 복잡한 코드나 빌드 과정 불필요
- 명확한 지침으로 Claude가 실행

**3. 점진적 개선**
- MVP로 시작 (최소 3가지 기능)
- 사용자 피드백 기반 개선
- 과도한 엔지니어링 지양

---

## 🎯 MVP 핵심 기능 정의

### 기능 1: `/cua-vl start` - Topic 시작

**목적**: 새로운 Topic 학습을 시작할 때 필요한 폴더 구조 및 파일 생성

**입력**:
- Topic 이름 (예: "MCP-Basics", "Claude-API")
- (선택) Topic 폴더 경로

**출력**:
- `Topics/{TopicName}/` 폴더 생성
- `topic_starter.md` 템플릿 제공
- 다음 단계 안내 (Roadmap 생성)

**동작 흐름**:
```
1. 사용자: "새 Topic을 시작하고 싶어"
2. Skill 활성화 (description 매칭)
3. Topic 이름 질문
4. 사용자: "MCP-Basics"
5. 폴더 생성: Topics/MCP-Basics/
6. topic_starter.md 템플릿 제공
7. "다음 단계: /cua-vl roadmap을 실행하세요" 안내
```

**성공 기준**:
- [ ] Topic 폴더가 올바른 위치에 생성됨
- [ ] topic_starter.md 템플릿이 제공됨
- [ ] 다음 단계가 명확히 안내됨

**구현 방법**:
- SKILL.md에 단계별 지침 작성
- Claude가 Bash tool을 사용하여 폴더 생성
- Read tool로 템플릿 읽어서 제공
- 변수 주입 안내 (Topic 이름)

---

### 기능 2: `/cua-vl roadmap` - Roadmap 생성 지원

**목적**: Topic의 Roadmap을 생성하기 위한 프롬프트 제공

**입력**:
- Topic 이름 (또는 현재 Topic 자동 감지)
- topic_info.md 존재 여부 확인

**출력**:
- `roadmap_prompt_template.md` 제공
- 변수 주입 방법 안내
- Roadmap 생성 프롬프트 완성본

**동작 흐름**:
```
1. 사용자: "Roadmap을 만들고 싶어"
2. Skill 활성화
3. 현재 Topic 확인 (topic_info.md 존재 확인)
4. roadmap_prompt_template.md 읽기
5. 변수 주입 안내 (Topic 이름, 학습 목표 등)
6. 완성된 프롬프트 제공
7. "이 프롬프트를 복사하여 새 대화에서 실행하세요" 안내
```

**성공 기준**:
- [ ] roadmap_prompt_template.md가 제공됨
- [ ] 변수 주입이 명확히 설명됨
- [ ] 사용자가 바로 사용 가능한 프롬프트 생성됨

**구현 방법**:
- topic_info.md 확인 (없으면 안내)
- Read tool로 roadmap_prompt_template.md 읽기
- 변수 치환 (Topic 이름 등)
- 최종 프롬프트 제공

---

### 기능 3: `/cua-vl daily` - 일일 학습 계획 지원

**목적**: 매일 학습을 시작할 때 필요한 프롬프트 및 안내 제공

**입력**:
- Topic 이름 (또는 현재 Topic 자동 감지)
- (선택) 가용 시간, 현재 모듈

**출력**:
- `daily_learning_prompt.md` 제공
- 현재 상황 파악 방법 안내
- 다음 단계 안내

**동작 흐름**:
```
1. 사용자: "오늘 학습을 시작하고 싶어"
2. Skill 활성화
3. 현재 Topic 확인
4. Roadmap 파일 확인 (vl_roadmap/*.md)
5. 최근 WorkLog 확인 (vl_worklog/*.md)
6. daily_learning_prompt.md 제공
7. 현재 상황 정보 요약 (모듈, 진행률 등)
8. "가용 시간을 입력하고 학습을 시작하세요" 안내
```

**성공 기준**:
- [ ] daily_learning_prompt.md가 제공됨
- [ ] 현재 학습 상황이 요약됨
- [ ] 사용자가 바로 학습 시작 가능

**구현 방법**:
- Roadmap 파일 찾기 (Glob tool)
- 최근 WorkLog 찾기 (Glob tool)
- Read tool로 상태 파악
- daily_learning_prompt.md 제공
- 현재 상황 요약 제공

---

## 🏗️ SKILL.md 구조 설계

### 메타데이터

```yaml
---
name: cua-vl
description: CUA_VL 학습 방법론을 지원합니다. 새 Topic 시작, Roadmap 생성, 일일 학습 계획 수립을 도와줍니다.
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---
```

**description 설계 이유**:
- "CUA_VL 학습 방법론" → 명확한 정체성
- "새 Topic 시작, Roadmap 생성, 일일 학습 계획" → 구체적 기능
- 사용자가 "Topic 시작", "Roadmap 만들기", "오늘 학습" 등으로 요청 시 자동 활성화

**allowed-tools 선택**:
- `Read`: 템플릿 파일 읽기
- `Write`: 파일 생성 (topic_info.md 등)
- `Bash`: 폴더 생성 (mkdir)
- `Glob`: 파일 찾기 (Roadmap, WorkLog)
- `Grep`: 내용 검색 (필요 시)

---

### 지침 구조

```markdown
# CUA_VL Skill

당신은 CUA_VL 학습 방법론을 지원하는 Assistant입니다.

## 핵심 기능

### 1. `/cua-vl start` - 새 Topic 시작
[상세 지침]

### 2. `/cua-vl roadmap` - Roadmap 생성
[상세 지침]

### 3. `/cua-vl daily` - 일일 학습
[상세 지침]

## 중요 원칙
- Repository를 메인으로 유지
- 템플릿은 c:\AI_study\2026\CatchUpAI_VL\templates\에 위치
- 사용자에게 명확한 다음 단계 안내
```

---

## 📁 폴더 구조 설계

### CUA_VL Skill 폴더

**위치**: `~/.claude/skills/cua-vl/`

```
cua-vl/
├── SKILL.md                 # 메인 Skill 파일
└── README.md                # Skill 설명 (선택)
```

**간단함의 이유**:
- SKILL.md만으로 충분
- 템플릿은 CUA_VL Repository에 유지
- Skill은 템플릿을 참조만 함

---

### M2 산출물 폴더

**위치**: `Topics/Claude-Skills/02-Skill-A-CUA-VL/`

```
02-Skill-A-CUA-VL/
├── README.md                        # M2 개요 및 결론
├── concepts/
│   ├── cua-vl-skill-design.md       # 이 파일
│   └── skill-vs-repo-decision.md    # M1 결론 참조
├── examples/
│   └── cua-vl-skill/
│       ├── SKILL.md                 # 실제 Skill 코드
│       └── README.md                # Skill 사용법
├── guides/
│   ├── user-guide.md                # 사용 가이드
│   ├── installation.md              # 설치 방법
│   └── troubleshooting.md           # 문제 해결
└── tests/
    └── integration-test.md          # 통합 테스트 결과
```

---

## 🔄 사용자 워크플로우

### Scenario 1: 완전히 새로운 Topic 시작

```
1. 사용자: "새 Topic 'Docker-Advanced'를 시작하고 싶어"
2. /cua-vl start 자동 활성화
3. Topic 폴더 생성: Topics/Docker-Advanced/
4. topic_starter.md 템플릿 제공
5. 사용자: topic_starter.md 작성
6. 사용자: "Roadmap을 만들고 싶어"
7. /cua-vl roadmap 자동 활성화
8. roadmap_prompt 제공
9. 사용자: 프롬프트로 Roadmap 생성
10. Roadmap 저장: vl_roadmap/YYYYMMDD_RoadMap_Docker-Advanced.md
```

### Scenario 2: 진행 중인 Topic의 일일 학습

```
1. 사용자: "오늘 학습을 시작하겠습니다"
2. /cua-vl daily 자동 활성화
3. 현재 Topic 확인 (Claude-Skills)
4. Roadmap 읽기 (진행 중인 모듈 확인)
5. 최근 WorkLog 읽기 (미완료 작업 확인)
6. daily_learning_prompt.md 제공
7. 현재 상황 요약 출력
8. 사용자: 가용 시간 입력
9. 학습 계획 수립 및 진행
```

---

## ⚙️ 구현 세부사항

### 기능 1: `/cua-vl start` 상세 지침

**SKILL.md 지침 예시**:
```markdown
### `/cua-vl start` - 새 Topic 시작

사용자가 새로운 Topic을 시작하고 싶어할 때 이 기능을 실행하세요.

**단계**:
1. Topic 이름을 질문하세요
   - "어떤 Topic을 시작하시겠습니까?"
   - 예: "MCP-Basics", "Claude-API"

2. Topic 폴더 생성
   - Bash tool 사용: `mkdir -p "c:\AI_study\2026\CatchUpAI_VL\Topics\{TopicName}"`
   - 성공 메시지 출력

3. topic_starter.md 템플릿 제공
   - Read tool로 읽기: `c:\AI_study\2026\CatchUpAI_VL\templates\topic_starter.md`
   - 전체 내용 출력
   - 사용자에게 작성 안내

4. 다음 단계 안내
   - "topic_starter.md를 작성하신 후, /cua-vl roadmap을 실행하여 Roadmap을 생성하세요"
```

---

### 기능 2: `/cua-vl roadmap` 상세 지침

**SKILL.md 지침 예시**:
```markdown
### `/cua-vl roadmap` - Roadmap 생성

사용자가 Roadmap을 만들고 싶어할 때 이 기능을 실행하세요.

**단계**:
1. 현재 Topic 확인
   - Glob tool로 현재 작업 중인 Topic 찾기
   - 또는 사용자에게 질문

2. topic_info.md 확인
   - Read tool로 `Topics/{TopicName}/topic_info.md` 읽기
   - 없으면: "/cua-vl start를 먼저 실행하세요" 안내

3. roadmap_prompt_template.md 제공
   - Read tool로 읽기: `c:\AI_study\2026\CatchUpAI_VL\templates\roadmap_prompt_template.md`
   - Topic 이름으로 변수 치환
   - 완성된 프롬프트 출력

4. 사용자 안내
   - "위 프롬프트를 복사하여 새 대화에서 실행하세요"
   - "생성된 Roadmap은 vl_roadmap/ 폴더에 저장하세요"
```

---

### 기능 3: `/cua-vl daily` 상세 지침

**SKILL.md 지침 예시**:
```markdown
### `/cua-vl daily` - 일일 학습 시작

사용자가 오늘의 학습을 시작하고 싶어할 때 이 기능을 실행하세요.

**단계**:
1. 현재 Topic 확인
   - 현재 작업 디렉토리에서 Topic 이름 추출
   - 또는 사용자에게 질문

2. Roadmap 파일 찾기
   - Glob tool: `Topics/{TopicName}/vl_roadmap/*.md`
   - 가장 최근 Roadmap 읽기

3. 최근 WorkLog 찾기
   - Glob tool: `Topics/{TopicName}/vl_worklog/*.md`
   - 가장 최근 WorkLog 읽기
   - Tomorrow's focus 확인

4. 현재 상황 요약
   - Topic 이름
   - 현재 모듈 (Roadmap에서 확인)
   - 진행률 (완료된 모듈 / 전체 모듈)
   - 미완료 작업 (WorkLog에서 확인)

5. daily_learning_prompt.md 제공
   - Read tool로 읽기
   - 사용자에게 제공

6. 다음 단계 안내
   - "가용 시간과 현재 상태를 입력하고 학습 계획을 수립하세요"
```

---

## 🧪 테스트 계획

### 단위 테스트

**기능 1 테스트**:
- [ ] Topic 폴더 생성 확인
- [ ] topic_starter.md 템플릿 제공 확인
- [ ] 다음 단계 안내 출력 확인

**기능 2 테스트**:
- [ ] Roadmap 프롬프트 제공 확인
- [ ] 변수 치환 정확성 확인
- [ ] topic_info.md 없을 때 안내 확인

**기능 3 테스트**:
- [ ] Roadmap/WorkLog 파일 찾기 확인
- [ ] 현재 상황 요약 정확성 확인
- [ ] daily_learning_prompt.md 제공 확인

---

### 통합 테스트

**Scenario: 새 Topic "TestTopic" 전체 플로우**

1. **시작**:
   - 요청: "새 Topic TestTopic을 시작하고 싶어"
   - 확인: `Topics/TestTopic/` 폴더 생성됨
   - 확인: topic_starter.md 템플릿 제공됨

2. **Roadmap 생성**:
   - topic_starter.md 작성 (간단하게)
   - 요청: "Roadmap을 만들고 싶어"
   - 확인: roadmap_prompt 제공됨
   - Roadmap 생성 및 저장

3. **일일 학습**:
   - 요청: "오늘 학습을 시작하겠습니다"
   - 확인: 현재 상황 요약 출력됨
   - 확인: daily_learning_prompt.md 제공됨

---

## 📊 성공 지표

### 기술적 성공

- [ ] 3가지 핵심 기능 모두 정상 동작
- [ ] Personal Skills 폴더에 설치 완료
- [ ] 통합 테스트 통과
- [ ] 오류 없이 전체 워크플로우 실행

### 사용자 경험

- [ ] 명령어 없이 자연어로 요청 가능 (description 매칭)
- [ ] 다음 단계가 명확히 안내됨
- [ ] 템플릿이 즉시 제공됨
- [ ] Repository와의 통합이 원활함

### 문서화

- [ ] README.md가 "교과서 수준"
- [ ] 다른 사람이 README만 보고 사용 가능
- [ ] 설치 방법이 명확함
- [ ] 예제가 실행 가능함

---

## 🚀 향후 개선 방향

### Phase 1: MVP (현재)
- 3가지 핵심 기능만 구현
- 간단하고 명확한 동작
- 사용자 피드백 수집

### Phase 2: 기능 확장 (선택)
- `/cua-vl worklog` - WorkLog 템플릿 제공
- `/cua-vl retro` - Retrospective 템플릿 제공
- `/cua-vl status` - 전체 학습 진행 상황 확인

### Phase 3: 고급 기능 (선택)
- 자동 변수 치환 (AI가 직접 처리)
- WorkLog 자동 분석 및 요약
- 진행률 시각화

---

## 💡 설계 인사이트

### 인사이트 1: "Skill은 Gateway, Repository는 Core"

**깨달음**:
- Skill은 사용자와 Repository를 연결하는 관문
- 실제 데이터와 템플릿은 모두 Repository에
- Skill은 안내자 역할만

**적용**:
- SKILL.md는 지침만 포함
- 모든 템플릿은 Repository 참조
- Skill 업데이트 없이도 템플릿 개선 가능

---

### 인사이트 2: "명확한 다음 단계가 핵심"

**깨달음**:
- 사용자가 "다음에 뭘 해야 하지?" 고민하지 않게
- 각 기능 실행 후 명확한 안내 필수
- 워크플로우가 자연스럽게 이어지도록

**적용**:
- `/cua-vl start` 후 → "/cua-vl roadmap 실행하세요" 안내
- `/cua-vl roadmap` 후 → "Roadmap 저장하세요" 안내
- `/cua-vl daily` 후 → "학습 계획 수립하세요" 안내

---

### 인사이트 3: "자동 감지보다 명확한 질문"

**깨달음**:
- 자동으로 Topic을 감지하려 하면 복잡해짐
- 사용자에게 질문하는 게 더 명확하고 간단
- 오류 가능성도 낮아짐

**적용**:
- Topic 이름을 항상 질문
- 또는 현재 디렉토리에서 명확히 추출
- 애매할 때는 사용자 확인

---

## ✅ 설계 완료 체크리스트

- [x] 3가지 핵심 기능 정의 완료
- [x] 각 기능의 입력/출력 명확화
- [x] SKILL.md 구조 설계 완료
- [x] 폴더 구조 정의
- [x] 사용자 워크플로우 시나리오 작성
- [x] 테스트 계획 수립
- [x] 성공 지표 정의
- [x] 향후 개선 방향 정리

---

**다음 단계**: SKILL.md 실제 구현

**예상 소요 시간**: 4시간 (3가지 기능 구현 + 테스트)

---

**작성자**: CUA_VL Claude Skills 학습
**버전**: 1.0
**최종 업데이트**: 2026-01-10
**상태**: ✅ 설계 완료, 구현 대기
