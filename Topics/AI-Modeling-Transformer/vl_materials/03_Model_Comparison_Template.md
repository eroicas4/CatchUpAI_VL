# 모델 비교표 템플릿

**Topic**: AI-Modeling-Transformer
**생성일**: 2026-01-10

> **사용 방법**: 각 모델을 학습하면서 표를 채워나가세요.
> M6 모듈에서 최종 마스터 비교표를 완성합니다.

---

## 📊 모델 마스터 비교표

| 모델 | 연도 | 조직 | 파라미터 | 아키텍처 | 학습 데이터 | 주요 벤치마크 | 핵심 혁신 |
|------|------|------|---------|---------|------------|-------------|---------|
| Transformer | 2017 | Google | - | Enc-Dec | WMT | BLEU | Attention |
| GPT-1 | 2018 | OpenAI | 117M | Decoder | BooksCorpus | - | Pre-training |
| BERT | 2018 | Google | 340M | Encoder | Wiki+Books | GLUE | Bidirectional |
| GPT-2 | 2019 | OpenAI | 1.5B | Decoder | WebText | - | Zero-shot |
| T5 | 2019 | Google | 11B | Enc-Dec | C4 | SuperGLUE | Text-to-Text |
| GPT-3 | 2020 | OpenAI | 175B | Decoder | - | - | Few-shot |
| InstructGPT | 2022 | OpenAI | - | Decoder | - | - | RLHF |
| ChatGPT | 2022 | OpenAI | - | Decoder | - | - | Dialogue |
| LLaMA | 2023 | Meta | 7B-65B | Decoder | - | - | Open Source |
| GPT-4 | 2023 | OpenAI | ? | Decoder | - | - | Multimodal |
| Claude 3 | 2024 | Anthropic | ? | - | - | - | Long Context |

> **작성 팁**: "?" 표시된 부분은 공개되지 않은 정보입니다. 학습하면서 알게 되는 내용을 추가하세요.

---

## 🔍 상세 비교표

### 1. GPT 시리즈 비교

| 특성 | GPT-1 | GPT-2 | GPT-3 | GPT-3.5 | GPT-4 |
|------|-------|-------|-------|---------|-------|
| 발표 연도 | 2018 | 2019 | 2020 | 2022 | 2023 |
| 파라미터 | 117M | 1.5B | 175B | ? | ? |
| 학습 데이터 | [작성] | [작성] | [작성] | [작성] | [작성] |
| 주요 능력 | [작성] | Zero-shot | Few-shot | RLHF | Multimodal |
| 핵심 혁신 | [작성] | [작성] | [작성] | [작성] | [작성] |
| 성능 (벤치마크) | [작성] | [작성] | [작성] | [작성] | [작성] |

**주요 개선사항**:
- GPT-1 → GPT-2: [학습 후 작성]
- GPT-2 → GPT-3: [학습 후 작성]
- GPT-3 → GPT-3.5: [학습 후 작성]
- GPT-3.5 → GPT-4: [학습 후 작성]

---

### 2. BERT 계열 모델 비교

| 특성 | BERT | RoBERTa | ALBERT | DistilBERT |
|------|------|---------|--------|------------|
| 발표 연도 | 2018 | 2019 | 2019 | 2019 |
| 파라미터 | 340M | [작성] | [작성] | [작성] |
| 핵심 기법 | MLM + NSP | [작성] | [작성] | [작성] |
| 개선사항 | - | [작성] | [작성] | [작성] |
| 성능 | [작성] | [작성] | [작성] | [작성] |

---

### 3. Encoder vs Decoder vs Encoder-Decoder

| 특성 | Encoder (BERT) | Decoder (GPT) | Enc-Dec (T5) |
|------|----------------|---------------|--------------|
| 아키텍처 | [다이어그램] | [다이어그램] | [다이어그램] |
| 학습 방식 | MLM | Auto-regressive | Seq2Seq |
| 주요 용도 | [작성] | [작성] | [작성] |
| 장점 | [작성] | [작성] | [작성] |
| 단점 | [작성] | [작성] | [작성] |
| 대표 모델 | BERT, RoBERTa | GPT 시리즈 | T5, BART |

---

### 4. 오픈소스 LLM 비교

| 특성 | LLaMA | LLaMA 2 | LLaMA 3 | Mistral | Falcon |
|------|-------|---------|---------|---------|--------|
| 발표 연도 | 2023 | 2023 | 2024 | 2023 | 2023 |
| 조직 | Meta | Meta | Meta | Mistral AI | TII |
| 파라미터 | 7B-65B | [작성] | [작성] | [작성] | [작성] |
| 라이선스 | [작성] | [작성] | [작성] | [작성] | [작성] |
| 성능 | [작성] | [작성] | [작성] | [작성] | [작성] |

---

### 5. 최신 Frontier 모델 비교 (2024-2026)

| 특성 | Claude 3 Opus | GPT-4 | Gemini 2.0 | [기타] |
|------|--------------|-------|-----------|--------|
| 조직 | Anthropic | OpenAI | Google | [작성] |
| 파라미터 | ? | ? | ? | ? |
| 컨텍스트 길이 | 200K | [작성] | [작성] | [작성] |
| Multimodal | Yes | Yes | Yes | [작성] |
| 핵심 기술 | [작성] | [작성] | [작성] | [작성] |
| 성능 | [작성] | [작성] | [작성] | [작성] |

---

## 📈 성능 비교 (벤치마크별)

### GLUE (General Language Understanding Evaluation)

| 모델 | GLUE 점수 | CoLA | SST-2 | MRPC | ... |
|------|-----------|------|-------|------|-----|
| BERT | [작성] | [작성] | [작성] | [작성] | ... |
| RoBERTa | [작성] | [작성] | [작성] | [작성] | ... |
| ALBERT | [작성] | [작성] | [작성] | [작성] | ... |

### MMLU (Massive Multitask Language Understanding)

| 모델 | MMLU 점수 | STEM | Humanities | Social Sciences |
|------|-----------|------|------------|-----------------|
| GPT-3 | [작성] | [작성] | [작성] | [작성] |
| GPT-4 | [작성] | [작성] | [작성] | [작성] |
| Claude 3 | [작성] | [작성] | [작성] | [작성] |

---

## 💡 비교 기준 가이드

### 파라미터 수
- **Small**: < 1B
- **Medium**: 1B - 10B
- **Large**: 10B - 100B
- **Very Large**: > 100B

### 아키텍처 타입
- **Encoder-only**: BERT 계열 (양방향 이해)
- **Decoder-only**: GPT 계열 (생성)
- **Encoder-Decoder**: T5, BART (번역, 요약)

### 학습 방식
- **MLM** (Masked Language Modeling): BERT
- **Auto-regressive**: GPT
- **Seq2Seq**: T5

### 주요 용도
- **분류/이해**: BERT 계열
- **생성**: GPT 계열
- **번역/요약**: Encoder-Decoder

---

## 🎯 M6에서 완성할 최종 비교표

M6 모듈에서 다음을 추가하여 최종 마스터 비교표를 완성하세요:

1. **시각화**:
   - 파라미터 수 증가 그래프 (연도별)
   - 성능 향상 그래프 (벤치마크별)
   - 아키텍처 진화 다이어그램

2. **상세 분석**:
   - 각 모델의 장단점
   - 사용 시나리오 (어떤 작업에 적합한가)
   - 비용/성능 트레이드오프

3. **인사이트**:
   - 모델 발전 패턴
   - 향후 발전 방향 예측
   - 실무 적용 팁

4. **참조 링크**:
   - 각 모델의 공식 문서
   - 벤치마크 사이트
   - 데모/플레이그라운드

---

**작성자**: CUA_VL Claude Skills 학습
**버전**: 1.0 (템플릿)
**최종 업데이트**: 2026-01-10
**상태**: 학습 진행하면서 채워나갈 것
