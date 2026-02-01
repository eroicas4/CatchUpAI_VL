# YouTube Video 5eN11aRvXhU

**Original Video**: [https://www.youtube.com/watch?v=5eN11aRvXhU](https://www.youtube.com/watch?v=5eN11aRvXhU)
**Generated**: 2026-01-28
**Video ID**: 5eN11aRvXhU
**Language**: English -> Korean

---

## Summary

이 영상은 Moltbot(구 Claudebot)이라는 오픈소스 AI 어시스턴트의 강력한 기능과 심각한 보안 취약점을 다룹니다. GitHub에서 폭발적인 인기를 얻은 이 도구는 메시지 전송, 웹 브라우징, 쉘 명령 실행 등 다양한 기능을 제공하지만, 보안 연구자가 수백 개의 노출된 인스턴스를 발견했으며, 제작자는 안전한 사용을 위한 여러 보안 지침을 제시합니다.

---

## Key Points

- Moltbot은 WhatsApp, Telegram, iMessage 등과 연동되는 강력한 오픈소스 AI 어시스턴트
- 로컬 연결을 자동 승인하는 설계로 인해 심각한 보안 취약점 존재
- 보안 연구자 Jameson O'Reilly가 수백 개의 노출된 인스턴스 발견
- 노출된 인스턴스에서 API 키, OAuth 인증 정보, 대화 기록 등이 평문으로 유출
- Signal 계정 전체 접근, 루트 권한 접근 등 심각한 보안 사고 가능성
- 역방향 프록시 사용 시 모든 연결이 로컬로 인식되어 공격자도 접근 가능
- AI 에이전트의 강력한 기능 자체가 보안 위험을 내포
- 안전한 사용을 위해서는 전용 하드웨어, 가상머신, 네트워크 격리 필요
- 인터넷 노출 금지, SSH 터널링 또는 Netbird 같은 VPN 사용 권장

---

## Main Content

### Section 1: Moltbot 소개 및 기능
- **기본 정보**: Anthropic의 요청으로 Claudebot에서 Moltbot으로 이름 변경
- **GitHub 인기**: 유례없는 속도로 스타 수 급증
- **주요 기능**:
  - 자체 하드웨어에서 실행
  - WhatsApp, Telegram, Nextcloud Talk, iMessage 등 메시징 서비스 연동
  - 메시지 전송, 캘린더 관리, 웹 브라우징
  - 쉘 명령 실행
  - 자체 플러그인 작성 가능
  - Claw skills와 호환

### Section 2: 보안 취약점 및 위험성
- **설계상의 문제**: 로컬 연결을 인증 없이 자동 승인
- **역방향 프록시 문제**: 
  - EngineX, Caddy 등 역방향 프록시 뒤에 배치 시
  - 외부 공격자의 연결도 로컬 연결로 인식
  
- **Jameson O'Reilly의 발견 사항**:
  - 수백 개의 노출된 Moltbot 인스턴스 발견
  - 대부분 인증이 전혀 없는 상태
  - Anthropic API 키가 평문으로 노출
  - OAuth 인증 정보 유출
  - 수개월간의 대화 기록 접근 가능
  - Signal 페어링 URI 노출로 타인의 Signal 계정 전체 접근 가능
  - 여러 시스템에 루트 권한 접근 가능

- **근본적인 문제**:
  - AI 에이전트가 전통적인 보안 모델을 설계상 위반
  - 메시지 읽기, 인증 정보 저장, 쉘 명령 실행, 지속적 상태 유지가 필수
  - 이러한 기능 없이는 도구가 무용지물
  - 보안을 강화하면 Claude Code를 쓰는 것과 다를 바 없음

### Section 3: 안전한 사용 지침
- **전용 하드웨어 사용**:
  - 모든 계정이 로그인된 주 컴퓨터에 설치 금지
  - 전용 하드웨어 또는 가상머신 사용 권장

- **격리 조치**:
  - 가상머신에서 실행하여 실제 시스템 접근 차단
  - VM이 손상되어도 영향 최소화
  - 별도 VLAN에서 네트워크 격리

- **인터넷 노출 방지**:
  - 절대 인터넷에 직접 노출 금지
  - SSH 터널링 사용
  - Netbird 같은 VPN 솔루션 직접 설치
  - WireGuard를 통한 직접 연결
  - SSO(Single Sign-On) 활용

### Section 4: 설치 및 실험 과정
- **설치 환경**: 전용 VM에 SSH 접속하여 설치
- **설치 과정**:
  - 강력한 권한에 대한 경고 메시지 표시
  - 서비스 프로바이더 선택 (제작자는 Anthropic 선택)
  - Ollama 등 로컬 AI 모델 사용도 가능하나 추가 설정 필요
  - 터미널로 대화 가능

- **Telegram 연동**:
  - 편의성을 위해 메시징 앱 연동
  - Bot Father를 통해 Telegram 연결
  - 다수의 사용자가 동시에 시도하여 사용자명 확보에 어려움

- **기능 설정**:
  - 사전 정의된 스킬 목록에서 선택 가능
  - CloudHub에서 추가 스킬 다운로드 가능
  - TUI(텍스트 사용자 인터페이스)를 통한 초기 설정
  - 신원 정보 입력

- **실험적 사용**:
  - VM 환경에서 sudo 비밀번호 비활성화 (실제로는 권장하지 않음)
  - 시스템 업데이트 명령 실행
  - Docker 설치 명령 성공
  - Netbird Docker 컨테이너 설치:
    - Netbird 설정 키 획득
    - AI에게 Docker 컨테이너로 Netbird 설치 지시
    - 성공적으로 설치 완료
    - 연결 통계 및 Netbird IP 확인
  - 서비스 노출 없이 Netbird로 직접 접속 가능

### Section 5: 결론 및 권장사항
- **실험 후 조치**: 모든 실험 후 VM 완전 삭제
- **향후 계획**: 6-7개월 후 프로젝트 성숙도를 지켜본 후 재평가 예정
- **프로젝트 특성**: 오픈소스 프로젝트로서 발전 가능성 존재
- **최종 권장**: 현재로서는 실험 목적으로만 사용하고, 실제 업무 환경에서는 신중한 접근 필요

---

## Timeline

- **00:00**: If you're a tech nerd like me and you've been on social media whatsoever, you've probably heard of Moltbot or formerly Claudebot before Anthropic forc...
- **05:00**: Docker. It did, which was cool. And then just just to test, this is the NetBird channel after all. I went ahead to Netbird, grabbed the setup key and ...

---

## Full Transcript

**[00:00]** If you're a tech nerd like me and you've

**[00:01]** been on social media whatsoever, you've

**[00:04]** probably heard of Moltbot or formerly

**[00:07]** Claudebot before Anthropic forced them

**[00:10]** to rebrand it. This tool is an open-

**[00:12]** source AI assistant and it has gotten a

**[00:15]** ridiculous amount of stars on GitHub.

**[00:17]** Probably the biggest jump that I have

**[00:19]** ever seen. It runs on your own hardware,

**[00:21]** connects to messaging services like

**[00:23]** WhatsApp, Telegram, whatever. Next cloud

**[00:25]** talk, which is pretty cool, even

**[00:27]** iMessage. And people like it because it

**[00:29]** actually does things. Messages,

**[00:32]** calendars, it could browse the web,

**[00:34]** execute shell commands. It could write

**[00:36]** its own plugins. It's compatible with a

**[00:39]** lot of the like claw skills. It on the

**[00:42]** surface looks like a really cool tool.

**[00:44]** But ignoring that, when you actually

**[00:46]** dive into what it does, the capabilities

**[00:47]** that you have to give it to really get

**[00:49]** the kind of feature list of

**[00:51]** functionality out of it, you should

**[00:53]** really really not just install it on

**[00:57]** your laptop with all your stuff logged

**[00:59]** into it. AI makes mistakes and giving it

**[01:01]** all that data and the ability to message

**[01:05]** people, change things, browse for you

**[01:08]** isn't a good idea. And that's just a

**[01:10]** little teeny problem with what's wrong

**[01:12]** with it. And that's u most people who

**[01:14]** are spinning this thing up are

**[01:16]** definitely not following good security

**[01:18]** practice. There's a great article

**[01:20]** security researcher Jameson O'Reilly.

**[01:23]** Basically in short he found hundreds of

**[01:25]** exposed instances of this software with

**[01:28]** many of them having absolutely zero

**[01:30]** authentication socket handshakes

**[01:33]** accepted and he had access meaning with

**[01:36]** some of these he had access to people's

**[01:38]** anthropic API keys ooth credentials just

**[01:42]** in plain text complete conversation

**[01:45]** histories going back months and one

**[01:47]** instance there was a signal pairing URI

**[01:50]** in a just readable file he could just

**[01:53]** open it and have full access to somebody

**[01:55]** else's signal account. And of course, he

**[01:57]** had full route access to multiple

**[01:59]** people's systems with, of course,

**[02:02]** command execution enabled. The real

**[02:04]** issue is Moltbot just auto approves

**[02:07]** local connections without

**[02:08]** authentication. And a lot of people are

**[02:10]** putting these connections behind reverse

**[02:12]** proxies such as EngineX, Caddy, so

**[02:15]** forth. So, every connection just looks

**[02:17]** local even from random attackers. AI

**[02:20]** agents like this violate traditional

**[02:22]** security models by design. Moltbot needs

**[02:25]** to read your messages, store your

**[02:26]** credentials, execute shell commands, and

**[02:29]** maintain that persistent state. Without

**[02:31]** all of those, the tool is basically

**[02:33]** useless, and the whole feature list is

**[02:37]** meaningless. If you really harden it and

**[02:39]** lock it down, you might as well just use

**[02:41]** claw code. The same capabilities that

**[02:43]** really truly make this powerful is what

**[02:47]** makes it something that is dangerous to

**[02:49]** use. if you don't know exactly what

**[02:52]** you're doing with that. I still wanted

**[02:54]** to try it out. It's worth playing around

**[02:56]** with. So, there are some key things to

**[02:59]** know if you are going to try this thing

**[03:01]** out for yourself. One, either use

**[03:04]** dedicated hardware specifically for it.

**[03:06]** Do not install it on your primary

**[03:08]** computer with all your stuff logged in.

**[03:09]** I would not do that. If you are going to

**[03:11]** run it, what you should do is run it in

**[03:13]** like a virtual machine so it really

**[03:15]** doesn't have access to anything. If it

**[03:17]** accidentally kills itself in the VM,

**[03:19]** it's fine. Isolating the network,

**[03:21]** running it in a separate VLAN is another

**[03:23]** really good step to do. And of course,

**[03:26]** never expose it to the internet. Either

**[03:28]** do SSH tunneling, use something like

**[03:30]** Netbird installed directly on it. So

**[03:33]** then you can just connect to it with

**[03:35]** WireGuard directly. That way, you got

**[03:37]** some good old SSO and all that fun

**[03:39]** stuff. When I went ahead and installed

**[03:40]** it, it was a fairly straightforward and

**[03:43]** easy process. I sshed into the VM that I

**[03:46]** set up specifically for it. It gave me

**[03:49]** this warning saying it's incredibly

**[03:50]** powerful. Be careful. So, I said yes.

**[03:53]** And then from there, it asks what

**[03:55]** service provider you're going to use. I

**[03:57]** went with Anthropic just to go ahead and

**[03:59]** test it out. There there is the ability

**[04:01]** to use local AI models, which is even

**[04:03]** better from like O Lama, but you do have

**[04:06]** to do some custom configuration to

**[04:07]** actually get those things to work. And

**[04:09]** then from there, of course, you could

**[04:10]** talk to it with the terminal. But the

**[04:12]** main kind of convenience factor of it is

**[04:15]** using some sort of app or messaging

**[04:17]** thing to communicate with it. So I just

**[04:19]** spun up an instance talked to the bot

**[04:22]** father and connected with Telegram.

**[04:24]** After of course trying numerous

**[04:26]** different usernames to try to get this

**[04:28]** spun up. Obviously everybody else is

**[04:31]** trying to do this too. From there you

**[04:32]** could set up some of their predefined

**[04:34]** skills just in a list. Of course you

**[04:36]** could use CloudHub to get more but they

**[04:38]** do have a nice list of things. And then

**[04:40]** you're done. It's installed. If you go

**[04:42]** ahead and jump on into the TUI, you

**[04:44]** could say hello, do a little more setup

**[04:46]** further, telling it who you are, who it

**[04:49]** is. Since I was in a VM, I experimented

**[04:51]** just a little bit and did something that

**[04:53]** you probably shouldn't do and disabled

**[04:54]** my pseudo password. So then I just tell

**[04:56]** it to update my system and stuff like

**[04:58]** that. And then I told it to install

**[05:00]** Docker. It did, which was cool. And then

**[05:02]** just just to test, this is the NetBird

**[05:05]** channel after all. I went ahead to

**[05:07]** Netbird, grabbed the setup key and told

**[05:09]** it, hey, spin up Netbird as a Docker

**[05:11]** container with the setup key and it

**[05:14]** worked perfectly. It was actually pretty

**[05:15]** cool. It gave me my connection stats, my

**[05:17]** Net Bird IP and all that fun stuff. So

**[05:19]** then theoretically I could use Netbird

**[05:22]** to connect directly to this machine

**[05:24]** without having to expose any services or

**[05:26]** anything like that. So that's something

**[05:28]** worth doing if you are going to do this.

**[05:31]** And then after all that, I nuked the VM

**[05:34]** because I'm not actually going to be

**[05:35]** using this for anything more than just

**[05:37]** mere experimentation. This is definitely

**[05:40]** a project I'm going to wait six, seven

**[05:43]** months to see how it matures, just just

**[05:45]** to see how it develops. I mean, it is an

**[05:47]** open- source project after all, which is

**[05:49]** great. Open source just like Netbird,

**[05:51]** which you should check out and subscribe

**[05:53]** to this channel so you don't miss any of

**[05:55]** our future videos. And with all that, I

**[05:58]** do hope you have an absolutely beautiful

**[06:00]** day. And goodbye.


---

*Generated by YouTube Transcript Summarizer*
