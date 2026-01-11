# Additional presentation 1

**원본 영상**: [https://www.youtube.com/watch?v=jgKJGdhWzkE](https://www.youtube.com/watch?v=jgKJGdhWzkE)
**작성일**: 2026-01-11
**Video ID**: jgKJGdhWzkE

---

## 요약

TiDB 데이터베이스 회사 창립자인 Ed가 AI 에이전트 간 협업을 위한 새로운 접근 방식을 제시합니다. 그는 파일 시스템을 통합 인터페이스로 사용하여 여러 AI 에이전트가 협업할 수 있는 오픈소스 프로젝트 AGFS(Agent File System)를 소개하며, Unix 철학의 "모든 것은 파일이다"라는 개념을 현대 AI 에이전트 아키텍처에 적용합니다.

---

## 핵심 포인트

- 현재 AI 코딩 에이전트는 순차적 작업 방식의 한계가 있으며, 다중 에이전트 협업 플랫폼이 필요함
- 파일 시스템을 통합 인터페이스로 사용하면 에이전트 간 협업이 단순하고 효율적으로 구현 가능
- Plan 9 운영체제의 "모든 것은 파일" 철학에서 영감을 받음
- AGFS 오픈소스 프로젝트를 통해 Queue, SQL, S3 등을 파일 시스템으로 추상화
- 벡터 데이터베이스보다 원시 데이터(raw data)가 더 효과적일 수 있음

---

## 주요 내용

### 섹션 1: 발표자 소개 및 배경
- Ed는 1990년대부터 프로그래밍을 시작한 베테랑 엔지니어
- TiDB(관계형 트랜잭션 데이터베이스) 창립자로, 현재도 50% 시간을 코딩에 할애
- TiDB는 Databricks, GitHub 등에서 사용되는 미션 크리티컬 데이터베이스
- 최근 클라우드 데이터베이스 인스턴스의 90%가 AI 에이전트에 의해 생성됨

### 섹션 2: 현재 AI 에이전트의 문제점
- 대부분의 코딩 에이전트(Claude, Cursor 등)는 순차적 작업 방식
- 사용자가 계속 승인(approve)해야 하는 구조
- 미래 비전: 복잡한 작업을 에이전트 팀에 맡기고 며칠 후 결과를 받는 방식
- 현재 병목: 다중 에이전트 협업 플랫폼 부재

### 섹션 3: 문제의 원인과 해결책
- 너무 많은 서비스 API와 기술이 존재 (Memory Machine 등)
- AI 에이전트가 모든 것을 학습하기 어려움
- 해결책: 파일 시스템을 통합 인터페이스로 사용
- 좋은 설계는 항상 단순한 설계 (seasoned engineer의 경험)

### 섹션 4: 파일 시스템의 장점
- 1990년대 초반에는 GUI 없이 셸 스크립트와 파이프라인으로 작업
- Unix 파이프라인과 셸 스크립트는 강력한 컴포넌트 결합 도구
- 에이전트 구축 패턴 예시: observation 파일 → LLM → 메모리 업데이트 → 데이터베이스 저장
- 파일 시스템은 앱에게 가장 친숙한 인터페이스

### 섹션 5: Plan 9 운영체제의 영감
- Plan 9은 "모든 것은 파일"이라는 Unix 철학을 극단적으로 구현
- 1990년대 초반에 이미 파일 시스템 인터페이스로 컴퓨터 간 협업 시도
- Compute-Storage Separation 개념을 선구적으로 도입
- 예시: HTTP 브라우징을 특수 파일로 읽고 쓰는 방식
- Linux VFS도 이 아이디어를 차용

### 섹션 6: 파일 시스템 방법론의 이점
- **통합 인터페이스**: Anthropic의 경험에 따르면 bash 스크립트나 로컬 파일 시스템이 벡터 데이터베이스보다 효과적
- **원시 데이터의 우월성**: 임베딩 데이터보다 raw data가 더 나은 품질 제공
- **조합성(Composition)**: 다양한 도구를 단순하게 결합 가능
- **간결성(Concision)**: 최소한의 코드로 강력한 기능 구현
- **분산 환경**: 블록 스토리지나 클라우드를 통해 쉽게 분산 환경 구축
- **LLM과의 호환성**: 최신 LLM은 뛰어난 셸 프로그래머

### 섹션 7: AGFS 프로젝트 소개
- AGFS = Aggregated File System 또는 Agent File System
- 다양한 서비스를 추상화된 파일 시스템 API로 통합
- 다중 에이전트 협업 프레임워크 구축용 오픈소스 프로젝트
- Unix/Linux 명령어를 포함한 간단한 셸 제공
- 몇 주 전에 시작한 신규 프로젝트

### 섹션 8: AGFS의 구성 요소들
**1. QueueFS (큐 파일 시스템)**
- 알림이나 메시지 전송 패턴 지원
- 디렉토리 생성 후 파일에 내용을 echo하여 메시지 전송
- cat 명령으로 dequeue 작업 수행

**2. S3FS**
- S3 버킷을 파일 시스템으로 마운트
- 모든 Unix 파일 도구 사용 가능

**3. SQLFS (SQL 데이터베이스를 파일 시스템으로)**
- 구조화된 데이터 필요시 사용
- 특수 파일에 쿼리를 작성하여 데이터베이스 탐색
- 계층적 파일 시스템 구조로 데이터베이스 브라우징
- INSERT JSON 등의 헬퍼 파일 제공

### 섹션 9: AGFS 활용 패턴들

**패턴 1: Message Queue 패턴**
- QueueFS를 사용한 에이전트 간 메시지 큐
- 세부 구현 설명은 생략되었으나 직관적인 구조

**패턴 2: Task Distribution (작업 분배)**
- 수백 개의 Claude Code 인스턴스 실행 가능
- 각 에이전트가 자신의 디렉토리 감시
- 코디네이터가 팀에 새 작업 전송

**패턴 3: Heartbeat/Keep-Alive**
- HeartbeatFS 시스템 구현
- 에이전트가 살아있으면 제어 파일을 touch
- 4줄의 코드로 하트비트 패턴 구현
- 에이전트 생존 여부 자동 확인

**패턴 4: Shared Memory**
- 별도의 메모리 프레임워크 불필요
- S3의 계층적 디렉토리를 메모리로 사용

**패턴 5: Parallel Research (병렬 연구)**
- 이전 빌딩 블록들을 모두 활용
- MapReduce 프레임워크 쉽게 구축
- 다수 에이전트와 대규모 협업 연구 가능

### 섹션 10: 고급 기능

**CrossFS (크로스 파일 시스템)**
- 여러 AGFS를 체인으로 연결
- 페더레이션(federation) 구성 가능

**StreamFS**
- Ring buffer 사용
- 흥미로운 유스케이스 구현 가능
- 스트리밍 데이터 처리

### 섹션 11: 결론
- 전체 프로젝트는 오픈소스로 공개
- 파일 시스템을 통한 에이전트 협업의 새로운 패러다임 제시
- 단순함과 강력함의 조합
- 컴퓨터 역사 박물관에서 발표한 것이 의미있는 이유: 과거의 지혜를 현대 AI에 적용

---

## 타임라인

- **00:00**: Okay. >> Okay. Well, um, hello everyone. It's really here to share. Yeah. Today I'm not going to talk about the database. Um, but I'm the founder of a database company. Uh, that actually used companies. Um, but then I'm going to talk about some my own experience about being a web platform. I think that would be more interesting. Um, a little background about myself. Uh, my name is Ed. I'm a seasoned engineer. I start programming since early 90s. That really related to today my my topic. Um, so yeah. Um, as a as a founder of a startup company, I still have like 50% of my time still writing it. So I'm super proud about that. Yeah, you can find me in uh okay uh a little bit background about uh my marketing team me is uh relational transactional database uh they actually you know you can consider it's a bigger and better postgress or my cloud so you can uh but most of can be used in the most extreme and most mission critical scenarios like go banking system or super extreme scale like billions or billions of rows and millions of uh you know transaction per second we find something like that. So uh it's a very important uh mission critical database infrastructure. So it's widely used in a lot of companies. Uh so basically every day uh if you are logging into the internet you basically uh maybe using V. Okay. So uh one of our famous customer and user is is data bricks. Um actually type is supporting mo basically 100% of their metadata system. So every time you run stuff on data bricks you actually you know supported part of this transaction supported by okay so uh this is the founder sharing you know how data bricks love okay [clears throat] um and oh sorry also what another customer is because I'm an engineer I also super proud of that is...
- **05:00**: go back to the uh go to sleep and three days later it my my agent team uh just you know stop their work it's like a you know operating system but if we want to achieve this goal we will found that the actual bottleneck is we don't have a collaboration collaborating platform for multiple agent. I'm I'm seeing like thousands of agent uh or like even more. Okay. But when because you know today the big problem is um we have so many different type of u service API technology you know today uh for example like memory machine is a is a good product but expose their own API is a new uh ecosystem and it is so I think today we have too many technologies too many companies in that too many things. So it is really hard for the AI agent to learn everything because you know it is um the the just have too too too many things. So you know I think today we are in a perfect place to share the my the idea I'm going to introduce in the following slides because we are in a computer history museum. Um and we have this uh problem but I see this problem already solved in you know in the Asian base and uh you know also as my as a seasoned engineer I think most of time the good design is always the the simple design and um what I'm going to say is that maybe we can use a file system as the unified and ultimate interface for uh you know all the agent to collaborating to you know share the memory or you know like uh using different patterns but uh all built with the the idea of the file system because I think file system is the most friendly interface for apps and you know if we talk about the file system Why fail system is so powerful? Uh because you know I started programming since early early 19s at that time we don't even have a you know GUI...
- **10:00**: already and but you know in the uh early 90s they plan already have a very ambitious goal. Uh they want to use a file system interface to you know collaborate like different uh computer together. You know I I today I look at this architecture is well it is like a uh you know I'm a database director uh recently in the develop uh in the database world there's a philosophy called uh compute storage separation uh you know this is uh nice already introduced this in uh decades ago so yeah and here's an example uh if you want to browse uh to to to uh surf the internet uh in plan 9 you have to do that um you you need to catch the the HTTP part to the special file and read the the output from another another file. So you know this is the uh example for um you know uh the cur uh to to to uh to access the HTV server just like this. Okay. So Linux VFS uh is they borrowed this idea and create a VFS. So uh if today you you're delivering the the new file system for for Linux uh basically you need to follow this uh API but I would say this ideas actually comes from the the plan I think. Okay why it matters uh I think the the benefit of this methodology is is very uh obvious. Um first unifi interface today if you want to create a new tool uh for the agent you know I I think uh if you read the recent blog posted by a uh publish shared experience about context engineering for cloud code uh you you can you can find uh they they found that oh using simple bash uh script like uh or bash tool like graph uh or using uh you know back in the the the local file system you actually have a really good uh you know quality compares to putting everything into the vector database. So raw data is actually better than embedding data. This is my my my sense you know I I'm not uh quite understand...
- **15:00**: different um cooks why not I can I create the abstract file system API like plan I um so I a couple weeks ago I started new open source project called HS um and open source uh you can you can say the a means aggregated and also means uh agent file system. So um I will share some you know example about how to use this file system to create a multiple agent collaboration framework. Um for example I I I will share some building FS uh in in my AGFS. Uh the first is uh Q and SQL X3 and hub. Okay. uh in the right side there's some you know uh I also created a simple uh cell for this uh file system uh that uh this cell included some building commands like uh if you're a Unix or Linux developer you will yeah it's like every day to you're using okay some examples you know there's a it's a pattern that uh you know the traditional So a file system doesn't support something like notification or you want to notify another user hey there's something new. Uh so that I I created pure SFL system uh to make uh FS to support uh the pattern like the notify or sending uh message. Um so yeah it's quite it's quite straightforward. So you can uh in this subsystem you just simply um create a new directory and uh oh sorry create a directory and uh echo or cat the file contents to uh your your ch directory and for the dq operation you can simply cat the the name the decco file and you can add the message [clears throat] is is very important. You can mount your three bucket as a factor. So that you can and then you can use all the Unix uh files you like. Yeah, it's just simply mapping the S3 bucket into the FS. Well, this doesn't really SQL database as FS. So because you know sometimes we still need to have some structure of the data uh and I create this file system uh for...
- **20:00**: very common pattern in the distributing system which is how to keep you know the the agent how do you know the the agent is still alive. So I created a new uh I created a system called hardware fs. So if you are still alive you can uh just touch your directory the control file and yeah if you are not alive anymore the the file system will do the thing by itself. So that um yeah if you use just four lines of codes uh you you you can implemented the the the heartbeat or keep alive um uh pattern and the share memory is is quite straightforward. I don't even need to create another memory framework. I just use the memory as a hierarchy directory in the S3. Yeah. And yeah it is uh the parallel research it is a the pattern that using all the tools building block I share in the previous slides so that you can easily create some you know map reduce framework using this file system um to do some large scale research collaborating with the m agents um and I don't know if I have time but this so I not only uh the building for FS. I also created cross FS so that you can create multiple. You can use this cross FS to chain up uh different uh AGFS together to have a a federation. Yeah, it's quite funny. >> Yeah. Okay. Um and the last page uh I have uh I created the very interesting FS or stream FS and it is using the uh rim buffer. Uh you know what I mean? Yeah. To improve this some very interesting use case like this. Okay. Um this is all I going to share. Um so yeah this and this project is open source. Okay. Thank you....

---

## 전체 자막 (타임스탬프 포함)

**[00:01]** Okay.

**[00:04]** >> Okay. Well, um, hello everyone. It's

**[00:07]** really here to share. Yeah. Today I'm

**[00:09]** not going to talk about the database.

**[00:12]** Um, but I'm the founder of a database

**[00:14]** company. Uh, that actually used

**[00:18]** companies. Um, but then I'm going to

**[00:21]** talk about some my own experience about

**[00:23]** being a web platform.

**[00:28]** I think that would be more interesting.

**[00:30]** Um, a little background about myself.

**[00:34]** Uh, my name is Ed. I'm a seasoned

**[00:37]** engineer.

**[00:39]** I start programming since early 90s.

**[00:41]** That really related to today my my

**[00:44]** topic. Um, so yeah. Um, as a as a

**[00:48]** founder of a startup company, I still

**[00:50]** have like 50% of my time still writing

**[00:53]** it. So I'm super proud about that.

**[00:57]** Yeah, you can find me in uh

**[01:01]** okay uh a little bit background about uh

**[01:05]** my marketing team me

**[01:11]** is uh relational transactional database

**[01:15]** uh they actually you know you can

**[01:17]** consider it's a bigger and better

**[01:19]** postgress or my cloud so you can uh but

**[01:22]** most of can be used in the most extreme

**[01:25]** and most mission critical scenarios like

**[01:27]** go banking system or super extreme scale

**[01:31]** like billions or billions of rows and

**[01:34]** millions of uh you know transaction per

**[01:36]** second we find something like that. So

**[01:39]** uh it's a very important uh mission

**[01:42]** critical database infrastructure. So

**[01:44]** it's widely used in a lot of companies.

**[01:46]** Uh so basically every day uh if you are

**[01:49]** logging into

**[01:51]** the internet you basically uh maybe

**[01:55]** using V. Okay. So uh one of our famous

**[02:00]** customer and user is is data bricks. Um

**[02:03]** actually type is supporting mo basically

**[02:07]** 100% of their metadata system. So every

**[02:11]** time you run stuff on data bricks you

**[02:13]** actually you know supported part of this

**[02:16]** transaction supported by okay so uh this

**[02:19]** is the founder sharing you know how data

**[02:22]** bricks love okay

**[02:25]** [clears throat] um and oh sorry also

**[02:28]** what another customer is because I'm an

**[02:32]** engineer I also super proud of that is

**[02:35]** actually a big tidb user uh supporting

**[02:38]** their s platform

**[02:41]** Okay.

**[02:43]** Um and today I actually want to talk

**[02:46]** about the AI agent and uh uh and also

**[02:49]** you know provide the the agent database

**[02:51]** platform on the cloud. I would say that

**[02:54]** 90% of our new cloud database instance

**[02:58]** is casually created by AI agent not by

**[03:01]** human being not by the developer

**[03:03]** anymore. So one of the uh most famous

**[03:07]** customer of our agent database platform

**[03:10]** is actually manus minus uh using pb to

**[03:14]** uh to to build their full stack uh agent

**[03:17]** web autation service recently. So it's

**[03:20]** actually supporting near millions of you

**[03:23]** know database cloud already. So this

**[03:26]** crazy but you know the fact that today

**[03:29]** I'm not going to talk about the race I'm

**[03:31]** going to talk about the the AI agent

**[03:34]** intro

**[03:36]** >> um you know as an engineer um you know I

**[03:41]** I bet most of you and are using you know

**[03:44]** coding agent like cloud code cursor

**[03:46]** every day but the the big problem of

**[03:49]** today's uh you know coding agent is all

**[03:52]** most of the agents is the you know it's

**[03:57]** a sequential action for example like you

**[03:59]** ask a question the agent give you a

**[04:01]** feedback asking hey I'm going to do that

**[04:04]** do you approve you know basically 90% of

**[04:09]** uh in this case it's like we can only

**[04:12]** approve approve approve and get the

**[04:14]** result but I think my vision is that in

**[04:19]** in the future uh you know we can you

**[04:22]** know the agent will it is a multi- aent

**[04:26]** uh architecture so that you can just uh

**[04:31]** ask the agents or the team of agent to

**[04:35]** to do some really complicated job

**[04:38]** complicated tasks and you can go to

**[04:41]** sleep and the agent will collaborate and

**[04:45]** do their job do their work and maybe

**[04:48]** three days later uh they will give you

**[04:51]** all you need. For example, uh I I want

**[04:54]** you I want my to agent like hey can you

**[04:56]** help me to build a Linux kernel uh

**[04:59]** something like Linux kernel and I just

**[05:01]** go back to the uh go to sleep and three

**[05:05]** days later it my my agent team uh just

**[05:10]** you know stop their work it's like a you

**[05:12]** know operating system but if we want to

**[05:16]** achieve this goal we will found that the

**[05:19]** actual bottleneck is we don't have a

**[05:22]** collaboration

**[05:23]** collaborating platform for multiple

**[05:25]** agent. I'm I'm seeing like thousands of

**[05:28]** agent uh or like even more. Okay.

**[05:33]** But when because you know today the big

**[05:36]** problem is um we have so many different

**[05:40]** type of u service API technology you

**[05:43]** know today

**[05:45]** uh for example like memory machine is a

**[05:47]** is a good product but expose their own

**[05:51]** API is a new uh ecosystem and it is so I

**[05:58]** think today we have too many

**[06:01]** technologies too many companies in that

**[06:03]** too many things. So it is really hard

**[06:06]** for the AI agent to learn everything

**[06:09]** because you know it is um the the just

**[06:14]** have too too too many things. So

**[06:18]** you know I think today we are in a

**[06:20]** perfect place to share the my the idea

**[06:24]** I'm going to introduce in the following

**[06:26]** slides because we are in a computer

**[06:28]** history museum. Um

**[06:32]** and we have this uh problem but I see

**[06:35]** this problem already solved in you know

**[06:38]** in the Asian base

**[06:41]** and uh you know also as my as a seasoned

**[06:45]** engineer I think most of time the good

**[06:48]** design is always the the simple design

**[06:51]** and um what I'm going to say is that

**[06:55]** maybe we can use a file system as the

**[06:58]** unified and ultimate interface for uh

**[07:02]** you know all the agent to collaborating

**[07:06]** to you know share the memory or you know

**[07:10]** like uh using different patterns but uh

**[07:12]** all built with the the idea of the file

**[07:16]** system

**[07:18]** because I think file system is the most

**[07:21]** friendly interface for apps

**[07:25]** and you know if we talk about the file

**[07:28]** system Why fail system is so powerful?

**[07:32]** Uh because you know I started

**[07:35]** programming since early early 19s at

**[07:38]** that time we don't even have a you know

**[07:40]** GUI

**[07:42]** and we we we need to you know achieve

**[07:44]** everything by you know using uh cell

**[07:47]** scripts and the pipeline to combine

**[07:50]** different uh tools together. But I think

**[07:53]** this idea is actually you know uh become

**[07:57]** very valuable in today's context. For

**[08:00]** example uh this is the minimal and very

**[08:04]** powerful

**[08:05]** um pattern for building the agent just

**[08:08]** just like this. For example it's like uh

**[08:11]** if we store all the observation and

**[08:14]** context in the in the file like for uh

**[08:17]** the name is observation. We c this file

**[08:20]** and it show the content of this file and

**[08:23]** send it to large language model with the

**[08:26]** context of the memory in this file

**[08:29]** system in another directory. And uh the

**[08:33]** error syncing will output the uh the

**[08:37]** content and send it to you know update

**[08:40]** in into the short memory and also insert

**[08:43]** to the database uh to store the the

**[08:46]** conversation history and the action will

**[08:50]** send to the uh execut in another step.

**[08:55]** So it is um you know just like I said

**[09:00]** the Unix pipeline and the cell script is

**[09:02]** a really good uh tool to combining

**[09:06]** different components together in the

**[09:08]** unified interface.

**[09:11]** You know actually someone have already

**[09:14]** uh you know used this idea in decades

**[09:16]** ago.

**[09:18]** Any of you know this operating system?

**[09:21]** Oh yeah cool. I'm a big fan of bling bl

**[09:25]** and it's really interesting operating

**[09:27]** system that uh you know in the Unix

**[09:32]** philosophy you know there is a

**[09:33]** philosophy called everything is a file

**[09:36]** but you know the Linux or most of the

**[09:39]** Unix uh system um they they actually not

**[09:45]** following this principle very well but

**[09:47]** you know planer is uh you know this the

**[09:52]** embody this philosophy uh in a very

**[09:55]** extreme way. So yeah, I'm I'm a big fan

**[09:58]** of this OS but it is totally dead

**[10:01]** already and but you know in the uh early

**[10:06]** 90s they plan already have a very

**[10:08]** ambitious goal. Uh they want to use a

**[10:12]** file system interface to you know

**[10:15]** collaborate

**[10:16]** like different uh computer together. You

**[10:21]** know I I today I look at this

**[10:23]** architecture is well it is like a uh you

**[10:27]** know I'm a database director uh recently

**[10:29]** in the develop uh in the database world

**[10:32]** there's a philosophy called uh compute

**[10:35]** storage separation uh you know this is

**[10:39]** uh nice already introduced this in uh

**[10:43]** decades ago so yeah and here's an

**[10:46]** example uh if you want to browse

**[10:51]** uh to to to

**[10:54]** uh surf the internet uh in plan 9 you

**[10:57]** have to do that um you you need to catch

**[11:01]** the the HTTP part to the special file

**[11:04]** and read the the output from another

**[11:08]** another file. So you know this is the uh

**[11:12]** example for um you know uh the cur uh to

**[11:18]** to to

**[11:20]** uh to access the HTV server just like

**[11:23]** this.

**[11:25]** Okay. So Linux VFS uh is they borrowed

**[11:31]** this idea and create a VFS. So uh if

**[11:35]** today you you're delivering the the new

**[11:38]** file system for for Linux uh basically

**[11:41]** you need to follow this uh API but I

**[11:43]** would say this ideas actually comes from

**[11:45]** the the plan I think. Okay why it

**[11:49]** matters uh I think the the benefit of

**[11:52]** this methodology is is very uh obvious.

**[11:57]** Um first unifi interface today if you

**[12:02]** want to create a new tool uh for the

**[12:06]** agent you know I I think uh if you read

**[12:11]** the recent blog posted by a uh publish

**[12:15]** shared experience about context

**[12:17]** engineering for cloud code uh you you

**[12:21]** can you can find uh they they found that

**[12:25]** oh using simple bash uh script like uh

**[12:30]** or bash tool like graph uh or using uh

**[12:35]** you know back in the the the local file

**[12:38]** system you actually have a really good

**[12:40]** uh you know quality compares to putting

**[12:43]** everything into the vector database. So

**[12:45]** raw data is actually better than

**[12:48]** embedding data. This is my my my sense

**[12:52]** you know I I'm not uh quite understand

**[12:54]** why everyone is so you know uh uh you

**[12:59]** know uh think when when they talk about

**[13:02]** the the AI uh database the the first

**[13:06]** impression is vector database. Um but I

**[13:10]** I I think from my own experience most of

**[13:13]** the time the raw data is better than you

**[13:17]** know the turn all the data into the the

**[13:19]** the embedding data. So unify interface

**[13:23]** really important. The second thing is

**[13:26]** comp um composition. You know today we

**[13:31]** have so many tools um and every tool is

**[13:34]** really you know powerful but uh you need

**[13:40]** to teach the AI to learn a lot of thing

**[13:45]** uh about how to use that. So but you

**[13:48]** know uh the the the fast system API will

**[13:52]** solve this problem uh very elegant

**[13:56]** and also

**[14:00]** uh it's like you uh for example

**[14:05]** this is the example of concision

**[14:08]** you can combine uh different tools in

**[14:12]** the very simple uh way. Okay. And also

**[14:19]** today when we talk about the agent

**[14:21]** sandbox agent uh file system most of

**[14:24]** time the we are just talking about local

**[14:27]** storage. Um but I think with the help of

**[14:30]** block storage or the cloud database or

**[14:32]** the cloud storage you can easily create

**[14:34]** the you know distributed environment uh

**[14:38]** with a file system API. Okay.

**[14:42]** And the most important thing is today's

**[14:44]** LM is actually the excellent cell

**[14:47]** programmer. You know the file system

**[14:49]** just simply give them the ritual to to

**[14:51]** script.

**[14:53]** So with this um uh assumption so I'm

**[14:58]** thinking hey today we have so many

**[15:01]** different um cooks why not I can I

**[15:04]** create the abstract file system API like

**[15:07]** plan I um so I a couple weeks ago I

**[15:11]** started new open source project called

**[15:14]** HS

**[15:16]** um and open source uh you can you can

**[15:19]** say the a means aggregated and also

**[15:23]** means uh agent file system.

**[15:27]** So um I will share some you know example

**[15:30]** about how to use this file system to

**[15:32]** create a multiple agent collaboration

**[15:36]** framework. Um for example I I I will

**[15:39]** share some building FS uh in in my AGFS.

**[15:44]** Uh the first is uh Q and SQL X3 and hub.

**[15:50]** Okay. uh in the right side there's some

**[15:52]** you know uh I also created a simple uh

**[15:56]** cell for this uh file system uh that uh

**[16:01]** this cell included some building

**[16:04]** commands like uh if you're a Unix or

**[16:07]** Linux developer you will yeah it's like

**[16:09]** every day to you're using

**[16:12]** okay some examples

**[16:16]** you know there's a it's a pattern that

**[16:18]** uh you know the traditional So a file

**[16:21]** system doesn't support something like

**[16:24]** notification or you want to notify

**[16:27]** another user hey there's something new.

**[16:30]** Uh so that I I created pure SFL system

**[16:35]** uh to make uh FS to support uh the

**[16:38]** pattern like the notify or sending uh

**[16:42]** message. Um so yeah it's quite

**[16:48]** it's quite straightforward. So you can

**[16:51]** uh in this subsystem you just simply um

**[16:55]** create a new directory and uh oh sorry

**[17:02]** create a directory and uh echo or cat

**[17:06]** the file contents to uh your your ch

**[17:10]** directory and for the dq operation you

**[17:13]** can simply cat the the name the decco

**[17:18]** file and you can add the message

**[17:20]** [clears throat]

**[17:23]** is is very important. You can mount your

**[17:25]** three bucket as a factor. So that you

**[17:27]** can and then you can use all the Unix uh

**[17:30]** files you like. Yeah, it's just simply

**[17:33]** mapping the S3 bucket into the FS.

**[17:37]** Well, this doesn't really

**[17:40]** SQL database as FS.

**[17:42]** So because you know sometimes we still

**[17:45]** need to have some structure of the data

**[17:48]** uh and I create this file system uh for

**[17:52]** for this purpose. Um but you can but you

**[17:55]** can see you can catch some special file

**[17:59]** and you can browse um browse your

**[18:03]** database just like a hierarchy file

**[18:06]** system structure and you can send a SQL

**[18:09]** query to the control file and uh yeah

**[18:13]** and you can use like a uh just like a

**[18:15]** SQL database. Can you do select call?

**[18:18]** >> H sorry can you do select call? Yes.

**[18:21]** >> You can you can see uh this select and

**[18:24]** >> yeah I can also use in search.

**[18:29]** Yeah I also create some helper file like

**[18:33]** insert JSON. So my file system

**[18:36]** implementation will convert the season

**[18:38]** into the SQL uh statement. So yeah

**[18:42]** and using all of this file system above

**[18:47]** uh you can create some you know

**[18:48]** patterns. Uh for example I created NCB

**[18:53]** uh for this file system and uh uh this

**[18:57]** is the the the pattern notify. I will

**[19:00]** not dive into the details but it is

**[19:03]** quite straightforward just um you know

**[19:06]** using the the the QFS uh for the message

**[19:09]** Q for different agents and the second

**[19:12]** pattern is a fast move so that you can

**[19:15]** easily launch you know hundreds of cloud

**[19:18]** code instance and and then this cloud

**[19:21]** code instance will uh wash the their own

**[19:26]** directory so that uh the co uh

**[19:31]** coordinator send a new task to the to

**[19:36]** their team and the agent will will

**[19:39]** receive the the task. So this is uh

**[19:42]** another pattern. So using this pattern

**[19:44]** you can easily create some something

**[19:47]** like a wider research

**[19:50]** uh uh in the just like several lines of

**[19:54]** batch script. Okay.

**[19:57]** And the pattern three it is uh also a

**[20:00]** very common pattern in the distributing

**[20:02]** system which is how to keep you know the

**[20:04]** the agent how do you know the the agent

**[20:07]** is still alive. So I created a new uh I

**[20:11]** created a system called hardware fs. So

**[20:15]** if you are still alive you can uh just

**[20:18]** touch your directory the control file

**[20:22]** and yeah if you are not alive anymore

**[20:26]** the the file system will do the thing by

**[20:28]** itself. So that um yeah if you use just

**[20:33]** four lines of codes uh you you you can

**[20:36]** implemented the the the heartbeat or

**[20:39]** keep alive um uh pattern

**[20:43]** and the share memory is is quite

**[20:46]** straightforward. I don't even need to

**[20:47]** create another memory framework. I just

**[20:50]** use the memory as a hierarchy directory

**[20:54]** in the S3. Yeah.

**[20:58]** And yeah it is uh the parallel research

**[21:00]** it is a the pattern that using all the

**[21:03]** tools building block I share in the

**[21:06]** previous slides so that you can easily

**[21:08]** create some you know map reduce

**[21:10]** framework using this file system um to

**[21:13]** do some large scale research

**[21:16]** collaborating with the m agents

**[21:20]** um and I don't know if I have time but

**[21:24]** this so I not only uh the building for

**[21:29]** FS. I also created cross FS so that you

**[21:32]** can create multiple. You can use this

**[21:34]** cross FS to chain up uh different

**[21:39]** uh AGFS together to have a a federation.

**[21:44]** Yeah, it's quite funny.

**[21:47]** >> Yeah. Okay. Um and the last page uh I

**[21:51]** have uh I created the very interesting

**[21:55]** FS or stream FS and it is using the uh

**[21:59]** rim buffer. Uh you know what I mean?

**[22:02]** Yeah. To improve this some very

**[22:04]** interesting use case like this. Okay. Um

**[22:08]** this is all I going to share. Um so yeah

**[22:13]** this and this project is open source.

**[22:15]** Okay. Thank you.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
