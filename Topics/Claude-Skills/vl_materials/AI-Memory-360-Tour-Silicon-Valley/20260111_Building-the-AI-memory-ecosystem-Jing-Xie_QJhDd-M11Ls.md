# Building the AI memory ecosystem - Jing Xie

**원본 영상**: [https://www.youtube.com/watch?v=QJhDd-M11Ls](https://www.youtube.com/watch?v=QJhDd-M11Ls)
**작성일**: 2026-01-11
**Video ID**: QJhDd-M11Ls

---

## 요약

Memgraph의 부사장 Jing Xie가 AI 메모리 생태계 구축에 대해 발표하며, AI 시스템이 유용하게 작동하려면 좋은 메모리와 컨텍스트가 필수적이라고 강조합니다. ChatGPT 출시 3주년을 앞두고 AI의 초기 단계에서 오픈소스 프로젝트 Memgraph를 통해 커뮤니티 중심의 협력적 메모리 시스템을 구축하고자 하는 비전을 제시합니다.

---

## 핵심 포인트

- AI 시스템은 산소처럼 메모리와 컨텍스트를 필요로 하며, 이것이 없으면 유용한 작업을 수행할 수 없음
- Memgraph는 3개월 미만의 오픈소스 프로젝트로 이미 여러 성공적인 배포 사례를 보유
- 개방적이고 사람 중심적인 커뮤니티 문화를 통해 개발자들을 지원
- 프로필 메모리, AI 코치, 생산성 에이전트 등 다양한 실제 활용 사례 존재
- Discord 커뮤니티와 AI Memory Dev Alliance를 통한 협력적 개발 환경 제공

---

## 주요 내용

### 섹션 1: AI 빅뱅과 현재 상황
- ChatGPT 출시(2022년 11월 30일/12월 1일) 이후 약 3년이 되어가는 시점
- AI 발전 속도가 매우 빨라 전문가도 따라가기 어려운 상황
- 빅뱅 직후의 원시 수프(primordial soup)와 같은 혼돈스럽고 초기 단계
- 현재는 AI 생태계가 복잡하고 각 주체들이 여러 역할을 중복 수행 중

### 섹션 2: 메모리의 중요성
- AI 시스템은 메모리와 컨텍스트를 "호흡"함 (생명체의 산소와 같음)
- 좋은 메모리와 컨텍스트 제공 없이는 유용한 AI 시스템 구축 불가능
- 이것이 궁극적으로 좋은 AI를 만드는 핵심 요소

### 섹션 3: Memgraph 커뮤니티와 문화
- Discord 커뮤니티를 통한 실시간 지원 제공
- 개방적(open)이고 사람 중심적(people-centered)인 문화 추구
- 디지털과 오프라인 이벤트의 혼합 (해커톤, 교육 이벤트 등)
- 3개월 미만의 공개 오픈소스 프로젝트로 이미 여러 성공적 배포 사례 보유

### 섹션 4: 실제 활용 사례

**사례 1: Jenny Ouang (Build to Launch)**
- Substack 콘텐츠 크리에이터 (3,000명 이상 팔로워)
- AI 도구 구축 관련 콘텐츠 작성
- 프로필 메모리 기능을 활용해 자신의 글쓰기 스타일과 다른 작가들의 스타일 비교 분석
- 협업과 차별화를 위한 유사/상이한 목소리 발견에 활용

**사례 2: Brandon Monroe (Character Engine)**
- 창업자가 피칭 능력 부족을 경험한 후 AI 코치 개발
- Marcus Sterling이라는 AI 코치 캐릭터 생성
- 과도하게 친절한 ChatGPT와 달리 솔직한 피드백 제공
- 여러 세션에 걸쳐 사용자의 강점/약점과 진행 상황을 기억
- 개인화된 코칭 경험 제공

**사례 3: Teammate (협업 에이전트)**
- 팀 전체의 작업을 이해하는 AI 에이전트
- Slack 기반으로 시작하여 팀 협업 지원
- Memgraph를 장기 메모리 및 컨텍스트 레이어로 활용
- Memgraph 내부에서도 기술 프로그램 관리, 마케팅, 콘텐츠 작업에 사용 중
- 실제 사례: SEO 에이전시 Taco의 베스트 프랙티스를 바탕으로 14일 실행 계획 수립

### 섹션 5: 개발자 참여 기회

**AI Memory Dev Alliance**
- 개발 담당자들을 위한 네트워킹 그룹
- 함께 커뮤니티 교육
- 서로의 성공 지원 및 노하우 공유
- 정기적인 교류를 통한 협력

**오픈소스 기여**
- GitHub 프로젝트에 스타 및 기여 요청
- 초기 기여자를 위한 보상 프로그램 제공
- 사용자를 넘어 코드 레벨의 기술 기여 환영

**스토리텔링 지원**
- Memgraph를 활용해 애플리케이션/에이전트를 구축하는 사용자 지원
- 첫 고객 확보 및 스토리 전파 지원
- 다양한 플랫폼에서 팀과 소통 가능

---

## 타임라인

- **00:00**: All right, good afternoon. Hope everybody had a good lunch. Uh, nice to meet you all. Uh, as Frank said, my name is Jing, uh, vice president, uh, driving the Meachine open source project and commercial. So, I thought it'd be fun to create this presentation today mostly with AI. So, you're going to see a lot of AI generated photos. Apologies for that in advance. Um but uh obviously the the person presenting is a real human being. Um so just to kick it off, I thought it might be fun. Uh this is actually we're very close to the three-year anniversary of Chad being kind of born. Uh I think in nine days, November 30th or December 1st was uh was when Chad GBT came out. And I think the reason we're all here today is because that really uh kicked off a spark uh or a big bang you might want to say. uh and it gave us all some new inspiration for what's possible uh with AI. And I think that um if some of you I I don't know if uh how many of you are uh kind of developers or if you're kind of you know very tied into this uh all the all the news and and developments with AI, but most days for me this is how it feels like. uh can barely keep up even though my full-time job is to keep up with AI and uh given Chat GBT is not even three years old uh this is still the very early years of uh call it the the big AI big bang. So this is kind of like the the primordial soup or the plasma or some of those things that scientists think uh came right after the big bang. And um I thought there was a lot of parallels to kind of like right where we are today here and uh this uh kind of early uh messy and kind of chaotic uh time period right after the uh the big bang. So then kind of like my next natural question afterwards was uh how did you know how did life form and and and kind of where did life form right and so uh apparently life formed in the ocean in the seas uh the kind of...
- **05:00**: with building an AI application and you're trying to use me machine, we want to be there for you. So, this is the culture that we're building. If it sounds good to you, encourage you to take an action to uh join us, to drop into our Discord, get to know some of the folks, see what other people are building. Uh we've only been uh a public uh open source project for less than three months, but we already have a few successful deployments uh which I'll I'll talk about later. Um and you can get to know these people. You can hear what they had to do to get from point A to point B. It's just a really great place to be. So invite all of you guys to join us. I also wanted to tell you a little bit more about some of those early users um how they think about me machine where it's been specifically helpful for them. You're going to see a lot of QR codes because I'm really here to like help other people look good, right? Our team is really focused on helping you get from your idea to the application that you're building to the startup that you're trying to launch to the enterprise agent that you're trying to build. We're trying to get you from point A to point B. So really, I see my job as helping to tell the stories that other people um have had uh as they have worked with our team and as they have um been able to use me machine. So on the left um I I want to profile kind of a few very different people and use cases. So on the left um you have a person named Jenny Oang. She is a very successful uh Substack content creator. uh she writes all sorts of content for folks that want to build uh with AI tools. So if you're somebody who wants to learn how to use uh different AI tools to build applications, she has a really good substack. We got to know each other a few months ago because she was looking for a better way to handle memory in some of the AI tools that she...
- **10:00**: company is called uh teammate and what their vision was is to not create an AI that just helps onetoone. They wanted to create an AI agent that is able to understand what an entire team is doing. Have the context and memory of what that team is doing down to the individual level. But at any given time, that AI agent can be called on to go and help get something done. Um, and so what they did was they implemented a Slack-based agent first. Um, by no means are they limiting themselves to just being a Slackbased uh teammate or agent, but they started there and then they used Memachine as that long-term memory context layer. And um, it's really really effective. In fact, they're so successful at building something useful that we decided to in-house uh teammate for both uh technical program management. So, think about keeping track of all the crazy stuff going on in our GitHub account. Um now that we're an open source project to also helping my team uh do more customerf facing, marketing focused, educational, content focused uh tasks. And so what you see on the right side is an example of teammate at work uh in a real way within our Slack. Um I can just give it a simple prompt like how can I start incorporating taco based on your knowledge of my work and it knows what it it knows what I'm talking about. So Taco is actually a uh it's an SEO focused agency uh based in Brooklyn, New York. uh they recently published a notion uh about how to drive better AI SEO to your company or website and they shared that notion with me. So then I shared my notion with teammate and then uh teammate now has the memory of these best practices that this uh SEO agency called Taco uh shared with me. And now I want to um start incorporating it into my job which is to uh talk about me to the community. And in this uh particular conversation,...
- **15:00**: coding level. Uh we would love to um also work with some of you as contributors to the project. And we do have some programs for uh rewarding uh our early call it our early adopters and early uh open source contributors. And uh lastly, we do have some folks that also are um doing the work of helping to tell your story, what you're building, why you're building it, what problems you're trying to solve. And so if you're building uh applications, agents, um all sorts of things with Memachine, we want to help you get the word out, get your first customers, tell your story. So um so these are all the call it the benefits for being uh plugged into our uh our our community here. Um yes and uh lastly uh if you want to just keep in touch with what I'm doing, what our team is doing, uh we're trying to uh be on all platforms as many as we can. So uh this is just a way to kind of keep in touch with with uh with me and and and the team that uh supports supports me....

---

## 전체 자막 (타임스탬프 포함)

**[00:02]** All right, good afternoon.

**[00:05]** Hope everybody had a good lunch. Uh,

**[00:08]** nice to meet you all. Uh, as Frank said,

**[00:10]** my name is Jing, uh, vice president, uh,

**[00:13]** driving the Meachine open source project

**[00:15]** and commercial.

**[00:18]** So, I thought it'd be fun to create this

**[00:21]** presentation today mostly with AI. So,

**[00:23]** you're going to see a lot of AI

**[00:24]** generated photos. Apologies for that in

**[00:27]** advance. Um but uh obviously the the

**[00:30]** person presenting is a real human being.

**[00:32]** Um so just to kick it off, I thought it

**[00:35]** might be fun. Uh this is actually we're

**[00:37]** very close to the three-year anniversary

**[00:40]** of Chad being kind of born. Uh I

**[00:43]** think in nine days, November 30th or

**[00:45]** December 1st was uh was when Chad GBT

**[00:48]** came out. And I think the reason we're

**[00:49]** all here today is because that really uh

**[00:51]** kicked off a spark uh or a big bang you

**[00:54]** might want to say. uh and it gave us all

**[00:57]** some new inspiration for what's possible

**[00:59]** uh with AI.

**[01:05]** And I think that um if some of you I I

**[01:08]** don't know if uh how many of you are uh

**[01:09]** kind of developers or if you're kind of

**[01:12]** you know very tied into this uh all the

**[01:14]** all the news and and developments with

**[01:16]** AI, but most days for me this is how it

**[01:20]** feels like. uh can barely keep up even

**[01:23]** though my full-time job is to keep up

**[01:26]** with AI and uh given Chat GBT is not

**[01:30]** even three years old uh this is still

**[01:32]** the very early years of uh call it the

**[01:34]** the big AI big bang. So this is kind of

**[01:37]** like the the primordial soup or the

**[01:40]** plasma or some of those things that

**[01:42]** scientists think uh came right after the

**[01:45]** big bang. And um I thought there was a

**[01:48]** lot of parallels to kind of like right

**[01:51]** where we are today here and uh this uh

**[01:54]** kind of early uh messy and kind of

**[01:57]** chaotic uh time period right after the

**[01:59]** uh the big bang. So then kind of like my

**[02:02]** next natural question afterwards was uh

**[02:04]** how did you know how did life form and

**[02:06]** and and kind of where did life form

**[02:08]** right and so uh apparently life formed

**[02:12]** in the ocean in the seas uh the kind of

**[02:15]** the first process for organisms was

**[02:17]** through chemosynthesis

**[02:19]** then you had photosynthesis and then uh

**[02:21]** you know you and I we all breathe

**[02:23]** primarily oxygen uh to uh stay alive and

**[02:27]** if you're also kind of you know in this

**[02:29]** space living and breathing every every

**[02:31]** other day we're kind of thinking about

**[02:33]** whether or not we're in a bubble or is

**[02:35]** AI going to truly you know deliver on

**[02:37]** the promise of uh you know on the

**[02:39]** technology. Are we going to find useful

**[02:41]** enough use cases to keep us all employed

**[02:43]** and you know help us to uh you know to

**[02:45]** make some money.

**[02:48]** So I'm going to transition obviously

**[02:50]** into a little bit more about my point of

**[02:52]** view and I think some of the team here

**[02:54]** at Meverg's point of view which is very

**[02:56]** much that um we have this ecosystem.

**[02:59]** It's a little bit messy. Everyone's

**[03:01]** trying to do a little bit of what

**[03:02]** everybody else is doing. You know, the

**[03:04]** uh the agent builders are not really

**[03:06]** just doing agent development kits. Some

**[03:07]** of them are doing memory. Some of them

**[03:09]** are doing interfaces. The apps, you

**[03:11]** know, the apps are doing all sorts of

**[03:13]** things that are really hard to keep

**[03:15]** track of. There's a new model coming out

**[03:16]** every day. But I believe fundamentally

**[03:20]** at the end of the day, AI systems

**[03:22]** breathe memory and context. So if you

**[03:25]** cannot deliver good memory and context,

**[03:27]** do the AI. it's not going to do a very

**[03:30]** useful thing for you at the very end of

**[03:31]** the day. So I'm very excited that all of

**[03:33]** you decided to spend your Friday here

**[03:35]** today uh to you know be part of this

**[03:38]** dialogue to hear all the speakers. Um we

**[03:41]** wanted to make this a very inclusive

**[03:42]** event. We invited everybody and um this

**[03:46]** really you know this is because we

**[03:48]** believe that if we work together to make

**[03:50]** good memory make good context that's

**[03:53]** that's ultimately what's going to make

**[03:55]** good AI because it is really the oxygen

**[03:57]** just like we require oxygen to stay

**[03:59]** alive AI requires context and memory.

**[04:03]** So um I know Charles covered a lot of

**[04:06]** the technical aspects of memachine this

**[04:08]** morning. Um, if you did miss his talk,

**[04:11]** it'll be recorded. And I'm not really

**[04:14]** here to talk too much about the

**[04:15]** technology, but I I did want to talk

**[04:16]** about the community that we're building.

**[04:18]** Um, and I and I wanted to invite all of

**[04:20]** you to participate. So, really the QR

**[04:23]** code on the top right is uh our Discord

**[04:26]** community. Um, and this is really the

**[04:29]** culture that we're we're trying to drive

**[04:31]** uh for everyone who is um working in

**[04:33]** this space. Uh, we want it to be uh a

**[04:36]** culture that is open. uh we want it to

**[04:39]** be a culture that is people centered

**[04:41]** even though we're doing a lot of things

**[04:42]** with AI. Um we're trying to do a lot of

**[04:45]** things that are a mix of digital as well

**[04:47]** as uh events in real life. Uh we're

**[04:49]** doing a mix of you know hackathons.

**[04:51]** We're doing a mix of educational events.

**[04:54]** And the reason we even have a discord is

**[04:56]** because any one of you guys can drop in

**[04:58]** on any given day. And if you need help

**[05:01]** with building an AI application and

**[05:03]** you're trying to use me machine, we want

**[05:05]** to be there for you. So, this is the

**[05:08]** culture that we're building. If it

**[05:09]** sounds good to you, encourage you to

**[05:11]** take an action to uh join us, to drop

**[05:14]** into our Discord, get to know some of

**[05:16]** the folks, see what other people are

**[05:18]** building. Uh we've only been uh a public

**[05:21]** uh open source project for less than

**[05:23]** three months, but we already have a few

**[05:25]** successful deployments uh which I'll

**[05:27]** I'll talk about later. Um and you can

**[05:29]** get to know these people. You can hear

**[05:30]** what they had to do to get from point A

**[05:32]** to point B. It's just a really great

**[05:34]** place to be. So invite all of you guys

**[05:36]** to join us.

**[05:39]** I also wanted to tell you a little bit

**[05:40]** more about some of those early users um

**[05:43]** how they think about me machine where

**[05:44]** it's been specifically helpful for them.

**[05:47]** You're going to see a lot of QR codes

**[05:49]** because I'm really here to like help

**[05:51]** other people look good, right? Our team

**[05:53]** is really focused on helping you get

**[05:55]** from your idea to the application that

**[05:58]** you're building to the startup that

**[05:59]** you're trying to launch to the

**[06:01]** enterprise agent that you're trying to

**[06:03]** build. We're trying to get you from

**[06:04]** point A to point B. So really, I see my

**[06:06]** job as helping to tell the stories that

**[06:10]** other people um have had uh as they have

**[06:13]** worked with our team and as they have um

**[06:16]** been able to use me machine. So on the

**[06:19]** left um I I want to profile kind of a

**[06:22]** few very different people and use cases.

**[06:24]** So on the left um you have a person

**[06:26]** named Jenny Oang. She is a very

**[06:29]** successful uh Substack content creator.

**[06:32]** uh she writes all sorts of content for

**[06:34]** folks that want to build uh with AI

**[06:38]** tools. So if you're somebody who wants

**[06:40]** to learn how to use uh different AI

**[06:42]** tools to build applications, she has a

**[06:45]** really good substack. We got to know

**[06:47]** each other a few months ago because she

**[06:49]** was looking for a better way to handle

**[06:50]** memory in some of the AI tools that she

**[06:53]** was building. And um when she was when

**[06:55]** she heard about Memachine, one of the

**[06:57]** types of memory that really uh intrigued

**[07:00]** her and excited her was profile memory

**[07:03]** because for her she has a brand, right?

**[07:05]** She writes all of this AI content. She

**[07:07]** has a voice and she's also looking for

**[07:10]** other people who live on Substack and

**[07:12]** write content and she wants to find

**[07:14]** other voices that are both similar and

**[07:16]** different from her because that way she

**[07:18]** can collaborate and she can contrast. So

**[07:21]** profile memory is a really uh great uh

**[07:24]** profile memory within me machine is a

**[07:25]** really great tool for her to quickly uh

**[07:28]** kind of encode what her profile of

**[07:31]** writing looks like compared to somebody

**[07:33]** else's profile of writing looks like. Um

**[07:36]** and this is how she uses us today for

**[07:38]** her uh her work uh which is called Build

**[07:40]** to Launch. It's her newsletter. She has

**[07:42]** over 3,000 followers. Um Brandon Monroe,

**[07:45]** he's the founder uh and creator of

**[07:48]** Character Engine. Um he had this idea to

**[07:51]** start Character Engine because he tried

**[07:54]** to uh raise money for his startup a few

**[07:56]** years ago and he found out he was a

**[07:58]** horrible uh he was horrible at pitching.

**[08:00]** He could not pitch for his life. And

**[08:03]** what he built was a set of AI coaches,

**[08:06]** characters that are specifically focused

**[08:09]** on helping him become a better version

**[08:10]** of himself. And so his first AI coach is

**[08:14]** this character named Marcus Sterling who

**[08:16]** is focused on helping you uh become a

**[08:18]** better pitcher of whatever idea whether

**[08:21]** it's to land a job whether it's to raise

**[08:24]** money basically he wanted to build an AI

**[08:27]** coach that wouldn't just tell you the

**[08:29]** things that you wanted to hear which a

**[08:30]** lot of times if you use chat BPT it's

**[08:32]** just overly nice and sickopantic he

**[08:34]** wanted to build an AI that is not afraid

**[08:36]** to call your BS if you're not giving the

**[08:40]** right effective you know, pitch and

**[08:42]** message. And what he found was that um

**[08:45]** by being able to then layer in this

**[08:48]** personality of a Marcus Sterling with

**[08:51]** the ability to remember each and every

**[08:53]** one of the users that is um that is

**[08:56]** using Marcus to help them pitch better.

**[08:58]** This creates a much better user

**[09:00]** experience over multiple sessions. So

**[09:02]** just like you would you would hire a

**[09:04]** human coach or a human counselor to help

**[09:06]** you work on different things to make you

**[09:08]** know to make yourself better. Uh now AI

**[09:11]** his AI characters can help you over

**[09:13]** multiple sessions and remember where you

**[09:15]** left off and also what your strengths

**[09:17]** and weaknesses are and what topics or

**[09:19]** what pitches that you were uh working on

**[09:21]** previously um to u you know that you

**[09:24]** needed help with. So Meachine is also uh

**[09:28]** now powering the characters that are uh

**[09:31]** part of the character engine portfolio.

**[09:33]** So again, QR code if you want to check

**[09:35]** out his website. Um he's basically

**[09:38]** bringing in the founding kind of

**[09:39]** founding members, founding users of

**[09:41]** these AI characters. Um you guys can

**[09:44]** just take these characters for a test

**[09:46]** drive and kind of see how how memory

**[09:48]** does augment and enhance some of these

**[09:50]** uh these types of AI coaching use cases.

**[09:55]** Um next we have another company. Um this

**[09:58]** is a collaboration use case. Um the

**[10:00]** company is called uh teammate and what

**[10:05]** their vision was is to not create an AI

**[10:09]** that just helps onetoone. They wanted to

**[10:12]** create an AI agent that is able to

**[10:14]** understand what an entire team is doing.

**[10:18]** Have the context and memory of what that

**[10:20]** team is doing down to the individual

**[10:23]** level. But at any given time, that AI

**[10:26]** agent can be called on to go and help

**[10:28]** get something done. Um, and so what they

**[10:30]** did was they implemented a Slack-based

**[10:33]** agent first. Um, by no means are they

**[10:36]** limiting themselves to just being a

**[10:38]** Slackbased uh teammate or agent, but

**[10:40]** they started there and then they used

**[10:43]** Memachine as that long-term memory

**[10:46]** context layer. And um, it's really

**[10:49]** really effective. In fact, they're so

**[10:51]** successful at building something useful

**[10:53]** that we decided to in-house uh teammate

**[10:56]** for both uh technical program

**[10:59]** management. So, think about keeping

**[11:00]** track of all the crazy stuff going on in

**[11:02]** our GitHub account. Um now that we're an

**[11:04]** open source project to also helping my

**[11:07]** team uh do more customerf facing,

**[11:10]** marketing focused, educational, content

**[11:13]** focused uh tasks. And so what you see on

**[11:17]** the right side is an example of teammate

**[11:20]** at work uh in a real way within our

**[11:22]** Slack. Um I can just give it a simple

**[11:25]** prompt like how can I start

**[11:27]** incorporating taco based on your

**[11:30]** knowledge of my work and it knows what

**[11:32]** it it knows what I'm talking about. So

**[11:34]** Taco is actually a uh it's an SEO

**[11:38]** focused agency uh based in Brooklyn, New

**[11:41]** York.

**[11:42]** uh they recently published a notion uh

**[11:46]** about how to drive better AI SEO to your

**[11:51]** company or website and they shared that

**[11:53]** notion with me. So then I shared my

**[11:55]** notion with teammate and then uh

**[11:58]** teammate now has the memory of these

**[12:01]** best practices that this uh SEO agency

**[12:04]** called Taco uh shared with me. And now I

**[12:08]** want to um start incorporating it into

**[12:11]** my job which is to uh talk about me to

**[12:14]** the community. And in this uh particular

**[12:18]** conversation,

**[12:19]** teammate helped me to uh to basically

**[12:22]** recommend or draft an initial 14-day

**[12:25]** action plan for how we can uh improve

**[12:28]** the AI searchability of Memachine and

**[12:31]** created a Google doc that we can then

**[12:32]** edit and work off of. So this is an

**[12:35]** example of that long-term memory and

**[12:36]** context in a very practical way

**[12:38]** implemented as a slack agent that we use

**[12:41]** and also teammate is helping other

**[12:43]** companies and startups uh to use as

**[12:46]** well. Um so yeah just wanted to give you

**[12:49]** guys kind of like three vignettes of how

**[12:51]** uh memory systems can be used. The first

**[12:54]** one was substack content creation. The

**[12:57]** second one was AI uh voice uh based uh

**[13:01]** coaches. And then the third one is as a

**[13:04]** productivity uh AI agent, you know, so

**[13:08]** to speak, teammate. It just it's it's in

**[13:10]** all it's in I have a DM with it in Slack

**[13:13]** and it's also in several of our Slack

**[13:15]** channels to help us with different uh

**[13:17]** projects and and uh and workloads.

**[13:22]** And so now, you know, a little bit more

**[13:24]** practical stuff. Um

**[13:26]** I don't know how many of you guys are in

**[13:29]** a dev rail kind of role but um one thing

**[13:33]** that we are also putting together is uh

**[13:37]** I guess what we'll call an AI memory dev

**[13:39]** alliance. So it's basically a way for uh

**[13:43]** folks who are driving dev at at your

**[13:45]** respective companies to kind of stay in

**[13:47]** touch uh for the goal of educating the

**[13:50]** community together. Uh we believe you

**[13:52]** know your perspective plus our

**[13:53]** perspective plus the pers perspective of

**[13:56]** others is going to be uh a better uh

**[13:58]** education for the folks that are trying

**[14:00]** to do some of this work. Also help each

**[14:02]** other succeed. Iron sharpens iron.

**[14:05]** There's different things that we're all

**[14:06]** good with and there's certain things

**[14:08]** that we're not. Um it's just a way to

**[14:10]** keep in touch on a regular basis and

**[14:12]** help each other out and also compare

**[14:14]** notes. What's working? What's not

**[14:16]** working? So, if you're interested in

**[14:17]** being part of this um this AI memory

**[14:21]** devalliance, uh please talk to me or

**[14:23]** please talk to Gary uh in our audience.

**[14:26]** Um we're we're driving some of this uh

**[14:28]** work together and we'd love to form a

**[14:30]** little uh working group. And then um for

**[14:33]** anyone who's uh primarily more of a

**[14:36]** developer versus a a dev uh evangelist

**[14:38]** or deval kind of person, would love to

**[14:41]** get a GitHub star from you guys, please

**[14:43]** check out our project. This QR code goes

**[14:45]** straight to our GitHub project page. Um,

**[14:48]** we also would uh welcome and uh invite

**[14:52]** all of you to uh be involved beyond just

**[14:54]** being a user if you're interested in

**[14:56]** this technology at a uh at a technical

**[15:00]** coding level. Uh we would love to um

**[15:03]** also work with some of you as

**[15:04]** contributors to the project. And we do

**[15:07]** have some programs for uh rewarding uh

**[15:09]** our early call it our early adopters and

**[15:12]** early uh open source contributors. And

**[15:15]** uh lastly, we do have some folks that

**[15:17]** also are um doing the work of helping to

**[15:19]** tell your story, what you're building,

**[15:21]** why you're building it, what problems

**[15:23]** you're trying to solve. And so if you're

**[15:25]** building uh applications, agents, um all

**[15:28]** sorts of things with Memachine, we want

**[15:31]** to help you get the word out, get your

**[15:33]** first customers, tell your story. So um

**[15:36]** so these are all the call it the

**[15:37]** benefits for being uh plugged into our

**[15:41]** uh our our community here. Um yes and uh

**[15:46]** lastly uh if you want to just keep in

**[15:48]** touch with what I'm doing, what our team

**[15:50]** is doing, uh we're trying to uh be on

**[15:53]** all platforms as many as we can. So uh

**[15:57]** this is just a way to kind of keep in

**[15:58]** touch with with uh with me and and and

**[16:01]** the team that uh supports supports me.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
