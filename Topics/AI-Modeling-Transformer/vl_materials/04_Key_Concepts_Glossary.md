# 핵심 용어 사전 (Glossary)

**Topic**: AI-Modeling-Transformer
**생성일**: 2026-01-10

> **사용 방법**: 논문 읽기 전이나 학습 중 모르는 용어가 나올 때 참고하세요.
> 학습하면서 새로운 용어를 추가하고, 이해한 내용으로 설명을 업데이트하세요.

---

## 🔤 핵심 용어 (알파벳순)

### A

#### Attention Mechanism
- **정의**: 입력 시퀀스의 각 요소에 대한 가중치를 학습하여 중요한 부분에 집중하는 메커니즘
- **등장**: 2014년 (Bahdanau et al.), Transformer에서 본격 활용 (2017)
- **핵심 아이디어**: "모든 것을 동등하게 보지 말고, 중요한 것에 집중하자"
- **수식**: `Attention(Q, K, V) = softmax(QK^T / √d_k)V`
- **비유**: [학습 후 작성 - 예: 책에서 중요한 부분에 형광펜 칠하기]
- **참조**: "Attention is All You Need" 논문 Section 3.2

#### Auto-regressive
- **정의**: 이전 출력을 다음 입력으로 사용하여 순차적으로 생성하는 방식
- **사용 모델**: GPT 시리즈
- **예시**: 문장 생성 시 단어를 하나씩 예측
- **장점**: [학습 후 작성]
- **단점**: [학습 후 작성]

---

### B

#### BERT (Bidirectional Encoder Representations from Transformers)
- **정의**: 양방향으로 문맥을 이해하는 Transformer Encoder 기반 모델
- **발표**: 2018년 10월, Google
- **핵심 기술**: Masked Language Modeling (MLM), Next Sentence Prediction (NSP)
- **차별점**: 왼쪽→오른쪽만 보는 GPT와 달리 양방향으로 문맥 파악
- **용도**: 분류, 질의응답, NER 등
- **비유**: [학습 후 작성]

#### Bidirectional
- **정의**: 문장의 양방향(왼쪽→오른쪽, 오른쪽→왼쪽)을 모두 고려하는 방식
- **BERT의 핵심**: Masked 단어 예측 시 앞뒤 문맥 모두 활용
- **vs Unidirectional**: GPT는 왼쪽→오른쪽만 (Unidirectional)

---

### C

#### Constitutional AI
- **정의**: [학습 후 작성]
- **제안**: Anthropic (Claude 모델)
- **핵심 아이디어**: [학습 후 작성]

#### Context Window / Context Length
- **정의**: 모델이 한 번에 처리할 수 있는 토큰 수
- **예시**: GPT-3 (4K), Claude 3 (200K), Gemini 1.5 (1M)
- **중요성**: 긴 문서를 한 번에 처리 가능 여부
- **제약**: 메모리, 계산 비용

---

### D

#### Decoder
- **정의**: Transformer의 절반, 출력 시퀀스를 생성하는 부분
- **구성**: Masked Multi-Head Attention + Encoder-Decoder Attention + FFN
- **사용 모델**: GPT 시리즈 (Decoder-only)
- **역할**: 생성 (Generation)

#### Distillation (Knowledge Distillation)
- **정의**: 큰 모델(Teacher)의 지식을 작은 모델(Student)에게 전달하는 기법
- **예시**: DistilBERT (BERT의 경량화 버전)
- **장점**: 성능은 유지하면서 모델 크기 축소
- **용도**: 모바일, 엣지 디바이스 배포

---

### E

#### Embedding
- **정의**: 단어나 토큰을 고차원 벡터로 변환한 것
- **예시**: "king"을 [0.2, -0.5, 0.8, ...] 벡터로 표현
- **목적**: 의미적 유사성을 벡터 공간에서 표현
- **Positional Embedding**: 위치 정보를 인코딩한 임베딩

#### Encoder
- **정의**: Transformer의 절반, 입력 시퀀스를 이해하는 부분
- **구성**: Multi-Head Self-Attention + FFN
- **사용 모델**: BERT (Encoder-only)
- **역할**: 이해 (Understanding)

#### Encoder-Decoder
- **정의**: Encoder와 Decoder를 모두 사용하는 아키텍처
- **사용 모델**: 원조 Transformer, T5, BART
- **용도**: 번역, 요약 등 (입력→출력 변환)

---

### F

#### Few-shot Learning
- **정의**: 몇 개의 예시만으로 새로운 작업을 수행하는 능력
- **등장**: GPT-3 (2020)
- **예시**: 번역 예시 3개를 보여주고 새 문장 번역 요청
- **vs Zero-shot**: 예시 없이도 작업 수행
- **vs Fine-tuning**: 모델 가중치를 업데이트하지 않음

#### FFN (Feed-Forward Network)
- **정의**: Transformer의 각 레이어에 포함된 완전 연결 신경망
- **구조**: Linear → ReLU → Linear
- **역할**: 비선형성 추가, 표현력 향상

#### Fine-tuning
- **정의**: Pre-trained 모델을 특정 작업에 맞게 추가 학습
- **과정**: Pre-training (범용 학습) → Fine-tuning (특화 학습)
- **예시**: BERT를 감정 분석 작업에 Fine-tuning
- **vs Few-shot**: 가중치 업데이트 O (Few-shot은 X)

---

### G

#### Generative Pre-training
- **정의**: 다음 단어를 예측하는 방식으로 Pre-training
- **제안**: GPT-1 (2018)
- **목적**: 범용 언어 이해 능력 획득
- **vs Discriminative**: 생성 vs 분류

#### GPT (Generative Pre-trained Transformer)
- **정의**: Transformer Decoder 기반 언어 생성 모델
- **시리즈**: GPT-1 (2018) → GPT-2 (2019) → GPT-3 (2020) → GPT-4 (2023)
- **핵심**: Auto-regressive 생성
- **특징**: [학습 후 작성]

---

### I

#### In-context Learning
- **정의**: 모델 가중치 업데이트 없이 프롬프트로 작업 수행
- **등장**: GPT-3
- **예시**: 프롬프트에 예시를 포함하여 새 작업 수행
- **vs Fine-tuning**: 가중치 변경 없음

---

### L

#### LLaMA (Large Language Model Meta AI)
- **정의**: Meta AI가 공개한 오픈소스 대규모 언어 모델
- **발표**: 2023년 2월
- **특징**: 오픈소스, 다양한 크기 (7B, 13B, 30B, 65B)
- **의의**: 오픈소스 LLM 활성화

#### LLM (Large Language Model)
- **정의**: 대규모 텍스트 데이터로 학습한 언어 모델
- **예시**: GPT-3, BERT, LLaMA
- **파라미터**: 보통 수십억~수천억 개
- **능력**: 텍스트 생성, 이해, 번역, 요약 등

---

### M

#### Masked Language Modeling (MLM)
- **정의**: 문장의 일부를 마스킹하고 예측하는 학습 방식
- **사용**: BERT
- **예시**: "The [MASK] is blue" → "The sky is blue"
- **장점**: 양방향 문맥 학습
- **vs Auto-regressive**: 순차적 예측 vs 임의 예측

#### MoE (Mixture of Experts)
- **정의**: 여러 전문가(Expert) 네트워크 중 일부만 활성화하는 구조
- **장점**: 파라미터는 많지만 실제 계산은 일부만
- **사용**: GPT-4 (추정), Mixtral
- **핵심**: Sparse Activation

#### Multi-Head Attention
- **정의**: 여러 개의 Attention을 병렬로 수행
- **목적**: 다양한 관점에서 문맥 파악
- **헤드 수**: Transformer 원조는 8개
- **수식**: [학습 후 작성]

#### Multimodal
- **정의**: 텍스트, 이미지, 오디오 등 여러 모달리티를 처리
- **예시**: GPT-4 (텍스트 + 이미지), Gemini
- **장점**: 더 풍부한 이해
- **도전**: 모달리티 간 정렬 (Alignment)

---

### P

#### Parameter
- **정의**: 모델 가중치의 총 개수
- **예시**: GPT-3은 175B (1,750억) 파라미터
- **의의**: 모델 크기와 성능의 지표
- **트렌드**: 점점 증가 (Scaling Laws)

#### Positional Encoding
- **정의**: 시퀀스 내 위치 정보를 인코딩
- **필요성**: Attention은 순서를 모르므로 위치 정보 추가 필요
- **방식**: Sinusoidal function 또는 Learned Embedding
- **수식**: [학습 후 작성]

#### Pre-training
- **정의**: 대규모 데이터로 범용 능력을 학습
- **목적**: 언어의 일반적 패턴 학습
- **방식**: MLM (BERT), Auto-regressive (GPT)
- **다음 단계**: Fine-tuning

#### Prompt
- **정의**: 모델에게 주는 입력 텍스트 (지시, 예시 등)
- **예시**: "Translate to Korean: Hello"
- **중요성**: LLM 시대의 핵심 인터페이스
- **Prompt Engineering**: 효과적인 프롬프트 설계 기법

---

### Q

#### Quantization
- **정의**: 모델 가중치를 낮은 비트로 표현하여 경량화
- **예시**: FP32 → INT8
- **장점**: 메모리 절약, 속도 향상
- **단점**: 약간의 성능 하락

---

### R

#### RLHF (Reinforcement Learning from Human Feedback)
- **정의**: 인간 피드백으로 모델을 강화학습
- **등장**: InstructGPT (2022)
- **과정**: 1) 모델 생성 → 2) 인간 평가 → 3) 보상 모델 학습 → 4) PPO로 Fine-tuning
- **목적**: 인간의 의도와 정렬 (Alignment)
- **효과**: 더 도움이 되고 해롭지 않은 응답

---

### S

#### Scaling Laws
- **정의**: 모델 크기, 데이터, 계산량이 증가하면 성능도 예측 가능하게 향상
- **발견**: GPT-3 논문 (2020)
- **함의**: "더 크면 더 좋다"
- **한계**: 언젠가 수렴 (Diminishing Returns)

#### Self-Attention
- **정의**: 입력 시퀀스 내 요소들 간의 관계를 스스로 학습
- **vs Attention**: RNN에서는 Encoder-Decoder 간, Transformer는 자기 자신
- **수식**: `Attention(Q, K, V)`
- **핵심**: Q(Query), K(Key), V(Value) 모두 같은 입력에서 유도

---

### T

#### T5 (Text-to-Text Transfer Transformer)
- **정의**: 모든 NLP 작업을 Text-to-Text로 통일한 모델
- **발표**: 2019년, Google
- **예시**: 번역 "translate English to German: ..." → 독일어 문장
- **아키텍처**: Encoder-Decoder
- **의의**: 통일된 프레임워크

#### Token
- **정의**: 모델이 처리하는 최소 단위 (단어, 서브워드, 문자 등)
- **예시**: "Hello, world!" → ["Hello", ",", " world", "!"]
- **Tokenization**: 텍스트를 토큰으로 분할
- **중요성**: 컨텍스트 길이는 토큰 수로 측정

#### Transformer
- **정의**: Attention 메커니즘 기반 아키텍처
- **제안**: "Attention is All You Need" (2017)
- **구성**: Encoder + Decoder
- **혁신**: RNN/CNN 없이 Attention만으로 구성
- **영향**: 현대 NLP의 기반

---

### Z

#### Zero-shot Learning
- **정의**: 예시 없이 새로운 작업을 수행하는 능력
- **등장**: GPT-2 (2019)
- **예시**: "Translate to French: Hello" (예시 없이 바로 번역)
- **vs Few-shot**: 예시 없음 vs 몇 개 예시
- **조건**: 사전 학습으로 충분한 지식 획득

---

## 📚 개념 연결 맵

```
Transformer (2017)
├── Encoder
│   └── BERT (2018)
│       ├── RoBERTa (2019)
│       ├── ALBERT (2019)
│       └── DistilBERT (2019)
├── Decoder
│   └── GPT (2018-)
│       ├── GPT-1 (2018)
│       ├── GPT-2 (2019)
│       ├── GPT-3 (2020)
│       └── GPT-4 (2023)
└── Encoder-Decoder
    ├── T5 (2019)
    └── BART (2019)

학습 기법
├── Pre-training
│   ├── MLM (BERT)
│   └── Auto-regressive (GPT)
├── Fine-tuning
├── Few-shot Learning (GPT-3)
└── RLHF (InstructGPT, 2022)
```

---

## 💡 학습 팁

### 용어 암기 전략
1. **비유로 이해**: 각 용어를 일상 비유로 설명
2. **비교로 이해**: 비슷한 용어들 비교 (예: Fine-tuning vs Few-shot)
3. **시각화**: 개념 다이어그램 그리기
4. **실습으로 체득**: 직접 사용해보기

### 헷갈리는 용어 정리
- **Pre-training vs Fine-tuning**: 범용 학습 vs 특화 학습
- **Zero-shot vs Few-shot vs Fine-tuning**: 예시 없음 vs 몇 개 vs 가중치 업데이트
- **Encoder vs Decoder**: 이해 vs 생성
- **Attention vs Self-Attention**: 외부와의 관계 vs 내부 관계

---

## 🎯 학습하면서 추가할 용어

각 모듈에서 새로운 용어를 만나면 여기에 추가하세요:

- [ ] [M1 추가 용어]
- [ ] [M2 추가 용어]
- [ ] [M3 추가 용어]
- [ ] [M4 추가 용어]
- [ ] [M5 추가 용어]

---

**작성자**: CUA_VL Claude Skills 학습
**버전**: 1.0
**최종 업데이트**: 2026-01-10
**총 용어 수**: 40+ (계속 추가 중)
