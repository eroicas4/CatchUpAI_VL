# Memory Aware Agents at the Edge - Tina Tsou

**원본 영상**: [https://www.youtube.com/watch?v=nbaxzt237r0](https://www.youtube.com/watch?v=nbaxzt237r0)
**작성일**: 2026-01-11
**Video ID**: nbaxzt237r0

---

## 요약

LF Edge의 Inquin Edge AI 의장 Tina Tsou가 AI 에이전트를 위한 확장 가능한 메모리 아키텍처에 대해 발표했습니다. 상태를 유지하지 않는 LLM의 한계를 극복하기 위해 단기 및 장기 메모리 계층을 통합한 메모리 아키텍처를 제안하며, 벡터 데이터베이스를 활용한 메모리 저장 및 검색 방법을 설명합니다. Inquin Edge AI 커뮤니티의 8개 워크스트림과 실제 응용 사례를 소개하며, AI 메모리가 개인화되고 적응적인 에이전트 구축에 필수적임을 강조했습니다.

---

## 핵심 포인트

- AI 에이전트는 과거 경험을 저장하고 회상하기 위한 메모리가 필수적이며, 상태를 유지하지 않는 LLM만으로는 불충분함
- 단기 메모리(작업 공간)와 장기 메모리(지식 저장)의 계층적 아키텍처가 필요함
- 벡터 데이터베이스(FAISS, Pinecone 등)를 활용한 임베딩 인덱싱 및 검색 방법
- LangChain, LlamaIndex 등의 프레임워크가 메모리 통합을 단순화함
- 저장 비용, 검색 효율성, 사용자 프라이버시 보호가 주요 과제임

---

## 주요 내용

### 섹션 1: AI 에이전트에서 메모리의 필요성
- 단순 반사 에이전트나 상태를 유지하지 않는 시스템은 각 입력을 새것으로 취급하여 반복적이고 비개인적인 상호작용을 제공함
- 메모리가 있는 에이전트는 경험을 저장하고, 시간에 따른 패턴을 인식하며, 그에 따라 적응할 수 있음
- 단기 메모리는 진행 중인 작업을 위한 작업 공간을 제공하고, 장기 메모리는 미래 작업을 위한 지식을 통합함

### 섹션 2: 메모리 타입과 계층
- **단기 메모리**: 몇 초에서 몇 분간 정보를 유지하며, 제한된 용량으로 즉각적인 작업 공간 역할을 함
- **장기 메모리**: 지식과 경험을 장기간 저장하여 패턴 인식과 적응을 가능하게 함
- 의미론적(semantic), 일화적(episodic), 절차적(procedural) 장기 메모리 유형이 엔티틱 AI 시스템에서 사용됨

### 섹션 3: 메모리 아키텍처 및 구현
- **캐싱 전략**: 단기 메모리 관리를 위한 방법
- **벡터 데이터베이스**: FAISS, Pinecone 등을 사용한 임베딩 인덱싱 및 검색
- **프레임워크**: LangChain, LlamaIndex가 메모리 통합을 단순화하고 검색 증강 생성(RAG)을 위한 모듈형 컴포넌트 제공
- 3계층 아키텍처: 상단(장기 저장소), 중간(작업 버퍼), 하단(환경과의 상호작용)

### 섹션 4: 실제 응용 사례
- 챗봇, 개인 비서, 도메인 특화 에이전트에 메모리 통합
- 교육, 금융, 고객 지원 분야에서 연속성과 개인화 제공
- API 및 검색 파이프라인을 통한 LLM 기반 에이전트와 메모리 모델 연결

### 섹션 5: 과제 및 모범 사례
- **과제**: 저장 비용 관리, 검색 효율성 확보, 사용자 프라이버시 보호
- **모범 사례**: 정보 필터링 및 우선순위 지정, 보존 정책 설정, 투명성 제어 구현
- Model Context Protocol(MCP) 등 진화하는 표준 및 보안 고려사항

### 섹션 6: Inquin Edge AI 커뮤니티 소개
- 20개 이상의 기업 및 대학이 참여하는 오픈소스 커뮤니티
- **8개 워크스트림**: 
  1. 분산 클라우드 (엣지 앱 지원)
  2. EDA (Edge Data Agent - 박물관 등 실시간 데이터 제공)
  3. Spear (Kubernetes 기반 런타임)
  4. Edge Lake (캔자스시 유틸리티 배포)
  5. Edge Gateway (IoT 프로토콜 지원)
  6. Physical AI (에이전트 플랫폼, 자동차용 생성 AI, 로보틱스)
  7. AI Security (지리적 펜싱)
  8. AI Ops (Red Hat 기여)
- 2개월마다 릴리스, 매주 화요일 온라인 미팅 진행
- UC Santa Cruz, Stanford, UC Berkeley 등 대학 및 Google, Meta, Nvidia 등 기업과 협력

### 섹션 7: 실제 사용 사례 예시
- 라이브 스트리밍 크리에이터를 위한 AI 에이전트
- 음성 명령으로 카메라 제어, 댓글 요약 및 분석
- 시청자 관심사 파악 및 비즈니스 우선순위 설정
- 각 사용자(엔지니어, 영업사원 등)에게 맞춤화된 답변 제공

---

## 타임라인

- **00:00**: You're gonna want to talk in this. >> Yeah, I'm short. Sorry. >> You want to hold it? >> Oh, yeah. Hi. Good afternoon, everybody. I'm Tina Joe, chair of Inquin Edge AI at the LF Edge. So, uh today I'm so excited to take you on the uh AI memory 360 tour focusing on scalable memory architectures uh for Asian builders. Sorry, I ran from office. Um yeah, because we're building things. Yeah. Uh we uh will ex explore um the um sorry we'll explore why memory is essential for the AI agents enabling them to uh store and recall past experience uh to improve decision making and uh perception and uh discuss how to uh implement the memory layers and vector storebased architectures. So by the end you will understand the current status the the current state of the AI memory and be ready to build agents that are fully remembered. So um here's the road map for our talk. Uh we'll start with the motivation for memory and AI agents and why stateless LMS are insufficient. Then we'll unpack the memory types and layers differentiating short memory, shorten uh and long-term memory and explore the memory architectures that support them. We'll discuss memory curing and retrieval through the vector. Um um sorry uh can anybody give me some water? Yeah. So, so we'll discuss the memory querying and retrieval through the vector stores and evaluate the algorithms and with sample magics. Oh, thank you so much. It's very sweet of you. We should run in the lunch panel in California. Okay. Finally, we'll conclude with key takeaways and open the floor for questions. All right. So the modern AI agents need the ability to remember uh context and past the uh interactions. Unlike the simple reflex agents or state...
- **05:00**: face and pine con to index and retrieve the embeddings. We'll also touch on frameworks like lamb chain and uh llama index that simplify the memory integration uh and provide the modular components for retrieval augmented generation. Next we explore how memory is integrated into real world agent applications. We'll walk through example integrations with chatbots, personal assistants, and domain specific agents. We'll highlight use cases in education, finance, and customer support where memory enables continuity and personalization. We'll also discuss best practices for connecting memory models to LM based agent through APIs and retrieval pipelines. Building memory into AI agent asent will discuss the challenges such as managing storage costs, ensuring retrieval efficiency and protecting user privacy. will share best practices for filtering and prioritizing information, setting retention policies, and implementing transparency controls so users can view and edit their stored data. We'll also discuss evolving standards like the model context protocol MCP and the security consideration for memory systems. This diagram summarize the layered memory architecture we are proposing. At the top we have long-term persistent storage implemented via the vector stores or knowledge basis. In the middle a working buffer caches uh resent interactions and indexes them for quick uh retrieval. At the bottom, the agent interacts with the environment and updates its memory layers accordingly. Use this diagram to guide your understanding of how different memory layers interact and support scalable agent behavior. In conclusion, AI agents need robust memory architectures to deliver personalized adaptive experiences by combining...
- **10:00**: provide the enident AI and the agent Asian platform it's a similar to autogen but it's a um developer from our community and workstream 4 is the edge lake so edge lake we have already have this open source deploy in the city of Kansas state and uh the whole city's uh utility is uh using our open source component um workstream five yeah I'm just retrieving in my long-term memory now workstream five is the edge gateway use open source called shifu and also use the uh um the edge gateway they they support a lot of uh like uh the IoT protocols which uh one of the use case is in Malaysia they can clean uh under the ocean for the yellow submarine. Oh, it doesn't have to be yellow. I'm just making it up. But the use case is real. And workstream six I'm not finishing. And workstream six is um oh you got me. What's Oh, it's a physical AI. The most popular thing and physical AI there are three sub sub uh subwork streams. Number one is the AI agent uh agent. It's based on the our agent platform. Uh our team is located in UK. So they cannot join this time and uh but it provides really good uh agent uh in integrated MCP and A2A. Uh the sub worksh uh um enentic no it's the generative AI for automotive yeah I know AMDIA have the similar thing uh but we are open sourcing it and uh third uh subwork stream is core um uh robotics so uh company like Fujitu uh signal logic they have those small language model robotics And the use case has been the ayurumba at your house and also the uh the robotics audience in the Tokyo summer Olympia and also those um the robotic arms serving in the Tokyo University in the campaign. Okay, this is about work stream. I only have two workstream uh lefts, don't worry. Workstream 7 is about AI security and it also leverage the AI memory and case is created something called uh uh ages edge AI which provide the gorgeous geo fencing...
- **15:00**: learned is that it's very important about the technical direction because in the beginning we do look at the what's available uh in the is existing open-source uh uh software we can take and uh if we couldn't we just uh reuse if we could if we cannot find it we just uh leverage it and another point is that we work very close with the uh PyTorch uh community and also the CNCF community. Uh there's something called Kubby Edge. I I personally work with I'm also the TSA member of Kubge TSA member for the open platform uh enterprise AI. So like our work stream is runtime working together with Opia from F AI data. Uh I think that one uh Opia leverage a lot of AI memory and we just run top of it build around time and on top of it we run the live streaming as the flagship use case. It's one of the uh simple example I can give is more like a okay uh doing think about you are a creator you run the live streaming right and then you want to just call your agent say uh you can give a name hey little Kevin uh can you turn on the camera or turn off the camera or summarize what people comment post their public comments there just in seconds it comes to you is analysis you know okay who's actually interested in the product I'm showcasing and like you wanted to get from the memory like uh what I wanted to see I want to see more like tables I wanted to see more storytelling and who's more important and exact to my business point I can follow up with a 90-day pilot etc I think in this case we really uh expect the AI memory to give us the uh right things. Each person or or each engineer or the salesperson they want different answers. That's where the the merit of AI memory is. And uh infinite edge AI is trying to build the uh full stack uh from button to up all the way to application and uh running with AI memory uh to make it happen. Yeah. Any other questions that become my talk...

---

## 전체 자막 (타임스탬프 포함)

**[00:01]** You're gonna want to talk in this.

**[00:02]** >> Yeah, I'm short. Sorry.

**[00:04]** >> You want to hold it?

**[00:05]** >> Oh, yeah. Hi. Good afternoon, everybody.

**[00:08]** I'm Tina Joe, chair of Inquin Edge AI at

**[00:12]** the LF Edge. So, uh today I'm so excited

**[00:16]** to take you on the uh AI memory 360 tour

**[00:21]** focusing on scalable memory

**[00:24]** architectures uh for Asian builders.

**[00:27]** Sorry, I ran from office.

**[00:33]** Um yeah, because we're building things.

**[00:35]** Yeah. Uh we uh will ex explore um the um

**[00:43]** sorry we'll explore why memory is

**[00:46]** essential for the AI agents enabling

**[00:49]** them to uh store and recall past

**[00:53]** experience uh to improve decision making

**[00:56]** and uh perception and uh discuss how to

**[01:00]** uh implement the memory layers and

**[01:03]** vector storebased architectures.

**[01:06]** So by the end you will understand the

**[01:09]** current status the the current state of

**[01:12]** the AI memory and be ready to build

**[01:14]** agents that are fully remembered.

**[01:19]** So um here's the road map for our talk.

**[01:23]** Uh we'll start with the motivation for

**[01:25]** memory and AI agents and why stateless

**[01:29]** LMS are insufficient.

**[01:32]** Then we'll unpack the memory types and

**[01:34]** layers differentiating short memory,

**[01:38]** shorten uh and long-term memory and

**[01:41]** explore the memory architectures that

**[01:44]** support them. We'll discuss memory

**[01:47]** curing and retrieval through the vector.

**[01:50]** Um um sorry uh can anybody give me some

**[01:54]** water?

**[01:59]** Yeah.

**[02:00]** So, so we'll discuss the memory querying

**[02:03]** and retrieval through the vector stores

**[02:05]** and evaluate the algorithms and with

**[02:08]** sample magics. Oh, thank you so much.

**[02:11]** It's very sweet of you.

**[02:14]** We should run in the lunch panel in

**[02:16]** California.

**[02:18]** Okay. Finally, we'll conclude with key

**[02:21]** takeaways and open the floor for

**[02:23]** questions.

**[02:27]** All right. So the modern AI agents need

**[02:31]** the ability to remember uh context and

**[02:35]** past the uh interactions.

**[02:37]** Unlike the simple reflex agents or state

**[02:41]** lists that cheat each input as new

**[02:46]** agents with memory can store and record

**[02:49]** experiences,

**[02:50]** recognize patterns over time and adapt

**[02:53]** accordingly.

**[02:55]** Short-term memory provides a a working

**[02:59]** space for ongoing tasks while long-term

**[03:03]** memory consolidates knowledge for future

**[03:06]** tasks. Without memory, interactions feel

**[03:10]** uh repetitive and impersonal.

**[03:14]** We we will motivate the need of uh for

**[03:17]** those uh dynamic memory and set the

**[03:20]** stage for the rest of this talk.

**[03:25]** AI agents rely on multiple memory

**[03:28]** layers. Shorter memory retains

**[03:31]** information for brief periods,

**[03:35]** typically seconds to minutes, acting as

**[03:38]** an immediate workspace with limited

**[03:41]** capacity. It allows agents to process

**[03:45]** ongoing interactions and maintain the

**[03:48]** contacts for a chatbot or tasks.

**[03:52]** However, the long-term memory stores

**[03:55]** knowledge and experiences over longer

**[03:59]** durations, enabling pattern recognition

**[04:02]** and adaption.

**[04:04]** We explore how these memory types work

**[04:08]** together and introduce sematic

**[04:11]** uh episodic and procedural long-term

**[04:15]** memory stores used in the enantic AI

**[04:19]** systems.

**[04:22]** AI agent uh rely on

**[04:26]** the I

**[04:28]** sorry

**[04:33]** a mess here.

**[04:38]** >> So let's look at the uh practical

**[04:40]** patterns and tools for building the

**[04:43]** memory into your agents. We'll discuss

**[04:46]** uh caching strategies to manage

**[04:50]** short-term memory persistent storage

**[04:53]** options for long-term memory. Hi my

**[04:56]** friend

**[04:58]** and how to use vector databases like uh

**[05:01]** face and pine con to index and retrieve

**[05:05]** the embeddings. We'll also touch on

**[05:08]** frameworks like lamb chain and uh llama

**[05:11]** index that simplify the memory

**[05:14]** integration

**[05:16]** uh and provide the modular components

**[05:18]** for retrieval augmented generation.

**[05:23]** Next we explore how memory is integrated

**[05:28]** into real world agent applications.

**[05:31]** We'll walk through example integrations

**[05:35]** with chatbots, personal assistants, and

**[05:38]** domain specific agents. We'll highlight

**[05:41]** use cases in education, finance, and

**[05:45]** customer support where memory enables

**[05:48]** continuity and personalization.

**[05:52]** We'll also discuss best practices for

**[05:55]** connecting memory models to LM based

**[05:58]** agent through APIs and retrieval

**[06:01]** pipelines.

**[06:05]** Building memory into AI agent asent will

**[06:09]** discuss the challenges such as managing

**[06:12]** storage costs, ensuring retrieval

**[06:16]** efficiency and protecting user privacy.

**[06:20]** will share best practices for filtering

**[06:23]** and prioritizing information, setting

**[06:26]** retention policies, and implementing

**[06:29]** transparency controls so users can view

**[06:33]** and edit their stored data. We'll also

**[06:37]** discuss evolving standards like the

**[06:40]** model context protocol MCP and the

**[06:44]** security consideration for memory

**[06:46]** systems.

**[06:49]** This diagram summarize the layered

**[06:51]** memory architecture we are proposing. At

**[06:55]** the top we have long-term persistent

**[06:58]** storage implemented via the vector

**[07:01]** stores or knowledge basis. In the middle

**[07:05]** a working buffer caches uh resent

**[07:09]** interactions and indexes them for quick

**[07:12]** uh retrieval. At the bottom, the agent

**[07:16]** interacts with the environment and

**[07:19]** updates its memory layers accordingly.

**[07:22]** Use this diagram to guide your

**[07:25]** understanding of how different memory

**[07:28]** layers interact and support scalable

**[07:31]** agent behavior.

**[07:36]** In conclusion, AI agents need robust

**[07:40]** memory architectures to deliver

**[07:43]** personalized

**[07:44]** adaptive experiences by combining

**[07:48]** short-term working memory with long-term

**[07:51]** vector storebased memory. Agents can

**[07:54]** retain context, learn from past

**[07:57]** interactions, and provide more humanlike

**[08:00]** responses.

**[08:02]** We've covered the motivation for memory

**[08:05]** types and layers, architectures,

**[08:09]** patterns, integration and challenges. As

**[08:13]** next step, I encourage you to experiment

**[08:16]** with vector databases, evaluate the

**[08:19]** memory retrieval algorithms and

**[08:22]** contribute to emerging memory standards.

**[08:25]** Thank you for joining me and I'm happy

**[08:27]** to answer questions. To give more uh

**[08:30]** context of Infinity Edge AI, we are

**[08:34]** going to have a collab of our release

**[08:37]** 2.2 tomorrow as part of a two-day

**[08:40]** hackathon of a scoop AI 2025 and

**[08:44]** Shinjzhen Bay Innovation Center which is

**[08:47]** the I forget the road scar across the

**[08:51]** street from Nvidia headquarters. uh and

**[08:54]** you contact me probably you can see I

**[08:56]** post it or I can send you the luma uh if

**[08:59]** you it's free to join feel free to join

**[09:01]** me uh tomorrow uh in 4:30 to 6:00 pm we

**[09:06]** do have uh eight uh work streams uh

**[09:10]** workstream one is called look at my

**[09:12]** memory so I have the longterm memory in

**[09:14]** my mind uh workstream one is called the

**[09:17]** distributed cloud it supports the edge

**[09:20]** app like sty now like instant in the

**[09:23]** translation.

**[09:24]** Um, workstream 2 is about EDA. Don't get

**[09:28]** me wrong, it's not the EDA you are

**[09:30]** thinking about the chipset. It's the

**[09:32]** edge data agent. It's like when you walk

**[09:35]** to the Egypt museum, you know, oh, okay.

**[09:39]** So, the chap GDP doesn't know the proper

**[09:42]** data. It doesn't know uh what's

**[09:44]** happening right now for the new show,

**[09:46]** the new exhibition. So uh we provide the

**[09:49]** EDA uh for you to know it and work

**[09:52]** stream 3 is called spear uh it's called

**[09:55]** it's the runtime it runs uh top of the

**[09:58]** kubernetes orchestration and uh we

**[10:01]** provide the enident AI and the agent

**[10:04]** Asian platform it's a similar to autogen

**[10:06]** but it's a um developer from our

**[10:09]** community and workstream 4 is the edge

**[10:13]** lake so edge lake we have already have

**[10:16]** this open source deploy in the city of

**[10:19]** Kansas state and uh the whole city's uh

**[10:23]** utility is uh using our open source

**[10:26]** component

**[10:27]** um workstream five yeah I'm just

**[10:30]** retrieving in my long-term memory now

**[10:32]** workstream five is the edge gateway use

**[10:35]** open source called shifu and also use

**[10:38]** the uh um the edge gateway they they

**[10:42]** support a lot of uh like uh the IoT

**[10:45]** protocols which uh one of the use case

**[10:48]** is in Malaysia they can clean uh under

**[10:51]** the ocean for the yellow submarine. Oh,

**[10:54]** it doesn't have to be yellow. I'm just

**[10:55]** making it up. But the use case is real.

**[10:58]** And workstream six I'm not finishing.

**[11:01]** And workstream six is um oh you got me.

**[11:05]** What's Oh, it's a physical AI. The most

**[11:07]** popular thing and physical AI there are

**[11:10]** three sub sub uh subwork streams. Number

**[11:14]** one is the AI agent uh agent. It's based

**[11:19]** on the our agent platform. Uh our team

**[11:22]** is located in UK. So they cannot join

**[11:25]** this time and uh but it provides really

**[11:29]** good uh agent uh in integrated MCP and

**[11:33]** A2A. Uh the sub worksh

**[11:39]** uh um enentic no it's the generative AI

**[11:43]** for automotive yeah I know AMDIA have

**[11:46]** the similar thing uh but we are open

**[11:48]** sourcing it and uh third uh subwork

**[11:52]** stream is core um uh robotics so uh

**[11:57]** company like Fujitu uh signal logic they

**[12:01]** have those small language model robotics

**[12:04]** And the use case has been the ayurumba

**[12:06]** at your house and also the uh the

**[12:09]** robotics audience in the Tokyo summer

**[12:13]** Olympia and also those um the robotic

**[12:18]** arms serving in the Tokyo University in

**[12:21]** the campaign. Okay, this is about work

**[12:24]** stream. I only have two workstream uh

**[12:27]** lefts, don't worry. Workstream 7 is

**[12:29]** about AI security and it also leverage

**[12:33]** the AI memory and case is created

**[12:37]** something called uh uh ages edge AI

**[12:42]** which provide the gorgeous geo fencing

**[12:45]** and then you can make sure your AI

**[12:48]** solutions and products are very secure.

**[12:50]** And the last not least the uh workstream

**[12:53]** is the uh uh what is it called uh AI ops

**[12:59]** yeah it's different from MO ops maybe

**[13:02]** bigger scope so uh red hat team has been

**[13:05]** contributing a lot so this community has

**[13:07]** more than 20 companies and universities

**[13:10]** contributing

**[13:12]** uh um I think it's really good last time

**[13:16]** uh during the pietorch conference we

**[13:18]** were part of open source AI week and uh

**[13:21]** we attracted 200 people uh sign up and

**[13:25]** uh um this time another 200 uh people

**[13:28]** sign up for the hackathon and uh our uh

**[13:31]** collab with part of it. Every two months

**[13:35]** we have a release and uh we do uh

**[13:38]** leverage a lot of long-term memory uh in

**[13:41]** our system design. I think this is a

**[13:44]** must have if we want the agent to behave

**[13:48]** uh uh really as personalized as precise

**[13:53]** what you need uh reduced uh hillerian

**[13:57]** and uh I think this is the only way so

**[14:00]** far um I'll pause here to see any

**[14:03]** questions and comments

**[14:06]** yeah and if you want to join uh our uh

**[14:10]** increased AI it's totally free and we

**[14:13]** have our weekly meeting at 6:00 p. p.m.

**[14:16]** Tuesday California time. It's online and

**[14:21]** like we have collab every two weeks. Oh,

**[14:24]** no. So, every two months, two weeks is

**[14:26]** too much. Yeah. Um and we collaborate

**[14:31]** with uh uh UC uh Santa Cruz, Stanford

**[14:36]** University and uh UC Berkeley and also

**[14:40]** San Jose State Universities and Santa

**[14:42]** Clara Universities and the companies

**[14:46]** include uh Google, Meta, uh Nvidia and

**[14:50]** uh uh Snapchat

**[14:53]** uh in my company. Yeah, there were many

**[14:57]** and I think the most takeaway lesson and

**[15:00]** learned is that it's very important

**[15:02]** about the technical direction because in

**[15:05]** the beginning we do look at the what's

**[15:08]** available uh in the is existing

**[15:10]** open-source uh uh software we can take

**[15:14]** and uh if we couldn't we just uh reuse

**[15:18]** if we could if we cannot find it we just

**[15:20]** uh leverage it and another point is that

**[15:24]** we work very close with the uh PyTorch

**[15:27]** uh community and also the CNCF

**[15:31]** community. Uh there's something called

**[15:33]** Kubby Edge. I I personally work with I'm

**[15:36]** also the TSA member of Kubge TSA member

**[15:39]** for the open platform uh enterprise AI.

**[15:44]** So like our work stream is runtime

**[15:47]** working together with Opia from F AI

**[15:50]** data. Uh I think that one uh Opia

**[15:54]** leverage a lot of AI memory and we just

**[15:57]** run top of it build around time and on

**[16:00]** top of it we run the live streaming as

**[16:03]** the flagship use case. It's one of the

**[16:07]** uh simple example I can give is more

**[16:09]** like a okay uh

**[16:13]** doing think about you are a creator you

**[16:16]** run the live streaming right and then

**[16:19]** you want to just call your agent say uh

**[16:21]** you can give a name hey little Kevin uh

**[16:24]** can you turn on the camera or turn off

**[16:26]** the camera or summarize what people

**[16:29]** comment post their public comments there

**[16:31]** just in seconds it comes to you is

**[16:35]** analysis you know okay who's actually

**[16:38]** interested in the product I'm showcasing

**[16:41]** and like you wanted to get from the

**[16:45]** memory like uh what I wanted to see I

**[16:48]** want to see more like tables I wanted to

**[16:51]** see more storytelling and who's more

**[16:54]** important and exact to my business point

**[16:57]** I can follow up with a 90-day pilot etc

**[17:01]** I think in this case we really uh expect

**[17:04]** the AI memory to give us the uh right

**[17:08]** things. Each person or or each engineer

**[17:12]** or the salesperson they want different

**[17:14]** answers. That's where the the merit of

**[17:18]** AI memory is. And uh infinite edge AI is

**[17:22]** trying to build the uh full stack uh

**[17:25]** from button to up all the way to

**[17:27]** application and uh running with AI

**[17:31]** memory uh to make it happen. Yeah. Any

**[17:35]** other questions that become my talk

**[17:38]** show?

**[17:40]** Uh yeah. Uh to share uh more about me.

**[17:43]** Uh yeah, I'm currently the uh Infinity

**[17:46]** Edge AI technical steering committee

**[17:48]** chair. Uh I work in the company like uh

**[17:52]** Tik Tok by dance uh on Philips Lighting,

**[17:56]** Futureway and Huawei. uh yeah for many

**[17:59]** years uh I know uh Charles and uh Frank

**[18:03]** has many years friends and I really

**[18:06]** think this community has a lot of uh uh

**[18:09]** experts and uh really energetic. Yeah, I

**[18:13]** would say I would encourage people like

**[18:16]** if you like I think L foundation is a

**[18:19]** good place to work with and to meet your

**[18:22]** fellow uh developers and maybe next time

**[18:25]** we can have uh the joint event but feel

**[18:28]** free to join for tomorrow's collab and

**[18:31]** if you miss tomorrow and in January

**[18:34]** we'll have the release 3.0 zero uh that

**[18:37]** will be hosted in the by UC Santa Cruz

**[18:42]** Silicon Valley uh campus in Santa Clara

**[18:45]** to don't worry you don't have to drive

**[18:46]** to Santa Cruz. Um yeah,

**[18:50]** any questions at all? Do I say something

**[18:52]** like you don't want to listen?

**[18:56]** Uh yeah. Uh thanks. Yeah. Thank you

**[19:00]** everybody. Appreciate


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
