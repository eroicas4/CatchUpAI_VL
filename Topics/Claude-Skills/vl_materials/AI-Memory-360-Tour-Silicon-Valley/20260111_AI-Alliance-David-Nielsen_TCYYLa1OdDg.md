# AI Alliance - David Nielsen

**원본 영상**: [https://www.youtube.com/watch?v=TCYYLa1OdDg](https://www.youtube.com/watch?v=TCYYLa1OdDg)
**작성일**: 2026-01-11
**Video ID**: TCYYLa1OdDg

---

## 요약

AI Alliance의 David Nielsen이 RAG(Retrieval-Augmented Generation) 기반 챗봇인 Alleycat을 소개하고, 이를 단순 RAG에서 메모리 기능을 갖춘 고급 AI 에이전트로 발전시키는 과정을 설명합니다. 청중과의 인터랙티브 세션을 통해 추론(reasoning), 계획(planning), 메모리 통합 등 에이전트의 핵심 개념을 실습 중심으로 다룹니다.

---

## 핵심 포인트

- AI Alliance는 IBM과 Meta가 주도하여 오픈소스 AI를 지원하기 위해 설립됨
- Alleycat 프로젝트는 웹사이트 스크래핑과 RAG를 결합한 챗봇에서 시작
- 단순 RAG는 항상 같은 프로세스를 반복하므로 진정한 에이전트가 아님
- 에이전트가 되려면 추론(reasoning)과 계획(planning) 단계가 필요
- 메모리 기능을 통해 사용자 컨텍스트를 유지하고 연속성 있는 대화 구현
- MCP(Model Context Protocol) 도구 호출을 통한 다중 경로 의사결정
- 최종 목표는 자율적으로 거래까지 수행하는 프로덕션 레벨 에이전트 개발

---

## 주요 내용

### 섹션 1: AI Alliance 소개
- 2년 전 ChatGPT 출시 당시 오픈소스 옵션 부재 우려로 IBM, Meta 등 50개 기업이 설립
- 현재는 Meta 등 다양한 오픈소스 LLM이 등장하여 위협 감소
- GitHub에 여러 프로젝트 운영 중 (예: Semiant - AI 에이전트와 인간을 위한 위키 시스템)

### 섹션 2: Alleycat 프로젝트 개요
- 원래 "Alliance Chat"으로 시작된 RAG 기반 챗봇
- 웹사이트 스크래핑 기능 포함 (HTML, PDF 등)
- 프로세스: 질문 → 벡터화 → 벡터 DB 검색 → 컨텍스트 생성 → LLM 답변
- 현재는 단순 RAG로 의사결정 트리가 없어 에이전트라 할 수 없음

### 섹션 3: 에이전트 핵심 개념 - 추론과 계획
- **추론(Reasoning)**: 질문을 받았을 때 어떤 경로를 선택할지 결정하는 단계
- **계획(Planning)**: 선택 후 실행할 워크플로우 설계
- MCP를 통한 도구 호출: LLM이 여러 MCP 중 적절한 것을 선택
- 모델이 각 도구의 설명을 보고 가장 적합한 도구를 자동 선택

### 섹션 4: 메모리 통합
- **단기 메모리(Short-term Memory/Profile Memory)**
  - 현재 대화 세션 내 정보 저장
  - 사용자 선호도, 프로그래밍 언어, 응답 스타일 등 저장
  - 예: "저는 Python 개발자입니다" → 이후 답변에서 Python 관련 정보 우선 제공

- **장기 메모리(Long-term Memory)**
  - 프로젝트 진행 상황, 과거 작업 이력 저장
  - 예: 사용자 위치(샌프란시스코) 저장 → 해당 시간대 이벤트 자동 추천
  
- **메모리의 효과**: RAG만 사용하면 매번 "첫 데이트"처럼 모든 컨텍스트를 다시 설정해야 하지만, 메모리는 연속성과 관련성 제공

### 섹션 5: 워크샵 로드맵
- **1단계**: 기본 RAG에서 시작하여 고급 에이전트로 발전
- **2단계**: 금융 분석 사례 (Deep Research Agent)
  - 주식 종목 심층 조사
  - 실시간 정보 제공
  - 이전 조사 내용과 연결하여 시장 변화 추적
  
- **3단계**: 미래 비전 - 자율 거래 에이전트
  - 조사 결과를 바탕으로 자동으로 거래 실행
  - 사용자 확인 없이 다른 API/MCP/에이전트와 통신하여 작업 완료
  - 예: 지인을 위한 선물 자동 구매 시스템

### 섹션 6: 실습 워크샵 목표
- 프로덕션 환경에 배포 가능한 실제 에이전트 구축
- 이론뿐 아니라 실제 구현 가능한 기술 전수
- 아직 시장에 나오지 않은 선진 기술 선도

---

## 타임라인

- **00:00**: So um first of all the AI alliance was originally formed by IBM and Meta and actually 50 other companies back when chatbt first came out and we were worried that there would be no open source options. So you know about two years ago that was a real threat and it still is sort of but there are many LLMs now that are doing quite well [clears throat] uh and open source options um from from meta but also from other uh companies and countries even. So that is not as near a threat as it was. And so we decided to branch out and go off here and support AI uh sorry open source for AI in a variety of ways. And so if you check out our GitHub repo, you'll see there's quite a few projects there. Um other than this one, one of my favorites is called Semiant. And it is the way I describe it. It's sort of like if you were to take um a wiki and make it useful for both humans and AI agents, what would that do? Like what would that look like? And they're the guy who's leading the project, they're they're putting like a an ontology onto it. So when you describe what's important to you and then when you go and ask questions of the content. It's it's using your own, you know, context uh to ask questions, but then the AI agents can also use that same context when trying to ask questions on your behalf. It's it's a very interesting project, but this project is very uh a much simpler project and it's really nothing groundbreaking, but it's I think it's going to be really useful for this uh presentation. So, I thought I'd start here. So, uh what is Alcat? Alleycat was originally called Alliance Chat and it was meant to be a way to scrape the AI Alliance website and give visitors a way to ask questions through simple RAG interface. Okay. And most of you probably know what RAG is, right? Please say yes. Okay. All right. Okay. Good....
- **05:00**: building natural advanced agent something you can actually put into production in [clears throat] your company and we have an example of that which lead you through the deep research agent. Uh what I thought I would do is just let's have an interactive session here and I'd like gallery to come up and join me. uh she can be my um I'm going to I'm going to well we're both going to play dumb and then uh invite you to help us solve this riddle. So first of all I'm asking what would you call that step where the question is um the question comes to the web page here and it asks me a side I've got a prompt the question and I've got multiple paths I can go what would you call that step where it decides what to do >> in Oh yes. >> I would call it in a less technical way a decision to be made between choosing which way to go next. >> Okay. How about you? We're going to do audience participation. Um we're we're done. We're going to help you and the audience they're smarter than us and you right. So what would you call that? What's that step? Yes. >> Planning. >> Planning. Okay. I definitely heard that word in context of that. Okay. Um, what else? I think there might be maybe one other word. Triage. Okay. I haven't that word, but what you mean? I think we can use that word too. >> Reasoning. Those are the two. Okay. That I was saying triage. I think maybe is the whole thing, right? But reasoning. So, first of all, what what is this? What do we do with this? Right? And then once you figure out what you might want to do, then there's plans, right? >> Okay. So, the next step that we would do...
- **10:00**: an agent should understand. So, it's basically the MCP tool line, right? this step right so now um how about the workflow so right now we've chosen between we're choosing one of many NCBS and then we answer back and we give it to the user so there's not a lot of planning the plan is call one SCP right now I think it actually gets a little more complicated uh when you start getting the planning goal steps and I'm not we're not going to go down that path right now because I think that's just too much for what we have to cover but Where does memory come in? You're going to you're going to let's say we have four options. So we got some planning. Okay. Um you know uh two MCPs you can call one or the other or both in options order. So that's four. Right. Somebody asked a question. I was going to bring up the image. I forgot bring it up. There's any um what where the different where where does memory play a role in this this uh this workshop with >> I think this way gives the agent the answer to what it's looking for but makes it remember what it's supposed to know. Um and what I mean by that is I think in this diagram memory will come somewhere uh where >> there's the question. >> Yeah. So memory will come somewhere here as >> right when the question is asked. >> Yes. Right after the question is asked, the agent will go look into the memory to find relevant details. And once it finds relevant details, that query will be augmented with all of the relevant details. So that every response that you get from the agent, it's got context aware. So I think of it this way. >> Well, okay. So, so in this case, we're we're literally solving the problem of you ask question about AI, you have many projects. So somebody might ask which...
- **15:00**: know what events are interesting today and it would know oh since you're in the local week and then also it say but this is one problem I love somebody oh since you're in you're in this time zone here are the online events that are appropriate for your right >> yeah so in this case the fact that The user does a counter view will be stored in the profile memory and then a tool an MCP tool that does web search and looks for all of these events can will then know what events to look for otherwise it will just look for all the events right but now with this information the result will be more enriched and relevant. >> Okay. All right. Well, that's I just wanted to kind of take you down that path because that's that's actually what we're doing right now as a a workshop is we're building out these steps so people can learn uh as they as we are basically and um and yeah and and just to give you a little taste of where we're going is we're trying to get this to the point where for deep research at least it's production ready like by the time the end of the workshop you are asking a series of questions And it's able to in in the use case that we're focused on first, it's you pass a financial instrument like stock symbol or something like that and it's going to go deep do you deep research on that uh item for just today like here's what's happening now. And then, you know, we would use a short-term memory for that. And then we can add the long-term memory for when they come back and ask questions about uh maybe another financial instrument that relates to that one or they ask about the same one contracts and say, well, the market has changed since the last time you were here. >> Um, yeah. So, we'll be doing that. And then where we plan to take this workshop is we want to go somewhere where...

---

## 전체 자막 (타임스탬프 포함)

**[00:00]** So um first of all the AI alliance was

**[00:04]** originally formed by IBM and Meta and

**[00:08]** actually 50 other companies back when

**[00:10]** chatbt first came out and we were

**[00:12]** worried that there would be no open

**[00:14]** source options. So you know about two

**[00:17]** years ago that was a real threat and it

**[00:19]** still is sort of but there are many LLMs

**[00:22]** now that are doing quite well

**[00:24]** [clears throat] uh and open source

**[00:25]** options um from from meta but also from

**[00:29]** other uh companies and countries even.

**[00:32]** So that is not as near a threat as it

**[00:35]** was. And so we decided to branch out and

**[00:37]** go off here and support AI uh sorry open

**[00:40]** source for AI in a variety of ways. And

**[00:43]** so if you check out our GitHub repo,

**[00:45]** you'll see there's quite a few projects

**[00:46]** there. Um other than this one, one of my

**[00:49]** favorites is called Semiant. And it is

**[00:53]** the way I describe it. It's sort of like

**[00:56]** if you were to take um

**[00:59]** a wiki and make it

**[01:03]** useful for both humans and AI agents,

**[01:08]** what would that do? Like what would that

**[01:10]** look like? And they're the guy who's

**[01:14]** leading the project, they're they're

**[01:15]** putting like a an ontology onto it. So

**[01:18]** when you describe what's important to

**[01:20]** you and then when you go and ask

**[01:22]** questions of the content. It's it's

**[01:25]** using your own, you know, context

**[01:29]** uh to ask questions, but then the AI

**[01:31]** agents can also use that same context

**[01:34]** when trying to ask questions on your

**[01:35]** behalf. It's it's a very interesting

**[01:37]** project, but this project is very uh a

**[01:39]** much simpler project and it's really

**[01:42]** nothing groundbreaking, but it's I think

**[01:44]** it's going to be really useful for this

**[01:46]** uh presentation. So, I thought I'd start

**[01:48]** here.

**[01:50]** So, uh what is Alcat? Alleycat was

**[01:52]** originally called Alliance Chat and it

**[01:55]** was meant to be a way to scrape the AI

**[01:57]** Alliance website and give visitors a way

**[02:00]** to ask questions through simple RAG

**[02:03]** interface. Okay. And most of you

**[02:05]** probably know what RAG is, right? Please

**[02:07]** say yes. Okay. All right. Okay. Good.

**[02:10]** So, Rag is

**[02:13]** um I guess somebody could say it's you

**[02:16]** could use it as an agent, but I don't

**[02:17]** think of it that way. I think of maybe

**[02:20]** it's an agent, but it's not an AI agent,

**[02:22]** right? It's it's doing something very

**[02:24]** specific. In fact, I have a diagram here

**[02:26]** that I wanted to show you.

**[02:29]** Oops.

**[02:31]** Not going to try to get too clever here,

**[02:32]** but in the diagram, um, this is going to

**[02:35]** set the stage. So, I thought I'd share

**[02:36]** with you. You have a person who's going

**[02:38]** to ask questions of the website. They

**[02:41]** type in a prompt. Prompt gets turned

**[02:44]** into an array. That array gets sent to a

**[02:46]** vector database where it then looks for

**[02:48]** similar arrays in the vector database.

**[02:51]** It returns a some number of arrays that

**[02:54]** is then used as a context for the

**[02:59]** question to be asked of and that those

**[03:03]** rows or arrays get sent along the prompt

**[03:05]** to the LLM and then the LLM will answer

**[03:08]** the question and get back an answer.

**[03:09]** Right. Okay, we're all good there. All

**[03:11]** right. So, but where's the data come

**[03:13]** from? Okay. So, we decided to also build

**[03:16]** the uh scraping mechanism. So, you can

**[03:18]** scrape your website or you can scrape a

**[03:21]** bunch of PDF files in like an Amazon S3

**[03:23]** bucket or something and it will take all

**[03:25]** that content. It'll pull out the HTML

**[03:28]** from well, first of all, it'll crawl the

**[03:29]** website, grab the URLs. It'll then

**[03:33]** scrape the content from each page, split

**[03:35]** it all up into chunks. It'll then

**[03:38]** vectorize the chunks to create the

**[03:39]** vector embeddings and put that content

**[03:41]** into the vector. So now we got both

**[03:44]** sides of the website of the chat the

**[03:47]** actual interface to the chat and then

**[03:49]** the actual content input into the vector

**[03:52]** right. So now what we have is just

**[03:56]** simply a a chat interface.

**[03:59]** Now is there anything aentic about this?

**[04:03]** Anybody?

**[04:05]** Not really.

**[04:07]** because it's always doing the same

**[04:08]** thing, right? It's always just taking

**[04:11]** the prompt, vectorizing it, sending to

**[04:13]** the vector database. There's no decision

**[04:15]** tree. [clears throat] So for something

**[04:16]** to be engaging, it's really got to be

**[04:18]** like thinking like a human trying to

**[04:19]** evaluate, you know, what what should I

**[04:22]** be doing with this content, right? Or

**[04:24]** this question. And maybe there's

**[04:26]** multiple paths that can take or even

**[04:28]** multiple workflows that can take and

**[04:30]** figure that out for you. Um and so what

**[04:34]** I thought we could do is talk about well

**[04:35]** okay

**[04:37]** um what what would that look like in the

**[04:39]** context of this session of this event?

**[04:43]** Um we want to use memory. Where does

**[04:45]** memory fit into that? So if we're going

**[04:48]** to take Alicat, which by the way we are,

**[04:51]** we are turning this into an agent

**[04:52]** workshop where we're going to start with

**[04:54]** rag and we're going to take the

**[04:56]** developers to attend a workshop and take

**[04:58]** them through the process of actually

**[05:00]** building natural advanced agent

**[05:02]** something you can actually put into

**[05:03]** production in [clears throat] your

**[05:04]** company and we have an example of that

**[05:06]** which lead you through the deep research

**[05:08]** agent.

**[05:10]** Uh what I thought I would do is just

**[05:11]** let's have an interactive session here

**[05:13]** and I'd like gallery to come up and join

**[05:15]** me. uh she can be my um I'm going to I'm

**[05:17]** going to well we're both going to play

**[05:19]** dumb and then uh invite you to help us

**[05:22]** solve this riddle. So first of all I'm

**[05:26]** asking

**[05:28]** what would you call that step where the

**[05:31]** question is um

**[05:34]** the question comes to the web page here

**[05:36]** and it asks me a side I've got a prompt

**[05:41]** the question and I've got multiple

**[05:44]** paths I can go what would you call that

**[05:47]** step where it decides what to do

**[05:52]** >> in

**[05:55]** Oh yes.

**[05:58]** >> I would call it

**[06:00]** in a less

**[06:03]** technical way a decision to be made

**[06:05]** between choosing which way to go next.

**[06:09]** >> Okay. How about you? We're going to do

**[06:11]** audience participation. Um we're we're

**[06:14]** done. We're going to help you and the

**[06:16]** audience they're smarter than us and you

**[06:18]** right. So what would you call that?

**[06:21]** What's that step? Yes.

**[06:24]** >> Planning.

**[06:24]** >> Planning. Okay. I definitely heard that

**[06:27]** word in context of that.

**[06:30]** Okay.

**[06:32]** Um, what else? I think there might be

**[06:34]** maybe one other word.

**[06:36]** Triage.

**[06:38]** Okay. I haven't that word, but what you

**[06:40]** mean? I think we can use that word too.

**[06:43]** >> Reasoning. Those are the two. Okay. That

**[06:46]** I was saying triage. I think maybe is

**[06:47]** the whole thing, right? But reasoning.

**[06:49]** So, first of all, what what is this?

**[06:51]** What do we do with this? Right? And then

**[06:53]** once you figure out what you might want

**[06:55]** to do, then there's plans, right?

**[06:59]** >> Okay. So, the next step that we would do

**[07:01]** in our workshop is we would say, okay,

**[07:04]** we need to figure out,

**[07:06]** you know, the reasoning step and then we

**[07:09]** need to do the planning. Now, in this

**[07:12]** case, this reasoning makes sense.

**[07:17]** You're always doing the same thing. the

**[07:19]** plan is already done.

**[07:21]** So there's no choices.

**[07:24]** But let's say we took the content of

**[07:27]** this web page which which basically

**[07:29]** sitting in that vector database and we

**[07:32]** turn that into an SCP. So now when now

**[07:36]** when the question comes in maybe we have

**[07:39]** MCPS for multiple websites.

**[07:42]** Now the reasoning could be I've got a

**[07:44]** prompt.

**[07:46]** Which website has the answers?

**[07:50]** How many of you have like worked with

**[07:51]** MCP?

**[07:54]** Okay. Who wants to answer the question?

**[07:56]** If you have multiple MCPS

**[07:59]** maybe content in multiple websites, what

**[08:01]** would you do?

**[08:04]** Again, I'm playing dumb. I don't know

**[08:05]** how this works. You got to help us.

**[08:10]** I heard somebody trying to But I can't

**[08:12]** understand the answer. Was that you?

**[08:16]** >> Yeah. Who who spoke out? Somebody said

**[08:19]** something.

**[08:20]** >> Um, I would try to maybe

**[08:24]** put it all in and then search through

**[08:25]** it.

**[08:27]** >> Okay.

**[08:28]** Where? Okay. Where would the LLM play a

**[08:31]** role?

**[08:33]** >> Uh, after I retreat the candidates.

**[08:36]** >> Okay. So, that's So, okay. So, how does

**[08:39]** the MCPS play the with the

**[08:42]** If you've worked with MCPS, you probably

**[08:44]** know this answer

**[08:47]** >> as an

**[08:48]** >> as an end point. Okay,

**[08:51]** so the question comes in, you're going

**[08:53]** to do some reasoning. The reasoning is

**[08:56]** where do I go to get the answer, right?

**[09:00]** Tool calling. There you go. And so, how

**[09:02]** does tool calling work?

**[09:07]** the uh yeah I describe multiple ways but

**[09:10]** yeah the model besides which CP is going

**[09:13]** to have the right one with the answer

**[09:15]** right so the the model is going to say

**[09:19]** you just ask this question

**[09:21]** I'm going to look at each one of the

**[09:23]** MCP's descriptions

**[09:25]** and it's and decide which one is most

**[09:28]** likely going to give me the answer right

**[09:30]** >> so the reasoning is really by calling

**[09:33]** the model with the prompt is thinking

**[09:36]** which tool should I call right? Are we

**[09:40]** all on board here? Okay. All right.

**[09:43]** Cool. Some of you are like, "Yeah, yeah,

**[09:44]** yeah. Okay, I get it." Right. Others, I

**[09:46]** hope you've been through this. So, I

**[09:47]** hope hopefully this is starting to make

**[09:49]** sense. You you pass the reasoning

**[09:51]** question to the LLM and let the LM

**[09:53]** basically make the decision. And uh

**[09:56]** there's a lot going on there that's

**[09:57]** really powerful. And I think that that's

**[09:59]** something that every developer building

**[10:01]** an agent should understand. So, it's

**[10:02]** basically the MCP tool line, right? this

**[10:05]** step right so now um

**[10:09]** how about the workflow so right now

**[10:11]** we've chosen between we're choosing one

**[10:14]** of many NCBS and then we answer back and

**[10:16]** we give it to the user so there's not a

**[10:18]** lot of planning the plan is call one SCP

**[10:22]** right now I think it actually gets a

**[10:23]** little more complicated uh when you

**[10:26]** start getting the planning goal steps

**[10:27]** and I'm not we're not going to go down

**[10:29]** that path right now because I think

**[10:30]** that's just too much for what we have to

**[10:32]** cover but

**[10:34]** Where does memory come in? You're going

**[10:36]** to you're going to let's say we have

**[10:39]** four options. So we got some planning.

**[10:41]** Okay. Um you know uh two MCPs you can

**[10:46]** call one or the other or both in options

**[10:49]** order. So that's four. Right. Somebody

**[10:52]** asked a question.

**[10:55]** I was going to bring up the image. I

**[10:57]** forgot bring it up. There's any um what

**[11:00]** where the different where where does

**[11:02]** memory play a role in this this uh this

**[11:07]** workshop with

**[11:09]** >> I think this way

**[11:13]** gives the agent the answer to what it's

**[11:16]** looking for but makes it remember what

**[11:21]** it's supposed to know.

**[11:24]** Um and what I mean by that is I think in

**[11:28]** this diagram memory will come somewhere

**[11:32]** uh where

**[11:33]** >> there's the question.

**[11:35]** >> Yeah. So memory will come somewhere here

**[11:39]** as

**[11:40]** >> right when the question is asked.

**[11:42]** >> Yes. Right after the question is asked,

**[11:44]** the agent will go look into the memory

**[11:47]** to find relevant details. And once it

**[11:50]** finds relevant details, that query will

**[11:52]** be augmented with all of the relevant

**[11:54]** details. So that every response that you

**[11:58]** get from the agent, it's got context

**[12:00]** aware. So I think of it this way.

**[12:02]** >> Well, okay. So, so in this case, we're

**[12:04]** we're literally solving the problem of

**[12:06]** you ask question about AI, you have many

**[12:09]** projects. So somebody might ask which

**[12:12]** product somebody might say I'm a Python

**[12:15]** developer and I have used um this you

**[12:21]** know let's say the long index framework

**[12:24]** long index is one of our

**[12:26]** >> and so you would remember that

**[12:29]** >> yes so it the user will ask I'm a Python

**[12:33]** developer I have experience working with

**[12:36]** which tools that are part of AI lines

**[12:38]** can I use for this particular project

**[12:40]** that I'm working on and the RA will

**[12:43]** fetch relevant information from the

**[12:44]** knowledge base and give it an answer.

**[12:47]** The next time the user comes in the user

**[12:49]** won't have to tell he's a Python

**[12:52]** developer they worked with text or even

**[12:55]** the project that they worked on before

**[12:58]** the memory will remember everything. The

**[13:00]** user can just say something like where

**[13:02]** did we uh work on this last time? Let's

**[13:07]** pick it up. And the memory will remember

**[13:10]** what what what the user knows what the

**[13:13]** user has been working on the rag results

**[13:16]** that they looked at previously and they

**[13:20]** can just resume working from there. So

**[13:22]** with just rag every independent question

**[13:27]** is like a first date you make to you

**[13:28]** need to make all the introductions set

**[13:31]** up the context do everything for every

**[13:34]** rap query but with memory it's it just

**[13:38]** brings continuity context and relevance

**[13:40]** to every query

**[13:43]** >> yeah the way we built it so far is every

**[13:45]** single time you ask a question it thinks

**[13:48]** it's seniors the first time so I think

**[13:51]** your image that you showed earlier uh

**[13:53]** today there was it said shortterm and

**[13:55]** long term so shortterm would be what

**[13:58]** during this conversation remember some

**[14:01]** shortterm things like whenever I said I

**[14:03]** am a Python developer say oh you let's

**[14:07]** keep this information about you remember

**[14:09]** that about you right

**[14:10]** >> and then that information about the user

**[14:13]** will be saved in what we now call the

**[14:15]** profile memory but that just that saves

**[14:18]** things like user preferences

**[14:21]** uh what they like to in this case they

**[14:25]** prefer coding language uh the way they

**[14:28]** like sponsors from the rank chatbot

**[14:31]** things like that.

**[14:32]** >> Yeah. Um, and then in the longterm

**[14:34]** memory, we can store information like

**[14:37]** their progress so far in this project or

**[14:40]** some other project that they've worked

**[14:41]** on. The longterm relevance,

**[14:44]** >> right? For example, we're going to add

**[14:46]** uh events to our website and it might

**[14:49]** remember uh maybe you say uh you know at

**[14:52]** some point you say I I live in

**[14:56]** >> and then it would remember that. Yes.

**[14:58]** And then in the future you might ask you

**[15:00]** know what events are interesting today

**[15:02]** and it would know oh since you're in the

**[15:06]** local week and then also it say but

**[15:11]** this is one problem I love somebody oh

**[15:14]** since you're in you're in this time zone

**[15:16]** here are the online events that are

**[15:17]** appropriate for your

**[15:20]** right

**[15:23]** >> yeah so in this case the fact that The

**[15:27]** user does a counter view will be stored

**[15:29]** in the profile memory and then a tool

**[15:34]** an MCP tool that does web search and

**[15:38]** looks for all of these events can will

**[15:42]** then know what events to look for

**[15:44]** otherwise it will just look for all the

**[15:46]** events right but now with this

**[15:49]** information the result will be more

**[15:51]** enriched and relevant.

**[15:53]** >> Okay. All right. Well, that's I just

**[15:56]** wanted to kind of take you down that

**[15:58]** path because that's that's actually what

**[15:59]** we're doing right now as a a workshop is

**[16:01]** we're building out these steps so people

**[16:03]** can learn uh as they as we are basically

**[16:07]** and um and yeah and and just to give you

**[16:12]** a little taste of where we're going is

**[16:14]** we're trying to get this to the point

**[16:16]** where for deep research at least it's

**[16:19]** production ready like by the time the

**[16:20]** end of the workshop you are asking a

**[16:23]** series of questions And it's able to in

**[16:26]** in the use case that we're focused on

**[16:28]** first, it's you pass a financial

**[16:30]** instrument like stock symbol or

**[16:31]** something like that and it's going to go

**[16:33]** deep do you deep research on that uh

**[16:35]** item for just today like here's what's

**[16:38]** happening now. And then, you know, we

**[16:40]** would use a short-term memory for that.

**[16:43]** And then we can add the long-term memory

**[16:45]** for when they come back and ask

**[16:46]** questions about uh maybe another

**[16:50]** financial instrument that relates to

**[16:52]** that one or they ask about the same one

**[16:55]** contracts and say, well, the market has

**[16:58]** changed since the last time you were

**[16:59]** here.

**[17:00]** >> Um, yeah. So, we'll be doing that. And

**[17:02]** then where we plan to take this workshop

**[17:04]** is we want to go somewhere where

**[17:06]** nobody's selling yet where, you know,

**[17:08]** this is Silicon Valley. Right now, I

**[17:10]** feel like we're playing catch up in this

**[17:11]** workshop or where you want to go is

**[17:13]** where no people have gone yet. That is

**[17:16]** what if you do some deep research

**[17:19]** and um it comes back with a list of

**[17:21]** things that you're interested in and you

**[17:23]** just want it to go ahead and transact

**[17:24]** for you but you it comes back with a

**[17:28]** list of things that you've never thought

**[17:30]** of before, never heard of before and you

**[17:33]** just wanted to go ahead and go find

**[17:35]** another API or MCP or agent and just get

**[17:40]** the work done. Don't even come back and

**[17:42]** ask them, right? There will become a

**[17:45]** time probably in the next few years

**[17:46]** where that's that's a reality. A good

**[17:49]** example of this that something already

**[17:51]** started building is they want to buy

**[17:53]** gifts for people they know well because

**[17:56]** you're constantly doing this, right? I

**[17:57]** probably probably over 10 people in my

**[18:00]** life who every year running something

**[18:02]** and they know them really well. So every

**[18:04]** time you buy can remember these things

**[18:06]** and then you can just tell it like a

**[18:07]** concierge look just within this

**[18:10]** parameters just go buy it surprisingly

**[18:13]** you know these days you can return

**[18:15]** things pretty well so it's actually a

**[18:17]** much more like it could be more likely

**[18:19]** maybe that it can just go buy something

**[18:22]** it's more likely to save you time by

**[18:24]** just buying it uh and then on off chance

**[18:28]** it's not good enough you return it right

**[18:30]** now to worry about that but anyway those

**[18:32]** are kind of things where you know

**[18:33]** there's not a lot of danger. Another one

**[18:35]** that I'm personally very interested in

**[18:37]** is you want to go in like this and you

**[18:40]** want to uh find people that you are

**[18:42]** interested in, have a little chat with

**[18:44]** them or their bot maybe and then figure

**[18:48]** out, oh, looks like you really should be

**[18:51]** having a conversation. Let's just

**[18:52]** schedule a meeting like a short little,

**[18:54]** you know, five minute or 10 minute

**[18:56]** during lunch or something, right? Very

**[18:58]** low risk. It is doing a lot of high

**[19:00]** value work, right? So we want to take it

**[19:02]** that direction. Let agents actually

**[19:04]** figure out how to transact on your

**[19:05]** behalf and and and what does that look

**[19:08]** like? What are the challenges you have

**[19:10]** to overcome like trust and you know

**[19:14]** personal information all that kind of

**[19:15]** stuff. So that's where we will be going.

**[19:17]** I'm working with a guy named uh well two

**[19:19]** people suji man um who just gave a

**[19:22]** workshop at jon and then also Michael

**[19:26]** prince who is uh working on a project

**[19:29]** called matchwise

**[19:32]** so we're using their experiences to

**[19:33]** build this workshop we're not going to b


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
