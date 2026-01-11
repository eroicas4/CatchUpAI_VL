# Critical Path to Memory Consistency - Bojana Miloradovic Parman

**원본 영상**: [https://www.youtube.com/watch?v=dXA5Ys32h7k](https://www.youtube.com/watch?v=dXA5Ys32h7k)
**작성일**: 2026-01-11
**Video ID**: dXA5Ys32h7k

---

## 요약

Cognee의 제품 담당 VP인 Bojana Miloradovic Parman이 AI 메모리의 정확성 확보를 위한 핵심 경로를 설명합니다. 단순히 LLM과의 대화 기록만으로는 프로덕션 환경에서 필요한 정확도를 달성할 수 없으며, 관계 기반 접근법, 지식 그래프, 하이퍼파라미터 최적화 등 다층적인 메모리 시스템이 필요하다고 강조합니다. Cognee는 이러한 문제를 해결하기 위한 오픈소스 AI 메모리 프레임워크를 제공하며, 현재 28,000개의 GitHub 스타와 47개 고객사에서 300,000개의 파이프라인을 운영 중입니다.

---

## 핵심 포인트

- LLM의 정확도 문제는 멀티턴 대화와 멀티 에이전트 시스템에서 복합적으로 증폭됨
- 관계 기반(Relationship-first) 접근법을 통해 작은 추론 단계들을 제어 가능하게 만들어 정확도 향상
- 단순한 청킹 문제가 아닌 온톨로지 문제로 접근해야 함
- 프로덕션 환경에서는 설계, 측정, 최적화, 배포의 전 단계에서 체계적 접근 필요
- 엔티티 추출, 하이퍼파라미터 튜닝, 그래프 완성 등 다양한 모듈의 조합 필요

---

## 주요 내용

### 섹션 1: Cognee 소개 및 배경
- 오픈소스 AI 메모리 회사로 28,000 GitHub 스타 보유
- 47개 고객사에서 300,000개 파이프라인 운영 중
- 발표자는 20년 엔지니어링 경력, 대규모 개인화 시스템에서 데이터 엔지니어링 수석으로 근무
- 프로덕션 규모의 실제 AI 시스템에서 발생하는 문제에 집중

### 섹션 2: LLM의 정확도 문제
- LLM만으로는 충분하지 않음: 생성형 AI는 강력하지만 정확도에 논란이 있음
- 에이전틱 AI에서 정확도는 더욱 중요: 에이전트 간 대화와 다중 턴 상호작용에서 오류가 복합적으로 증폭됨
- 두 가지 수준의 복합화: (1) 에이전트와 모델 간 멀티턴 대화, (2) 멀티 에이전트 시스템 내 에이전트 간 대화
- 메모리 레이어를 통해 정확도를 시스템에 재주입 가능

### 섹션 3: 관계 기반 접근법
- Cognee의 핵심 이론: 관계(Relationships) 우선 접근
- 관계는 확고하고 제어 가능한 작은 추론 단계 또는 종속성
- 충분한 관계 단계를 주입하면 필요한 정확도 수준 달성 가능
- 단순히 과거 상호작용 기록을 컨텍스트에 제공하는 것만으로는 부족
- HotpotQA, MuSiQue, LoCoMo 등 업계 벤치마크로 검증 가능

### 섹션 4: 메모리의 복잡성
- 메모리는 단순한 청킹 문제가 아닌 온톨로지 문제
- Cognee의 여러 모듈:
  - 데이터 수집 모듈
  - 엔티티 추출
  - 자가 개선 레이어
  - 에이전트를 위한 LLM 준비 컨텍스트 튜닝
- 모든 모듈을 조정 가능하게 만들어야 필요한 정확도 달성 가능

### 섹션 5: 시스템 설계 단계
- **1단계**: 스마트 프롬프트로 LLM이 초기 그래프 생성 (Instructor 라이브러리 등 활용)
- **2단계**: 청킹, 리트리버, 그래프 유사성, 개선된 프롬프트 추가
- **3단계**: 엔드투엔드 파이프라인의 하이퍼파라미터 튜닝
  - 베이지안 종속성 주입
  - 트리 구조 파서 및 추정기
  - 다양한 인코더 사용 (텍스트, 수학, 범주형/연속형 값 등)

### 섹션 6: 하이퍼파라미터 최적화
- 수집, 그래프 구축, 검색, 프롬프트를 모두 함께 튜닝해야 함
- 무차별 대입이 아닌 교육된 시행착오 추측 방식 사용
- 도메인 지식의 휴리스틱 활용: 알려진 패턴과 온톨로지를 그래프로 주입
- 검색 공간 포함 요소:
  - 청크 크기
  - 리트리버 유형 및 전략
  - 그래프 완성 여부
  - 그래프 트리플릿 추출 방식
- 지식 그래프와 LLM 간 인터페이스 최적화에 관한 백서 발표

### 섹션 7: 측정 및 평가
- **단일 상호작용 측정**:
  - 데이터셋: HotpotQA, MuSiQue, LoCoMo
  - 메트릭: Exact Match, F1, LLM Judge (BLEU 등)
- **멀티 에이전트 시스템 측정**:
  - 패턴 전이 능력 (예: 50가지 다른 로그인 방식 인식)
  - 워크플로우 간 전이
  - 루프 횟수 (에이전트가 시나리오를 반복하는 횟수)
  - 안전성 (기업 안전 방향성)
  - 문제 해결 시간
  - 인간 에스컬레이션 빈도

### 섹션 8: 거버넌스
- 프로덕션 시스템에 필요한 표준 요소:
  - 역할 관리
  - 멀티테넌트 데이터 격리
  - 감사 및 로깅
  - 개인정보 유출 방지
  - API 키 관리

### 섹션 9: 배포
- 표준 시스템 설계 고려사항:
  - 모니터링 및 관찰 가능성
  - 데이터 품질
  - 피드백 루프
  - 캐싱 및 확장성
  - 배치 및 실시간 모드
  - 클라우드 vs 엣지 배포
- 지속적 학습 지원: 새로운 상호작용으로 그래프와 관계형 데이터 업데이트

### 섹션 10: Cognee 활용 방법
- 라이브 오픈소스 프로젝트
- SaaS 제공 (로그인하여 시도 가능)
- 데스크톱용 이미지 다운로드 가능
- 다양한 그래프/벡터 스토어 및 에이전트 프레임워크와 통합:
  - LlamaIndex, LangChain, LangGraph
  - Cursor, CrewAI 등
- YouTube에 통합 가이드 비디오 제공

---

## 타임라인

- **00:00**: Hi uh my name is Vana Mileradovich Harvin uh I know very hard to pronounce uh and I'm an advising BP product at Cognney. We're an AI memory company and we are an open-source company with a lot of uh contributors and uh very active in the open source community. We have uh 8.8 28,000 GitHub stars. Um, lots of active contributors were outpacing a lot of other memory projects um in terms of the speed of contributions and activity. And we have about 300,000 pipelines running live at 47 customers. So, this is an open-source project but with a lot of adoption and some maturity. Uh today I'm uh we're going to discuss what cogni focuses on for AI memory because there are many different areas of focus but a lot of people think about memor AI memory as just a conversation between uh your program and a large language model and if my model is smart enough I just talk back and forth from my agents and everything works out perfectly. Uh well this whole summit is dedicated to well we need some memory. Okay, we we need to understand the paths of this conversation. But what my talk focus on is you need way more than that. And because of some intrinsic uh uh things that exist in large language models and in the way the past conversations are are composed, you'll need more to achieve the level of accuracy that is critical for the success of your production grade system. and um why I focus on production grade systems. So um in the past years I've been working in engineering for 20 years and one of the last companies I worked for was a large scale personalization. I was a data engineering principal engineer running on that and I noticed what what level of problems arise when you move into the real AI situation at large production scale. uh it goes way beyond um just a a few steps that are needed for demos. So with that, let's look at some of the um things that happen uh that exist at the controversy. So uh why is large language...
- **05:00**: accuracy you need or you can control the accuracy you're getting from the model. uh we uh uh we provide a solution where the um final outcome will be way more accurate than what you would need um than what you would get by just directly interacting with model. Now let's step back for a second. You say okay so if we just provide the record of past interactions in the multi-term conversation whether it's by the human or or different agents wouldn't that be enough so just put that in the context and with some smart fate turns out it's not enough if you run any of the industry established benchmarks to check on accuracy say hot pot or musicique or locomo you'll see that that's not enough and so uh finally will um also suggest that um in addition to reach the top level accuracy uh there is some collaboration needed with from the application teams where you can inject relationships into the graphs and uh from there get the level of accuracy needed. So uh if you look at it in in its entirety uh memory is not a chunking uh problem only. It's an ontology problem as well. And so Cognney has a couple of different modules that help it deal uh with this um reality of uh systems in production. We've got data ingestion modules. Um entity extraction which is probably closest to what you do when you try to talk just to LLM to get the uh extraction of everything. Then we have some self-improvement layers which I'll discuss uh next. Uh and uh some um other ongoing uh tuning that makes LLM uh ready context for for agents. And um only after you have all of these different modules in place and you make them tunable is when you can get to the level of accuracy that is needed. And so uh basically uh when people start how do we design so let's talk about how we design these systems how we measure them uh how we optimize them how we deploy...
- **10:00**: dependencies or relationships that you already know existed. So you don't have to depend just on the model to to inherit this patterns. If you know of some patterns, you also give it to the model. And all of these things are needed to make things work in production. So search space again uh is going to be your chunking size, your retrieval retriever type uh strategy used to retrieve content. Are you going to retrieve chunk level summary or are you going to uh retrieve original chunk based on embedding similarity? Then are you going to use graph completion? Are you going to push the model to extract graph triplet and then give it the subg graph and see or are these two subg graphs looking alike or not? These are all the things that need to be done during the phase of hyperparameter tuning. And so uh we've done all of this and published a white paper on how to optimize this interface between knowledge graphs and LLMs and uh I encourage you to take a look and um see what happens with accuracy and how uh what were all the hyperparameters that we need. So that was the first step that helped productionize uh these systems. uh there are subsequent steps but well let's look at how we need to measure end to end system to see if we're there yet. So uh data sets that we used were hotpot two week multihop music you know locomo those are all good to try. The metrics used were exact match f1 and dpl b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b basically an LLM judge to to judge whether the the responses were good and we're using a certain number of trials per run. So that's one way to measure the singular interaction, but you're building a multi- aent system. So now there's a whole bunch of measures that need to apply to how these uh agents interact. So uh how you want to measure...
- **15:00**: deploying it on cloud am I deploying it on the edge system all of these matters uh when when you're going live in production and finally this um system memory system needs to be able to support the ongoing learning over time keep the graphs in relational data updated with new interaction to optimize the end to end agentic system. And so that's all it takes to put this into production. Once you have it, you're you're good to go. It's working. It's working well. It it it fulfills it promises. And so, uh, that's what we're all about. And Cognney um live open-source project. Give it a try. We have SAS offering. You can, uh, go log in and, uh, and try it. You can download an image and play at home and your desktop. And uh we also integrate with um all kinds of uh graph or vector stores and the agentic frameworks uh lamb index lang chain um the langraph etc cursor crew AI um that we have YouTube videos showing you how to integrate with those. And that's it. Um do you have any questions?...

---

## 전체 자막 (타임스탬프 포함)

**[00:02]** Hi uh my name is Vana Mileradovich

**[00:05]** Harvin uh I know very hard to pronounce

**[00:09]** uh and I'm an advising BP product at

**[00:11]** Cognney. We're an AI memory company and

**[00:14]** we are an open-source company with a lot

**[00:17]** of uh contributors and uh very active in

**[00:21]** the open source community. We have uh

**[00:24]** 8.8 28,000 GitHub stars. Um, lots of

**[00:28]** active contributors were outpacing a lot

**[00:31]** of other memory projects um in terms of

**[00:33]** the speed of contributions and activity.

**[00:36]** And we have about 300,000 pipelines

**[00:39]** running live at 47 customers. So, this

**[00:42]** is an open-source project but with a lot

**[00:45]** of adoption and some maturity. Uh today

**[00:48]** I'm uh we're going to discuss what cogni

**[00:51]** focuses on for AI memory because there

**[00:54]** are many different areas of focus but a

**[00:56]** lot of people think about memor AI

**[00:59]** memory as just a conversation between uh

**[01:02]** your program and a large language model

**[01:04]** and if my model is smart enough I just

**[01:07]** talk back and forth from my agents and

**[01:08]** everything works out perfectly. Uh well

**[01:11]** this whole summit is dedicated to well

**[01:14]** we need some memory. Okay, we we need to

**[01:16]** understand the paths of this

**[01:17]** conversation. But what my talk focus on

**[01:20]** is you need way more than that. And

**[01:23]** because of some intrinsic uh uh things

**[01:26]** that exist in large language models and

**[01:29]** in the way the past conversations are

**[01:31]** are composed, you'll need more to

**[01:34]** achieve the level of accuracy that is

**[01:37]** critical for the success of your

**[01:39]** production grade system. and um why I

**[01:43]** focus on production grade systems. So um

**[01:45]** in the past years I've been working in

**[01:47]** engineering for 20 years and one of the

**[01:50]** last companies I worked for was a large

**[01:52]** scale personalization. I was a data

**[01:54]** engineering principal engineer running

**[01:56]** on that and I noticed what what level of

**[01:59]** problems arise when you move into the

**[02:02]** real AI situation at large production

**[02:05]** scale. uh it goes way beyond um just a a

**[02:09]** few steps that are needed for demos. So

**[02:11]** with that, let's look at some of the um

**[02:15]** things that happen uh that exist at the

**[02:18]** controversy. So uh why is large language

**[02:21]** model not enough? There's an accuracy

**[02:23]** controversy around AI. So generative AI,

**[02:26]** we love it. Uh we embrace it. It's

**[02:29]** phenomenal. It's smart. However, there's

**[02:31]** a a controversy. every time something

**[02:33]** new appears or predictability it it'll

**[02:37]** catch its attention and that's it um

**[02:39]** string and uh they say attention is all

**[02:42]** you need to focus on the right um part

**[02:46]** of that that's when you're talking just

**[02:48]** to the model however smart it is however

**[02:51]** accuracy controversy uh you may get

**[02:54]** something you're not expecting from that

**[02:57]** and so this controversy around accuracy

**[03:01]** with large language model is the key

**[03:04]** reason why uh a different memory

**[03:07]** structure and what we can inject into

**[03:09]** memory is incredibly helpful into

**[03:13]** getting accuracy

**[03:15]** at the level that agencies. So let's

**[03:18]** look at the agentic AI. So unlike a

**[03:22]** one-on-one conversation where just one

**[03:24]** person is interacting with a large

**[03:25]** language model, as you're putting your

**[03:28]** agents into production at scale, this

**[03:31]** accuracy becomes even more important.

**[03:33]** Why? Because it compounds over the

**[03:37]** conversation turns and interactions

**[03:39]** among agents. So you have two different

**[03:42]** levels of compounding. one as the

**[03:45]** conversations progress in the multi-turn

**[03:47]** way between agents and the the model and

**[03:50]** the second as the conversation

**[03:51]** progresses among the agents themselves

**[03:54]** in the multioagogenic system. So as this

**[03:56]** error compounds the the the result is

**[04:00]** further and further away from where it

**[04:01]** needs to be and accuracy becomes

**[04:04]** actually on the critical path for this.

**[04:07]** And so our thesis and cogni is that we

**[04:11]** through AI memory we can inject that

**[04:14]** accuracy back into the system and LLM uh

**[04:18]** being as they are as that guy on the mic

**[04:22]** are behaving exactly how they should be

**[04:24]** behaving. But we can look at the memory

**[04:27]** layer to give it what it needs to become

**[04:30]** production grade. And so um our theory

**[04:34]** is that it's all driven by

**[04:36]** relationships. Relationship first

**[04:38]** approach. What are relationships? There

**[04:41]** are little snippets of um dependencies

**[04:45]** or reasoning. little little steps of

**[04:48]** reasoning that are uh firm and

**[04:51]** controllable and that provide accuracy.

**[04:55]** And on the theory that when you inject

**[04:57]** enough of these steps, you can reach the

**[05:00]** accuracy you need or you can control the

**[05:03]** accuracy you're getting from the model.

**[05:05]** uh we uh uh we provide a solution where

**[05:10]** the um final outcome will be way more

**[05:14]** accurate than what you would need um

**[05:17]** than what you would get by just directly

**[05:19]** interacting with model. Now let's step

**[05:22]** back for a second. You say okay so if we

**[05:26]** just provide the record of past

**[05:28]** interactions in the multi-term

**[05:30]** conversation whether it's by the human

**[05:32]** or or different agents wouldn't that be

**[05:35]** enough so just put that in the context

**[05:38]** and with some smart fate turns out it's

**[05:40]** not enough if you run any of the

**[05:43]** industry established benchmarks to check

**[05:45]** on accuracy say hot pot or musicique or

**[05:48]** locomo you'll see that that's not enough

**[05:51]** and so uh finally

**[05:54]** will um also suggest that um in addition

**[05:58]** to reach the top level accuracy uh there

**[06:01]** is some collaboration needed with from

**[06:04]** the application teams where you can

**[06:06]** inject relationships into the graphs and

**[06:10]** uh from there get the level of accuracy

**[06:12]** needed.

**[06:14]** So uh if you look at it in in its

**[06:17]** entirety uh memory is not a chunking uh

**[06:22]** problem only. It's an ontology problem

**[06:24]** as well.

**[06:27]** And so Cognney has a couple of different

**[06:29]** modules that help it deal uh with this

**[06:32]** um reality of uh systems in production.

**[06:35]** We've got data ingestion modules. Um

**[06:38]** entity extraction which is probably

**[06:40]** closest to what you do when you try to

**[06:42]** talk just to LLM to get the uh

**[06:45]** extraction of everything. Then we have

**[06:48]** some self-improvement layers which I'll

**[06:50]** discuss uh next. Uh and uh some um other

**[06:55]** ongoing uh tuning that makes LLM uh

**[06:59]** ready context for for agents. And um

**[07:02]** only after you have all of these

**[07:04]** different modules in place and you make

**[07:06]** them tunable is when you can get to the

**[07:09]** level of accuracy that is needed. And so

**[07:13]** uh basically uh when people start how do

**[07:16]** we design so let's talk about how we

**[07:18]** design these systems how we measure them

**[07:21]** uh how we optimize them how we deploy

**[07:23]** them in production. So when designing

**[07:27]** the first impulse uh people have is to

**[07:29]** put in some smart prompts into LLM and

**[07:33]** have LLM generate the the original graph

**[07:36]** which is fine. That's a good uh first

**[07:38]** start and there are whole libraries that

**[07:40]** exist for this. For example, instructor

**[07:43]** uh library by a popular um uh person

**[07:46]** called Jason Leu does that does it very

**[07:49]** well. But that's your first step. Uh

**[07:52]** second step, okay, people realize, well,

**[07:55]** we need to put in some chunking and

**[07:57]** retrievers. We need to do the similarity

**[07:59]** on graphs. We need to put in some better

**[08:01]** prompts to reinforce the the the LLM to

**[08:05]** extract some of the missing links and

**[08:07]** missing nodes. So you try that, you tune

**[08:10]** your prompts, you provide some

**[08:12]** templates, you keep pushing that model.

**[08:14]** Is that enough? Again, no. If you go to

**[08:17]** production, you'll see this is not

**[08:19]** enough. Um then the next step people

**[08:22]** realize oh we need to actually two these

**[08:26]** hyperparameters across the end to end

**[08:28]** pipeline. So what do we do? We um inject

**[08:33]** some uh Beijian uh dependency inside. We

**[08:36]** use tree structured pars and estimators.

**[08:39]** We use the encoders different encoders.

**[08:41]** So for example the text encoders the

**[08:44]** text model scorable in math we need to

**[08:46]** compute a little bit of something. So we

**[08:48]** a different encoder, different model uh

**[08:51]** that to deal with categorical and

**[08:53]** continual values and so on and so forth.

**[08:56]** Um the the things um get complicated if

**[09:00]** you're trying to increase accuracy and

**[09:03]** again by trying the benchmark you will

**[09:05]** notice how these things start popping up

**[09:08]** one by one.

**[09:10]** So that's all you'll need to be able to

**[09:13]** design it.

**[09:15]** Um so once it's designed uh you need to

**[09:19]** go through an automated hyperar

**[09:22]** parameter optimization process and again

**[09:25]** uh it is the ingestion graph building

**[09:28]** retrieval and the prompts all together

**[09:31]** that need to be tuned in this process.

**[09:34]** Then um you cannot just go brute force

**[09:36]** through it. You have to get smarter than

**[09:38]** that. um uh because just searching

**[09:41]** through all the combination of these

**[09:43]** parameters you'll never finish in real

**[09:45]** time. So what you do is educated trial

**[09:48]** and error guessing and one of the things

**[09:50]** you do you use every possible huristic

**[09:53]** that is known to you about your domain

**[09:55]** space and inject some ontologies in

**[09:59]** other words in gel some graphs or some

**[10:01]** dependencies or relationships that you

**[10:03]** already know existed. So you don't have

**[10:06]** to depend just on the model to to

**[10:09]** inherit this patterns. If you know of

**[10:11]** some patterns, you also give it to the

**[10:13]** model. And all of these things are

**[10:15]** needed to make things work in

**[10:17]** production.

**[10:19]** So search space again uh is going to be

**[10:22]** your chunking size, your retrieval

**[10:25]** retriever type uh strategy used to

**[10:27]** retrieve content. Are you going to

**[10:29]** retrieve chunk level summary or are you

**[10:32]** going to uh retrieve original chunk

**[10:34]** based on embedding similarity? Then are

**[10:37]** you going to use graph completion? Are

**[10:40]** you going to push the model to extract

**[10:42]** graph triplet and then give it the subg

**[10:44]** graph and see or are these two subg

**[10:46]** graphs looking alike or not? These are

**[10:49]** all the things that need to be done

**[10:50]** during the phase of hyperparameter

**[10:53]** tuning.

**[10:55]** And so uh we've done all of this and

**[10:57]** published a white paper on how to

**[11:00]** optimize this interface between

**[11:01]** knowledge graphs and LLMs and uh I

**[11:04]** encourage you to take a look and um see

**[11:07]** what happens with accuracy and how uh

**[11:10]** what were all the hyperparameters that

**[11:12]** we need. So that was the first step that

**[11:14]** helped productionize uh these systems.

**[11:19]** uh there are subsequent steps but well

**[11:21]** let's look at how we need to measure end

**[11:23]** to end system to see if we're there yet.

**[11:27]** So uh data sets that we used were hotpot

**[11:31]** two week multihop music you know locomo

**[11:34]** those are all good to try. The metrics

**[11:37]** used were exact match f1 and dpl b b b b

**[11:41]** b b b b b b b b b b b b b b b b b b b b

**[11:41]** b b b b b b b b b b b b b b b basically

**[11:42]** an LLM judge to to judge whether the the

**[11:45]** responses were good and we're using a

**[11:47]** certain number of trials per run. So

**[11:49]** that's one way to measure the singular

**[11:52]** interaction, but you're building a

**[11:54]** multi- aent system. So now there's a

**[11:58]** whole bunch of measures that need to

**[12:00]** apply to how these uh agents interact.

**[12:04]** So uh how you want to measure

**[12:07]** effectiveness of that system. So you

**[12:09]** want to wanted to uh get to um capture

**[12:12]** the transfer of patterns.

**[12:15]** For example, if you have a pattern

**[12:17]** around logging in, but people are

**[12:20]** authenticated and logging in in 50

**[12:22]** different ways, you want your multioic

**[12:25]** system to be able to catch on to those

**[12:26]** patterns and recognize um then uh you

**[12:31]** want it to be able to transfer between

**[12:33]** workflows. So that's the first one that

**[12:35]** is totally different than what you see

**[12:37]** in the benchmark, but it's going to hit

**[12:38]** you first when you deploy your

**[12:40]** multioenic system. Then you're going to

**[12:44]** measure the number of loops that these

**[12:46]** agents go through. So what they'll do is

**[12:48]** they'll try different things and that

**[12:50]** orchestrator agents are going to start

**[12:53]** looping through different scenarios. You

**[12:55]** want to see whether it's uh doing too

**[12:58]** many loops or what is it doing? Then

**[13:01]** you're going to look at safety. Okay,

**[13:03]** are they all going into some direction

**[13:05]** that is unsafe for the enterprise?

**[13:08]** And so you're thinking, okay, we've got

**[13:10]** the workflow patterns, loom safety, it

**[13:13]** can pattern match. This is great.

**[13:17]** But then what comes is time to

**[13:20]** resolution. Okay, how did my

**[13:23]** multioetenic system resolve the actual

**[13:26]** issues?

**[13:27]** Then how many times did you have to

**[13:29]** escalate to human? That's another

**[13:32]** measure that you're going to u have to

**[13:34]** resolve during um these trial runs. And

**[13:37]** so when all of this is taken in

**[13:40]** consideration, those are the

**[13:41]** comprehensive measures you need to have

**[13:44]** to to put these systems in production.

**[13:48]** Now there is hope. All of this is

**[13:50]** solvable and uh advanced AI techniques

**[13:54]** some of the tuning plus some of the good

**[13:56]** old software engineering can solve all

**[13:59]** these problems. And uh what we are

**[14:02]** trying to offer at Cognney is a

**[14:04]** framework so that a combin that software

**[14:07]** engineers with a little bit of advanced

**[14:08]** AI can solve all of these problems and

**[14:11]** reliably put into production highly

**[14:14]** accurate systems.

**[14:16]** Okay, moving on. Governing these

**[14:19]** systems. What does it take? This is very

**[14:21]** familiar to anybody who's put any system

**[14:23]** in production. You're going to need to

**[14:25]** have some roles. You're going to need to

**[14:27]** have multi-tenant data set isolation,

**[14:30]** auditing, logging, no not leaking of

**[14:32]** privacy information, API key management,

**[14:36]** etc. You know it all. Then deploying it

**[14:40]** again uh the the um usual illities um uh

**[14:45]** is it uh monitoring is it observable?

**[14:49]** What's the data quality? What are the

**[14:50]** feedback loops? Then also the systems

**[14:53]** design uh issues like oh is it caching

**[14:56]** well uh is it scaling well do I have it

**[14:59]** in batch and real time mode um then am I

**[15:03]** deploying it on cloud am I deploying it

**[15:05]** on the edge system all of these matters

**[15:08]** uh when when you're going live in

**[15:09]** production

**[15:12]** and finally this um system memory system

**[15:15]** needs to be able to support the ongoing

**[15:18]** learning over time keep the graphs in

**[15:21]** relational data updated with new

**[15:23]** interaction to optimize the end to end

**[15:26]** agentic system.

**[15:29]** And so that's all it takes to put this

**[15:31]** into production. Once you have it,

**[15:33]** you're you're good to go. It's working.

**[15:35]** It's working well. It it it fulfills it

**[15:38]** promises. And so, uh, that's what we're

**[15:40]** all about. And Cognney um live

**[15:43]** open-source project. Give it a try. We

**[15:46]** have SAS offering. You can, uh, go log

**[15:49]** in and, uh, and try it. You can download

**[15:51]** an image and play at home and your

**[15:54]** desktop. And uh we also integrate with

**[15:58]** um all kinds of uh graph or vector

**[16:00]** stores and the agentic frameworks uh

**[16:04]** lamb index lang chain um the langraph

**[16:08]** etc cursor crew AI um that we have

**[16:12]** YouTube videos showing you how to

**[16:14]** integrate with those. And that's it. Um

**[16:18]** do you have any questions?


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
