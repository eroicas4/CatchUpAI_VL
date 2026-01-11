# Enabling Context Engineering - Zaid Zaim

**원본 영상**: [https://www.youtube.com/watch?v=3dSO5_Lh3uE](https://www.youtube.com/watch?v=3dSO5_Lh3uE)
**작성일**: 2026-01-11
**Video ID**: 3dSO5_Lh3uE

---

## 요약

Amazon Bedrock Agent Core의 메모리 기능에 대한 기술 발표로, AI 에이전트가 컨텍스트를 유지하고 학습하기 위한 단기 및 장기 메모리 시스템을 소개합니다. 메모리가 없는 에이전트는 금붕어처럼 이전 대화를 기억하지 못하지만, 메모리 기능을 통해 사용자 선호도를 저장하고 맥락을 유지하며 개인화된 경험을 제공할 수 있습니다.

---

## 핵심 포인트

- 2028년까지 기업 소프트웨어의 33%가 에이전틱 AI를 포함할 것으로 예상 (현재 1% 미만)
- AI 에이전트에는 단기 메모리(RAM처럼 세션 기반)와 장기 메모리(하드 드라이브처럼 영구 저장) 두 가지 유형이 필요
- 메모리가 없는 에이전트는 이전 대화 맥락을 잃어 반복적인 질문을 하게 됨
- Amazon Bedrock Agent Core는 서버리스 인프라로 메모리 관리를 자동화
- 세밀한 접근 제어, 암호화, 관찰 가능성 등 보안 기능이 내장됨

---

## 주요 내용

### 섹션 1: 에이전틱 AI의 진화
- 1세대: 단순 콘텐츠 생성 (프롬프트 입력 → 결과 출력)
- 2세대: 추론 프레임워크를 활용한 초기 에이전트 (API 통합, 함수 호출)
- 3세대: 완전 자율적인 멀티 에이전트 시스템 (복잡한 워크플로우 자동 실행)
- IT 문제 자동 진단/해결, 단일 프롬프트로 풀스택 앱 생성 등 가능

### 섹션 2: 메모리의 필요성
- 메모리 없는 에이전트의 문제점: iPhone 모델을 반복적으로 물어보는 사례
- "메모리 없는 에이전트는 금붕어와 같다"
- 컨텍스트 손실로 인한 비개인화된 사용자 경험
- 스마트한 메모리 필요: 맥락 이해, 사용자 선호도 저장, 지식 보유

### 섹션 3: 단기 메모리 (Short-term Memory)
- 컴퓨터의 RAM처럼 작동하는 임시 세션 기반 메모리
- 현재 대화의 맥락 유지 및 즉각적인 응답성 제공
- 이벤트 만료 기간 설정 가능 (예: 7일)
- 예시: 전자상거래에서 4일간 쇼핑하다 구매 완료 시 맥락 유지

### 섹션 4: 장기 메모리 (Long-term Memory)
- 하드 드라이브처럼 영구적으로 저장되는 메모리
- 지속적 학습 및 진화 가능
- 사용자 선호도 저장 (예: 흰색 오픈형 헤드폰 선호, 회사 할인 25%)
- 축적된 경험을 바탕으로 추론 능력 지속적 개선
- 적응형 팀원처럼 과거 경험을 기반으로 가치 있는 상호작용 제공

### 섹션 5: Amazon Bedrock Agent Core 기능
- 모듈형 서버리스 플랫폼으로 에이전트 구축/배포/운영
- 내장된 암호화, 유연한 TTL(Time To Live), 관찰 가능성
- 단기 및 장기 메모리 옵션 제공
- 메모리 통합 기능: 하나의 API로 여러 메시지를 하나의 상호작용으로 저장
- 메모리 추출 옵션: 세션별 요약, 사용자 선호도, 의미론적 메모리

### 섹션 6: 메모리 관리 및 보안
- 이벤트 기반 메시지 구성: 메시지를 그룹화하여 맥락 유지
- 네임스페이스를 통한 세밀한 접근 제어
- IAM(Identity and Access Management) 정책 통합
- 멀티 사용자/멀티 세션 보안 메모리 관리
- CloudWatch 로그를 통한 관찰 가능성 및 피드백 루프

### 섹션 7: 아키텍처 예시
- 단기 메모리: 로컬 에이전트 → 대화 이력 저장 → Bedrock LLM 선택
- 장기 메모리: 벡터 데이터베이스에 저장 → 선택한 모델 호출
- 모듈형 접근으로 필요한 서비스 조합 가능
- GitHub에 AWS 코드 샘플 제공

---

## 타임라인

- **00:00**: I'm here to talk about Amazon's offering bedrock agent core uh and we'll deep dive on memory stuff specifically and my name is Aligerat I'm a senior startup solutions architect I work with u a lot of health center startups within uh the area so while we get into some of these details I wanted to talk about little about the evolution of agentic AI right so it's been just fascinating to see how Jai has evolved in the agent AI space in the first wave here JI was used for simple content generation you give it a prompt it gives you an output a paragraph an image a line of code etc then we kind of saw the emergence of early agents that leverage reasoning frameworks right and then access and learn from proprietary information and data sources uh and integrate with APIs to take actions via function calling and so on and so forth. However, over the last year, we started seeing agents transition into fully autonomous multi- aent systems that can seamlessly kind of execute multi-step workflows dynamically, right? Adapting to the changing environments that we have. As a result, they're now capable of tackling far more complex real world use cases like autonomously diagnosing and remediating IT production issues perhaps or even generate and deploy full stack applications from a single prompt. Right? This this leap in agents capability is driven by some fundamental shifts. Now some of the Gartner research that we've collected says so about 33% of enterprise software apps will include agentic AI by 2028 up from less than 1% a couple of years ago right and he also got predicts 15% of day-to-day work decisions will be made autonomously through agenti by 2028. Before we get into the actual service itself, I want to talk about some use...
- **05:00**: June 3rd, 2025. How do I take a screenshot on my phone? What is the iPhone model you're using? Right? We want to get from here past that. Right? Loss of context does not give you personalized user experience. Now what we want to do is don't just remember be smart have contextual intelligence have user preferences stored and also have knowledge retention right we'll double click a little bit more on these for agentic memory the core concepts are broken down into two segments one is the short-term memory and one is the long-term memory while short-term memory functions like RAM and computer temporary session based long-term memory acts more like a hard drive right persistent evolutionary learning this dual memory architecture enables both immediate responsiveness and sustained improvement over time long-term memory is crucial for enabling AI self-evolution where models and agents can continuously learn adapt and refine their reasoning and capabilities based on accumulated experiences right by incorporating long-term memory. AI agents become more like adaptive teammates capable of building on past experiences to provide increasingly valuable and intelligent interactions. Now, if we go back to the short memory question, right, this is what we want to achieve. If I ask, how do I take a screenshot on my phone? readers guide on taking screenshots of so what's happening here is it's staying present not just recalling words but following your thoughts it recognizes what you're trying to accomplish right now picks up exactly where you left off and also keeps recent insights accessible right treats your clothes as part of the conversation now for long-term memory right here's the interesting part so I'm I want to make a purchase is I like both headphones. My company gives me 25% discount. I prefer...
- **10:00**: is implemented, you have conversational log JSON. Now within the agent memory, you sync chat messages, session state and checkpoint while also syncing all the list events. Now here I want to break down a little bit of how these entities operate together for short-term memory. Right? Event is a collection of messages who they belong to an actual ID organized and separate accordingly to group the events and maintain context. Now here's an example, right? I want the event expiry days to meet seven. So let's just say that you have a conversational chatbot in front of an e-commerce website and I'm trying to buy advanced day while I ask questions. Day four, I come back and I complete my purchase. It still retains my contents. This is something you can set up during configurations based on your use cases. I have a few more examples of how we can contribute this. I will also share a QR code for this tech where you can actually double click and look at this. So for long-term memory, right, section summaries creates condensed representation of interaction content outcomes. Same thing with name spaces. Uh you folks coming with AWS will understand you'll need an ARN permissions to be granted. Earlier in my uh in one of my decks I presented this modular approach about agent pro right one of them is identity. What we try to achieve is for fine grain access controls. If you have identity and access management defined at your org level, all of these translate into your bedrock agent core service as well. So you don't have to redefine access. Now I want to show you a couple of uh diagrams in the interest of time. Before we get into the uh couple of architecture examples, I want to showcase uh the observability concept of this. So like I mentioned, you can uh...

---

## 전체 자막 (타임스탬프 포함)

**[00:01]** I'm here to talk about Amazon's offering

**[00:03]** bedrock agent core uh and we'll deep

**[00:06]** dive on memory stuff specifically and my

**[00:10]** name is Aligerat I'm a senior startup

**[00:12]** solutions architect I work with u a lot

**[00:16]** of health center startups within uh the

**[00:19]** area

**[00:22]** so while we get into some of these

**[00:25]** details I wanted to talk about little

**[00:27]** about the evolution of agentic AI right

**[00:30]** so it's been just fascinating to see how

**[00:33]** Jai has evolved in the agent AI space in

**[00:37]** the first wave here JI was used for

**[00:40]** simple content generation you give it a

**[00:42]** prompt it gives you an output a

**[00:44]** paragraph an image a line of code etc

**[00:48]** then we kind of saw the emergence of

**[00:50]** early agents that leverage reasoning

**[00:53]** frameworks right and then access and

**[00:55]** learn from proprietary information and

**[00:57]** data sources

**[00:59]** uh and integrate with APIs to take

**[01:01]** actions via function calling and so on

**[01:03]** and so forth. However, over the last

**[01:07]** year, we started seeing agents

**[01:09]** transition into fully autonomous multi-

**[01:12]** aent systems that can seamlessly kind of

**[01:14]** execute multi-step workflows

**[01:16]** dynamically, right? Adapting to the

**[01:19]** changing environments that we have. As a

**[01:22]** result, they're now capable of tackling

**[01:24]** far more complex real world use cases

**[01:26]** like autonomously diagnosing and

**[01:29]** remediating IT production issues perhaps

**[01:32]** or even generate and deploy full stack

**[01:34]** applications from a single prompt.

**[01:36]** Right? This this leap in agents

**[01:39]** capability is driven by some fundamental

**[01:42]** shifts.

**[01:44]** Now some of the Gartner research that

**[01:47]** we've collected says

**[01:53]** so about 33% of enterprise software apps

**[01:56]** will include agentic AI by 2028

**[01:59]** up from less than 1% a couple of years

**[02:01]** ago right and he also got predicts 15%

**[02:06]** of day-to-day work decisions will be

**[02:09]** made autonomously through agenti by

**[02:11]** 2028.

**[02:13]** Before we get into the actual service

**[02:15]** itself, I want to talk about some use

**[02:18]** cases that we see across the industry,

**[02:20]** right? Agentic use cases in automotive,

**[02:23]** energy, financial services, healthcare,

**[02:25]** licenses, media.

**[02:27]** I'd like to take a pause here and and

**[02:30]** see if you have any questions around

**[02:33]** what what do you see any interesting

**[02:34]** stories

**[02:36]** in the crowd?

**[02:39]** Cool.

**[02:42]** We'll talk about these in detail.

**[02:47]** So to introduce you, Amazon Bedrock

**[02:50]** Agent Core is a platform where you can

**[02:52]** build and deploy and operate highly

**[02:54]** capable agents securely at scale using

**[02:58]** any framework and model. We do the

**[03:01]** underlying

**[03:03]** uh undifferiated heavy lifting for you.

**[03:05]** So we provide you with a set of

**[03:10]** modular services that you can mix and

**[03:13]** match with everything you need to get

**[03:16]** agents production ready. Right? You have

**[03:19]** our runtime module memory which you're

**[03:21]** going to double in a bit. Identity

**[03:23]** access management gateways code

**[03:25]** integrated so on and so forth.

**[03:28]** Now this picture kind of gives you a

**[03:30]** block view of all the modular services

**[03:34]** that I just showed on the previous

**[03:35]** slide. You need enhancing with tools in

**[03:38]** memory. How do you deploy securely at

**[03:41]** scale and also getting like operational

**[03:43]** insights with agentic operations right

**[03:46]** along with all of this we've also baked

**[03:48]** in observability and security into this

**[03:51]** agent core platform.

**[03:55]** Now what is actually needed to build a

**[03:58]** context aware AI agents right the answer

**[04:01]** is simple agents need memory

**[04:05]** now let's look at a couple of scenarios

**[04:07]** here agents without memory on the left

**[04:09]** hand side and agents with memory enabled

**[04:12]** users interacting with agents you get a

**[04:15]** response

**[04:17]** but response without previous context

**[04:20]** right now if you have memory you're

**[04:22]** writing the agents is within the context

**[04:26]** of the memory and responses come with

**[04:30]** contextual awareness. Every time you

**[04:32]** have a new conversation, it retains the

**[04:34]** context. Here's an example, right? I

**[04:37]** like this quote which says a data agent

**[04:39]** without memory is like a goldfish. Uh

**[04:42]** because essentially if you look at this

**[04:44]** chat, the user says, "How do I switch

**[04:47]** apps on my iPhone?"

**[04:50]** The chatbot replied saying, "What is the

**[04:52]** iPhone model that you're using?" iPhone

**[04:54]** 16. If I this link, it has all the

**[04:56]** gestures to switch between apps. This

**[04:59]** was on June 1st, 2025.

**[05:02]** June 3rd, 2025. How do I take a

**[05:04]** screenshot on my phone? What is the

**[05:06]** iPhone model you're using? Right? We

**[05:09]** want to get from here past that. Right?

**[05:11]** Loss of context does not give you

**[05:13]** personalized user experience.

**[05:17]** Now what we want to do is don't just

**[05:19]** remember be smart have contextual

**[05:22]** intelligence have user preferences

**[05:25]** stored and also have knowledge retention

**[05:28]** right we'll double click a little bit

**[05:30]** more on these for agentic memory the

**[05:34]** core concepts are broken down into two

**[05:38]** segments one is the short-term memory

**[05:40]** and one is the long-term memory while

**[05:43]** short-term memory functions like RAM and

**[05:45]** computer temporary session based

**[05:48]** long-term memory acts more like a hard

**[05:50]** drive right persistent evolutionary

**[05:52]** learning this dual memory architecture

**[05:55]** enables both immediate responsiveness

**[05:57]** and sustained improvement over time

**[06:00]** long-term memory is crucial for enabling

**[06:03]** AI self-evolution where models and

**[06:05]** agents can continuously learn adapt and

**[06:08]** refine their reasoning and capabilities

**[06:10]** based on accumulated experiences right

**[06:13]** by incorporating long-term memory. AI

**[06:16]** agents become more like adaptive

**[06:18]** teammates capable of building on past

**[06:20]** experiences to provide increasingly

**[06:22]** valuable and intelligent interactions.

**[06:26]** Now, if we go back to the short memory

**[06:29]** question, right, this is what we want to

**[06:31]** achieve. If I ask, how do I take a

**[06:33]** screenshot on my phone? readers guide on

**[06:36]** taking screenshots of

**[06:39]** so what's happening here is it's staying

**[06:41]** present not just recalling words but

**[06:43]** following your thoughts it recognizes

**[06:46]** what you're trying to accomplish right

**[06:48]** now picks up exactly where you left off

**[06:51]** and also keeps recent insights

**[06:52]** accessible right treats your clothes as

**[06:55]** part of the conversation

**[06:57]** now for long-term memory right here's

**[07:01]** the interesting part so I'm I want to

**[07:03]** make a purchase is I like both

**[07:05]** headphones. My company gives me 25%

**[07:07]** discount. I prefer

**[07:10]** they don't

**[07:12]** but that's an example.

**[07:14]** Uh my company gives 5% discount and then

**[07:17]** I prefer white open gear headphones.

**[07:20]** Right now what it understands is user

**[07:25]** preferences memory right likes both

**[07:27]** headphones and also likes the color

**[07:29]** white

**[07:31]** stores like what users likes prefers

**[07:33]** buys you know gets updated over time I

**[07:35]** want new headphones to change the old

**[07:37]** ones it's checking memory and it

**[07:40]** responds hey I can suggest some wide

**[07:42]** opener investment options under $300 to

**[07:46]** we would fit your budget etc. So that's

**[07:49]** what we want to achieve,

**[07:52]** right? Um

**[07:54]** some repetative slides here want to

**[07:56]** skip. So it it it so the whole context

**[08:00]** of these slides is to kind of emphasize

**[08:02]** that memory is being stored and used as

**[08:05]** part of whenever relevant within the

**[08:07]** conversation.

**[08:09]** So while Amazon has been building this

**[08:13]** uh service, we did see a lot of

**[08:16]** challenges that come from the market

**[08:18]** especially about how do you you know

**[08:21]** storage scalability issues. How do I

**[08:24]** refresh the memory? How do I integrate

**[08:26]** with 40 different systems that we have

**[08:29]** privacy which is day zero concern for

**[08:33]** AWS privacy and security? what are my

**[08:36]** retrieval options and observability on

**[08:38]** top of everything right

**[08:41]** so why solving this let's double click

**[08:44]** on bedrock agent core memory now

**[08:48]** here you know the core infrastructure is

**[08:52]** serverless with minimal setup like I

**[08:54]** mentioned we do the underlying

**[08:56]** undifferiated heavy lifting so you don't

**[08:58]** have to manage all of your

**[09:00]** infrastructure there's built-in

**[09:01]** encryption enabled

**[09:03]** flexible time to in observability. Same

**[09:06]** thing with memory management. You have

**[09:08]** options for short-term and long-term

**[09:10]** built-in memory consolidation. One API

**[09:13]** to store multiple messages as one

**[09:15]** interaction, right? Same thing with

**[09:17]** memory extraction options, summary per

**[09:19]** session, user preferences, semantic

**[09:21]** memory to understand the context

**[09:23]** meaningfully and then multiple retrieval

**[09:26]** patterns. Right

**[09:29]** now uh a little bit in a modular section

**[09:33]** about high level overview. You have ages

**[09:36]** feeding and raw events short-term

**[09:38]** memory. You have a memory extraction

**[09:41]** module.

**[09:43]** This is pretty similar to how memor

**[09:46]** operates. And you have memory records

**[09:48]** being stored in a long-term vector store

**[09:51]** which are uh retrieved back as memories.

**[09:55]** short-term draw storage. We want to

**[09:58]** double click on this. So when the agent

**[10:00]** is implemented, you have conversational

**[10:03]** log JSON. Now within the agent memory,

**[10:06]** you sync chat messages, session state

**[10:09]** and checkpoint while also syncing all

**[10:12]** the list events.

**[10:14]** Now

**[10:16]** here I want to break down a little bit

**[10:18]** of how these entities operate together

**[10:21]** for short-term memory. Right? Event is a

**[10:24]** collection of messages who they belong

**[10:26]** to an actual ID organized and separate

**[10:30]** accordingly to group the events and

**[10:32]** maintain context.

**[10:36]** Now here's an example, right? I want the

**[10:39]** event expiry days to meet seven. So

**[10:43]** let's just say that you have a

**[10:45]** conversational chatbot in front of an

**[10:47]** e-commerce website and I'm trying to buy

**[10:49]** advanced day while I ask questions. Day

**[10:52]** four, I come back and I complete my

**[10:54]** purchase. It still retains my contents.

**[10:56]** This is something you can set up during

**[10:59]** configurations based on your use cases.

**[11:04]** I have a few more examples of how we can

**[11:06]** contribute this. I will also share a QR

**[11:09]** code for this tech where you can

**[11:10]** actually double click and look at this.

**[11:14]** So for long-term memory, right, section

**[11:16]** summaries creates condensed

**[11:18]** representation of interaction content

**[11:20]** outcomes. Same thing with name spaces.

**[11:23]** Uh you folks coming with AWS will

**[11:28]** understand you'll need an ARN

**[11:30]** permissions to be granted.

**[11:33]** Earlier in my uh in one of my decks I

**[11:36]** presented this modular approach about

**[11:38]** agent pro right one of them is identity.

**[11:42]** What we try to achieve is

**[11:44]** for fine grain access controls. If you

**[11:46]** have identity and access management

**[11:48]** defined at your org level, all of these

**[11:51]** translate into your bedrock agent core

**[11:54]** service as well. So you don't have to

**[11:56]** redefine access.

**[12:00]** Now I want to show you a couple of uh

**[12:03]** diagrams in the interest of time.

**[12:12]** Before we get into the uh couple of

**[12:14]** architecture examples, I want to

**[12:15]** showcase uh the observability concept of

**[12:18]** this. So like I mentioned, you can uh

**[12:22]** capture all your cloudatch logs for the

**[12:24]** way these agents and the memory is

**[12:27]** behaving. So this kind of gives you the

**[12:30]** overall observability

**[12:32]** and and uh you can build on top of that

**[12:34]** as a feedback loop. In terms of security

**[12:38]** um like I mentioned just now you can

**[12:41]** have anti- access management where you

**[12:44]** have a basic IM policy pure internal

**[12:46]** long-term memory or you can implement

**[12:48]** fine grain access controls you know

**[12:51]** secure multi-user or multi session

**[12:52]** memory management within patient core

**[12:54]** memory

**[12:58]** couple of example architectures I wanted

**[13:00]** to showcase for short term um I'll leave

**[13:04]** this for a second if you want to click

**[13:06]** pictures. Um, user question agent

**[13:09]** responses. So, you have your local

**[13:11]** environment.

**[13:15]** I didn't realize this is a hot screen.

**[13:17]** Uh, local agents, you could use trans

**[13:21]** agents store conversational history

**[13:23]** within agent course memory. And then you

**[13:26]** could use bedrocks offerings of LLMs

**[13:29]** that we have. Uh, you could choose the

**[13:33]** model of your choice. uh by evaluation

**[13:36]** and then u work work with it for

**[13:40]** long-term uh similarly like I mentioned

**[13:43]** long-term memory is stored in the vector

**[13:45]** database and then there there multiple

**[13:48]** choices of vectors vector database you

**[13:50]** can pick from again invoking a model of

**[13:53]** your choice within within

**[13:59]** so a couple of decks here you we have

**[14:02]** some AWS code samples available in gith

**[14:04]** UB and uh also the deck where you can

**[14:08]** actually look at uh multiple options

**[14:10]** that are available.

**[14:14]** >> Thank you.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
