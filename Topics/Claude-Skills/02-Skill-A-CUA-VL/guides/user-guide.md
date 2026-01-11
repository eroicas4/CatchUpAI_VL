# CUA_VL Skill 사용자 가이드

**문서 버전**: 1.0
**작성일**: 2026-01-10
**대상**: CUA_VL 학습 방법론 사용자

---

## 📘 시작하기

### CUA_VL Skill이란?

CUA_VL Skill은 **Catch Up AI Vibe Learning** 학습 방법론을 지원하는 도구입니다. 새로운 Topic을 시작하고, Roadmap을 생성하고, 매일 학습을 시작할 때 필요한 템플릿과 안내를 자동으로 제공합니다.

### 왜 필요한가요?

**Skill 없이** (수동):
1. 폴더를 직접 생성해야 함
2. 템플릿을 찾아서 복사해야 함
3. 다음에 뭘 해야 할지 Roadmap을 읽어야 함

**Skill 사용** (자동):
1. Skill이 폴더를 자동 생성
2. 템플릿을 즉시 제공
3. 다음 단계를 명확히 안내

**결과**: 약 70% 시간 절약

---

## 🚀 빠른 시작 (5분)

### Step 1: 새 Topic 시작하기

Claude에게 다음과 같이 말하세요:

```
"새 Topic 'Python-FastAPI'를 시작하고 싶어"
```

**Skill이 자동으로**:
- Topic 폴더 생성
- topic_starter.md 템플릿 제공
- 다음 단계 안내

### Step 2: topic_info.md 작성하기

제공된 템플릿을 보고 `Topics/Python-FastAPI/topic_info.md` 파일을 작성하세요.

**필수 항목**:
- Topic 이름
- 학습 목적
- 예상 기간
- 학습 목표

### Step 3: Roadmap 생성하기

topic_info.md 작성 후:

```
"Roadmap을 만들고 싶어"
```

**Skill이 자동으로**:
- topic_info.md 확인
- Roadmap 생성 프롬프트 제공
- Roadmap 저장 방법 안내

### Step 4: 학습 시작!

Roadmap이 준비되면:

```
"오늘 학습을 시작하겠습니다"
```

**Skill이 자동으로**:
- 현재 학습 상황 분석
- 일일 학습 프롬프트 제공
- 학습 계획 수립 지원

---

## 📋 상세 사용 가이드

### 기능 1: 새 Topic 시작

#### 사용 시나리오

**언제 사용하나요?**
- 새로운 기술/프레임워크/개념을 학습하고 싶을 때
- CUA_VL 방법론으로 체계적으로 학습하고 싶을 때

**어떻게 요청하나요?**

자연어로 편하게 요청하세요:
- "새 Topic을 시작하고 싶어"
- "Docker 학습을 시작하려고"
- "FastAPI Topic을 만들고 싶어"

또는 정확한 명령어:
- "/cua-vl start"

#### 실행 과정

1. **Topic 이름 질문**:
   ```
   Skill: "어떤 Topic을 시작하시겠습니까?"
   예: MCP-Basics, Docker-Advanced, React-Hooks 등
   ```

2. **사용자 응답**:
   ```
   사용자: "Docker-Advanced"
   ```

3. **폴더 자동 생성**:
   ```
   Topics/Docker-Advanced/
   ├── vl_prompts/
   ├── vl_roadmap/
   ├── vl_worklog/
   └── vl_materials/
   ```

4. **템플릿 제공**:
   - topic_starter.md 전체 내용 출력
   - 작성 방법 안내

5. **다음 단계 안내**:
   ```
   📌 다음 단계:
   1. topic_info.md 파일을 작성하세요
   2. 작성 완료 후, 'Roadmap을 만들고 싶어'를 요청하세요
   ```

#### 예시 대화

```
사용자: "Machine Learning 기초를 배우고 싶어서 Topic을 만들고 싶어"

Skill: "어떤 Topic을 시작하시겠습니까?"

사용자: "ML-Basics"

Skill:
✅ Topic 폴더가 생성되었습니다: Topics/ML-Basics/

[topic_starter.md 템플릿 제공]
...

📌 다음 단계:
1. topic_info.md 파일을 작성하세요
2. 작성 완료 후, 'Roadmap을 만들고 싶어'를 요청하세요
```

---

### 기능 2: Roadmap 생성

#### 사용 시나리오

**언제 사용하나요?**
- topic_info.md 작성을 완료했을 때
- 체계적인 학습 계획이 필요할 때

**사전 조건**:
- ✅ `/cua-vl start` 실행 완료
- ✅ topic_info.md 작성 완료

#### 실행 과정

1. **Roadmap 생성 요청**:
   ```
   사용자: "Roadmap을 만들고 싶어"
   ```

2. **Topic 확인**:
   ```
   Skill: "어떤 Topic의 Roadmap을 만드시겠습니까?"
   (또는 현재 디렉토리에서 자동 감지)
   ```

3. **topic_info.md 확인**:
   - 파일 존재 확인
   - 없으면: "/cua-vl start를 먼저 실행하세요" 안내

4. **Roadmap 프롬프트 제공**:
   - topic_info.md 내용 읽기
   - roadmap_prompt_template.md 읽기
   - Topic 정보로 변수 치환
   - 완성된 프롬프트 제공

5. **사용 방법 안내**:
   ```
   📌 Roadmap 생성 방법:
   1. 위 프롬프트를 복사하세요
   2. 새 대화 또는 현재 대화에서 실행하세요
   3. 생성된 Roadmap을 저장하세요:
      Topics/{TopicName}/vl_roadmap/YYYYMMDD_RoadMap_{TopicName}.md
   ```

#### 예시 대화

```
사용자: "topic_info.md 작성 완료했어. 이제 Roadmap을 만들고 싶어"

Skill: "어떤 Topic의 Roadmap을 만드시겠습니까?"

사용자: "ML-Basics"

Skill:
✅ topic_info.md 확인 완료

[완성된 Roadmap 생성 프롬프트 제공]
...

📌 Roadmap 생성 방법:
1. 위 프롬프트를 복사하세요
2. 프롬프트를 실행하여 Roadmap을 생성하세요
3. 생성된 Roadmap을 다음 위치에 저장하세요:
   vl_roadmap/20260110_RoadMap_ML-Basics.md

📌 다음 단계:
Roadmap 생성 완료 후, '오늘 학습을 시작하고 싶어'를 요청하세요
```

---

### 기능 3: 일일 학습 시작

#### 사용 시나리오

**언제 사용하나요?**
- 매일 아침 학습을 시작할 때
- 학습 계획을 세우고 싶을 때

**사전 조건**:
- ✅ Roadmap 생성 완료
- ✅ (선택) 이전 WorkLog 존재

#### 실행 과정

1. **일일 학습 시작 요청**:
   ```
   사용자: "오늘 학습을 시작하겠습니다"
   ```

2. **Topic 확인**:
   ```
   Skill: "어떤 Topic의 학습을 시작하시겠습니까?"
   ```

3. **현재 상황 분석**:
   - Roadmap 파일 찾기 (vl_roadmap/*.md)
   - 최근 WorkLog 찾기 (vl_worklog/*.md)
   - 현재 모듈, 미완료 작업 파악

4. **현재 상황 요약 출력**:
   ```
   📊 현재 학습 상태

   **Topic**: ML-Basics
   **현재 모듈**: M2 - 데이터 전처리
   **최근 WorkLog**: 20260109_M2_ML-Basics.md

   **미완료 작업**:
   - [ ] Pandas DataFrame 실습
   - [ ] 결측치 처리 방법 정리

   **Tomorrow's focus**:
   - 데이터 정규화 학습
   - Scikit-learn 실습
   ```

5. **daily_learning_prompt.md 제공**:
   - 전체 프롬프트 출력
   - 사용 방법 안내

6. **학습 시작 안내**:
   ```
   📌 일일 학습 시작 방법:
   1. 위의 현재 상황을 참고하세요
   2. 가용 시간을 입력하세요 (예: 3시간)
   3. 프롬프트를 실행하여 학습 계획을 수립하세요
   ```

---

## 💡 실전 팁 및 모범 사례

### Tip 1: Topic 이름 짓기

**좋은 예시**:
- `Docker-Advanced` (기술-난이도)
- `React-Hooks` (기술-특정 주제)
- `ML-Basics` (약어-난이도)

**피해야 할 예시**:
- `Docker` (너무 광범위)
- `docker advanced` (공백 사용)
- `도커 고급` (한글 사용 지양)

**규칙**:
- 영문, 하이픈만 사용
- 구체적이고 명확하게
- 검색 가능한 이름

---

### Tip 2: topic_info.md 작성 요령

**핵심**: 구체적으로 작성할수록 좋은 Roadmap 생성

**필수 항목**:
- [x] Topic 이름
- [x] 학습 목적 (왜 배우는가)
- [x] 학습 목표 (3-5개, 검증 가능하게)
- [x] 예상 기간 (현실적으로)
- [x] 사전 지식

**선택 항목**:
- [ ] 참조 자료 (공식 문서, 튜토리얼)
- [ ] 학습 접근 방식
- [ ] 특별히 집중하고 싶은 영역

**예시** (좋은 학습 목표):
- ✅ "Docker 컨테이너를 생성하고 실행할 수 있다"
- ✅ "Dockerfile을 작성하여 커스텀 이미지를 만들 수 있다"
- ❌ "Docker를 이해한다" (너무 추상적)
- ❌ "Docker 전문가가 된다" (검증 불가)

---

### Tip 3: 학습 루틴 만들기

**권장 루틴**:

1. **매일 아침** (5분):
   ```
   "오늘 학습을 시작하겠습니다"
   → 현재 상황 확인
   → 오늘의 학습 계획 수립
   ```

2. **학습 중** (2-3시간):
   - Roadmap의 실습 과제 진행
   - WorkLog 실시간 작성

3. **매일 저녁** (10분):
   - Daily Retrospective 작성
   - Tomorrow's focus 정리

4. **모듈 완료 시** (20분):
   - Module Retrospective 작성
   - 다음 모듈 준비

---

### Tip 4: WorkLog 활용하기

**WorkLog를 왜 작성하나요?**
- 진행 상황 추적
- 문제 해결 과정 기록
- 학습 내용 정리
- Daily Retrospective 기반 자료

**효과적인 작성 방법**:
1. **실시간 작성**: 학습하면서 즉시 기록
2. **구체적으로**: "공부함" (X) → "Pandas DataFrame 5개 예제 실습 완료" (O)
3. **문제 해결 로그**: 막혔던 부분과 해결 방법 상세히
4. **인사이트 포함**: 배운 점, 깨달음, 개선 아이디어

---

## 🔧 자주 묻는 질문 (FAQ)

### Q1: Skill을 사용하지 않고 Repository만 써도 되나요?

**A**: 네, 가능합니다!

Skill은 **선택사항**입니다. Repository의 templates/ 폴더에서 템플릿을 직접 복사하고 수동으로 폴더를 생성해도 됩니다.

**Skill의 장점**:
- 자동화로 시간 절약 (70%)
- 다음 단계 명확한 안내
- 실수 방지 (폴더 구조 일관성)

---

### Q2: 여러 Topic을 동시에 학습할 수 있나요?

**A**: 네, 가능합니다!

각 Topic은 독립적인 폴더로 관리되므로 여러 Topic을 병행할 수 있습니다.

**방법**:
```
"Claude-Skills Topic의 학습을 시작하겠습니다"
[Claude-Skills 학습]

"이제 ML-Basics Topic으로 전환"
"ML-Basics 학습을 시작하겠습니다"
[ML-Basics 학습]
```

---

### Q3: Roadmap을 수정하고 싶은데 어떻게 하나요?

**A**: Roadmap 파일을 직접 편집하세요.

1. `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md` 파일 열기
2. 내용 수정
3. 저장

Roadmap은 고정된 것이 아니라 학습하면서 조정 가능합니다.

---

### Q4: Skill이 제대로 작동하지 않아요

**체크리스트**:
1. [ ] Personal Skills 폴더에 SKILL.md가 있는지 확인
   - 위치: `~/.claude/skills/cua-vl/SKILL.md`
2. [ ] 자연어 요청이 description과 일치하는지 확인
3. [ ] VS Code Extension 재시작
4. [ ] 정확한 명령어 사용 (예: `/cua-vl start`)

**여전히 안 되면**:
- Repository 직접 사용 (Skill 없이도 CUA_VL 사용 가능)
- GitHub Issues에 문제 보고

---

## 📊 효과 측정

### CUA_VL Skill 사용 전후 비교

| 작업 | Skill 없음 | Skill 사용 | 개선 |
|------|-----------|----------|------|
| Topic 시작 | 5분 (수동 폴더 생성) | 1분 | 80% ⬇ |
| Roadmap 생성 | 10분 (템플릿 찾기/복사) | 3분 | 70% ⬇ |
| 일일 학습 시작 | 5분 (WorkLog 찾기/분석) | 2분 | 60% ⬇ |
| **전체** | **20분** | **6분** | **70% ⬇** |

### 사용자 만족도 (실전 테스트)

- ✅ **사용 편의성**: ⭐⭐⭐⭐⭐ (자연어 인터페이스)
- ✅ **시간 절약**: ⭐⭐⭐⭐⭐ (70% 단축)
- ✅ **안내 명확성**: ⭐⭐⭐⭐⭐ (다음 단계 명확)
- ✅ **오류 처리**: ⭐⭐⭐⭐ (명확한 오류 메시지)

---

## 🎓 학습 자료

### CUA_VL 방법론 이해하기

- **CUA_VL README**: [Repository 링크]
- **Getting Started**: 빠른 시작 가이드
- **Templates 폴더**: 모든 템플릿 확인

### Skill 개발 배경

- **M1 - Claude Skills 기본 개념**: Skill 구조 이해
- **M2 - CUA_VL Skill 개발**: 이 Skill의 설계 및 구현 과정

---

## 📞 지원 및 커뮤니티

### 도움이 필요하신가요?

- **GitHub Issues**: 버그 보고, 기능 제안
- **이메일**: solkit70@gmail.com
- **CUA_VL 커뮤니티**: [링크]

### 피드백 환영합니다

사용하면서 불편한 점이나 개선 아이디어가 있으면 언제든 알려주세요!

---

**가이드 버전**: 1.0
**작성자**: CUA_VL Claude Skills 학습
**최종 업데이트**: 2026-01-10
**문의**: solkit70@gmail.com
