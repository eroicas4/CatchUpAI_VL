# AI Memory for Team Collaboration - Bei Zhang

**원본 영상**: [https://www.youtube.com/watch?v=xMNfRmXICJI](https://www.youtube.com/watch?v=xMNfRmXICJI)
**작성일**: 2026-01-11
**Video ID**: xMNfRmXICJI

---

## 요약

Bei Zhang이 패밀리 오피스에서 탄생한 Tetra와 Evermem OS를 소개하는 발표입니다. 창업자들이 정보 과부하로 인해 제품 개발에 집중하지 못하는 문제를 해결하기 위해, 장기 메모리 기반의 AI 협업 도구를 개발하여 창업자들이 목적과 맥락을 유지하면서 효율적으로 업무를 수행할 수 있도록 지원합니다.

---

## 핵심 포인트

- 창업자들은 여러 플랫폼의 정보 처리에 과도한 시간을 소비하여 제품 개발에 집중하지 못함
- Tetra는 사용자의 의도와 목적을 이해하는 "목적 레이어(Purpose Layer)"로 작동
- 장기 메모리를 통해 과거 대화와 문서를 자동으로 기억하고 맥락을 유지
- Evermem OS라는 독자적인 메모리 시스템을 개발하여 Tetra의 핵심 엔진으로 활용
- 스탠ford, Berkeley 등의 초기 창업자들을 타겟으로 서비스 제공
- Evermem Bench라는 실제 업무 환경에 가까운 새로운 벤치마크 개발 중

---

## 주요 내용

### 섹션 1: 배경 및 문제 정의
- 패밀리 오피스에서 스탠ford, Berkeley, CMU 등의 창업자들을 지원하며 공통 문제점 발견
- 창업자들이 여러 플랫폼의 정보 과부하로 인해 제품 개발에 집중할 시간 부족
- 투자자들도 수천 개의 프로젝트 정보가 산재되어 최적의 투자 결정을 내리기 어려움
- 기존 AI 도구들은 작업 실행은 잘하지만 "왜" 하는지 목적을 이해하지 못함

### 섹션 2: Tetra의 솔루션
- 창업 생태계의 "목적 레이어(Purpose Layer)"로 포지셔닝
- 사용자의 역할과 의도를 이해하고 여러 도구와 사용자 사이에서 메모리를 유지
- 일대일 및 일대다 커뮤니케이션 도구로 설계
- 명령을 기다리는 것이 아니라 능동적으로 맥락을 이해

### 섹션 3: 실제 사용 사례

**사례 1: PR 작업 재개**
- 몇 달 전 진행했던 PR 프로젝트를 5시간이 아닌 5초 만에 재개
- 과거 문서와 대화 내용을 자동으로 검색하여 맥락 제공
- 출처 참조 기능으로 정보의 근거 확인 가능

**사례 2: 주간 업무 마무리**
- 금요일 퇴근 전 미완료 작업을 자동으로 정리
- 이메일과 대화 내용을 분석하여 중요 항목 요약
- 최고운영책임자(Chief of Staff) 역할을 AI가 대신 수행

**사례 3: 글로벌 팀 협업**
- 다른 시간대의 동료 메시지에 대한 답변 초안 자동 작성
- 사용자의 맥락과 목적을 이해하여 적절한 응답 생성
- 2시간 걸리던 업무를 3-5분으로 단축

### 섹션 4: 기술적 기반
- Evermem OS라는 독자적인 메모리 시스템 개발
- 최근 Tetra에서 분리하여 Evermem이라는 별도 브랜드로 출시
- 기존 벤치마크의 한계(수백 개 대화만 테스트)를 인식
- Duke University와 협력하여 수만 개 대화를 다루는 Evermem Bench 개발 중

### 섹션 5: 향후 계획
- Stanford, Berkeley의 초기 창업자들을 주요 타겟으로 설정
- VC 파트너들과 협력하여 창업자-투자자 간 커뮤니케이션 지원
- 자금 조달 및 시장 진출 관련 기능 추가 예정
- Evermem.ai를 개발자들에게 오픈소스로 제공 (GitHub)
- 애플리케이션과 개발자 도구 양쪽 모두에서 커뮤니티 피드백 수집 중

---

## 타임라인

- **00:00**: All right. Good morning. Morning. Uh, hi everyone. My name is F from KA and Ever. Uh, thank you. Thank you Charles and Frank for inviting me. Uh, great great to be here telling about our product and our technology underneath. Uh, so the topic of the conversation is a persistence of memory and purposeful action. uh and I will get into on what what it really means. Um so uh a little context about um our company is born out of the family office. Uh inside the family office uh we do a lot of investments. uh we curate a lot of startups and we work very closely with founders from Stanford, from Berkeley or from CMU, from all over the places and helping the young brave, the most brave uh the the most ambitious founders to be successful and helping them to go from ideas to business plan and to get funded as as fast as possible. So in in between uh we have we have been we have been witnessing a lot of struggles for the founders right. So when the founders switching roles whether from school to the founders directly or whether from a big tech W2 job into a funer directly uh almost all the time uh the absolute overload of information is uh is occupying their attention very extensively because that's where we've seen the uh super super intelligent thunders getting spending majority of the time um processing all different information from different platforms and they go out speaking to the investors, speaking to the the the mentors and which leave them very little time to actually building the product. Right? So this is and the outcome is a lot of the companies we've been curating, we've been investing that the progress has been uh not as fast, right, as the result it would be and uh will post a huge stress to to prevent integration to become actual functioning product. Um and this also applies in other ways too right as a as a investors as a as a enablers in the ecosystem we're also...
- **05:00**: uh because uh my role is more on the product build um so I'll focus on a few use cases because to to us it's a less less less about scores it's more about user experience. So if I jump right into a few actual use cases, we're trying to curate our tool too. Uh the the first one is for myself. Uh so when I've been I've been working with the company for a bit and we've been we've been working on the PR project uh continuously. Uh so this is where I I've spent months uh building the PR article uh with KA. So when I want to come in um I just uh ask the guy hey let's it's time for the next milestone right so we got to work on the next round of the PR because so many so many technical challenges have been solved and I want to make sure right we incorporate our latest update into the next version of the PR announcement. So normally if I work with any other other tools I would definitely end uploading a documents right all the historical articles or leas and that's been difficult because we have so many papers in between and uh and a lot of the building information are not even in the paper they're embedded into the conversations uh so in this case because because the documents are already down between me and uh and also as a as a collaboration tools all the conversations are already happening within the platform. So I don't I don't need to feel any of the problem. I just ready to get ping ping tank. Hey, right. Let's recap our work so far. We jump right into the next phase. So this is where this is this is where the uh the temp is capable of searching the historical information was high fidelity and then and also with the reference where where the information come from if I need to recall myself to come from too and that's where I'm I'm able to go from where we left off probably two months back right into the next in five seconds as opposed to five hours just just trying to get all the docets sorted...
- **10:00**: move very quickly on pushing things forward rather than looking things backward. Right. just to just to put a few things out here uh for example uh as examples on how we are trying to apply this long-term memory into the key applications. So going forward this is just the beginning of the journey also this has been an internal tool for a bit uh I was standing with uh Charles and we just went to market uh earlier this year and so far we've been hyper focused on putting the tool out for the early stage founders right we're we're we're team out with the Stanford and the Berkeley to let the uh the uh future founders apply the tool so that they can stay focused on what they're building rather than being distracted into different things and and furthermore we're we're also teaming up with the right people experts. Uh so because we do believe is a world of a hybrid business tool can only go so far. uh and in order to in order to get the founders to be more successful, we're also teaming up with our VC partners, right? Making sure as a young founders starting their company, we not only get get the ideation to the product very fast, but we also want to take a step further to say how we can how we can empower conversations like this between the founder and the investors, right? And founder with all the consultants to get the funded fast. So more to come but uh definitely give us a follow uh to stay tuned for more of early stage fun related features. So uh well we have a full team of technical experts here. So I I will uh I won't go too deep into the technical aspect to it. Um well the reason the reason we achieved the long-term memory and the function within attack is because we we have our own prop proprietary system called ever met OS with behind behind the scenes and uh recently we call this we p we split this out of the Tekk to be a separate...
- **15:00**: I uh try it out uh and uh leave us any comments. All right. Thank you. Thank you again for inviting. Thank Thank you very much....

---

## 전체 자막 (타임스탬프 포함)

**[00:07]** All right. Good morning. Morning. Uh, hi

**[00:10]** everyone. My name is F from KA and Ever.

**[00:14]** Uh, thank you. Thank you Charles and

**[00:15]** Frank for inviting me. Uh, great great

**[00:18]** to be here telling about our product and

**[00:20]** our technology underneath. Uh, so the

**[00:24]** topic of the conversation is a

**[00:26]** persistence of memory and purposeful

**[00:28]** action. uh and I will get into on what

**[00:32]** what it really means. Um so uh a little

**[00:36]** context about um our company is born out

**[00:39]** of the family office. Uh inside the

**[00:42]** family office uh we do a lot of

**[00:44]** investments. uh we curate a lot of

**[00:46]** startups and we work very closely with

**[00:49]** founders from Stanford, from Berkeley or

**[00:52]** from CMU, from all over the places and

**[00:54]** helping the young brave, the most brave

**[00:57]** uh the the most ambitious founders to be

**[01:00]** successful and helping them to go from

**[01:02]** ideas to business plan and to get funded

**[01:05]** as as fast as possible. So in in between

**[01:10]** uh we have we have been we have been

**[01:12]** witnessing a lot of struggles for the

**[01:14]** founders right. So when the founders

**[01:16]** switching roles whether from school to

**[01:18]** the founders directly or whether from a

**[01:21]** big tech W2 job into a funer directly uh

**[01:25]** almost all the time uh the absolute

**[01:27]** overload of information is uh is

**[01:31]** occupying their attention very

**[01:33]** extensively because that's where we've

**[01:34]** seen the uh super super intelligent

**[01:38]** thunders getting spending majority of

**[01:40]** the time um processing all different

**[01:42]** information from different platforms and

**[01:45]** they go out speaking to the investors,

**[01:47]** speaking to the the the mentors and

**[01:49]** which leave them very little time to

**[01:51]** actually building the product. Right? So

**[01:54]** this is and the outcome is a lot of the

**[01:57]** companies we've been curating, we've

**[01:58]** been investing that the progress has

**[02:00]** been uh not as fast, right, as the

**[02:03]** result it would be and uh will post a

**[02:06]** huge stress to to prevent integration to

**[02:09]** become actual functioning product. Um

**[02:12]** and this also applies in other ways too

**[02:14]** right as a as a investors as a as a

**[02:17]** enablers in the ecosystem we're also

**[02:20]** we've also seen our investor friends uh

**[02:22]** reviewing thousands of projects every

**[02:24]** year and all the information are

**[02:27]** scattered around. So when they are

**[02:29]** asking hey why did you make why did you

**[02:31]** make the certain decisions back in time

**[02:33]** right and uh and uh are all the critical

**[02:37]** information being processed in order to

**[02:39]** make the most informed uh investment

**[02:41]** decision and often the the uh the the

**[02:45]** decision wasn't optimal. So, so that's

**[02:47]** why uh we decide

**[02:50]** thanks to a lot of the uh ex

**[02:53]** distinguished scientists we've been

**[02:55]** working with, we decide to tackle this

**[02:56]** problem within. So, that's where we we

**[02:59]** build a tetra

**[03:01]** uh to be the purpose layer of the the

**[03:05]** thunder ecosystem.

**[03:07]** So, uh this is where we we're we're

**[03:12]** doing we are focusing on the specific

**[03:14]** vertical, right? So we we as a as a part

**[03:16]** of the family office we want to we want

**[03:19]** to drive more success to the founders.

**[03:21]** So we build this tank up to be both of a

**[03:23]** oneonone and one to many communication

**[03:25]** tools and in this case we let the we let

**[03:29]** the tank understand the ro awareness uh

**[03:31]** the moment we get engaged with the tool

**[03:34]** and uh as the users starting to get more

**[03:38]** involved into the conversation we make

**[03:40]** sure that tank AI understands the intent

**[03:44]** or the purposes right because the the

**[03:46]** situation today as our friend uh from uh

**[03:51]** Cameron laid out if we if we operate our

**[03:54]** business in different platforms often

**[03:57]** the single platform are very good at

**[03:59]** executing the mission uh but the

**[04:02]** founders often have a longer term

**[04:04]** mission right so if we what's what's

**[04:07]** missing out there is you got a 10 tool

**[04:10]** you got a 15 tools that can execute your

**[04:12]** your task very precisely but none of

**[04:15]** them knows why you're doing it right all

**[04:17]** of them are waiting for you to give the

**[04:19]** command

**[04:20]** And but if you're not given the command,

**[04:22]** you're often the founders are often

**[04:25]** buried into well where where should I

**[04:28]** start, right? The the uh and even even

**[04:32]** if you're you're working with the most

**[04:34]** intelligent uh AI tools, you you still

**[04:37]** would end up uh spending all the time

**[04:39]** typing all the prompts just because

**[04:41]** we're switching a different platform. So

**[04:43]** we're we're positioning our tank a to be

**[04:45]** the purpose layer because we want to

**[04:47]** apply this techa in between the tools

**[04:50]** you're using and your own brain just so

**[04:52]** the tank remembers you and carry over

**[04:55]** through the execution uh process. So

**[04:58]** just to show uh I'll be very brief here

**[05:02]** uh because uh my role is more on the

**[05:03]** product build um so I'll focus on a few

**[05:06]** use cases because to to us it's a less

**[05:09]** less less about scores it's more about

**[05:11]** user experience. So if I jump right into

**[05:14]** a few actual use cases, we're trying to

**[05:17]** curate our tool too. Uh the the first

**[05:20]** one is for myself. Uh so when I've been

**[05:23]** I've been working with the company for a

**[05:25]** bit and we've been we've been working on

**[05:27]** the PR project uh continuously. Uh so

**[05:31]** this is where I I've spent months uh

**[05:34]** building the PR article uh with KA. So

**[05:37]** when I want to come in um I just uh ask

**[05:42]** the guy hey let's it's time for the next

**[05:45]** milestone right so we got to work on the

**[05:46]** next round of the PR because so many so

**[05:49]** many technical challenges have been

**[05:51]** solved and I want to make sure right we

**[05:53]** incorporate our latest update into the

**[05:56]** next version of the PR announcement. So

**[05:59]** normally if I work with any other other

**[06:02]** tools I would definitely end uploading a

**[06:04]** documents right all the historical

**[06:06]** articles or leas and that's been

**[06:08]** difficult because we have so many papers

**[06:10]** in between and uh and a lot of the

**[06:12]** building information are not even in the

**[06:14]** paper they're embedded into the

**[06:16]** conversations uh so in this case because

**[06:19]** because the documents are already down

**[06:21]** between me and uh and also as a as a

**[06:26]** collaboration tools all the

**[06:27]** conversations are already happening

**[06:29]** within the platform. So I don't I don't

**[06:31]** need to feel any of the problem. I just

**[06:33]** ready to get ping ping tank. Hey, right.

**[06:37]** Let's recap our work so far. We jump

**[06:39]** right into the next phase. So this is

**[06:41]** where this is this is where the uh the

**[06:44]** temp is capable of searching the

**[06:47]** historical information was high fidelity

**[06:50]** and then and also with the reference

**[06:52]** where where the information come from if

**[06:55]** I need to recall myself to come from too

**[06:58]** and that's where I'm I'm able to go from

**[07:00]** where we left off probably two months

**[07:02]** back right into the next in five seconds

**[07:05]** as opposed to five hours just just

**[07:08]** trying to get all the docets sorted

**[07:10]** Um

**[07:12]** so the next next use case will be uh

**[07:16]** well in a in a busy world right today

**[07:18]** Friday and normally what I do on Friday

**[07:20]** is uh before before I sign off I would

**[07:24]** like to make sure I check the box on on

**[07:26]** all the all I finished the tasks uh so

**[07:29]** this is where I I typically ask to say

**[07:33]** hey help me wrap up all the tasks I'm

**[07:35]** driving because I don't want to be

**[07:36]** anything unfinished before before I

**[07:39]** close to the computer. So, so this is

**[07:41]** this is where the the the platform is

**[07:44]** capable of searching understanding all

**[07:46]** the conversations and my emails and from

**[07:48]** different sources, right? Because

**[07:50]** because with the memory that there is a

**[07:53]** there is a good understanding of who I

**[07:55]** am and what I need to do uh and who is

**[07:58]** expecting certain things from me. So,

**[08:00]** this is where the uh uh my my assistant

**[08:03]** is capable of summarizing all the key

**[08:05]** items. Uh in this case, it's product

**[08:07]** release, right?

**[08:08]** PI alignment or with specific

**[08:10]** collaborators I need to pay attention

**[08:13]** before before I finish off the day. So

**[08:15]** this is normally would be done by roles

**[08:17]** like a default staff which I don't have

**[08:21]** and and uh and it tend to be a a huge

**[08:25]** time saver for for

**[08:29]** and the and the next one the the last

**[08:31]** one here is uh I want to share because

**[08:34]** because Tekka this is uh the

**[08:38]** collaboration is not just me versus the

**[08:41]** alo between me and my co-workers and the

**[08:43]** so we we are putting

**[08:45]** into the team environment and and

**[08:47]** specifically chose also I chose the case

**[08:49]** to be in English because it's a language

**[08:51]** I take uh so this is where because uh I

**[08:55]** wake up in the morning uh my co-workers

**[08:58]** get from a different time zone like the

**[09:00]** message actually I have a lot of

**[09:02]** messages from a different groups uh and

**[09:05]** I know the message was from eight hours

**[09:07]** ago so I want to keep my Jack my friend

**[09:10]** Jack hanging there also I'm also tied up

**[09:13]** on a few So I'm com because at this

**[09:16]** point after after putting my memory into

**[09:20]** this platform uh I'm comfortable

**[09:22]** delegating uh my own digital bubble to

**[09:25]** help me create this reply to my coworker

**[09:28]** Jack because there is a a full context

**[09:31]** on what I'm doing and what I'm doing

**[09:33]** with Jack. So I'm just while I'm

**[09:35]** catching up on other things uh I'm just

**[09:37]** letting AI help me draft the reply

**[09:40]** according to all the context and

**[09:41]** purposes behind the scenes. So in this

**[09:44]** case every every morning when I wake up

**[09:47]** right I don't I don't end up spending

**[09:48]** two hours just to catch up with all the

**[09:50]** global stuff. I typically will spend

**[09:53]** three to five minutes first let to drop

**[09:56]** the response for me and then I just need

**[09:58]** to confirm and press send just so I can

**[10:01]** move very quickly on pushing things

**[10:03]** forward rather than looking things

**[10:05]** backward. Right.

**[10:07]** just to just to put a few things out

**[10:09]** here uh for example uh as examples on

**[10:12]** how we are trying to apply this

**[10:15]** long-term memory into the key

**[10:17]** applications. So going forward this is

**[10:20]** just the beginning of the journey also

**[10:22]** this has been an internal tool for a bit

**[10:24]** uh I was standing with uh Charles and we

**[10:27]** just went to market uh earlier this year

**[10:30]** and so far we've been hyper focused on

**[10:33]** putting the tool out for the early stage

**[10:35]** founders right we're we're we're team

**[10:38]** out with the Stanford and the Berkeley

**[10:39]** to let the uh the uh future founders

**[10:42]** apply the tool so that they can stay

**[10:44]** focused on what they're building rather

**[10:46]** than being distracted into different

**[10:48]** things and and furthermore we're we're

**[10:51]** also teaming up with the right people

**[10:53]** experts. Uh so because we do believe is

**[10:55]** a world of a hybrid business tool can

**[10:58]** only go so far. uh and in order to in

**[11:01]** order to get the founders to be more

**[11:03]** successful, we're also teaming up with

**[11:04]** our VC partners, right? Making sure as a

**[11:07]** young founders starting their company,

**[11:09]** we not only get get the ideation to the

**[11:12]** product very fast, but we also want to

**[11:14]** take a step further to say how we can

**[11:16]** how we can empower conversations like

**[11:18]** this between the founder and the

**[11:19]** investors, right? And founder with all

**[11:21]** the consultants to get the funded fast.

**[11:23]** So more to come but uh definitely give

**[11:26]** us a follow uh to stay tuned for more of

**[11:29]** early stage fun related features.

**[11:34]** So uh well we have a full team of

**[11:36]** technical experts here. So I I will uh I

**[11:40]** won't go too deep into the technical

**[11:42]** aspect to it. Um

**[11:45]** well the reason the reason we achieved

**[11:47]** the long-term memory and the function

**[11:48]** within attack is because we we have our

**[11:51]** own prop proprietary system called ever

**[11:53]** met OS with behind behind the scenes and

**[11:57]** uh recently we call this we p we split

**[12:00]** this out of the Tekk to be a separate

**[12:02]** brand called Evernite so that's where

**[12:04]** the second brand is coming from and uh

**[12:08]** it it did achieve a pretty high score

**[12:11]** not as high as language presented by

**[12:14]** Charles. So, but we're working on it. Uh

**[12:17]** and in between we also realize even the

**[12:20]** local benchmark is pretty limited,

**[12:22]** right? It has a it's have the

**[12:24]** conversation in the in the scale of only

**[12:27]** hundreds whereas in real life right the

**[12:29]** the conversation can be tens of

**[12:31]** thousands. So while while we while we

**[12:35]** okay we we achieved some of the scores

**[12:37]** it's really just the very beginning of

**[12:39]** the journey. So in this case we're came

**[12:41]** out with our uh brand researchers from

**[12:44]** Duke University working on a much much

**[12:46]** more in-depth uh benchmark called

**[12:48]** Everman bench. Uh it is we're we're at

**[12:51]** the very very tail end of releasing the

**[12:54]** the score. So once it's out, I would

**[12:56]** like to invite all everyone in this room

**[13:00]** the Kai to see further use the more the

**[13:03]** benchmark that's more close to the real

**[13:05]** life interactions to evaluate right your

**[13:07]** framework and then see how we how we

**[13:10]** stack against each other right or or

**[13:12]** more importantly how how how your

**[13:14]** framework can solve the get a better

**[13:16]** accuracy and address your customer's

**[13:19]** problem right more accurately.

**[13:23]** Yeah. And uh and what's next? Uh so

**[13:27]** briefly uh as I as I mentioned uh we are

**[13:30]** we're a combination I'm I'm here

**[13:32]** representing proudly representing two

**[13:34]** brands. Uh uh we're here right in the

**[13:37]** center of the Silicon Valley and for for

**[13:40]** Tanka uh we are we will go much much

**[13:43]** deep to help the native funders to be

**[13:45]** more successful. So uh yeah give us give

**[13:48]** us a follow. we will cut out more

**[13:50]** features and the functions towards the

**[13:52]** fundraising and go to market uh around

**[13:55]** this uh this application. U the line is

**[13:59]** still fairly new uh it just went online

**[14:03]** a few weeks ago. So thanks thank you

**[14:05]** thank thank you everyone who have

**[14:06]** already checked out the the the source

**[14:09]** the GitHub will continue to update

**[14:11]** itself. Uh definitely give it a try uh

**[14:14]** and see if it powers any of your agent

**[14:17]** tools.

**[14:21]** So uh and last uh that's that my uh join

**[14:24]** us. I welcome everyone to join us to

**[14:26]** explore the memory journey. Uh both on

**[14:29]** the application side we think this is

**[14:30]** still very early uh in the in the use

**[14:33]** cases. So if if you're a user uh you

**[14:36]** want to try it out how the long-term

**[14:38]** memory can deals differently compared to

**[14:41]** the other tools you're using you you

**[14:43]** feel free to try out and please give us

**[14:45]** any any thoughts and feedbacks right if

**[14:47]** you've seen any any function or any of

**[14:50]** the key features missing there I'm more

**[14:53]** years uh and separately right if you're

**[14:56]** a developer uh definitely give a follow

**[14:58]** to everm.ai

**[15:00]** I uh try it out uh and uh leave us any

**[15:04]** comments.

**[15:06]** All right. Thank you. Thank you again

**[15:07]** for inviting. Thank Thank you very much.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
