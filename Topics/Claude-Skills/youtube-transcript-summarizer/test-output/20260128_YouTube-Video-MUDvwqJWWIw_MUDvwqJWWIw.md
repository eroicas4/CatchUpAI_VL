# YouTube Video MUDvwqJWWIw

**Original Video**: [https://www.youtube.com/watch?v=MUDvwqJWWIw](https://www.youtube.com/watch?v=MUDvwqJWWIw)
**Generated**: 2026-01-28
**Video ID**: MUDvwqJWWIw
**Language**: English -> Korean

---

## Summary

이 영상은 Claudebot이라는 오픈소스 개인 AI 비서를 소개합니다. 로컬에서 실행되며, 사용자의 컴퓨터에 완전한 접근 권한을 가지고 WhatsApp, Telegram, Slack 등 다양한 채팅 서비스를 통해 사용할 수 있습니다. Claude Code와 Claude Co-work의 기능을 결합하여, 이메일 관리, 파일 업로드, 코드 작성 및 실행, 실시간 리서치 등 다양한 작업을 자동화할 수 있는 강력한 AI 어시스턴트입니다.

---

## Key Points

- 완전한 오픈소스로 사용자의 로컬 컴퓨터에서 실행됨
- Gemini, OpenAI, Claude 등 다양한 모델 연결 가능하며 로컬 모델도 사용 가능
- 지속적인 메모리 기능으로 사용자의 선호도와 작업 패턴을 학습
- 매우 능동적이며 이메일 체크, 요약, 답변 초안 작성 등을 자동으로 수행
- 컴퓨터 전체 접근 권한으로 코드 작성, 실행, 반복 작업 가능
- soul.md 파일을 통해 AI의 성격 커스터마이징 가능
- 50개 이상의 네이티브 통합 및 커뮤니티 스킬 제공
- Cron job 설정으로 정기적인 작업 자동화
- 원격에서도 Telegram 등을 통해 접근 가능
- 자체 개선 능력으로 실수를 학습하고 수정

---

## Main Content

### Section 1: Claudebot 소개 및 주요 특징

**기본 개념**
- Siri가 되었어야 할 모습의 완벽한 개인 AI 비서
- 영상 제작자가 실제로 이 영상을 준비하는 데 Claudebot을 활용
- Asana와 Grok에 연결하여 현재 정보, 트윗, 게시물 수집
- Obsidian 사용 환경을 인식하고 자동으로 hourly cron job 설정
- LM Studio의 GLM 4.7 모델 사용 환경을 스스로 인지

**다른 AI 비서보다 우수한 점**
1. 완전한 오픈소스로 사용자의 기기에서 직접 실행
2. 여러 AI 모델 믹스 앤 매치 가능 (복잡한 작업은 Claude Opus 4.5, 단순 작업은 로컬 모델)
3. 지속적인 메모리로 사용자 학습
4. 매우 능동적인 작업 수행 (이메일 체크 및 자동 요약/답변 초안)
5. 컴퓨터 전체 접근으로 코드 작성, 실행, 반복 가능

### Section 2: 개성화 및 커뮤니티

**Soul.md 파일**
- AI의 성격을 결정하는 파일
- "진정으로 도움이 되어라, 형식적으로 도움이 되지 말고"
- "의견을 가져라"
- "질문하기 전에 먼저 자원을 찾아라"
- "역량을 통해 신뢰를 얻어라"
- 완전히 커스터마이징 가능

**커뮤니티 활동**
- 거의 매일 업데이트가 이루어짐
- X(Twitter)에서 많은 사람들이 논의 중
- 많은 사용자들이 Mac mini를 구매하여 Claudebot 전용으로 사용
- 격리된 환경에서 실행하여 보안 우려 최소화

### Section 3: 설치 및 설정

**설치 과정**
- Mac, Windows, Linux 모두 지원
- clog.bot 웹사이트에서 curl 명령어로 간단히 설치
- 컴퓨터 어느 영역에 접근 권한을 줄지 질문
- 어떤 서비스와 채팅 앱을 사용할지 선택

**지원 앱 및 통합**
- 채팅 앱: WhatsApp, Telegram, Discord, Slack, Signal, iMessage
- AI 모델: Frontier 모델들 및 로컬 모델
- 기타 서비스: Spotify, Obsidian, Twitter, Chrome
- 50개 이상의 네이티브 통합 제공
- Chrome 확장 프로그램으로 브라우저 제어 가능

**Claude Hub**
- 커뮤니티에서 검증된 스킬 다운로드 가능
- Self-improving agent: 학습, 오류, 수정 사항 캡처
- Gogg: Google Workspace 연결 (Gmail, Calendar, Drive)
- Remind me, Home Assistant, Twitter, Hacker News, Obsidian 등
- Grok API 연결로 실시간 X/Twitter 정보 접근

### Section 4: 실제 사용 사례 - Google Drive 파일 업로드

**문제 상황**
- YouTube 채널의 모든 영상을 로컬 하드 드라이브에 보관
- Google Drive에 업로드 중 중간에 중단됨
- 어떤 파일이 업로드되었고 안 되었는지 비교 필요

**Claudebot의 해결 과정**
1. Drive 폴더와 로컬 폴더 비교 실행
2. 212개의 누락된 파일 발견
3. 업로드 시도 중 Google API 속도 제한 발생
4. 15분 후 자동으로 속도 제한 해제 확인 및 재시도 제안
5. Google Drive의 일일 750GB 제한 문제 진단
6. 속도 제한 해제 후 자동으로 파일 업로드 재개
7. 업로드된 파일 목록을 데스크톱에 저장 및 업데이트
8. 각 파일 업로드 후 Drive 링크 제공 및 진행 상황 실시간 보고

### Section 5: Cron Job을 통한 이메일 자동화

**설정 과정**
- 5분마다 이메일을 체크하도록 cron job 설정
- 긴급 이메일을 찾아 요약하고 답변 초안 작성
- 긴급/중간/낮은 우선순위를 자동으로 판단
- 실제 테스트에서 매우 정확한 우선순위 분류

**자체 개선 기능**
- 일반적인 영업 이메일을 긴급이 아닌 것으로 재분류
- "표준 영업 메일. 초안 불필요. 더 나은 필터링으로 업데이트하겠습니다"
- 사용자가 원하면 간단히 cron job 제거 가능

### Section 6: 로컬 모델 실행

**LM Studio 통합**
- GLM4 mixture of experts 모델 다운로드 (내장 thinking 기능)
- Claudebot이 더 나은 모델 제안 (응답 시간 4-6초)
- 원격에서 Telegram을 통해 Quen 3 mixture of experts 모델 다운로드 지시
- 레스토랑에서 원격으로 모델 다운로드를 지시하는 것이 가능

**모델 체인 설정**
- Opus 4.5, Haiku, Quen 3 로컬 모델로 데이지 체인 구성
- Cron job이나 쉬운 작업에는 로컬 모델 사용 지시
- 때때로 AI가 자동으로 다른 모델 선택 (개선 필요)
- Tools.md 파일을 자동 업데이트하여 어떤 모델을 언제 사용할지 기록

**실제 테스트**
- "Quen 3에서 짧은 이야기를 만들고 응답을 답장해줘"
- LM Studio의 개발자 로그에서 실제 로컬 모델 사용 확인
- 원격에서도 완벽하게 작동

### Section 7: Twitter 통합 및 추가 기능

**Twitter 접근**
- Twitter 계정에 접근 권한 부여
- 몇 분마다 특정 게시물의 모든 답변 수집 가능
- Grok API를 통한 실시간 리서치

**영상 제작자의 설치 접근 방식**
- 많은 사용자들과 달리 메인 컴퓨터에 직접 설치
- 이유: Gmail, Slack, Telegram 등 모든 인증 정보를 제공하므로 별도 기기에 설치해도 동일한 접근 권한
- 하지만 Claudebot이 자체 기기를 가진다는 개념도 매력적

### Section 8: 보안 고려사항

**잠재적 위험**
- 비결정론적 시스템에 인증 정보 제공
- 컴퓨터 전체 접근 권한 부여
- 가드레일 설정 가능하지만 제한적

**Dell ProMax 스폰서십**
- AI 워크로드를 위한 강력한 PC
- Grace Blackwell 시리즈 Nvidia GPU (GB300, GB10)
- Nvidia RTX Pro GPU 탑재 워크스테이션

### Section 9: 향후 전망

**개선이 필요한 부분**
- 어떤 모델을 언제 사용할지 더 정확한 판단 필요
- 명시적으로 특정 모델 사용을 지시할 때 더 나은 준수
- 후속 버전 및 업데이트로 개선 예상

**가능성**
- 24/7 실행되는 수십, 수백, 수천 개의 Claudebot 인스턴스
- 클라우드에서 실행하며 모든 파일, Gmail, 캘린더 접근
- 완전히 자동화된 개인 비서의 미래

## 결론
Claudebot은 오픈소스, 로컬 실행, 완전한 커스터마이징이 가능한 차세대 개인 AI 비서입니다. 강력한 자동화 기능, 다양한 통합, 자체 학습 능력으로 개인 생산성을 크게 향상시킬 수 있으며, 활발한 커뮤니티와 지속적인 업데이트로 계속 발전하고 있습니다.

---

## Timeline

- **00:00**: This is Claudebot, the ultimate personal AI assistant that is open-source, runs locally, and can basically do everything. It is what Siri should have ...
- **05:00**: ask you a few questions. What areas of your computer do you want to give it access to? What services do you want to install? Which chat apps you want ...
- **10:00**: if I check back here, there it is. Just makes everything so easy. But let me show you what else we can do. You can set up different cron jobs. So, for...
- **15:00**: found so far? Email plus calendar awareness. Boring, but immediately useful. It checks my three inboxes and tells me what actually needs attention. Dr...
- **20:00**: Today, we're already up to $32. So, immediately I'm thinking, how do I start using other models that aren't so expensive? So, that's where local model...

---

## Full Transcript

**[00:00]** This is Claudebot, the ultimate personal

**[00:04]** AI assistant that is open-source, runs

**[00:07]** locally, and can basically do

**[00:09]** everything. It is what Siri should have

**[00:12]** been. I'm going to break down everything

**[00:14]** you need to know about it. I'm going to

**[00:16]** show you how to use it. And by the end

**[00:17]** of this video, you are also going to be

**[00:21]** beyond impressed with Claudebot. It

**[00:23]** actually helped me researching and

**[00:24]** preparing for this video. I connected it

**[00:27]** to my ASA. I connected it to Grock. So,

**[00:30]** it has all current information, current

**[00:33]** tweets, current exposts that I wanted to

**[00:36]** include. And check this out. So, I said,

**[00:38]** put together a video outline. And here

**[00:41]** it is. And it even said, okay, you're

**[00:43]** using Obsidian. Here's your hourly cron

**[00:46]** job. You're using LM Studio with GLM

**[00:48]** 4.7. So, it knew everything about

**[00:50]** itself. It put it all in here. It pulled

**[00:52]** specific tweets, told me how many views

**[00:54]** they have, and it added it all

**[00:57]** programmatically to this ASA card. It

**[00:59]** can run on your machine. You can then

**[01:01]** connect it to any of the chat services

**[01:03]** that you use like WhatsApp, Telegram,

**[01:05]** Slack, and chat with it directly from

**[01:09]** those channels. It is so cool to see. It

**[01:12]** is essentially cloud code plus cloud

**[01:15]** co-work but wrapped up with so much more

**[01:18]** capability and then directly accessible

**[01:21]** from wherever you are even if you're not

**[01:23]** home. And so there are a number of ways

**[01:25]** in which this is better than other AI

**[01:27]** assistants that I've seen in the market.

**[01:29]** One, it is fully open source and you run

**[01:31]** it on your own machine. You can connect

**[01:33]** models from Gemini, from OpenAI. You can

**[01:36]** even run models locally and use those

**[01:38]** and you can mix and match as you wish.

**[01:40]** So if you have really complex tasks that

**[01:42]** you need accomplished, go with Claude

**[01:45]** Opus 4.5. But if you're running a cron

**[01:48]** job, for example, you could just run it

**[01:50]** locally and just have it going. And I'm

**[01:52]** doing that with LM Studio. It also has

**[01:54]** persistent memory. So as you're using

**[01:57]** it, it learns about you. It learns what

**[01:59]** you like. It learns what you don't like.

**[02:01]** It learns different tasks that you do

**[02:03]** often. And that leads me to the third

**[02:05]** point, which is it is very proactive.

**[02:09]** You could tell it to do things like,

**[02:10]** "Check my email and anytime you think I

**[02:13]** got a very urgent, important email, go

**[02:15]** ahead and message me, give me a summary

**[02:17]** of it, and in fact, draft a reply." And

**[02:20]** of course, all of this requires you

**[02:22]** giving it access to a lot of different

**[02:24]** services that you use. And yes, you're

**[02:27]** giving your credentials to a

**[02:28]** non-deterministic system. So, there are

**[02:31]** some risks there. I'll talk about that a

**[02:33]** little bit later. And then last and

**[02:35]** probably most important is it has full

**[02:38]** computer access. You can limit it. You

**[02:40]** can put some guardrails on it, but you

**[02:42]** are essentially giving Claudebot access

**[02:45]** to your computer. But that also means

**[02:48]** that it could write code. It can execute

**[02:50]** code. It can iterate on that code. It is

**[02:52]** essentially what cursor or claude code

**[02:55]** or codeex is doing locally. So if you're

**[02:57]** already using one of those systems, this

**[02:59]** is not that much different. And it has

**[03:01]** kind of a unique personality. And that

**[03:03]** personality is determined through

**[03:05]** something they call a soul.md file. This

**[03:08]** is what that looks like. Be genuinely

**[03:10]** helpful, not performatively helpful.

**[03:12]** Have opinions. Be resourceful before

**[03:15]** asking. Earn trust through competence.

**[03:17]** Get some boundaries. We have a vibe. And

**[03:19]** you can edit it to be anything you want.

**[03:21]** So if you have a certain personality in

**[03:23]** mind for your Claudebot, you could just

**[03:25]** tell it and it will behave like that. It

**[03:28]** can be more proactive. It can ask more

**[03:31]** questions up front. It can verify things

**[03:33]** before trying things. Fully customizable

**[03:35]** and again because it's open source and

**[03:37]** it already has a thriving community.

**[03:40]** There are basically daily updates for

**[03:42]** Claude. And it seems everybody on X is

**[03:45]** talking about it right now and also

**[03:47]** buying Mac minis. I'll explain that in a

**[03:49]** moment. So Cloudbot is a 24/7 assistant

**[03:52]** with access to its own computer. What if

**[03:54]** there were 10 or 100 or a thousand all

**[03:56]** running 24/7 in the cloud with access to

**[03:58]** your files, your Gmail calendar,

**[03:59]** everything about you? Now, I'm going to

**[04:01]** break down exactly what access I gave it

**[04:03]** and so you can kind of get a sense of

**[04:05]** how I'm using it. But why is everybody

**[04:08]** buying Mac minis and putting Cloudbot on

**[04:10]** it? Well, they basically want an

**[04:13]** isolated environment in which to install

**[04:15]** Claudebot and to just go crazy, give it

**[04:18]** access to the entire system and not

**[04:21]** really worry about, ooh, is it going to

**[04:23]** also have access to things that I don't

**[04:24]** want it to. Now, I took a different

**[04:26]** approach. which I just installed it on

**[04:28]** my main computer because my thinking is

**[04:30]** if I'm giving it access to all of my

**[04:31]** credentials anyways, Gmail, Slack,

**[04:34]** Telegram, then it is going to have that

**[04:37]** even if I put it on its own machine. But

**[04:39]** there's something cool also about

**[04:41]** thinking that Claudebot has its own

**[04:44]** machine. It's kind of living in this

**[04:46]** device. So, how do you actually install

**[04:48]** it? Well, of course, it depends on what

**[04:50]** OS you have. It does support Mac,

**[04:52]** Windows, and Linux. So, you just go to

**[04:54]** clog.bot. You grab this curl command and

**[04:57]** it will install. The installation

**[04:58]** process is dead simple. It's going to

**[05:00]** ask you a few questions. What areas of

**[05:02]** your computer do you want to give it

**[05:04]** access to? What services do you want to

**[05:06]** install? Which chat apps you want to use

**[05:08]** to communicate with it? And more. And so

**[05:10]** here are just a few examples of the apps

**[05:11]** that it works with. So here's WhatsApp,

**[05:13]** Telegram, which is what I'm using,

**[05:15]** Discord, Slack Signal, iMessage, which

**[05:17]** is really cool. Any of the Frontier

**[05:18]** models that I mentioned, you could also

**[05:20]** use it with local models. I'll show you

**[05:22]** how to do that. In fact, it kind of set

**[05:24]** it up itself. It's kind of wild to see

**[05:26]** this stuff. Spotify, Obsidian, you can

**[05:28]** give it access to Twitter. You can also

**[05:31]** give it Chrome access. So, you install a

**[05:33]** little Chrome extension and it can

**[05:35]** browse Chrome on your behalf. Remember,

**[05:37]** again, because it's installed locally,

**[05:39]** so it's basically operating your

**[05:41]** computer on your behalf. It already has

**[05:43]** 50 native integrations. And what's

**[05:46]** really cool is, as I mentioned, there's

**[05:48]** a community and they're already

**[05:50]** releasing skills that people have

**[05:52]** already tested and proven work really

**[05:54]** well. And so if this all sounds very

**[05:56]** familiar, if it sounds like claude code

**[05:59]** or other agentic coding assistants that

**[06:01]** you've used, it basically is. It's just

**[06:03]** Claude code wrapped in a bunch of

**[06:05]** functionality that makes it really easy

**[06:07]** to use as a personal AI assistant. So

**[06:10]** here's Claude Hub where you can download

**[06:12]** a bunch of skills. So if we go to browse

**[06:14]** skills, we could see some that are

**[06:16]** available. So here are some of those

**[06:17]** examples. We have self-improving agent

**[06:19]** which captures learnings, errors, and

**[06:21]** corrections to enable continuous

**[06:22]** improvement. Now Claudebot has that

**[06:24]** built in natively, but this might be a

**[06:27]** better version of it. We have Gogg,

**[06:29]** which allows you to connect to Google

**[06:31]** Workspaces. So that's Gmail, Calendar,

**[06:33]** Drive, and I'll show you a use case that

**[06:35]** I just did with Google Workspace. Remind

**[06:37]** me, you can connect to your home

**[06:39]** assistant bird if you want to connect to

**[06:41]** Twitter. We have hacker news. We can

**[06:43]** connect to Obsidian. We can use Nano

**[06:45]** Banana Pro. We can do Brave Search. All

**[06:48]** of this stuff is just dead simple. And

**[06:50]** the more tools, the more skills that you

**[06:53]** give Claudebot, the better it is. So,

**[06:55]** one of my favorite things that I gave it

**[06:57]** was access to the Gro G

**[07:01]** API. And thus, as it's doing research

**[07:04]** for me, it has access to X. It has

**[07:06]** access to Twitter and everything going

**[07:08]** on there. So, it really is incredible at

**[07:10]** doing real-time research for me. Here is

**[07:13]** my Clawbot running in Telegram. And

**[07:15]** remember, I can run this even if I'm not

**[07:17]** home. And I can just say, "Hi." And it

**[07:20]** starts typing back.

**[07:25]** And so, it's actually reminding me about

**[07:26]** a previous task that I had going with

**[07:29]** it. So, let me tell you about this task

**[07:30]** and see if we can get it finalized. So,

**[07:32]** this is an example of something really

**[07:34]** useful that it can help you with. I have

**[07:36]** a bunch of videos locally. Basically,

**[07:39]** all the videos I've ever made for my

**[07:40]** YouTube channel, I save them on a hard

**[07:43]** drive. I zip it up. Then now what I'm

**[07:45]** trying to do is upload them to Google

**[07:47]** Drive. And I tried to do that, but there

**[07:49]** are a lot of videos as you know. And so

**[07:52]** halfway through the upload broke. So

**[07:55]** some files have been uploaded, others

**[07:56]** have not. And I didn't really see an

**[08:00]** easy way to do that comparison. So I

**[08:02]** asked my Cloudbot to do it. And I said,

**[08:03]** "Run a comparison. Here's the folder in

**[08:05]** Drive. Here's the folder locally. Let me

**[08:08]** know which videos have been uploaded and

**[08:10]** which have not. And it ran a bunch of

**[08:11]** comparisons and it figured out that

**[08:13]** there are 212

**[08:15]** missing. So now I'm testing it and I'm

**[08:19]** saying, okay, let's try to upload one.

**[08:22]** Maybe Claude can do that directly for

**[08:24]** me. So we ran into some Google API

**[08:26]** errors because we got rate limited. But

**[08:28]** now I just said hi again about 15

**[08:29]** minutes later and it says rate limit

**[08:31]** should have been reset by now. Do you

**[08:32]** want me to try to upload again? Sure. So

**[08:35]** now just imagine cloud code running in

**[08:37]** the background and it's writing code to

**[08:39]** actually do the upload and it does say

**[08:42]** okay still hitting the rate limit. Let

**[08:43]** me check if simple API calls work. Okay,

**[08:46]** so this is in fact a Google Drive

**[08:48]** problem because I've been uploading so

**[08:50]** much recently. You're only allowed to

**[08:52]** upload 750 GB per day and I hit that

**[08:55]** rate limit and so that's what we're

**[08:56]** getting. When we try to upload it's

**[08:58]** hitting the rate limit. Okay. And so now

**[09:00]** the rate limit for Google Drive has been

**[09:02]** removed, and it is working flawlessly.

**[09:05]** It ran a comparison of all the files

**[09:06]** that I've already uploaded to Google

**[09:08]** Drive against all the files that I have

**[09:10]** locally, made a list, saved it to my

**[09:13]** desktop, and now I'm just saying, go

**[09:15]** ahead, upload it for me, then update the

**[09:18]** list. Look at this. The .tterar file

**[09:20]** says 211 files remaining. I said, okay,

**[09:23]** do it again. Choose a larger file. It

**[09:25]** shows this video right here. Uploaded

**[09:28]** it. Linked me to it. There it is in my

**[09:32]** drive. Let's do it again just so you can

**[09:33]** see. Okay, do one more. There we go.

**[09:36]** Cloud's working. So, I had it start to

**[09:38]** tell me which model it's using. So,

**[09:40]** that's why it says Opus right there.

**[09:42]** Uploading cloud 3.7.zip.

**[09:45]** 773 megabytes. If we look up here, I can

**[09:48]** actually see my internet is going burr.

**[09:51]** 20 megabytes per second, which actually

**[09:53]** on the slower side, but soon enough,

**[09:55]** what we're going to see right here is

**[09:56]** the uploaded file. Okay, so it's

**[09:58]** complete. It gave me the drive link. And

**[10:00]** if I check back here, there it is. Just

**[10:03]** makes everything so easy. But let me

**[10:05]** show you what else we can do. You can

**[10:07]** set up different cron jobs. So, for

**[10:09]** example, every 10 minutes, go check my

**[10:12]** email, look for any urgent emails,

**[10:15]** summarize them, draft a reply, and then

**[10:18]** let me know. Here I say set up a cron

**[10:20]** job for every 5 minutes to check my

**[10:22]** email for any urgent emails that need

**[10:24]** response, summarize them and then draft

**[10:26]** a reply and show me here. So I hit enter

**[10:28]** and it starts working. It creates that

**[10:30]** crown job. It creates the code to go get

**[10:32]** those urgent emails. It does the

**[10:34]** determination itself of what counts as

**[10:36]** an urgent email versus not. And I

**[10:38]** actually tested it. I said, "Okay, tell

**[10:40]** me how you define urgent verse not." And

**[10:42]** it went out. It grabbed a bunch of

**[10:44]** example emails and it said this is

**[10:46]** urgent. This is middle priority and this

**[10:48]** is low priority. And it was extremely

**[10:50]** accurate. Done. Created CROM job

**[10:52]** scheduled every 5 minutes. Here's my

**[10:54]** account. Check unread emails. Want me to

**[10:56]** do a manual check right now. Sure. Okay.

**[10:59]** So, found one unread email. Let me get

**[11:01]** the full context. So, this is

**[11:03]** interesting. It actually didn't find an

**[11:06]** urgent email and it corrected itself and

**[11:08]** it said this is not urgent. Standard

**[11:10]** cold outreach. No draft needed unless

**[11:12]** you want me to write one. I'll update

**[11:14]** the cron job to better filter out

**[11:16]** pitches. And this is another benefit of

**[11:19]** using cloudbot. It self-improves as it

**[11:22]** goes. And I can simply say remove this

**[11:25]** cron job. And now it's not going to run

**[11:27]** anymore. And so you can start to get

**[11:30]** very creative with the tasks that you

**[11:32]** give it with the combination of memory

**[11:34]** and cron jobs and access to your

**[11:37]** computer, the ability to write and

**[11:38]** execute code locally. All of this stuff

**[11:41]** is really cool. One other thing I

**[11:42]** mentioned is you can run local models.

**[11:45]** By the way, if you want to run this

**[11:47]** locally, you can also run it on the

**[11:49]** sponsor of today's video. And a special

**[11:51]** thank you to Dell Technologies for

**[11:52]** sponsoring this portion of the video.

**[11:55]** Dell's ProMax family of PCs are

**[11:58]** incredibly powerful for AI workloads

**[12:01]** using the new Grace Blackwell series of

**[12:03]** Nvidia GPUs, including GB300 and GB10.

**[12:08]** These are absolute monster GPUs in your

**[12:11]** desktop. Learn more about DellPro Max

**[12:14]** GB10 and GB300 and the Dell Pro Max

**[12:17]** lineup of workstations with Nvidia RTX

**[12:20]** Pro GPUs. Click the link in the

**[12:23]** description below. Let them know I sent

**[12:25]** you. Check it out. So, I'm running LM

**[12:27]** Studio. I downloaded GLM4, which is a

**[12:30]** mixture of experts model with built-in

**[12:31]** thinking, which I can't seem to disable

**[12:33]** the thinking. And I actually had

**[12:34]** Claudebot tell me like, "Hey, is this

**[12:37]** the best model to use since I want to

**[12:39]** use this? I want really fast responses

**[12:42]** and I want to use it for easier tasks,

**[12:44]** less sophisticated tasks." And it said,

**[12:46]** "Well, it takes about 4 to 6 seconds on

**[12:48]** average to get a response. I think we

**[12:50]** can get a better model." And literally

**[12:52]** through Telegram, I had it tell LM

**[12:54]** Studio to download whatever model it

**[12:56]** wanted. And it chose Quen 3 mixture of

**[12:59]** experts without thinking. So it's very

**[13:01]** fast. It downloaded this, remember,

**[13:03]** completely remotely. I was out. I was at

**[13:05]** a restaurant and I was telling it to do

**[13:07]** this. It was really mind-blowing. So, LM

**[13:10]** Studio downloaded it and now we have

**[13:12]** access to it. So, just to show you it's

**[13:14]** working, run this prompt on Quen 3 and

**[13:16]** LM Studio. Tell me a short story, then

**[13:18]** reply back with its response. Now, I

**[13:20]** shouldn't have to explicitly tell it to

**[13:22]** run Quen 3 on LM Studio. And in fact,

**[13:24]** you can actually set up a daisy chain.

**[13:26]** In my daisy chain of large language

**[13:28]** models, I'm using Opus 4.5 Haiku and I'm

**[13:32]** using Quen 3 locally. So here it is,

**[13:34]** Quen 3 response. And if I open up LM

**[13:37]** Studio, we can see the developer logs.

**[13:39]** This is it. So we know it actually used

**[13:41]** the local model. And I can explicitly

**[13:44]** tell it use the local model for cron

**[13:47]** jobs for easy tasks. And it will

**[13:50]** remember to do that. Now, it's not

**[13:52]** perfect. I will say that sometimes it

**[13:54]** just thinks, okay, I think I'm just

**[13:56]** going to use Haik coup here or I'm going

**[13:58]** to use Opus 4.5. And I think with

**[14:00]** subsequent versions, subsequent updates

**[14:02]** of Claude, it's going to be better at

**[14:04]** knowing when to use which model. And if

**[14:07]** I tell it to use a specific model, it's

**[14:09]** going to be much better at actually

**[14:10]** listening to what I'm telling it. But

**[14:12]** for now, it's pretty good. Here's what

**[14:14]** that looks like. I have Claude opened

**[14:18]** and it suggested using Quen 3 and I

**[14:20]** said, "Can you install it for me?" I

**[14:21]** didn't even know if it was possible.

**[14:23]** Downloading now. And it was downloading

**[14:25]** it. It gave me updates along the way. It

**[14:27]** said it stalled, but then said, "Nope,

**[14:28]** it downloaded. Here it is. LM Studio."

**[14:31]** And it updated tools.md to say when to

**[14:35]** use that local model. I also gave it

**[14:37]** access to my Twitter and I asked it,

**[14:39]** okay, every few minutes grab all the

**[14:41]** replies to this post, tell me the ones

**[14:43]** that I haven't replied to, draft a

**[14:45]** reply, and then wait, let me tell you if

**[14:48]** I want to publish it or not. So, here's

**[14:49]** an example. Someone said, "Hide

**[14:51]** Claudebot," and it said, "Hey, drafted

**[14:53]** and sent with Claude." Here's another

**[14:55]** one. Drafted and sent with Claude.

**[14:57]** Greetings, Claude. Drafted and sent with

**[14:58]** Claude. So, what's the best utility you

**[15:00]** found so far? Email plus calendar

**[15:02]** awareness. Boring, but immediately

**[15:04]** useful. It checks my three inboxes and

**[15:06]** tells me what actually needs attention.

**[15:08]** Drafted and sent with glad. That is

**[15:10]** based on what it is actually doing for

**[15:11]** me. So, I asked it to show me its memory

**[15:14]** file. So, let's take a look at what it

**[15:16]** knows about me so far. So Matt's

**[15:18]** preferences writing always use the

**[15:20]** humanizer skill. So that's something

**[15:22]** that I installed to make it sound more

**[15:23]** human, less AI. And that's a skill that

**[15:26]** you can install on cloud code. And

**[15:28]** because you can install it on cloud

**[15:30]** code, you can install it in cloudbot. I

**[15:32]** use superhuman for email. I use Slack.

**[15:35]** Make sure if it is posting on my behalf,

**[15:37]** I want it to prefix with from Claude.

**[15:40]** Here are my email accounts. Not going to

**[15:41]** show those. I am an early bird. usually

**[15:44]** up at 7:00, probably earlier, but that's

**[15:46]** the first I want to hear from it. I have

**[15:47]** a show called Forward Future Live. My

**[15:49]** wife and I often times share calendars,

**[15:52]** so sometimes stuff she's doing shows up

**[15:54]** on mine and I don't want it to get

**[15:56]** confused about that and think I'm busy.

**[15:59]** So, it's using its judgment as it says

**[16:01]** here. If it looks like a joint event or

**[16:03]** something, he'd attend, remind him.

**[16:04]** Remember I said, okay, it determined

**[16:06]** what is high priority versus medium and

**[16:08]** low here. That is so meetings and

**[16:10]** calendar invites high priority partner

**[16:12]** communication medium priority sponsor

**[16:14]** pitches guest bookings and then low

**[16:16]** newsletters LinkedIn and marketing

**[16:17]** access to Grock. It has access to

**[16:20]** Twitter and that is what it knows about

**[16:23]** me so far. And then I said show me your

**[16:26]** soul. Again the cool thing is you can

**[16:28]** basically modify it all you like

**[16:30]** directly from Telegram. So it it's like

**[16:33]** selfch changing self- evvolving. It's

**[16:36]** kind of wild to think about. A couple

**[16:38]** other things, it uses sub agents, so you

**[16:40]** can have a conversation with it, kick

**[16:41]** off a sub agent, it's going to go do its

**[16:43]** thing in parallel, and then come back

**[16:44]** when it's done, and you can continue

**[16:46]** talking. It does not lock up

**[16:48]** synchronously. You can also cue up

**[16:50]** multiple tasks. So, if I type, tell me

**[16:52]** the date, and then I say, tell me the

**[16:53]** date again, I can cue those up and it

**[16:56]** will do it and then go to the next one.

**[16:58]** So, there you go. So, you can ceue up as

**[17:00]** many tasks as you want. Obviously, this

**[17:02]** is quick and easy, but if you have a

**[17:04]** more complex task, you can set it off

**[17:07]** and do your next thing. It's not all

**[17:09]** perfect. Let me break down some of the

**[17:11]** issues. One, certainly there is a

**[17:14]** security risk. You're dealing with

**[17:16]** non-deterministic systems and you're

**[17:18]** giving it access to really important

**[17:22]** things like Gmail and Calendar and Drive

**[17:25]** and whatever other services you want to

**[17:26]** give it access to. You're basically

**[17:28]** giving it to an AI to act on your

**[17:30]** behalf. Sometimes it's going to make

**[17:32]** mistakes. Sometimes it's going to make

**[17:35]** an irreversible change that is painful

**[17:38]** for you. So, this is really right now

**[17:40]** for more power users. You really have to

**[17:43]** understand the consequences of what

**[17:44]** you're asking it. And it's really

**[17:47]** important to think about it as you're

**[17:49]** prompting it. So, for example, for that

**[17:51]** Google Drive task, I said, "Okay, tell

**[17:53]** me exactly what you're going to do

**[17:54]** before you do it." and let's test it

**[17:56]** with one file before trying to upload

**[17:58]** all of them. It also has rough edges. It

**[18:01]** is far from perfect. It is a project

**[18:04]** that is only 2 months old. I believe

**[18:06]** it's only a solo developer building it,

**[18:08]** but there is a growing community. But

**[18:09]** that means there are problems. And just

**[18:13]** like any artificial intelligence system,

**[18:15]** there are things where you're looking at

**[18:16]** it, you're like, I I'm pretty sure you

**[18:18]** should be able to do this or how did you

**[18:20]** make that mistake? How did you forget

**[18:22]** about that? And speaking of forgetting,

**[18:24]** memory compaction still is an issue. And

**[18:28]** it's not specific to Claude, but any AI

**[18:31]** system when you're compacting the

**[18:33]** memory, when you're taking all of the

**[18:35]** memory that you have given it, and at a

**[18:38]** certain point, it needs to start

**[18:40]** compressing that memory because you've

**[18:41]** hit the context window limit. When you

**[18:43]** compress the memory, it loses detail.

**[18:46]** So, it might forget something that you

**[18:47]** told it in the past, and you're like,

**[18:49]** "Oh my god, how do I have to keep

**[18:50]** telling you that?" And the way to solve

**[18:52]** that is to continue to help it memorize

**[18:55]** those things. So just tell it, no,

**[18:57]** explicitly write this down. Crashes also

**[19:00]** happen. And I was out of my house

**[19:02]** yesterday and all of a sudden I got into

**[19:04]** this weird tool call loop and it was

**[19:07]** basically broken. It I could not use it

**[19:09]** anymore. Any message I would send, it

**[19:11]** would tell me that the tool call was

**[19:12]** malformed and I had to wait until I got

**[19:15]** home and I restarted the system and then

**[19:17]** it finally worked again. And next, it's

**[19:19]** not free if you're using Claude.

**[19:21]** Obviously, if you're using different

**[19:23]** Frontier LLMs and you're giving

**[19:24]** Claudebot your API key, it's using

**[19:27]** tokens and it costs money. So, for

**[19:28]** example, just yesterday I used 70

**[19:32]** million tokens. The vast majority of

**[19:34]** which it chose to use Claude Opus 4.5.

**[19:37]** Some you can see Haiku 4.5 right there.

**[19:40]** Then today, just so far and it's only

**[19:43]** 9:30 in the morning, 25 million tokens

**[19:46]** total. Now, for costs, that is a lot

**[19:48]** more than I thought it would be. Holy

**[19:50]** crap, it is very expensive. In fact, I'm

**[19:54]** just seeing it now. I'm kind of

**[19:55]** surprised. So, yesterday I paid about

**[19:58]** $130.

**[20:00]** Today, we're already up to $32. So,

**[20:03]** immediately I'm thinking, how do I start

**[20:06]** using other models that aren't so

**[20:08]** expensive? So, that's where local models

**[20:10]** start coming into play. So, you really

**[20:12]** need to be careful. Obviously, I need to

**[20:14]** be careful about costs. very cool

**[20:16]** project. I think this is something

**[20:19]** special. I do recommend trying it out.

**[20:21]** Just be careful. If you're really

**[20:23]** worried, install it on a VPS, but

**[20:26]** definitely give it a try and get a feel

**[20:28]** of what is likely to be the future of AI

**[20:31]** assistance. Now, I mentioned this is

**[20:34]** what Siri should have been, and the one

**[20:37]** piece missing is some hardware device

**[20:39]** that I can actually speak to and have it

**[20:42]** talk back to me. Having to type

**[20:44]** everything out is great, but I really

**[20:46]** want to be able to have a voice

**[20:48]** assistant powered by Cloudbot. So, it

**[20:51]** would be cool if it worked via my phone.

**[20:52]** I'm sure there's going to be a skill

**[20:54]** released soon that allows for that, but

**[20:56]** for now, it's all through Telegram or

**[20:58]** whatever chat app you're using. Now, it

**[21:00]** does have TTS support, so you can use

**[21:02]** your voice, but it all goes through

**[21:04]** whatever chat app you're using. Go try

**[21:06]** it out. Let me know what you think. If

**[21:07]** you enjoyed this video, please consider

**[21:09]** giving a like and subscribe.


---

*Generated by YouTube Transcript Summarizer*
