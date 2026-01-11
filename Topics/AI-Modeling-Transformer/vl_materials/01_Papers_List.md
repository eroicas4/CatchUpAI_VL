# 주요 논문 목록 및 링크

**Topic**: AI-Modeling-Transformer
**생성일**: 2026-01-10

---

## 📋 모듈별 필수 논문

### M1 - Transformer 탄생과 기본 원리

#### 1. Attention is All You Need (2017) ⭐⭐⭐
- **저자**: Vaswani et al., Google
- **발표**: NIPS 2017
- **ArXiv**: https://arxiv.org/abs/1706.03762
- **핵심 내용**: Transformer 아키텍처 최초 제안, Self-Attention 메커니즘
- **읽기 우선순위**: 최우선 (M1 핵심)
- **다운로드**: PDF 저장 권장

#### 2. Improving Language Understanding by Generative Pre-Training (GPT-1, 2018)
- **저자**: Radford et al., OpenAI
- **발표**: OpenAI Blog
- **링크**: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- **핵심 내용**: Transformer Decoder 기반 언어 모델, Pre-training + Fine-tuning
- **읽기 우선순위**: 필수 (M1/M2)

#### 3. BERT: Pre-training of Deep Bidirectional Transformers (2018)
- **저자**: Devlin et al., Google
- **발표**: NAACL 2019
- **ArXiv**: https://arxiv.org/abs/1810.04805
- **핵심 내용**: Bidirectional Transformer, MLM (Masked Language Modeling)
- **읽기 우선순위**: 필수 (M1/M3)

---

### M2 - GPT 시리즈의 진화

#### 4. Language Models are Unsupervised Multitask Learners (GPT-2, 2019)
- **저자**: Radford et al., OpenAI
- **링크**: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **핵심 내용**: Zero-shot Learning, 1.5B 파라미터
- **읽기 우선순위**: 필수

#### 5. Language Models are Few-Shot Learners (GPT-3, 2020)
- **저자**: Brown et al., OpenAI
- **발표**: NeurIPS 2020
- **ArXiv**: https://arxiv.org/abs/2005.14165
- **핵심 내용**: Few-shot Learning, 175B 파라미터, Scaling Laws
- **읽기 우선순위**: 최우선 (M2 핵심)

---

### M3 - Encoder-Decoder 및 양방향 모델

#### 6. Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5, 2019)
- **저자**: Raffel et al., Google
- **발표**: JMLR 2020
- **ArXiv**: https://arxiv.org/abs/1910.10683
- **핵심 내용**: Text-to-Text Framework, Encoder-Decoder 구조
- **읽기 우선순위**: 필수

#### 7. RoBERTa: A Robustly Optimized BERT Pretraining Approach (2019)
- **저자**: Liu et al., Facebook AI
- **ArXiv**: https://arxiv.org/abs/1907.11692
- **핵심 내용**: BERT 최적화 개선
- **읽기 우선순위**: 권장 (시간 있을 때)

#### 8. ALBERT: A Lite BERT for Self-supervised Learning (2019)
- **저자**: Lan et al., Google
- **ArXiv**: https://arxiv.org/abs/1909.11942
- **핵심 내용**: 파라미터 공유, 경량화
- **읽기 우선순위**: 선택

---

### M4 - 대규모 모델과 최신 기법

#### 9. Training language models to follow instructions with human feedback (InstructGPT, 2022)
- **저자**: Ouyang et al., OpenAI
- **ArXiv**: https://arxiv.org/abs/2203.02155
- **핵심 내용**: RLHF (Reinforcement Learning from Human Feedback)
- **읽기 우선순위**: 최우선 (M4 핵심)

#### 10. GPT-4 Technical Report (2023)
- **저자**: OpenAI
- **ArXiv**: https://arxiv.org/abs/2303.08774
- **핵심 내용**: Multimodal, 성능 향상
- **읽기 우선순위**: 필수

#### 11. LLaMA: Open and Efficient Foundation Language Models (2023)
- **저자**: Touvron et al., Meta AI
- **ArXiv**: https://arxiv.org/abs/2302.13971
- **핵심 내용**: 오픈소스 대규모 모델, 7B-65B
- **읽기 우선순위**: 필수

#### 12. Llama 2: Open Foundation and Fine-Tuned Chat Models (2023)
- **저자**: Touvron et al., Meta AI
- **ArXiv**: https://arxiv.org/abs/2307.09288
- **핵심 내용**: LLaMA 개선, 챗봇 최적화
- **읽기 우선순위**: 권장

---

### M5 - 최신 트렌드와 미래 방향

#### 13. Gemini: A Family of Highly Capable Multimodal Models (2023)
- **저자**: Google DeepMind
- **ArXiv**: https://arxiv.org/abs/2312.11805
- **핵심 내용**: Multimodal, Ultra/Pro/Nano 시리즈
- **읽기 우선순위**: 권장

#### 14. Claude 3 Model Card (2024)
- **저자**: Anthropic
- **링크**: https://www.anthropic.com/news/claude-3-family
- **핵심 내용**: Opus/Sonnet/Haiku, Constitutional AI
- **읽기 우선순위**: 권장 (공식 블로그)

---

## 📚 추가 읽기 (선택)

### Attention 메커니즘 이전 (역사적 맥락)

#### 15. Neural Machine Translation by Jointly Learning to Align and Translate (2014)
- **저자**: Bahdanau et al.
- **ArXiv**: https://arxiv.org/abs/1409.0473
- **핵심 내용**: Attention 메커니즘 최초 제안 (RNN 기반)
- **읽기 우선순위**: 선택 (역사 이해용)

#### 16. Sequence to Sequence Learning with Neural Networks (2014)
- **저자**: Sutskever et al., Google
- **ArXiv**: https://arxiv.org/abs/1409.3215
- **핵심 내용**: Seq2Seq 아키텍처
- **읽기 우선순위**: 선택

### 최적화 기법

#### 17. LoRA: Low-Rank Adaptation of Large Language Models (2021)
- **저자**: Hu et al., Microsoft
- **ArXiv**: https://arxiv.org/abs/2106.09685
- **핵심 내용**: 효율적 Fine-tuning
- **읽기 우선순위**: 선택 (M5)

#### 18. QLoRA: Efficient Finetuning of Quantized LLMs (2023)
- **저자**: Dettmers et al.
- **ArXiv**: https://arxiv.org/abs/2305.14314
- **핵심 내용**: Quantization + LoRA
- **읽기 우선순위**: 선택

### Mixture of Experts (MoE)

#### 19. Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer (2017)
- **저자**: Shazeer et al., Google
- **ArXiv**: https://arxiv.org/abs/1701.06538
- **핵심 내용**: MoE 기본 개념
- **읽기 우선순위**: 권장 (M4)

---

## 📥 논문 다운로드 방법

### ArXiv에서 다운로드
1. ArXiv 링크 클릭
2. 우측 "Download PDF" 클릭
3. `vl_materials/papers/` 폴더에 저장 (폴더 직접 생성)
4. 파일명 예시: `Attention_is_All_You_Need_2017.pdf`

### 명명 규칙
```
{논문명}_{연도}.pdf
예: GPT3_Language_Models_are_Few_Shot_Learners_2020.pdf
```

---

## 📖 논문 읽기 전략

### 효율적 읽기 순서
1. **Abstract**: 1-2분, 핵심 아이디어 파악
2. **Introduction**: 5분, 배경 및 동기
3. **Conclusion**: 3분, 주요 결과
4. **Figures/Tables**: 5분, 시각적 이해
5. **Method**: 30분-1시간, 상세 내용

### 메모 방법
- 각 논문마다 1-2페이지 요약 작성
- 핵심 아이디어를 한 문장으로 정리
- 이해 안 되는 부분은 블로그/유튜브 참고
- 타임라인에 추가할 내용 표시

---

## 🔗 유용한 리소스

### 논문 검색
- **ArXiv**: https://arxiv.org/ (최신 논문)
- **Papers with Code**: https://paperswithcode.com/ (코드 포함)
- **Google Scholar**: https://scholar.google.com/ (인용 정보)

### 논문 관리
- **Zotero**: 무료 논문 관리 도구
- **Notion**: 논문 요약 정리
- **Obsidian**: 연결된 노트 작성

---

**작성자**: CUA_VL Claude Skills 학습
**버전**: 1.0
**최종 업데이트**: 2026-01-10
**총 논문 수**: 19개 (필수 14개, 선택 5개)
