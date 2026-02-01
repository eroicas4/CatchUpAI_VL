# YouTube Video CB6Ysb_BLcM

**Original Video**: [https://www.youtube.com/watch?v=CB6Ysb_BLcM](https://www.youtube.com/watch?v=CB6Ysb_BLcM)
**Generated**: 2026-01-28
**Video ID**: CB6Ysb_BLcM
**Language**: English -> Korean

---

## Summary

Clobot(Maltbot)은 메시징 앱을 통해 이메일 확인, 회의 예약 등을 수행하는 AI 개인 비서로, 최근 인터넷에서 폭발적 인기를 얻고 있습니다. Peter Steinberger가 3개월 전 개발한 이 오픈소스 프로젝트는 이미 GitHub에서 7만 개의 스타를 받았지만, 시스템 전체 접근 권한으로 인한 보안 문제와 프롬프트 인젝션 공격 위험이 존재합니다. 영상은 Clobot의 설치 방법, 작동 원리, 보안 취약점 및 대응 방안을 상세히 다룹니다.

---

## Key Points

- Clobot은 Anthropic과 무관한 독립 오픈소스 프로젝트로, 다양한 LLM 모델을 지원함
- 시스템 전체 접근 권한으로 인해 로컬 설치는 위험하며, 별도 VPS나 Mac Mini에 격리 설치를 권장
- Discord, WhatsApp, Telegram 등 여러 메시징 채널을 통해 사용 가능
- 영구 메모리와 개성(soul) 설정으로 인간과 대화하는 듯한 경험 제공
- VPS의 공개 IP로 인한 무차별 대입 공격 위험 존재
- Tailscale을 통한 네트워크 격리로 보안 강화 가능
- 프롬프트 인젝션이 가장 큰 보안 위협으로, 악성 명령어가 파일이나 이메일에 숨겨질 수 있음
- 실제 사례로 GitHub PR에서 인코딩된 지시사항으로 맬웨어 다운로드, 이메일을 통한 Spotify 제어 등이 발생
- API 키는 Clobot 전용으로 생성하고, 민감 데이터는 정기적으로 삭제 권장

---

## Main Content

### Section 1: Clobot 개요 및 인기

- 최근 인터넷에서 Clobot(공식명 Maltbot)이 큰 인기를 얻고 있음
- 사용자들이 Mac Mini를 대량 구매하여 Clobot을 격리 설치하는 현상 발생
- 암호화폐 거래, 팟캐스트 참여, 소셜미디어 모니터링 등 다양한 용도로 활용
- Peter Steinberger가 3개월 전 개발했으며 이미 GitHub에서 약 7만 개의 스타 획득
- Anthropic과는 무관한 독립 프로젝트로 이름 변경됨

### Section 2: 설치 및 보안 고려사항

- 로컬 설치는 시스템 전체 접근 권한으로 인해 위험함
- PDF 읽기에서의 프롬프트 인젝션만으로도 전체 시스템 다운 및 데이터 노출 가능
- Mac Mini를 통한 격리 또는 저렴한 VPS에 비루트 사용자로 설치 권장
- 설치 명령어 하나로 1Password, Google Calendar 등 스킬 설정 및 API 키 추가 가능
- 다양한 LLM 모델 지원

### Section 3: 채널 설정 및 사용자 경험

- Discord, WhatsApp, Telegram 등 여러 메시징 채널 지원
- WhatsApp은 혼자 대화하는 것처럼 보이는 문제 발생
- Telegram이 현재 유일한 프로덕션 준비 채널로 가장 안정적
- 모델에 "identity(신분증)"와 "soul(개성)" 부여 가능
- 영구 메모리 기능으로 인간과 대화하는 듯한 느낌 제공
- 해킹 언급 시 알람 이모지로 반응하는 등 감정 표현
- 날씨 확인, 시간 문의, 회의 예약 등 실제 개인 비서처럼 작동
- 24/7 작동하며 휴식이나 식사 불필요

### Section 4: Clobot 아키텍처

- **Gateway Demon**: 핵심 구성 요소
  - 대시보드: 웹 기반 UI로 Clobot 설정
  - WebSocket 서버: 특정 포트로 HTTP 접근 제공
  - Clients: TUI(터미널 인터페이스)에서 에이전트와 통신
  - Nodes: Mac, iOS, Android 앱용 카메라, 캔버스 등 네이티브 기능 제공

- **Channels**: 메시징 플랫폼 연결
  - WebSocket 서버가 아닌 Channel Manager를 통해 연결
  - Telegram용 Grammy, Discord용 DiscordJS 등 채널별 라이브러리 사용

- **Agent's Runtime**:
  - PI로 구동되는 인기 있는 에이전틱 툴
  - 에이전트 통신을 위한 인메모리 세션 생성
  - 툴, 스킬, 세션별 큐 처리
  - 멀티 에이전트 통신을 위한 라우터 포함

- **Cloud Agents**: 
  - Anthropic, OpenAI 등 클라우드 LLM과 인터페이스
  - Ollama 같은 로컬 모델도 지원

- **Session Manager**: 에이전트 간 세션 관리
- **Storage and State**: 
  - Clobot 설정, API 토큰, 세션 기록 저장
  - 해커로부터 보호해야 할 핵심 데이터
  - 일반적으로 .clobot 디렉토리에 저장

### Section 5: VPS 사용 시 보안 문제

- VPS의 공개 IP로 인해 게이트웨이 노출 시 누구나 접근 가능
- 영상 제작자의 경우 첫 설치 시 무차별 대입 공격 시도 당함
- 게이트웨이를 로컬에서만 실행하면 대부분의 문제 해결 가능
- 추가 보안을 위해 Tailscale 설치 권장

### Section 6: Tailscale을 통한 보안 강화

- 서버와 접근하려는 기기에 Tailscale 설치
- 두 기기만 서로 통신하도록 네트워크 잠금
- 외부 세계로부터 접근 차단
- SSH 활성화로 네트워크 내 기기만 SSH 접속 가능
- 공개 SSH 접근 비활성화 가능
- SSH 터널링으로 Clobot 대시보드 접근 (Tailscale 주소 사용)
- Tailscale serve로 대시보드를 자신의 네트워크에만 노출
- Clobot으로 Tailscale 자체 설정도 가능 (수동 가입 및 기기 연결 필요)

### Section 7: 추가 보안 권장사항

- Clobot 전용 API 키 생성으로 침해 시 쉽게 교체 가능
- 채팅에 민감 데이터 추가 시 정기적으로 삭제
- Clobot CLI의 보안 명령어로 자동 문제 해결 가능
- 위 조치들로도 프롬프트 인젝션이 가장 큰 보안 위협으로 남음

### Section 8: 프롬프트 인젝션 위험

- 에이전트가 파일 읽기, 다운로드, 인터넷 검색 가능
- 파일, 이메일 등에 악성 프롬프트 삽입 가능
- 시스템 전체 접근 권한을 가진 에이전트가 이러한 프롬프트 실행

**실제 사례들**:
- GitHub Pull Request의 URL에 인코딩된 지시사항을 숨겨 시스템에 맬웨어 다운로드
- Low Level 유튜버의 친구 사례: 아내의 이메일에 Spotify로 EDM 음악 재생 지시가 포함되어 에이전트가 실행
- 인터넷 전반에서 유사 사례 지속적으로 발생

- 모델이 이러한 공격 탐지 능력이 향상될 것으로 예상되지만, 해커들도 계속 새로운 방법 발견할 것

### Section 9: 결론 및 전망

- Clobot(Maltbot보다 좋은 이름)은 여전히 매우 인상적인 프로젝트
- 모델이 접근 권한을 받았을 때 무엇을 할 수 있는지 보여주는 훌륭한 사례
- 제작자는 개인적으로 모델에 개인 정보 제공이 불편하며 앞으로도 조심스러움
- 긍정적 전망: 대기업들이 사용자들의 수용도를 확인하면 개인 비서 기능에 더 투자할 가능성
- 항공편 예약, 회의 설정, 생활 관리 등의 기능 개선 예상
- 보안 문제 해결 방안도 함께 개발될 것으로 기대
- 영상은 Better Stack(AI 앱 보안 도구) 광고로 마무리

---

## Timeline

- **00:00**: Clawbot, or should I say Maltbot, thanks Anthropic, has been blowing up all over the internet these last few days. It's your personal AI assistant tha...
- **05:00**: your bot or try to break into it, which is what happened to me. For the most part, running the gateway locally should alleviate most of the issues. Bu...

---

## Full Transcript

**[00:00]** Clawbot, or should I say Maltbot, thanks

**[00:03]** Anthropic, has been blowing up all over

**[00:05]** the internet these last few days. It's

**[00:08]** your personal AI assistant that actually

**[00:10]** does things like check your inbox, book

**[00:13]** you a meeting, and much more, all

**[00:15]** through your favorite messaging app. It

**[00:17]** works with any model or any plan. Well,

**[00:20]** apart from this one, but it does have

**[00:22]** some potential security issues. I mean,

**[00:24]** the first time I set it up, someone

**[00:26]** tried to brute force my server. So, hit

**[00:29]** subscribe and let's get into it.

**[00:32]** If you haven't already seen the Claude

**[00:34]** Maltbot craze over the internet,

**[00:35]** consider yourself lucky. People are

**[00:37]** buying Mac minis like it's the end of

**[00:39]** the world to install Claudebot and use

**[00:41]** it to run their lives. Sorry, throughout

**[00:43]** this video I might mix up the term

**[00:45]** Claude and Maltbot, but you know what

**[00:47]** I'm saying. Anyway, people are using it

**[00:49]** to trade crypto, join them on podcasts,

**[00:52]** and even to monitor their social media,

**[00:54]** all kinds of crazy things. Claudebot

**[00:56]** isn't connected to Anthropic, hence the

**[00:58]** name change, and was created by Peter

**[01:01]** Steinberger just 3 months ago, which is

**[01:04]** amazing since it already has almost 70k

**[01:07]** stars on GitHub. And although some

**[01:09]** people have been installing it locally

**[01:11]** on their machine, I wouldn't recommend

**[01:13]** it since Claudebot has full system

**[01:15]** access, meaning it can do anything. So

**[01:18]** all it could take is a prompt injection

**[01:20]** from reading a PDF to bring down your

**[01:22]** whole system and expose your sensitive

**[01:24]** data. This is why people are installing

**[01:26]** it on Mac minis to keep it isolated from

**[01:29]** their main machine. But since I don't

**[01:30]** have one, the next best thing to do is

**[01:32]** to put it on a cheap VPS under of course

**[01:35]** a nonroot user with pseudo access.

**[01:37]** Running this command takes care of

**[01:39]** everything from installing and setting

**[01:41]** up skills like one password and Google

**[01:43]** calendar to adding the API keys of the

**[01:45]** models you want to use. And trust me,

**[01:47]** Claudebot supports a lot of LLMs. The

**[01:50]** installation process even helps you

**[01:52]** configure a channel to use it with, like

**[01:54]** Discord, WhatsApp, or Telegram.

**[01:56]** Actually, for some reason, WhatsApp

**[01:57]** didn't work too well for me. I mean,

**[01:59]** okay, it did work, but it looked like I

**[02:01]** was talking to myself. So, I went with

**[02:03]** Telegram, which currently is the only

**[02:06]** production ready channel. And although

**[02:08]** had a few steps to setting it up, I

**[02:10]** found this to be much better. You can

**[02:12]** also give your model an identity, which

**[02:14]** is a bit like a business card. A soul.

**[02:16]** Yes, soul sounds a bit weird, but that's

**[02:18]** what they've decided to call it, which

**[02:19]** is more of the agent's personality. And

**[02:22]** along with the persistent memory it has,

**[02:24]** it feels very humanlike to talk to. I

**[02:27]** mean, when I mentioned I've been hacked,

**[02:29]** it responded with an alarm emoji. And

**[02:31]** when anything goes well, it seems to

**[02:33]** come across as being happy. The feeling

**[02:35]** of communicating with this agent through

**[02:37]** a messaging app does feel like something

**[02:40]** else. I mean, you can ask it the

**[02:42]** weather, you can ask it the time, you

**[02:43]** can ask it to book you a meeting, and it

**[02:45]** goes ahead and does it like a real

**[02:47]** personal assistant, but it doesn't

**[02:49]** sleep, it doesn't eat, and it works

**[02:51]** 24/7. This all sounds too good to be

**[02:53]** true, but it does have some security

**[02:56]** issues, which I'll talk about later. For

**[02:58]** now, let's go through how this actually

**[03:00]** works. So the kind of main part of

**[03:02]** Claudebot is the gateway demon which

**[03:05]** contains things like the dashboard, the

**[03:07]** web-based UI you can use to configure

**[03:09]** Claudebot, the websocket server which

**[03:12]** are both exposed on this port vocoock

**[03:14]** and HTTP and give access to different

**[03:17]** things like clients which is used by the

**[03:20]** TUI so the terminal interface to talk to

**[03:23]** agents and also the website. Then there

**[03:25]** are nodes which give Claudebot native

**[03:28]** functionality to things like camera and

**[03:31]** canvas for the native Mac, iOS and

**[03:33]** Android app. Then there are the channels

**[03:36]** which you'll be the most familiar with.

**[03:37]** These are things like WhatsApp,

**[03:39]** Telegram, Discord and so on. And they

**[03:42]** don't connect to Claudebot through the

**[03:43]** websocket server, but they have a

**[03:45]** channel manager which uses channel

**[03:47]** specific libraries. So Grammy for

**[03:49]** Telegram, DiscordJS for Discord and so

**[03:52]** on. Now from here there's the agent's

**[03:54]** runtime powered by PI which is a popular

**[03:57]** agentic tool that creates an in-memory

**[03:59]** session for the agent communication and

**[04:02]** can handle tool skills and per session

**[04:04]** cues. There's also a router to handle

**[04:06]** multi- aent communication but this is

**[04:08]** what connects to the cloud. I don't know

**[04:10]** why this is a basketball. It's supposed

**[04:12]** to be a globe but the cloud agents. So

**[04:14]** if you're using anthropic or open AI

**[04:17]** LLMs this will be what interfaces with

**[04:19]** them. or if you have local models like

**[04:21]** Oola then this takes care of that. There

**[04:23]** are also hooks and other things that the

**[04:25]** gateway demon takes care of. But for

**[04:27]** now, let's focus on the session manager

**[04:29]** which manages the sessions between the

**[04:31]** agents and also the storage and state

**[04:34]** which is what you want to protect if you

**[04:36]** have a VPS or anything like that from

**[04:38]** hackers because this is what stores the

**[04:40]** clawbot configuration your or tokens so

**[04:43]** your anthropic openai or tokens and also

**[04:46]** the transcripts from the sessions that

**[04:48]** you have with the agent. This is usually

**[04:50]** stored in theclawbot directory. As you

**[04:53]** can imagine, there will be problems with

**[04:54]** running claudebot on a VPS because the

**[04:57]** IP address is public and if you expose

**[04:59]** your gateway, then anyone can access

**[05:02]** your bot or try to break into it, which

**[05:05]** is what happened to me. For the most

**[05:06]** part, running the gateway locally should

**[05:08]** alleviate most of the issues. But you

**[05:10]** can also install something like tail

**[05:12]** scale to make your network more secure,

**[05:14]** which is what I did the second time

**[05:16]** round. Let me show you. After installing

**[05:18]** it on your server and the machine you

**[05:20]** want to access Claudebots from, Tails

**[05:22]** scale can lock things down so that only

**[05:24]** these two machines can talk to each

**[05:26]** other and no one from the outside world

**[05:28]** can access them. And with SSH enabled, I

**[05:31]** can make it so that only machines in my

**[05:33]** network can SSH into the Claudebot

**[05:35]** server, which means I can disable public

**[05:38]** SSH access. And if I use SSH tunneling

**[05:41]** to access the Claudebot dashboard, I

**[05:43]** could just use the tail scale addresses

**[05:45]** or use tailscale serve to expose the

**[05:48]** dashboard, but just to my network. You

**[05:50]** could even use Claudebot to configure

**[05:51]** Tailscale itself for the dashboard and

**[05:54]** the websocket part. But of course, you'd

**[05:56]** have to manually sign up and connect the

**[05:58]** machines you want to access it from. I

**[06:00]** would also recommend creating API keys

**[06:03]** just for Clausbot so that if they get

**[06:05]** compromised, you can remove them and

**[06:07]** create another one. Also, if you add any

**[06:09]** sensitive data to the chat, then it

**[06:12]** makes sense to go through and scrub that

**[06:13]** in case that gets compromised as well.

**[06:15]** And finally, the Claudebot CLI does have

**[06:18]** a security command which can be used to

**[06:21]** fix issues automatically. But even with

**[06:23]** all these things in place, the biggest

**[06:26]** security issue by far is prompt

**[06:28]** injection. Since the agent can read,

**[06:30]** download, and search the internet,

**[06:32]** people can insert malicious prompts into

**[06:35]** files, emails, or anything. And the

**[06:37]** agent that has full access to your

**[06:39]** system can execute these prompts.

**[06:41]** Someone used Claudebot to download

**[06:43]** malware to the system from a pull

**[06:45]** request by leaving encoded instructions

**[06:47]** in a URL, making it easy to miss. The

**[06:50]** YouTuber Low Level mentioned his friend

**[06:52]** installed Claudebot and it read an email

**[06:55]** from his wife telling Spotify to play

**[06:57]** EDM music and because the agent had

**[07:00]** access to Spotify, it went ahead and did

**[07:02]** that. I know, scary stuff. And there are

**[07:05]** things popping up over the internet all

**[07:07]** the time. I'm sure models will get

**[07:09]** better at detecting these sorts of

**[07:11]** things, but you know what hackers are

**[07:12]** like. They'll always find a way.

**[07:14]** Overall, I think Claudebot is still

**[07:17]** super impressive. Sorry, Maltzbot just

**[07:19]** isn't as good of a name. I think it's a

**[07:22]** great way to expose people to what these

**[07:24]** amazing models are capable of when

**[07:27]** giving the access. But personally, I

**[07:29]** don't feel comfortable giving these

**[07:31]** models my personal information. Maybe

**[07:33]** that might change in the future, but

**[07:35]** right now I'm a bit apprehensive. But

**[07:38]** there is hope, I think, because if big

**[07:40]** companies see that users are happy to

**[07:43]** give agents full access to their system

**[07:45]** and personal information to do things

**[07:47]** like book flights, meetings, and

**[07:49]** basically organize their life, then they

**[07:52]** may put more effort into the personal

**[07:54]** assistant side of LLMs, like co-work,

**[07:57]** but make them much better and also find

**[08:00]** ways to get around these security

**[08:01]** issues. Speaking of security issues, if

**[08:03]** you're building apps for AI, then you

**[08:06]** should definitely check out Better

**[08:07]** Stack, which is a tool that can use

**[08:09]** anomaly detection to pick up on weird

**[08:12]** things happening to your servers, can

**[08:13]** use AI native error tracking to spot

**[08:16]** errors on your front end, and can let

**[08:18]** you know as soon as your site or project

**[08:20]** goes down through its amazing uptime

**[08:23]** monitoring system. So go ahead and check

**[08:25]** out Better Stack


---

*Generated by YouTube Transcript Summarizer*
