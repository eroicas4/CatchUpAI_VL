# AI-Modeling-Transformer 학습 로드맵

**생성일**: 2026-01-10
**방법론**: CUA_VL (Catch Up AI Vibe Learning)
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개

Transformer 아키텍처의 탄생("Attention is All You Need", 2017)부터 현재까지의 발전 과정을 학습합니다.
GPT, BERT, T5 등 주요 모델들의 핵심 아이디어와 혁신을 이해하고, Transformer가 AI 분야를 어떻게 변화시켰는지 탐구합니다.

### 학습 목표

- Transformer 아키텍처의 핵심 원리와 혁신적 아이디어 이해
- GPT 시리즈, BERT, T5, LLaMA 등 주요 모델의 발전 과정 파악
- Attention 메커니즘부터 최신 기법(MoE, RLHF 등)까지 기술 진화 추적
- AI 모델링의 역사적 맥락과 미래 방향성 통찰
- 논문 읽기 및 분석 능력 향상
- "교과서 품질"의 Transformer 발전사 타임라인 문서 작성

### 예상 학습 기간

**총 4주 (32-40시간)**
- 1주차: Transformer 기본 (Attention is All You Need)
- 2주차: GPT 시리즈 (GPT-1/2/3/3.5/4)
- 3주차: BERT, T5 및 기타 주요 모델
- 4주차: 최신 발전 (LLaMA, Claude, Gemini 등)

### 학습 환경

- **OS**: Windows 11
- **도구**: VS Code, Python 3.11+, PyTorch 2.0+, Jupyter Notebook, Git, ArXiv/Papers with Code
- **사전 지식**:
  - 필수: 딥러닝 기본, 선형대수/확률통계, Python 기본, 영어 논문 읽기
  - 권장: RNN/LSTM, NLP 기본, PyTorch/TensorFlow, Attention 메커니즘

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | Transformer 탄생과 기본 원리 (2017-2018) | ⭐⭐ | 6-8h | 01-Transformer-Basics/ |
| M2 | GPT 시리즈의 진화 (2018-2020) | ⭐⭐ | 6-8h | 02-GPT-Evolution/ |
| M3 | Encoder-Decoder 및 양방향 모델 | ⭐⭐ | 5-7h | 03-Encoder-Models/ |
| M4 | 대규모 모델과 최신 기법 (2020-2024) | ⭐⭐⭐ | 6-8h | 04-Large-Models/ |
| M5 | 최신 트렌드와 미래 방향 (2024-2026) | ⭐⭐⭐ | 5-6h | 05-Latest-Trends/ |
| M6 | 통합 정리 및 타임라인 문서 완성 | ⭐⭐ | 4-5h | 06-Timeline-Final/ |

**총 예상 시간**: 32-42시간 (버퍼 20% 포함)

---

## 📖 모듈별 상세 계획

### M1 - Transformer 탄생과 기본 원리 (2017-2018)

**난이도**: ⭐⭐
**예상 시간**: 6-8h
**산출물 폴더**: `01-Transformer-Basics/`

#### 학습 목표

- [ ] "Attention is All You Need" 논문을 읽고 핵심 내용을 3페이지 이내로 요약할 수 있다
- [ ] Self-Attention 메커니즘의 작동 원리를 수식과 다이어그램으로 설명할 수 있다
- [ ] Multi-Head Attention의 필요성과 작동 방식을 이해하고 시각화할 수 있다
- [ ] Positional Encoding이 왜 필요한지, 어떻게 구현되는지 설명할 수 있다
- [ ] Transformer 아키텍처 전체 구조를 블록 다이어그램으로 그릴 수 있다

#### 주요 개념

1. **Self-Attention**: Query, Key, Value 벡터를 사용하여 입력 시퀀스 내 각 토큰이 다른 토큰들과의 관계를 학습하는 메커니즘. RNN 없이도 시퀀스 처리 가능.

2. **Multi-Head Attention**: 여러 개의 Attention 헤드를 병렬로 사용하여 다양한 표현 부공간(representation subspaces)을 학습. 모델이 다양한 관점에서 정보를 포착 가능.

3. **Positional Encoding**: Transformer는 순환 구조가 없어 위치 정보가 없으므로, 삼각함수 기반 인코딩을 통해 토큰의 위치 정보를 주입.

4. **Feed-Forward Network (FFN)**: 각 위치마다 독립적으로 적용되는 2층 완전 연결 네트워크. 비선형성 추가 및 표현력 향상.

5. **Encoder-Decoder 구조**: Encoder는 입력을 임베딩하고, Decoder는 출력을 생성. Machine Translation 등에 사용.

**오해하기 쉬운 포인트**:
- Self-Attention은 "자기 자신에 대한 Attention"이 아니라 "같은 시퀀스 내 모든 요소 간 Attention"
- Positional Encoding은 학습되지 않고 고정된 함수 (일부 변형에서는 학습 가능)

#### 실습 과제

**실습 1: "Attention is All You Need" 논문 핵심 분석** ⭐⭐

- **목적**: 원조 논문을 통해 Transformer의 탄생 배경과 핵심 아이디어를 이해
- **단계**:
  1. ArXiv에서 "Attention is All You Need" (2017) 논문 다운로드
  2. Abstract, Introduction, Conclusion 읽기 (30분)
  3. Section 3 (Model Architecture) 정독하며 다이어그램 이해 (60분)
  4. Self-Attention 수식 분석 및 예제로 계산 (30분)
  5. 핵심 내용 2-3페이지 요약 문서 작성 (60분)
- **예상 시간**: 180분
- **검증**: 요약 문서에 다음 포함되었는지 확인
  - Transformer 이전의 문제점 (RNN/LSTM의 한계)
  - Self-Attention 메커니즘 설명
  - Multi-Head Attention 구조
  - Positional Encoding 방식
  - 실험 결과 요약 (WMT 번역 성능)

**실습 2: Transformer 아키텍처 시각화** ⭐⭐

- **목적**: 논문의 Figure 1을 자신의 언어로 재해석하여 깊이 이해
- **단계**:
  1. "The Illustrated Transformer" 블로그 읽기 (45분)
  2. PowerPoint/Diagrams.net으로 Transformer 구조도 작성 (60분)
  3. 각 컴포넌트에 1-2줄 설명 추가 (30분)
  4. Self-Attention 계산 과정을 예시 입력으로 단계별 시각화 (45분)
- **예상 시간**: 180분
- **검증**:
  - 다이어그램에 Encoder 6층, Decoder 6층 표현
  - Multi-Head Attention, Add & Norm, FFN 블록 명시
  - Self-Attention 계산 예시 (3-4단어 입력)
  - 다른 학습자가 이것만 보고 이해 가능한 수준

**실습 3: 간단한 Self-Attention 구현 (선택)** ⭐⭐⭐

- **목적**: PyTorch로 Self-Attention을 직접 구현하여 내부 작동 원리 체득
- **단계**:
  1. Jupyter Notebook 생성
  2. Q, K, V 행렬 생성 코드 작성 (30분)
  3. Attention Score 계산 (Scaled Dot-Product) (30분)
  4. 간단한 문장으로 테스트 및 Attention 가중치 시각화 (60분)
  5. 코드에 주석 상세히 작성 (30분)
- **예상 시간**: 150분
- **검증**:
  - 코드 실행 시 Attention 가중치 행렬 출력
  - 입력 시퀀스의 각 단어가 어떤 단어에 주목하는지 확인
  - Heatmap으로 시각화

#### 산출물

```
01-Transformer-Basics/
├── README.md                          # 모듈 개요, 학습 목표, 주요 내용 요약
├── concepts/
│   ├── attention-mechanism.md         # Self-Attention 상세 설명
│   ├── multi-head-attention.md        # Multi-Head Attention 설명
│   ├── positional-encoding.md         # Positional Encoding 설명
│   └── architecture-overview.md       # 전체 아키텍처 개요
├── papers/
│   ├── Attention-is-All-You-Need.pdf  # 원본 논문
│   └── paper-summary.md               # 논문 핵심 요약 (2-3페이지)
├── diagrams/
│   ├── transformer-architecture.png   # 전체 구조도
│   ├── self-attention-process.png     # Self-Attention 계산 과정
│   └── multi-head-attention.png       # Multi-Head Attention 구조
├── examples/
│   └── self_attention_implementation.ipynb  # (선택) PyTorch 구현
└── guides/
    └── how-to-read-transformer-papers.md  # 논문 읽기 가이드
```

**README.md 필수 내용**:
- 모듈 학습 목표 및 완료 기준
- Transformer 탄생 배경 (2017년 NLP의 상황)
- 핵심 혁신 3가지 (Self-Attention, No RNN, Parallel Processing)
- 주요 참조 자료 링크
- 다음 모듈 (M2) 연결 고리

#### Definition of Done

- [ ] "Attention is All You Need" 논문 읽기 완료 및 2-3페이지 요약 작성
- [ ] Self-Attention 메커니즘을 수식과 함께 설명한 문서 작성
- [ ] Transformer 아키�ecture 다이어그램 3개 이상 생성
- [ ] Multi-Head Attention, Positional Encoding 개념 문서 작성
- [ ] 산출물 폴더 `01-Transformer-Basics/` 생성 및 README.md 작성
- [ ] (선택) Self-Attention 구현 코드 작성 및 실행 성공
- [ ] WorkLog 작성 완료
- [ ] M1 Module Retrospective 작성

#### Self-Assessment

**개념 이해** (10분):
- [ ] Transformer가 RNN/LSTM을 대체할 수 있는 이유를 3가지 이상 설명 가능
- [ ] Self-Attention의 Q, K, V가 무엇인지 예시와 함께 설명 가능
- [ ] Positional Encoding이 없으면 어떤 문제가 발생하는지 설명 가능

**실무 활용** (10분):
- [ ] AI에게 "Transformer 기반 모델로 번역 시스템 구축" 요청 시 필요한 구조 설명 가능
- [ ] Hugging Face Transformers 라이브러리의 기본 사용법을 AI에게 효과적으로 질문 가능
- [ ] Transformer 모델의 성능이 낮을 때 어떤 부분을 점검해야 하는지 방향 제시 가능

**문제 해결** (10분):
- [ ] "Attention 가중치가 특정 토큰에 과도하게 집중" 문제 발생 시 원인 추정 가능
- [ ] 입력 시퀀스 길이가 매우 길 때 메모리 문제 발생 이유 설명 가능

#### 예상 시간 배분

- 개념 학습 (논문 읽기 + 블로그): 120분 (30%)
- 실습 1 (논문 요약): 180분 (37%)
- 실습 2 (시각화): 180분 (37%)
- 실습 3 (구현, 선택): 150분
- 문서화 (README 등): 60분 (15%)
- **합계**: 6-8시간 (버퍼 20% 포함)

#### 참조 자료

- [Attention is All You Need (2017)](https://arxiv.org/abs/1706.03762): 원조 Transformer 논문
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/): 시각화로 이해하는 Transformer
- [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/): 코드와 함께 보는 논문 주석
- [Stanford CS224N Lecture on Transformers](http://web.stanford.edu/class/cs224n/): 강의 노트 및 슬라이드
- [Hugging Face - Transformer Models](https://huggingface.co/docs/transformers/model_doc/auto): 공식 문서

---

### M2 - GPT 시리즈의 진화 (2018-2020)

**난이도**: ⭐⭐
**예상 시간**: 6-8h
**산출물 폴더**: `02-GPT-Evolution/`

#### 학습 목표

- [ ] GPT-1, GPT-2, GPT-3의 핵심 차이점을 표로 정리하고 설명할 수 있다
- [ ] Generative Pre-training 방식과 Fine-tuning의 개념을 이해하고 설명할 수 있다
- [ ] Zero-shot, One-shot, Few-shot Learning의 차이를 예시와 함께 설명할 수 있다
- [ ] Scaling Laws (모델 크기 증가에 따른 성능 향상)를 이해하고 그래프로 표현할 수 있다
- [ ] GPT 시리즈의 발전 과정을 타임라인으로 정리할 수 있다

#### 주요 개념

1. **Generative Pre-training**: 대규모 비지도 학습 데이터로 언어 모델을 사전 학습한 후, 특정 태스크에 Fine-tuning하는 방식. GPT의 핵심 전략.

2. **Decoder-only Architecture**: GPT는 Transformer의 Decoder만 사용 (Encoder 없음). Autoregressive 방식으로 다음 토큰 예측.

3. **Few-shot Learning**: 별도의 Fine-tuning 없이 프롬프트에 몇 개 예시만 제공하여 태스크 수행. GPT-3의 핵심 능력.

4. **Scaling Laws**: 모델 크기, 데이터셋 크기, 컴퓨팅 자원을 늘릴수록 성능이 지속적으로 향상. GPT-3는 175B 파라미터로 검증.

5. **In-Context Learning**: Fine-tuning 없이 프롬프트 내 맥락만으로 새로운 태스크를 학습하는 능력.

**오해하기 쉬운 포인트**:
- GPT-2는 "Zero-shot"이 아니라 "Fine-tuning 없이 다양한 태스크 수행"에 초점 (완전한 Zero-shot은 GPT-3)
- Few-shot Learning이 "데이터가 적다"는 의미가 아니라 "태스크 예시가 적다"는 의미

#### 실습 과제

**실습 1: GPT-1/2/3 논문 비교 분석** ⭐⭐

- **목적**: GPT 시리즈의 진화 과정을 단계별로 이해하고 핵심 혁신 파악
- **단계**:
  1. GPT-1, GPT-2, GPT-3 논문의 Abstract와 Introduction 읽기 (60분)
  2. 각 논문의 핵심 기여 (Key Contribution) 1-2페이지씩 요약 (90분)
  3. 모델 비교표 작성: 파라미터 수, 학습 데이터, 주요 혁신, 성능 (60분)
  4. 발전 과정 타임라인 작성 (2018 GPT-1 → 2019 GPT-2 → 2020 GPT-3) (30분)
- **예상 시간**: 240분
- **검증**:
  - 비교표에 최소 5개 항목 (파라미터, 데이터, 아키텍처, 학습 방식, 성능)
  - 각 버전의 핵심 혁신이 명확히 구분됨
  - 타임라인에 주요 벤치마크 성능 포함

**실습 2: Few-shot Learning 실습 (Hugging Face)** ⭐⭐

- **목적**: GPT-3의 핵심 능력인 Few-shot Learning을 직접 체험
- **단계**:
  1. Hugging Face Transformers 라이브러리 설치 (10분)
  2. GPT-2 모델 로드 및 기본 텍스트 생성 테스트 (20분)
  3. Few-shot 프롬프트 작성 (예: 감정 분류 3개 예시 제공) (30분)
  4. Zero-shot vs Few-shot 성능 비교 실험 (40분)
  5. 결과 분석 및 문서화 (20분)
- **예상 시간**: 120분
- **검증**:
  - GPT-2 모델이 정상적으로 텍스트 생성
  - Few-shot 프롬프트 3개 이상 작성
  - Zero-shot과 Few-shot 결과 비교 문서 작성

**실습 3: Scaling Laws 시각화** ⭐⭐

- **목적**: 모델 크기 증가에 따른 성능 향상 추세를 그래프로 이해
- **단계**:
  1. GPT-1 (117M), GPT-2 (1.5B), GPT-3 (175B) 파라미터 및 성능 데이터 수집 (30분)
  2. Python matplotlib/seaborn으로 그래프 작성 (60분)
  3. Scaling Laws 논문 참고하여 해석 (30분)
  4. "왜 큰 모델이 필요한가" 분석 문서 작성 (30분)
- **예상 시간**: 150분
- **검증**:
  - 그래프에 GPT-1/2/3 포인트 표시
  - X축: 파라미터 수 (로그 스케일), Y축: 성능 (Perplexity 등)
  - 해석 문서에 Scaling Laws 핵심 내용 포함

#### 산출물

```
02-GPT-Evolution/
├── README.md                          # 모듈 개요, GPT 시리즈 발전사
├── concepts/
│   ├── generative-pretraining.md      # Pre-training 개념
│   ├── few-shot-learning.md           # Zero/One/Few-shot 설명
│   ├── scaling-laws.md                # Scaling Laws 분석
│   └── decoder-only-architecture.md   # Decoder-only 구조
├── papers/
│   ├── GPT-1-summary.md               # GPT-1 논문 요약
│   ├── GPT-2-summary.md               # GPT-2 논문 요약
│   ├── GPT-3-summary.md               # GPT-3 논문 요약
│   └── model-comparison-table.md      # 모델 비교표
├── timeline/
│   └── gpt-evolution-timeline.md      # 2018-2020 타임라인
├── examples/
│   ├── few_shot_demo.ipynb            # Few-shot Learning 실습
│   └── scaling_laws_visualization.ipynb  # Scaling Laws 그래프
└── guides/
    └── how-to-use-gpt-models.md       # Hugging Face 사용 가이드
```

#### Definition of Done

- [ ] GPT-1, GPT-2, GPT-3 논문 핵심 요약 각 1-2페이지 작성
- [ ] 모델 비교표 작성 (최소 5개 비교 항목)
- [ ] Few-shot Learning 실습 완료 및 Zero-shot과 비교 문서 작성
- [ ] Scaling Laws 그래프 생성 및 해석 문서 작성
- [ ] GPT 발전 타임라인 (2018-2020) 작성
- [ ] 산출물 폴더 `02-GPT-Evolution/` 생성 및 README.md 작성
- [ ] WorkLog 작성 완료
- [ ] M2 Module Retrospective 작성

#### Self-Assessment

**개념 이해** (10분):
- [ ] GPT-1과 GPT-2의 가장 큰 차이점을 설명 가능 (Fine-tuning 유무)
- [ ] Few-shot Learning이 어떻게 가능한지 In-Context Learning 개념으로 설명 가능
- [ ] Scaling Laws를 한 문장으로 요약 가능

**실무 활용** (10분):
- [ ] AI에게 "GPT 모델로 감정 분류" 요청 시 Few-shot 프롬프트 설계 가능
- [ ] GPT-2와 GPT-3 중 어느 모델을 사용할지 상황에 따라 판단 가능
- [ ] Hugging Face에서 GPT 모델 로드 및 텍스트 생성 코드를 AI에게 요청 가능

**문제 해결** (10분):
- [ ] GPT 모델이 반복적인 텍스트 생성 시 원인 및 해결 방향 제시 가능
- [ ] Few-shot 프롬프트 성능이 낮을 때 개선 방법 제안 가능

#### 예상 시간 배분

- 개념 학습 (논문 읽기): 90분 (22%)
- 실습 1 (논문 비교): 240분 (50%)
- 실습 2 (Few-shot 실습): 120분 (25%)
- 실습 3 (Scaling Laws): 150분
- 문서화: 60분 (15%)
- **합계**: 6-8시간 (버퍼 20% 포함)

#### 참조 자료

- [GPT-1: Improving Language Understanding (2018)](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf): GPT-1 원본 논문
- [GPT-2: Language Models are Unsupervised Multitask Learners (2019)](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf): GPT-2 논문
- [GPT-3: Language Models are Few-Shot Learners (2020)](https://arxiv.org/abs/2005.14165): GPT-3 논문
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361): Scaling Laws 논문
- [Hugging Face GPT-2 Model Card](https://huggingface.co/gpt2): GPT-2 사용 가이드

---

### M3 - Encoder-Decoder 및 양방향 모델

**난이도**: ⭐⭐
**예상 시간**: 5-7h
**산출물 폴더**: `03-Encoder-Models/`

#### 학습 목표

- [ ] BERT의 Bidirectional Pre-training과 GPT의 Unidirectional 차이를 이해하고 설명할 수 있다
- [ ] Masked Language Modeling (MLM)과 Next Sentence Prediction (NSP)의 원리를 설명할 수 있다
- [ ] T5의 Text-to-Text Framework가 무엇인지, 왜 혁신적인지 설명할 수 있다
- [ ] Encoder-only, Decoder-only, Encoder-Decoder 아키텍처의 사용 사례를 구분할 수 있다
- [ ] BERT, RoBERTa, ALBERT, T5를 비교 분석하여 표로 정리할 수 있다

#### 주요 개념

1. **Bidirectional Encoding**: BERT는 양방향으로 문맥을 이해 (왼쪽과 오른쪽 모두). GPT는 왼쪽만 보는 단방향.

2. **Masked Language Modeling (MLM)**: 입력의 일부 토큰을 [MASK]로 가리고 예측하는 사전 학습 방식. BERT의 핵심.

3. **Text-to-Text Framework**: 모든 NLP 태스크를 "텍스트 입력 → 텍스트 출력" 형식으로 통일. T5의 혁신.

4. **Encoder vs Decoder**: Encoder는 이해(Classification, NER 등)에 강하고, Decoder는 생성(Text Generation)에 강함. Encoder-Decoder는 번역, 요약 등에 최적.

5. **Fine-tuning Strategies**: BERT는 태스크별 Fine-tuning 필요, GPT-3는 Few-shot으로 가능, T5는 Text-to-Text 통일.

**오해하기 쉬운 포인트**:
- BERT는 "양방향 Transformer"가 아니라 "양방향 Encoder" (Decoder는 없음)
- T5의 "모든 태스크를 Text-to-Text로"는 단순히 입출력 형식 통일이지만, 학습 효율과 전이 학습에 큰 영향

#### 실습 과제

**실습 1: BERT와 T5 논문 비교 분석** ⭐⭐

- **목적**: Encoder-only (BERT)와 Encoder-Decoder (T5)의 차이를 명확히 이해
- **단계**:
  1. BERT 논문 (2018) Abstract, Introduction, Section 3 읽기 (60분)
  2. T5 논문 (2019) Abstract, Introduction, Section 2-3 읽기 (60분)
  3. MLM vs Text-to-Text 비교 분석 (30분)
  4. 아키텍처 차이점 다이어그램 작성 (45분)
  5. 사용 사례별 최적 모델 정리 (분류→BERT, 생성→GPT, 번역→T5) (45분)
- **예상 시간**: 240분
- **검증**:
  - BERT와 T5의 사전 학습 방식 차이 설명 문서
  - 아키텍처 비교 다이어그램 (Encoder-only vs Encoder-Decoder)
  - 태스크별 최적 모델 추천표 작성

**실습 2: BERT로 감정 분류 Fine-tuning** ⭐⭐

- **목적**: BERT의 Fine-tuning 방식을 실제로 체험
- **단계**:
  1. Hugging Face Transformers로 사전 학습된 BERT 모델 로드 (15분)
  2. 간단한 감정 분류 데이터셋 준비 (IMDb 또는 자체 제작) (30분)
  3. BERT Fine-tuning 코드 작성 (Trainer API 사용) (60분)
  4. 학습 및 평가 (30분)
  5. 결과 분석 및 문서화 (25분)
- **예상 시간**: 160분
- **검증**:
  - Fine-tuning 코드 실행 성공
  - 학습 전후 성능 비교 (Accuracy, F1)
  - 결과 분석 문서 작성

**실습 3: 모델 아키텍처 비교표 작성** ⭐

- **목적**: Transformer 기반 주요 모델들의 아키텍처를 체계적으로 정리
- **단계**:
  1. GPT, BERT, T5, BART 아키텍처 조사 (45분)
  2. 비교표 작성: 구조, 사전 학습, 강점, 약점, 사용 사례 (60분)
  3. 각 모델의 역사적 맥락 정리 (30분)
- **예상 시간**: 135분
- **검증**:
  - 최소 5개 모델 비교 (GPT, BERT, T5, RoBERTa, ALBERT)
  - 비교 항목: 아키텍처, 파라미터, 사전 학습 방식, 주요 태스크
  - 사용 사례별 추천 모델 명시

#### 산출물

```
03-Encoder-Models/
├── README.md                          # 모듈 개요, Encoder 모델 특징
├── concepts/
│   ├── bidirectional-encoding.md      # 양방향 인코딩 설명
│   ├── masked-language-modeling.md    # MLM 원리
│   ├── text-to-text-framework.md      # T5의 Text-to-Text
│   └── encoder-decoder-comparison.md  # 아키텍처 비교
├── papers/
│   ├── BERT-summary.md                # BERT 논문 요약
│   ├── T5-summary.md                  # T5 논문 요약
│   ├── RoBERTa-summary.md             # RoBERTa 요약
│   └── ALBERT-summary.md              # ALBERT 요약
├── comparisons/
│   ├── architecture-comparison-table.md  # 모델 비교표
│   └── use-case-recommendations.md    # 태스크별 모델 추천
├── diagrams/
│   ├── bert-architecture.png          # BERT 구조도
│   ├── t5-architecture.png            # T5 구조도
│   └── encoder-decoder-comparison.png # 아키텍처 비교
├── examples/
│   └── bert_finetuning_sentiment.ipynb  # BERT Fine-tuning 실습
└── guides/
    └── when-to-use-which-model.md     # 모델 선택 가이드
```

#### Definition of Done

- [ ] BERT와 T5 논문 핵심 요약 각 1-2페이지 작성
- [ ] MLM과 Text-to-Text Framework 개념 문서 작성
- [ ] BERT Fine-tuning 실습 완료 및 결과 문서 작성
- [ ] 모델 아키텍처 비교표 작성 (최소 5개 모델)
- [ ] 태스크별 모델 추천 가이드 작성
- [ ] 산출물 폴더 `03-Encoder-Models/` 생성 및 README.md 작성
- [ ] WorkLog 작성 완료
- [ ] M3 Module Retrospective 작성

#### Self-Assessment

**개념 이해** (10분):
- [ ] BERT가 GPT보다 분류 태스크에 강한 이유를 양방향 인코딩으로 설명 가능
- [ ] MLM이 무엇인지, 왜 [MASK] 토큰을 사용하는지 설명 가능
- [ ] T5의 Text-to-Text Framework가 왜 혁신적인지 예시와 함께 설명 가능

**실무 활용** (10분):
- [ ] 감정 분류 프로젝트 시 BERT를 선택하는 이유를 설명하고 AI에게 Fine-tuning 요청 가능
- [ ] 번역 프로젝트 시 T5를 추천할 수 있으며, Text-to-Text 형식으로 데이터 준비 가능
- [ ] Encoder-only와 Encoder-Decoder 중 선택 기준을 AI에게 설명 가능

**문제 해결** (10분):
- [ ] BERT Fine-tuning 시 성능이 낮을 때 데이터 품질, 학습률 등을 점검 방향 제시
- [ ] T5 모델이 생성한 텍스트가 부정확할 때 프롬프트 개선 방법 제안 가능

#### 예상 시간 배분

- 개념 학습 (논문 읽기): 90분 (25%)
- 실습 1 (논문 비교): 240분 (50%)
- 실습 2 (BERT Fine-tuning): 160분 (33%)
- 실습 3 (비교표 작성): 135분 (28%)
- 문서화: 45분 (12%)
- **합계**: 5-7시간 (버퍼 20% 포함)

#### 참조 자료

- [BERT: Pre-training of Deep Bidirectional Transformers (2018)](https://arxiv.org/abs/1810.04805): BERT 원본 논문
- [T5: Exploring the Limits of Transfer Learning (2019)](https://arxiv.org/abs/1910.10683): T5 논문
- [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692): RoBERTa 논문
- [ALBERT: A Lite BERT](https://arxiv.org/abs/1909.11942): ALBERT 논문
- [Hugging Face BERT Fine-tuning Tutorial](https://huggingface.co/docs/transformers/training): Fine-tuning 가이드

---

### M4 - 대규모 모델과 최신 기법 (2020-2024)

**난이도**: ⭐⭐⭐
**예상 시간**: 6-8h
**산출물 폴더**: `04-Large-Models/`

#### 학습 목표

- [ ] GPT-3.5와 GPT-4의 기술적 차이점과 성능 향상 요인을 설명할 수 있다
- [ ] RLHF (Reinforcement Learning from Human Feedback)의 원리와 필요성을 이해하고 설명할 수 있다
- [ ] InstructGPT가 GPT-3와 어떻게 다른지, 왜 중요한지 설명할 수 있다
- [ ] LLaMA 시리즈 (LLaMA 1/2/3)의 특징과 오픈소스 전략을 이해하고 설명할 수 있다
- [ ] Mixture of Experts (MoE) 아키텍처의 원리와 장점을 설명할 수 있다

#### 주요 개념

1. **RLHF (Reinforcement Learning from Human Feedback)**: 인간 피드백을 활용한 강화 학습으로 모델을 사람의 의도에 맞게 정렬. InstructGPT/ChatGPT의 핵심.

2. **InstructGPT**: GPT-3를 RLHF로 Fine-tuning하여 지시 따르기 능력 향상. "유용하고, 정직하며, 무해한" 모델 목표.

3. **LLaMA (Large Language Model Meta AI)**: Meta의 오픈소스 대규모 언어 모델. 작은 모델로도 높은 성능 달성 (효율성 강조).

4. **Mixture of Experts (MoE)**: 여러 전문가 모델을 병렬로 두고 입력에 따라 선택적으로 활성화. 파라미터는 많지만 계산 비용은 낮음.

5. **Instruction Tuning**: 지시문(Instruction)과 응답 쌍으로 Fine-tuning하여 모델이 다양한 명령을 이해하고 수행하도록 학습.

**오해하기 쉬운 포인트**:
- RLHF는 "강화 학습만"이 아니라 "SFT(Supervised Fine-Tuning) → Reward Model → PPO" 3단계
- LLaMA는 완전 오픈소스가 아니었으나 (라이선스 제한), LLaMA 2부터 상업적 사용 가능
- MoE는 "전체 파라미터"는 크지만 "활성 파라미터"는 작아 효율적

#### 실습 과제

**실습 1: InstructGPT와 RLHF 논문 분석** ⭐⭐⭐

- **목적**: RLHF의 작동 원리와 InstructGPT의 혁신을 깊이 이해
- **단계**:
  1. InstructGPT 논문 (2022) 읽기 (90분)
  2. RLHF 3단계 (SFT, Reward Model, PPO) 다이어그램 작성 (60분)
  3. GPT-3 vs InstructGPT 성능 비교 정리 (30분)
  4. RLHF가 필요한 이유 분석 (Alignment Problem) (30분)
  5. 핵심 내용 2-3페이지 요약 (30분)
- **예상 시간**: 240분
- **검증**:
  - RLHF 3단계 프로세스 다이어그램 완성
  - GPT-3와 InstructGPT 비교 (유용성, 정직성, 무해성)
  - Alignment Problem 설명 문서

**실습 2: LLaMA 시리즈 비교 및 타임라인 작성** ⭐⭐

- **목적**: LLaMA 1/2/3의 발전 과정과 오픈소스 전략 이해
- **단계**:
  1. LLaMA 1 (2023), LLaMA 2 (2023), LLaMA 3 (2024) 논문/발표 자료 읽기 (90분)
  2. 각 버전의 파라미터 수, 학습 데이터, 성능 비교표 작성 (45분)
  3. LLaMA가 GPT-3 대비 효율적인 이유 분석 (30분)
  4. 오픈소스 전략이 AI 생태계에 미친 영향 정리 (30분)
  5. 타임라인 업데이트 (2020-2024) (15분)
- **예상 시간**: 210분
- **검증**:
  - LLaMA 1/2/3 비교표 (파라미터, 성능, 라이선스)
  - 효율성 분석 문서 (작은 모델, 높은 성능)
  - 타임라인에 LLaMA 시리즈 추가

**실습 3: Mixture of Experts (MoE) 개념 정리** ⭐⭐

- **목적**: MoE 아키텍처의 원리와 대규모 모델에서의 활용 이해
- **단계**:
  1. MoE 관련 자료 읽기 (Switch Transformer, GPT-4 추정) (60분)
  2. MoE 작동 원리 다이어그램 작성 (45분)
  3. Dense Model vs MoE 비교 (파라미터, 계산 비용, 성능) (30분)
  4. GPT-4가 MoE를 사용한다는 추정 근거 정리 (30분)
- **예상 시간**: 165분
- **검증**:
  - MoE 작동 원리 다이어그램 (Gating Network, Experts)
  - Dense vs MoE 비교표
  - GPT-4 MoE 추정 근거 문서

#### 산출물

```
04-Large-Models/
├── README.md                          # 모듈 개요, 대규모 모델 트렌드
├── concepts/
│   ├── rlhf-explained.md              # RLHF 상세 설명
│   ├── instruction-tuning.md          # Instruction Tuning 설명
│   ├── mixture-of-experts.md          # MoE 아키텍처
│   └── alignment-problem.md           # AI Alignment 문제
├── papers/
│   ├── InstructGPT-summary.md         # InstructGPT 논문 요약
│   ├── LLaMA-1-summary.md             # LLaMA 1 요약
│   ├── LLaMA-2-summary.md             # LLaMA 2 요약
│   ├── LLaMA-3-summary.md             # LLaMA 3 요약
│   └── GPT-4-technical-report.md      # GPT-4 Technical Report 요약
├── comparisons/
│   ├── gpt3-vs-instructgpt.md         # GPT-3와 InstructGPT 비교
│   ├── llama-series-comparison.md     # LLaMA 시리즈 비교
│   └── dense-vs-moe.md                # Dense Model vs MoE
├── diagrams/
│   ├── rlhf-process.png               # RLHF 3단계 프로세스
│   ├── moe-architecture.png           # MoE 구조도
│   └── llama-timeline.png             # LLaMA 발전 타임라인
├── timeline/
│   └── 2020-2024-major-models.md      # 2020-2024 주요 모델 타임라인
└── guides/
    └── opensource-vs-closed-models.md # 오픈소스 vs 클로즈드 모델 비교
```

#### Definition of Done

- [ ] InstructGPT 논문 요약 및 RLHF 3단계 다이어그램 작성
- [ ] GPT-3 vs InstructGPT 비교 문서 작성
- [ ] LLaMA 1/2/3 비교표 및 타임라인 작성
- [ ] MoE 아키텍처 개념 문서 및 다이어그램 작성
- [ ] GPT-4 Technical Report 요약 (MoE 추정 포함)
- [ ] 2020-2024 주요 모델 타임라인 업데이트
- [ ] 산출물 폴더 `04-Large-Models/` 생성 및 README.md 작성
- [ ] WorkLog 작성 완료
- [ ] M4 Module Retrospective 작성

#### Self-Assessment

**개념 이해** (10분):
- [ ] RLHF의 3단계 (SFT, Reward Model, PPO)를 순서대로 설명 가능
- [ ] InstructGPT가 GPT-3보다 나은 이유를 "Alignment"로 설명 가능
- [ ] MoE가 왜 효율적인지 "활성 파라미터" 개념으로 설명 가능

**실무 활용** (10분):
- [ ] 챗봇 프로젝트 시 RLHF를 적용해야 하는 이유를 AI에게 설명 가능
- [ ] LLaMA 2와 GPT-3.5 중 선택 기준 (오픈소스, 비용, 성능)을 판단 가능
- [ ] AI에게 "MoE 기반 모델 구현" 요청 시 핵심 구조 설명 가능

**문제 해결** (10분):
- [ ] 모델이 유해한 응답 생성 시 RLHF 적용 방향 제시 가능
- [ ] 대규모 모델 학습 시 메모리 부족 문제에 MoE 고려 가능

#### 예상 시간 배분

- 개념 학습 (논문 읽기): 120분 (28%)
- 실습 1 (InstructGPT/RLHF): 240분 (48%)
- 실습 2 (LLaMA 시리즈): 210분 (42%)
- 실습 3 (MoE): 165분 (33%)
- 문서화: 60분 (12%)
- **합계**: 6-8시간 (버퍼 20% 포함)

#### 참조 자료

- [InstructGPT: Training language models to follow instructions (2022)](https://arxiv.org/abs/2203.02155): InstructGPT 논문
- [LLaMA: Open and Efficient Foundation Language Models (2023)](https://arxiv.org/abs/2302.13971): LLaMA 1 논문
- [LLaMA 2: Open Foundation and Fine-Tuned Chat Models (2023)](https://arxiv.org/abs/2307.09288): LLaMA 2 논문
- [GPT-4 Technical Report (2023)](https://arxiv.org/abs/2303.08774): GPT-4 기술 보고서
- [Switch Transformers: Scaling to Trillion Parameter Models (2021)](https://arxiv.org/abs/2101.03961): MoE 논문
- [OpenAI RLHF Blog](https://openai.com/research/learning-from-human-preferences): RLHF 설명

---

### M5 - 최신 트렌드와 미래 방향 (2024-2026)

**난이도**: ⭐⭐⭐
**예상 시간**: 5-6h
**산출물 폴더**: `05-Latest-Trends/`

#### 학습 목표

- [ ] Claude 3.5 Sonnet/Opus의 기술적 특징과 경쟁 우위를 설명할 수 있다
- [ ] Gemini 2.0의 멀티모달 능력과 기술적 혁신을 이해하고 설명할 수 있다
- [ ] Multimodal Transformers (Vision-Language Models)의 작동 원리를 이해할 수 있다
- [ ] Quantization, Distillation 등 모델 경량화 기법을 설명할 수 있다
- [ ] 2024-2026 최신 Transformer 트렌드를 정리하고 미래 방향을 예측할 수 있다

#### 주요 개념

1. **Multimodal Transformers**: 텍스트, 이미지, 오디오 등 여러 모달리티를 통합 처리. Vision-Language 모델 (CLIP, GPT-4V, Gemini)의 기반.

2. **Constitutional AI**: Anthropic의 접근 방식. RLHF 대신 AI가 스스로 원칙(Constitution)을 학습하여 안전한 응답 생성.

3. **Long Context Window**: 최신 모델들은 수십만~수백만 토큰 처리 가능 (Claude 3.5: 200K, Gemini 1.5: 1M+). 긴 문서 분석에 유용.

4. **Quantization**: 모델 가중치를 낮은 비트 (8-bit, 4-bit)로 표현하여 메모리와 계산 비용 절감. 성능 손실 최소화.

5. **Knowledge Distillation**: 큰 모델(Teacher)의 지식을 작은 모델(Student)에 전이. 효율성 향상.

**오해하기 쉬운 포인트**:
- Multimodal은 "단순히 여러 입력 받기"가 아니라 "모달리티 간 관계 학습"
- Constitutional AI는 RLHF를 완전 대체가 아니라 보완적 접근
- Long Context는 단순 길이 증가가 아니라 Attention 메커니즘 최적화 필요

#### 실습 과제

**실습 1: Claude 3.5와 Gemini 2.0 기술 분석** ⭐⭐⭐

- **목적**: 최신 최고 성능 모델들의 기술적 특징 이해
- **단계**:
  1. Anthropic Claude 3.5 발표 자료 및 블로그 읽기 (60분)
  2. Google Gemini 2.0 기술 문서 읽기 (60분)
  3. 두 모델의 핵심 차이점 정리 (Constitutional AI vs Gemini 아키텍처) (45분)
  4. 벤치마크 성능 비교 (MMLU, HumanEval 등) (30분)
  5. 각 모델의 강점/약점 분석 문서 작성 (45분)
- **예상 시간**: 240분
- **검증**:
  - Claude 3.5 핵심 특징 요약 (Constitutional AI, 200K context)
  - Gemini 2.0 핵심 특징 요약 (Multimodal, 1M+ context)
  - 비교표 작성 (성능, 가격, 사용 사례)

**실습 2: Multimodal Transformers 개념 정리** ⭐⭐

- **목적**: Vision-Language 모델의 작동 원리 이해
- **단계**:
  1. CLIP, GPT-4V, Gemini Vision 관련 자료 읽기 (60분)
  2. Multimodal Fusion 방식 정리 (Early Fusion vs Late Fusion) (30분)
  3. 이미지-텍스트 임베딩 정렬 원리 다이어그램 작성 (45분)
  4. 사용 사례 정리 (이미지 캡셔닝, VQA, 문서 분석) (30분)
- **예상 시간**: 165분
- **검증**:
  - Multimodal Fusion 방식 설명 문서
  - 이미지-텍스트 정렬 다이어그램
  - 사용 사례 3개 이상 정리

**실습 3: 모델 경량화 기법 조사** ⭐⭐

- **목적**: Quantization, Distillation 등 효율성 향상 기법 이해
- **단계**:
  1. Quantization (8-bit, 4-bit) 개념 조사 (45분)
  2. Knowledge Distillation 원리 조사 (30분)
  3. LoRA, QLoRA 등 Fine-tuning 효율화 기법 조사 (30분)
  4. 각 기법의 장단점 비교표 작성 (30분)
  5. 실무 적용 시나리오 정리 (15분)
- **예상 시간**: 150분
- **검증**:
  - 경량화 기법 비교표 (Quantization, Distillation, LoRA)
  - 각 기법의 성능-효율 트레이드오프 분석
  - 적용 시나리오 3개 이상

#### 산출물

```
05-Latest-Trends/
├── README.md                          # 모듈 개요, 최신 트렌드 요약
├── concepts/
│   ├── multimodal-transformers.md     # Multimodal 개념
│   ├── constitutional-ai.md           # Constitutional AI 설명
│   ├── long-context-window.md         # Long Context 기법
│   ├── quantization.md                # Quantization 설명
│   └── knowledge-distillation.md      # Distillation 설명
├── models/
│   ├── claude-3.5-analysis.md         # Claude 3.5 분석
│   ├── gemini-2.0-analysis.md         # Gemini 2.0 분석
│   ├── gpt4-vision-analysis.md        # GPT-4V 분석
│   └── latest-models-comparison.md    # 최신 모델 비교표
├── trends/
│   ├── 2024-2026-trends.md            # 최신 트렌드 정리
│   ├── multimodal-revolution.md       # Multimodal 혁명
│   ├── efficiency-improvements.md     # 효율성 개선 트렌드
│   └── future-directions.md           # 미래 방향 예측
├── diagrams/
│   ├── multimodal-fusion.png          # Multimodal Fusion 다이어그램
│   ├── claude-vs-gemini.png           # Claude vs Gemini 비교
│   └── quantization-comparison.png    # Quantization 비교
└── guides/
    └── how-to-choose-latest-model.md  # 최신 모델 선택 가이드
```

#### Definition of Done

- [ ] Claude 3.5와 Gemini 2.0 기술 분석 문서 작성
- [ ] 최신 모델 비교표 작성 (성능, 가격, 특징)
- [ ] Multimodal Transformers 개념 문서 및 다이어그램 작성
- [ ] 모델 경량화 기법 비교표 작성 (Quantization, Distillation, LoRA)
- [ ] 2024-2026 트렌드 정리 및 미래 방향 예측 문서 작성
- [ ] 산출물 폴더 `05-Latest-Trends/` 생성 및 README.md 작성
- [ ] WorkLog 작성 완료
- [ ] M5 Module Retrospective 작성

#### Self-Assessment

**개념 이해** (10분):
- [ ] Claude 3.5의 Constitutional AI가 무엇인지 RLHF와 비교하여 설명 가능
- [ ] Multimodal Transformers가 이미지와 텍스트를 어떻게 통합하는지 설명 가능
- [ ] Quantization이 모델 크기와 속도에 미치는 영향 설명 가능

**실무 활용** (10분):
- [ ] 프로젝트에 Claude 3.5, GPT-4, Gemini 중 선택 기준 판단 가능
- [ ] 이미지 분석 태스크 시 Multimodal 모델 활용 방안 AI에게 설명 가능
- [ ] 모바일 배포 시 Quantization 적용 여부를 판단하고 AI에게 요청 가능

**문제 해결** (10분):
- [ ] Long Context 처리 시 메모리 부족 문제 해결 방향 제시 가능
- [ ] Quantization 후 성능 저하 시 원인 분석 및 개선 방법 제안 가능

#### 예상 시간 배분

- 개념 학습 (자료 읽기): 90분 (27%)
- 실습 1 (Claude/Gemini 분석): 240분 (55%)
- 실습 2 (Multimodal): 165분 (38%)
- 실습 3 (경량화 기법): 150분 (34%)
- 문서화: 45분 (10%)
- **합계**: 5-6시간 (버퍼 20% 포함)

#### 참조 자료

- [Anthropic Claude 3.5 Release](https://www.anthropic.com/news/claude-3-5-sonnet): Claude 3.5 발표
- [Constitutional AI Paper](https://arxiv.org/abs/2212.08073): Constitutional AI 논문
- [Google Gemini 2.0 Report](https://deepmind.google/technologies/gemini/): Gemini 기술 문서
- [CLIP: Connecting Text and Images](https://arxiv.org/abs/2103.00020): CLIP 논문
- [Quantization Methods Overview](https://huggingface.co/docs/transformers/quantization): Quantization 가이드
- [LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685): LoRA 논문

---

### M6 - 통합 정리 및 타임라인 문서 완성

**난이도**: ⭐⭐
**예상 시간**: 4-5h
**산출물 폴더**: `06-Timeline-Final/`

#### 학습 목표

- [ ] 2017-2026 Transformer 발전사를 연도별 타임라인으로 완성할 수 있다
- [ ] 주요 모델 15개 이상의 핵심 특징과 혁신을 정리할 수 있다
- [ ] 각 시대별 주요 트렌드와 패러다임 전환을 분석할 수 있다
- [ ] 전체 학습 내용을 "교과서 품질" 문서로 통합할 수 있다
- [ ] Transformer 발전사의 인사이트를 도출하고 미래를 예측할 수 있다

#### 주요 개념

1. **Transformer 시대 구분**:
   - 탄생기 (2017-2018): Attention is All You Need, GPT-1, BERT
   - 성장기 (2019-2020): GPT-2/3, T5, Scaling Laws
   - 대규모화 (2021-2023): GPT-3.5/4, InstructGPT, LLaMA, RLHF
   - 다변화 (2024-2026): Claude 3.5, Gemini 2.0, Multimodal, 효율화

2. **핵심 혁신 요소**:
   - 아키텍처: Self-Attention, Multi-Head Attention, MoE
   - 학습 방식: Pre-training, Fine-tuning, RLHF, Constitutional AI
   - 확장성: Scaling Laws, Long Context, Multimodal
   - 효율성: Quantization, Distillation, LoRA

3. **패러다임 전환**:
   - RNN → Transformer (병렬 처리)
   - Fine-tuning → Few-shot (GPT-3)
   - 텍스트 전용 → Multimodal
   - 클로즈드 → 오픈소스 (LLaMA)

#### 실습 과제

**실습 1: 2017-2026 Transformer 타임라인 작성** ⭐⭐

- **목적**: 전체 학습 내용을 시각적 타임라인으로 통합
- **단계**:
  1. 각 모듈에서 작성한 타임라인 취합 (30분)
  2. 연도별 주요 모델과 논문 정리 (60분)
  3. 각 모델의 핵심 혁신 1-2문장으로 요약 (60분)
  4. 시대별 구분 및 트렌드 추가 (30분)
  5. 타임라인 시각화 (Markdown 표 또는 다이어그램) (60분)
- **예상 시간**: 240분
- **검증**:
  - 2017-2026 모든 연도 커버
  - 주요 모델 15개 이상 포함 (Transformer, GPT-1/2/3/3.5/4, BERT, T5, InstructGPT, LLaMA 1/2/3, Claude 3.5, Gemini 2.0 등)
  - 각 모델의 핵심 혁신 명시
  - 시대별 구분 및 트렌드 설명

**실습 2: 모델 비교 마스터 테이블 작성** ⭐⭐

- **목적**: 주요 모델들을 한눈에 비교할 수 있는 종합 비교표 작성
- **단계**:
  1. 각 모듈의 비교표 통합 (30분)
  2. 비교 항목 확정 (아키텍처, 파라미터, 학습 데이터, 사전 학습 방식, 주요 태스크, 핵심 혁신) (15분)
  3. 15개 이상 모델의 정보 수집 및 정리 (90분)
  4. Markdown 표로 정리 (30분)
  5. 사용 사례별 추천 모델 섹션 추가 (15분)
- **예상 시간**: 180분
- **검증**:
  - 최소 15개 모델 비교
  - 비교 항목 6개 이상
  - 사용 사례별 추천 (분류, 생성, 번역, 대화 등)

**실습 3: 최종 "교과서 품질" 문서 작성** ⭐⭐⭐

- **목적**: 다른 학습자가 이 문서만으로 Transformer 발전사를 이해할 수 있는 고품질 문서 작성
- **단계**:
  1. 전체 학습 내용 리뷰 및 핵심 추출 (45분)
  2. 목차 구성 (Introduction, Timeline, 시대별 분석, 핵심 혁신, 미래 방향, Conclusion) (30분)
  3. 각 섹션 작성 (120분)
  4. 다이어그램, 표, 참조 자료 추가 (45분)
  5. 교정 및 최종 검토 (30분)
- **예상 시간**: 270분
- **검증**:
  - 전체 15-25페이지 분량
  - Introduction에 Transformer의 중요성 설명
  - 타임라인 및 비교표 포함
  - 시대별 분석 (탄생기, 성장기, 대규모화, 다변화)
  - 핵심 혁신 정리 (Self-Attention, Scaling Laws, RLHF, Multimodal 등)
  - 미래 방향 예측 (AGI, 효율화, 다중 모달리티 등)
  - 모든 논문 및 참조 자료 링크 포함

#### 산출물

```
06-Timeline-Final/
├── README.md                          # 모듈 개요, Capstone 프로젝트 설명
├── final-deliverables/
│   ├── Transformer-Timeline-2017-2026.md  # 최종 타임라인 문서 (교과서 품질)
│   ├── Model-Comparison-Master-Table.md   # 종합 비교표
│   ├── Key-Innovations-Summary.md         # 핵심 혁신 요약
│   └── Future-Directions-Analysis.md      # 미래 방향 분석
├── diagrams/
│   ├── transformer-timeline-visual.png    # 타임라인 시각화
│   ├── architecture-evolution.png         # 아키텍처 진화
│   ├── performance-trends.png             # 성능 트렌드 그래프
│   └── paradigm-shifts.png                # 패러다임 전환 다이어그램
├── presentations/
│   └── Transformer-Evolution-Slides.pptx  # (선택) 발표 자료
├── references/
│   └── All-Papers-Bibliography.md         # 모든 참조 논문 목록
└── retrospectives/
    └── Topic-Final-Retrospective.md       # 전체 Topic 회고
```

**최종 타임라인 문서 구조**:
```markdown
# Transformer 발전사: 2017-2026

## 1. Introduction
- Transformer의 탄생 배경
- AI 분야에 미친 영향
- 본 문서의 목적

## 2. Timeline (2017-2026)
- 연도별 주요 모델 및 논문
- 핵심 혁신 요약

## 3. 시대별 분석
- 3.1 탄생기 (2017-2018)
- 3.2 성장기 (2019-2020)
- 3.3 대규모화 (2021-2023)
- 3.4 다변화 (2024-2026)

## 4. 핵심 혁신
- Self-Attention 메커니즘
- Scaling Laws
- RLHF와 Alignment
- Multimodal Transformers
- 효율화 기법

## 5. 모델 비교표
- 주요 모델 15개 비교

## 6. 미래 방향
- AGI로 가는 길
- 효율성과 접근성
- 윤리와 안전성

## 7. Conclusion
- 핵심 인사이트
- 학습자를 위한 조언

## 8. References
- 모든 논문 및 자료
```

#### Definition of Done

- [ ] 2017-2026 Transformer 타임라인 완성 (주요 모델 15개 이상)
- [ ] 모델 비교 마스터 테이블 작성 (15개 모델, 6개 이상 비교 항목)
- [ ] 최종 "교과서 품질" 문서 작성 (15-25페이지)
- [ ] 다이어그램 4개 이상 생성 (타임라인, 아키텍처 진화, 성능 트렌드, 패러다임 전환)
- [ ] 핵심 혁신 요약 문서 작성
- [ ] 미래 방향 분석 문서 작성
- [ ] 전체 참조 논문 목록 정리
- [ ] Topic Final Retrospective 작성
- [ ] 산출물 폴더 `06-Timeline-Final/` 생성 및 README.md 작성

#### Self-Assessment

**개념 이해** (15분):
- [ ] Transformer 발전사를 4개 시대로 구분하고 각 시대의 특징 설명 가능
- [ ] Self-Attention부터 Multimodal까지 핵심 혁신을 시간순으로 설명 가능
- [ ] GPT, BERT, T5의 차이를 아키텍처와 사용 사례로 비교 가능

**실무 활용** (15분):
- [ ] 프로젝트 유형에 따라 최적 모델 추천 가능 (예: 분류→BERT, 생성→GPT, 번역→T5)
- [ ] 2017-2026 Transformer 발전사를 20분 내로 발표 가능
- [ ] 다른 학습자에게 Transformer를 가르칠 수 있는 자료 보유

**문제 해결** (10분):
- [ ] 최신 모델 등장 시 기존 지식으로 핵심 혁신을 빠르게 파악 가능
- [ ] Transformer 기반 프로젝트 실패 시 역사적 맥락에서 문제 분석 가능

#### 예상 시간 배분

- 실습 1 (타임라인): 240분 (50%)
- 실습 2 (비교표): 180분 (38%)
- 실습 3 (최종 문서): 270분 (56%)
- 검토 및 교정: 60분 (12%)
- **합계**: 4-5시간 (버퍼 20% 포함)

#### 참조 자료

- 이전 모듈(M1-M5)의 모든 산출물
- [Papers with Code - Transformers](https://paperswithcode.com/methods/category/transformers): 최신 Transformer 논문
- [Hugging Face Model Hub](https://huggingface.co/models): 모델 정보
- [The AI Index Report](https://aiindex.stanford.edu/): AI 트렌드 분석
- [State of AI Report](https://www.stateof.ai/): 연례 AI 동향

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

### 파일명 규칙

`vl_worklog/YYYYMMDD_MX_AI-Modeling-Transformer.md`
- 예: `vl_worklog/20260112_M1_AI-Modeling-Transformer.md`

### WorkLog 필수 섹션

1. **오늘의 학습 목표** (체크리스트)
   ```markdown
   - [ ] "Attention is All You Need" 논문 읽기 (Abstract, Introduction, Section 3)
   - [ ] Self-Attention 메커니즘 이해 및 다이어그램 작성
   - [ ] 논문 핵심 요약 2페이지 작성
   ```

2. **진행 내용** (실습별 상세 기록)
   ```markdown
   ### 실습 1: "Attention is All You Need" 논문 분석
   - **시작 시간**: 10:00
   - **종료 시간**: 13:00
   - **실제 소요**: 180분 (예상: 180분)
   - **진행 상황**:
     - Abstract, Introduction 읽기 완료
     - Section 3 (Model Architecture) 정독
     - Self-Attention 수식 이해에 어려움 → The Illustrated Transformer 참고
     - 다이어그램 2개 작성 (Self-Attention, Multi-Head Attention)
   - **산출물**: `01-Transformer-Basics/papers/paper-summary.md` (초안)
   ```

3. **문제 해결 로그**
   ```markdown
   ### 문제 1: Self-Attention 수식 이해 어려움
   - **문제**: Scaled Dot-Product Attention 수식이 직관적이지 않음
   - **해결**: The Illustrated Transformer 블로그 읽고 예시로 이해
   - **소요 시간**: 30분
   - **학습**: Q, K, V를 실제 단어로 계산해보니 이해됨

   ### 문제 2: Positional Encoding 공식 복잡
   - **문제**: sin/cos 공식의 의미 불명확
   - **해결**: Claude에게 질문하여 "위치 정보 주입" 개념으로 이해
   - **소요 시간**: 15분
   ```

4. **DoD 체크리스트** (모듈 완료 기준)
   ```markdown
   - [x] "Attention is All You Need" 논문 읽기 완료
   - [x] Self-Attention 메커니즘 설명 문서 작성
   - [ ] Transformer 아키텍처 다이어그램 3개 생성 (2/3 완료)
   - [ ] Multi-Head Attention, Positional Encoding 개념 문서 작성
   - [ ] 산출물 폴더 생성 및 README.md 작성
   ```

5. **Daily Retrospective**
   ```markdown
   **What went well?**
   - 논문 읽기가 예상보다 수월했음 (The Illustrated Transformer 덕분)
   - Self-Attention 다이어그램 작성으로 이해 깊어짐

   **What could be improved?**
   - 수식 이해에 시간 소요 → 다음부터 먼저 시각화 자료 참고
   - 문서화를 미뤄서 내일 추가 작업 필요

   **Insights**
   - Transformer의 핵심은 "병렬 처리 가능한 Self-Attention"
   - RNN 없이도 시퀀스 처리 가능하다는 게 혁신적

   **Tomorrow's focus**
   - Multi-Head Attention, Positional Encoding 개념 문서 완성
   - 실습 2 (아키텍처 시각화) 시작
   ```

6. **참조 및 산출물**
   ```markdown
   **참조 자료**:
   - [Attention is All You Need](https://arxiv.org/abs/1706.03762)
   - [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

   **생성 산출물**:
   - `01-Transformer-Basics/papers/paper-summary.md` (초안, 2페이지)
   - `01-Transformer-Basics/diagrams/self-attention-process.png`
   ```

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)

WorkLog 내에 작성:
- **What went well?**: 오늘 잘된 점 1-2가지
- **What could be improved?**: 개선할 점 1-2가지
- **Insights**: 오늘의 핵심 인사이트
- **Tomorrow's focus**: 내일 집중할 영역

### Module Retrospective (모듈 완료 시, 15-20분)

`vl_worklog/YYYYMMDD_MX_Retrospective_AI-Modeling-Transformer.md`:

```markdown
# M1 Module Retrospective

**모듈명**: Transformer 탄생과 기본 원리
**시작일**: 2026-01-12
**종료일**: 2026-01-14
**예상 시간**: 6-8h
**실제 소요**: 7.5h

## 계획 대비 실제

| 항목 | 계획 | 실제 | 차이 |
|------|------|------|------|
| 논문 읽기 | 120분 | 150분 | +30분 |
| 실습 1 | 180분 | 180분 | 0분 |
| 실습 2 | 180분 | 150분 | -30분 |
| 문서화 | 60분 | 90분 | +30분 |
| **합계** | 6-8h | 7.5h | 적정 |

## 핵심 학습 내용

1. **Self-Attention 메커니즘**: Q, K, V 개념과 Scaled Dot-Product Attention
2. **Multi-Head Attention**: 다양한 표현 부공간 학습
3. **Positional Encoding**: sin/cos 함수로 위치 정보 주입
4. **Transformer 아키텍처**: Encoder-Decoder 구조, 6층 스택

## 발생한 문제와 해결

**문제 1**: Self-Attention 수식 이해 어려움
- **해결**: The Illustrated Transformer로 시각화 학습
- **교훈**: 복잡한 개념은 시각화 자료부터 시작

**문제 2**: 실습 3 (구현) 시간 부족
- **해결**: 선택 과제로 분류하고 다음에 진행
- **교훈**: 필수/선택 구분 명확히

## Roadmap 정확도 평가

- **학습 목표**: ⭐⭐⭐⭐⭐ (5/5 달성)
- **예상 시간**: ⭐⭐⭐⭐☆ (7.5h, 6-8h 범위 내)
- **실습 난이도**: ⭐⭐⭐⭐☆ (적절, 약간 도전적)
- **산출물 품질**: ⭐⭐⭐⭐☆ (만족, 다이어그램 개선 필요)

**Roadmap 개선 제안**:
- 실습 1에 "수식 이해 전 시각화 자료 참고" 단계 추가
- 실습 3 (구현)을 완전히 선택으로 명시

## 다음 모듈 준비사항

- GPT 시리즈 논문 3개 미리 다운로드
- Hugging Face Transformers 라이브러리 설치 완료
- Few-shot Learning 개념 사전 조사
```

### Topic Retrospective (전체 완료 시, 30-60분)

`vl_worklog/YYYYMMDD_AI-Modeling-Transformer_Final_Retrospective.md`:

```markdown
# AI-Modeling-Transformer Topic Final Retrospective

**Topic 이름**: AI-Modeling-Transformer
**시작일**: 2026-01-12
**종료일**: 2026-02-09
**예상 기간**: 4주 (32-40h)
**실제 소요**: 4주 1일 (38h)

## 전체 학습 여정 통계

| 모듈 | 예상 시간 | 실제 시간 | DoD 달성률 | 비고 |
|------|----------|----------|-----------|------|
| M1 | 6-8h | 7.5h | 100% | Self-Attention 이해 깊음 |
| M2 | 6-8h | 7h | 100% | Few-shot 실습 재미있었음 |
| M3 | 5-7h | 6h | 100% | BERT Fine-tuning 성공 |
| M4 | 6-8h | 8.5h | 100% | RLHF 복잡했지만 중요 |
| M5 | 5-6h | 5.5h | 100% | 최신 트렌드 흥미로움 |
| M6 | 4-5h | 4.5h | 100% | 타임라인 작성 보람 있음 |
| **합계** | 32-42h | 38h | 100% | 계획 대비 적정 |

## CUA_VL 방법론 효과성 평가

### 긍정적 측면
- **실습 중심**: 논문 읽기 후 즉시 실습으로 이해 강화
- **산출물 품질**: "교과서 품질" 목표로 타임라인 문서 우수
- **모듈 구조**: 6개 모듈로 점진적 학습, 난이도 적절
- **Retrospective**: 매일/모듈/전체 회고로 학습 개선

### 개선 필요
- **시간 추정**: 초반 모듈은 시간 부족 (익숙해지면 정확해짐)
- **선택 과제**: 필수/선택 구분이 명확하지 않은 부분 있음
- **참조 자료**: 일부 링크가 오래되거나 접근 불가

## 산출물 품질 평가

### 최종 산출물
1. **Transformer 타임라인 (2017-2026)**: ⭐⭐⭐⭐⭐ (교과서 품질 달성)
2. **모델 비교표**: ⭐⭐⭐⭐⭐ (18개 모델, 상세 비교)
3. **논문 요약 문서**: ⭐⭐⭐⭐☆ (10개 논문, 핵심 추출)
4. **다이어그램**: ⭐⭐⭐⭐☆ (12개 생성, 일부 개선 필요)
5. **개념 문서**: ⭐⭐⭐⭐⭐ (20개 핵심 개념, 명확)

### "교과서 품질" 달성 여부
- ✅ **달성**: 다른 학습자가 이 산출물만으로 Transformer 발전사 이해 가능
- ✅ 시각화, 참조, 설명 모두 포함
- ✅ 구조화되고 체계적

## 핵심 인사이트

1. **Self-Attention의 혁명**: RNN 없이 병렬 처리 가능 → NLP 패러다임 전환
2. **Scaling Laws**: 모델 크기 증가가 성능 향상으로 이어짐 (GPT-3 검증)
3. **Alignment의 중요성**: RLHF/Constitutional AI로 안전한 AI 구현
4. **오픈소스 영향**: LLaMA가 AI 생태계 민주화에 기여
5. **Multimodal 미래**: 텍스트 넘어 다양한 모달리티 통합 트렌드

## 향후 학습 개선 사항

### 다음 Topic에 적용할 점
1. **시간 추정**: 첫 모듈은 +20% 여유 두기
2. **참조 자료**: 학습 전 모든 링크 검증
3. **실습 균형**: 필수 70%, 선택 30% 명확히 구분
4. **일일 목표**: 3-4시간 세션으로 집중도 유지

### CUA_VL 방법론 피드백
- Roadmap 템플릿 우수, 9가지 필수 항목 효과적
- WorkLog가 진행 상황 추적에 매우 유용
- Retrospective로 지속적 개선 가능

## 다음 학습 계획

**추천 다음 Topic**:
1. **AI-Modeling-Diffusion**: Diffusion Models (DALL-E, Stable Diffusion)
2. **AI-Agents**: LangChain, AutoGPT, Agent 아키텍처
3. **MLOps-Deployment**: 모델 배포 및 운영

**우선순위**: AI-Agents (Transformer 지식 활용)
```

---

## 📂 전체 폴더 구조

```
AI-Modeling-Transformer/
├── topic_info.md              # Topic 기본 정보 (참조)
├── vl_prompts/
│   ├── roadmap_prompt.md      # Roadmap 생성 프롬프트
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260110_RoadMap_AI-Modeling-Transformer.md  # 이 로드맵
├── vl_worklog/
│   ├── 20260112_M1_AI-Modeling-Transformer.md
│   ├── 20260113_M1_AI-Modeling-Transformer.md
│   ├── 20260114_M1_Retrospective_AI-Modeling-Transformer.md
│   ├── 20260115_M2_AI-Modeling-Transformer.md
│   ├── ...
│   └── 20260209_AI-Modeling-Transformer_Final_Retrospective.md
├── vl_materials/              # 참조 자료 (선택)
│   ├── papers/
│   │   ├── Attention-is-All-You-Need.pdf
│   │   ├── GPT-3.pdf
│   │   └── ...
│   ├── slides/
│   └── videos/
├── 01-Transformer-Basics/
│   ├── README.md
│   ├── concepts/
│   ├── papers/
│   ├── diagrams/
│   ├── examples/
│   └── guides/
├── 02-GPT-Evolution/
│   ├── README.md
│   ├── concepts/
│   ├── papers/
│   ├── timeline/
│   ├── examples/
│   └── guides/
├── 03-Encoder-Models/
│   ├── README.md
│   ├── concepts/
│   ├── papers/
│   ├── comparisons/
│   ├── diagrams/
│   ├── examples/
│   └── guides/
├── 04-Large-Models/
│   ├── README.md
│   ├── concepts/
│   ├── papers/
│   ├── comparisons/
│   ├── diagrams/
│   ├── timeline/
│   └── guides/
├── 05-Latest-Trends/
│   ├── README.md
│   ├── concepts/
│   ├── models/
│   ├── trends/
│   ├── diagrams/
│   └── guides/
└── 06-Timeline-Final/
    ├── README.md
    ├── final-deliverables/
    │   ├── Transformer-Timeline-2017-2026.md  # 핵심 산출물
    │   ├── Model-Comparison-Master-Table.md
    │   ├── Key-Innovations-Summary.md
    │   └── Future-Directions-Analysis.md
    ├── diagrams/
    ├── presentations/
    ├── references/
    └── retrospectives/
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | | | ⏳ | 0% | |
| M2 | | | ⏳ | 0% | |
| M3 | | | ⏳ | 0% | |
| M4 | | | ⏳ | 0% | |
| M5 | | | ⏳ | 0% | |
| M6 | | | ⏳ | 0% | |

**범례**:
- ⏳ 대기
- 🔄 진행 중
- ✅ 완료

**진행 방법**:
1. 모듈 시작 시 "시작일" 기록, 상태를 🔄로 변경
2. 매일 DoD 체크리스트 확인하여 달성률 업데이트
3. 모듈 완료 시 "종료일" 기록, 상태를 ✅로 변경, DoD 100% 확인
4. Module Retrospective 작성

---

## 🎯 성공 기준

전체 Topic 완료 기준:

- [ ] 모든 모듈 완료 (M1-M6, DoD 100%)
- [ ] 6개 산출물 폴더 생성 (`01-`~`06-`)
- [ ] 주요 논문 10개 이상 읽기 및 요약
- [ ] Transformer 타임라인 (2017-2026) 작성 (교과서 품질)
- [ ] 모델 비교 마스터 테이블 작성 (15개 이상 모델)
- [ ] 핵심 개념 문서 20개 이상 작성
- [ ] 다이어그램 10개 이상 생성
- [ ] Topic Final Retrospective 작성
- [ ] Self-Assessment 평균 80% 이상 (모든 항목 체크 가능)
- [ ] 최종 산출물을 다른 학습자와 공유 가능한 수준

**품질 기준**:
- **교과서 품질**: 타임라인 문서를 읽으면 Transformer 발전사 이해 가능
- **시각화**: 모든 주요 개념이 다이어그램으로 표현
- **참조 완비**: 모든 정보에 논문/블로그 출처 명시
- **실용성**: 실무에서 모델 선택 시 참고 가능

---

## 💡 학습 팁

### 효율적 논문 읽기
1. **3-Pass 방법**:
   - 1차: Abstract, Introduction, Conclusion (10분)
   - 2차: 섹션 제목, 다이어그램, 표 (20분)
   - 3차: 상세 읽기 (필요한 섹션만, 30-60분)

2. **핵심 추출**:
   - "이 논문의 핵심 기여는?" 1문장으로 요약
   - "이전 연구와 어떻게 다른가?" 비교
   - "실험 결과는 무엇을 증명하는가?" 파악

3. **AI 활용**:
   - Claude에게 논문 요약 요청 가능
   - 이해 안 되는 수식/개념 질문
   - 다만 직접 읽기를 우선, AI는 보조

### 시각화 전략
1. **다이어그램 도구**: Draw.io, Excalidraw, PowerPoint
2. **그래프**: Python matplotlib, seaborn
3. **타임라인**: Markdown 표 또는 Mermaid 다이어그램

### 시간 관리
1. **포모도로**: 50분 집중 + 10분 휴식
2. **일일 목표**: 3-4시간 세션 (너무 길면 집중력 저하)
3. **주말 활용**: 토/일 각 4-5시간 집중 학습

### 막힐 때
1. **The Illustrated Transformer**: 시각화로 이해
2. **YouTube 강의**: Andrej Karpathy, Stanford CS224N
3. **Claude/ChatGPT**: 개념 설명 요청
4. **커뮤니티**: Reddit r/MachineLearning, Papers with Code

---

## 🔗 주요 참조 자료

### 논문 검색
- [ArXiv](https://arxiv.org/): 최신 논문
- [Papers with Code](https://paperswithcode.com/): 논문 + 코드
- [Hugging Face Papers](https://huggingface.co/papers): 일간 최신 논문

### 공식 블로그
- [OpenAI Research](https://openai.com/research)
- [Google AI Blog](https://ai.googleblog.com)
- [Anthropic Research](https://www.anthropic.com/research)
- [Meta AI](https://ai.meta.com/research/)

### 학습 자료
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/)
- [Stanford CS224N](http://web.stanford.edu/class/cs224n/)
- [Hugging Face Course](https://huggingface.co/learn/nlp-course)

### 구현 참조
- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [nanoGPT (Karpathy)](https://github.com/karpathy/nanoGPT)
- [Annotated Transformer](https://github.com/harvardnlp/annotated-transformer)

---

**생성자**: Claude with CUA_VL
**Roadmap 버전**: 1.0
**생성일**: 2026-01-10
**방법론**: CUA_VL (Catch Up AI Vibe Learning) 2.0
**다음 단계**: `/cua-vl daily`로 M1 학습 계획 수립
