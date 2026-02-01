# YouTube Video mDsyFrQPPfg

**Original Video**: [https://www.youtube.com/watch?v=mDsyFrQPPfg](https://www.youtube.com/watch?v=mDsyFrQPPfg)
**Generated**: 2026-01-28
**Video ID**: mDsyFrQPPfg
**Language**: English -> Korean

---

## Summary

이 영상은 Moltbot(구 Clawdbot)이라는 AI 에이전트를 안전하고 쉽게 설정하는 방법을 다룹니다. 발표자는 가상 머신(UTM)을 사용하여 보안 리스크를 최소화하고, Zapier의 MCP(Model Context Protocol)를 통해 복잡한 API 설정 없이 8000개 이상의 앱과 연동하는 방법을 시연합니다. 실제 컴퓨터를 손상시킬 위험 없이 AI가 브라우저를 제어하고, 이메일을 작성하고, Notion 페이지를 만들고, 음성을 생성하는 과정을 보여줍니다.

---

## Key Points

- Moltbot은 컴퓨터를 제어할 수 있는 Claude 기반 AI 에이전트로, 사용자에 대한 모든 것을 기억함
- 주요 문제점: 보안 리스크와 복잡한 설정 과정(Google Cloud Console, API 키 등)
- 해결책: UTM 가상 머신으로 실제 컴퓨터를 보호하면서 실험 가능
- Zapier MCP를 사용하면 한 번 로그인으로 8000개 이상의 앱 연동 가능
- 별도의 Mac Mini나 VPS 서버 구매 불필요
- 영상 전체 작업 비용은 단돈 $0.77
- 이메일 프롬프트 인젝션 해킹 취약점이 존재하여 가상 환경 사용이 중요

---

## Main Content

### Section 1: 문제 정의
- **보안 우려**: AI에게 컴퓨터의 전체 제어권을 주는 것은 위험함
- **복잡한 설정**: Gmail, 캘린더 등 기본 기능을 위해 Google Cloud Console에서 API 키 설정 필요
- **해킹 취약점**: 이메일 프롬프트 인젝션을 통한 해킹 사례 존재
- Gmail, Slack, Notion 등 모든 계정 키를 Moltbot에 직접 제공하는 것은 위험

### Section 2: UTM 가상 머신 설정
- **UTM 앱**: 무료 오픈소스 앱으로 Mac 안에서 macOS 실행 가능 ("Mac Inception")
- **설치 과정**:
  - UTM 다운로드 후 Applications 폴더로 드래그
  - "새 가상 머신 생성" 클릭
  - Virtualize 옵션 선택 (Emulate가 아닌)
  - macOS 12+ 사전 구성 선택
  - 메모리, CPU 코어는 기본 설정 사용
  - 몇 분 안에 가상 macOS 생성 완료
- **장점**: AI가 문제를 일으켜도 가상 컴퓨터의 파일만 삭제되고 실제 Mac은 안전함
- Mac Mini 구매나 클라우드 VPS 서버 설정 불필요

### Section 3: Zapier MCP 설정
- **MCP란**: Model Context Protocol - 범용 어댑터 역할
- **장점**: 
  - 한 번 로그인으로 수천 개의 앱 사용 가능
  - Zapier 무료 플랜에서도 작동
  - 8000개 이상의 통합 앱 제공
  - 보안 키가 Zapier에 저장되고 Moltbot에는 저장되지 않음
- **초기 설정**:
  - Zapier 계정에서 MCP 클라이언트로 "Other" 선택
  - "Molty Server"로 이름 지정
  - 첫 번째 도구로 Gmail 초안 작성 추가 (안전한 기능부터 시작)

### Section 4: 가상 Mac 기본 설정
- 새로운 Mac처럼 초기 설정 진행
- Mac 이름을 "Molty"로 지정
- Apple 계정 설정은 나중으로 미룸
- 다크 모드 선택
- Chrome 브라우저 다운로드 (Moltbot이 제어할 수 있도록)

### Section 5: Moltbot 설치
- **설치 과정**:
  - Moltbot 웹사이트에서 한 줄 명령어 복사
  - 가상 Mac의 터미널 열기
  - 명령어 앞에 `sudo` 추가하여 권한 부여
  - 원라인 설치로 모든 종속성 자동 설치
- **초기 구성**:
  - 강력하고 위험하다는 경고에 동의
  - Quickstart 옵션 선택
  - AI 제공자로 Anthropic 선택
  - Claude Console에서 API 키 생성 및 입력
  - 모델로 Claude Sonnet 4.5 선택

### Section 6: Telegram 연동
- **설정 이유**: 전 세계 어디서나 Moltbot에 메시지 가능
- **설정 과정**:
  - Telegram에서 Botfather와 채팅
  - `/newbot` 명령어 실행
  - 봇 이름을 "molty_dude"로 지정
  - 생성된 토큰을 Moltbot에 입력

### Section 7: 스킬 구성
- **설치할 스킬**: mcporter (Zapier MCP와 인터페이스하기 위한 유일한 필수 스킬)
- **거부한 옵션들**:
  - Google Places - 아니오
  - Gemini - 아니오
  - OpenAI - 아니오
  - Whisper - 아니오
  - ElevenLabs - 나중에 추가 가능
- Gateway 서비스 설치로 상호작용 가능

### Section 8: Moltbot 첫 상호작용
- **"해칭" 순간**: Moltbot이 깨어남
- **메모리 기능**: 사용자에 대한 모든 것을 기억
- **개인화**:
  - AI 이름을 "Papaya"로 지정
  - 사용자 이름을 "Mike"로 설정
  - "친근하고 소문자로만 말하기" 요청 → 즉시 적용됨
- Telegram에서 채팅 작동 확인

### Section 9: Zapier MCP 연결
- "Zapier MCP에 연결할 수 있어?" 요청
- Moltbot이 자동으로 MCP 도구 확인
- Zapier에서 연결 세부정보 및 토큰 생성
- 토큰을 Moltbot에 전송
- Moltbot이 자동으로 Zapier MCP 서버 추가
- 사용 가능한 도구 확인 (Gmail 초안 작성)

### Section 10: 첫 번째 작업 테스트
- **요청**: "파파야의 건강상 이점에 대한 이메일 초안 작성"
- **실행 과정**:
  - Moltbot이 가상 Mac에서 작업
  - 실제 Mac으로 언제든 전환 가능
  - Gmail 초안 생성 완료
- **결과**: 실제 Gmail 계정에 "파파야의 놀라운 건강상 이점 발견" 제목의 초안 생성됨

### Section 11: 추가 도구 연동
- **추가한 앱들**:
  - Notion (모든 도구 선택)
  - ElevenLabs (모든 도구 선택)
- 몇 번의 클릭만으로 Gmail, Notion, ElevenLabs가 Moltbot에 연결됨

### Section 12: 복잡한 작업 실행
- **첫 번째 복합 작업**:
  - 요청: "웹에서 멋진 이미지가 있는 파파야에 대한 Notion 페이지 만들기"
  - 추가: "ElevenLabs를 사용하여 파파야에 대한 10초 음성해설 만들기"
  - 방법을 구체적으로 알려주지 않음
- **실행 과정**:
  - Moltbot이 Notion과 ElevenLabs 도구 발견
  - 가상 Mac에서 브라우저 자동 열기
  - 키보드 입력 없이 인터넷 검색하여 파파야 이미지 수집
  - 1분 만에 작업 완료
- **결과**:
  - 파파야 이미지와 정보가 포함된 Notion 페이지 생성
  - ElevenLabs에서 음성해설 생성 (비타민 C, 파파인 효소, 항산화제 등 설명)

### Section 13: 메모리 기능 테스트
- **두 번째 요청**: "섬뜩한 목소리로 10초짜리 뭔가 만들어서 만든 Notion 페이지에 임베드해줘"
- **지능 확인**:
  - 이미 ElevenLabs와 Notion 접근 권한이 있다는 것을 기억
  - "Hades" 음성 선택 (섬뜩한 음성)
  - 기존 파파야 페이지 자동 찾기
  - 오디오 임베드 추가
- **결과**: 
  - Notion 페이지에 "Listen to the Dark Side of Papaya" 섹션 추가
  - "부드럽고 주황색 과육이 고대의 비밀을 감춘다..." 등의 섬뜩한 내용

### Section 14: 비용 분석
- **전체 영상 작업 비용**: $0.77
- 하루 종일 많이 사용하면 비용이 증가할 수 있음
- 생산성 향상을 고려하면 가치가 있을 수 있음

### Section 15: 주요 장점 요약
- **메모리**: Moltbot이 사용자에 대한 모든 것을 기억
- **보안 접근**: Zapier MCP 서버를 통한 안전한 앱 접근
- **샌드박스 환경**: UTM으로 실제 컴퓨터를 건드리지 않음
- **자동화 능력**: Chrome 제어, 파일 시스템 접근 등
- **확장성**: 필요에 따라 도구를 점진적으로 추가 가능

### Section 16: 마무리
- 모든 사용 도구 링크가 설명란에 제공됨
- 따라하기 튜토리얼 링크 제공
- 시청자들에게 Moltbot 사용 경험 공유 요청

---

## Timeline

- **00:00**: Hey, I'm Mike, and everyone is obsessed
with Moltbot right now. Formerly known as Clawdbot, but for obvious trademark
sensitivities, it's now Moltbot....
- **05:00**: So I'll go for Anthropic. Now this is the only technical bit. I simply need to log in to the Claude
Console with my Claude account. Now that I've done...
- **10:00**: Computer over here. And what do you know
multi has use the Zapier MCP to access the create draft feature
only of my Gmail account to create this amazi...

---

## Full Transcript

**[00:00]** Hey, I'm Mike, and everyone is obsessed
with Moltbot right now.

**[00:03]** Formerly known as Clawdbot,

**[00:05]** but for obvious trademark
sensitivities, it's now Moltbot.

**[00:09]** It's essentially Claude with hands.

**[00:10]** It lives on your computer, remembers

**[00:11]** everything about you,
and pretty much can control everything.

**[00:15]** But if you're like me,
you've probably got two problems.

**[00:17]** One, that's a security nightmare.

**[00:19]** Giving an AI full control of my computer
is just terrifying.

**[00:25]** And two, it's really complicated.

**[00:27]** I mean, setting up some of these skills,
like reading your email requires

**[00:31]** going into Google Cloud Console,
setting up API keys,

**[00:34]** and that's just to check emails
and do calendar entries.

**[00:37]** No thank you.

**[00:39]** So in this video
I'm going to do a non-technical lowest

**[00:43]** barrier to entry setup for Moltbot.

**[00:46]** Let's dive in.

**[00:47]** and I'm going to use this free
and open source app called UTM

**[00:50]** to run Mac OS inside my Mac.

**[00:53]** It's like Mac Inception,
and that's really cool

**[00:55]** because it means if the AI goes rogue,
it'll only mess up and delete

**[00:59]** files on your virtual computer,
not your actual Mac.

**[01:02]** So those people going out, buying
Mac Minis,

**[01:04]** or setting up VPS servers in the cloud,
you really don't need to do that.

**[01:09]** Just use UTM.

**[01:10]** Okay, so I downloaded UTM it’s
just a simple case of drag

**[01:14]** into my applications
folder and running the app.

**[01:16]** Okay, and it's a really simple app.

**[01:18]** I just click
create a new virtual machine right here.

**[01:22]** And then I'm allowed to virtualize
or emulate.

**[01:24]** I suggest virtualizing,
especially if you're cloning macOS,

**[01:28]** and we'll go for the preconfigured
macOS 12+.

**[01:32]** Absolutely perfect.

**[01:33]** Now I can choose how much memory,
how many CPU cores to assign.

**[01:37]** I'm going to leave everything. Default is
I've found those settings.

**[01:39]** Worked quite well.

**[01:40]** Will continue and continue again
and continue again and save.

**[01:45]** And that's all I needed to do.

**[01:47]** And now look at this.

**[01:48]** In just a few minutes,
macOS will be cloned inside my computer

**[01:53]** and I'll have a virtual computer
to set up on.

**[01:57]** Staying with security for a moment,

**[01:58]** this dude found out how to hack Clawdbot
or Moltbot as it's known now

**[02:02]** with email prompt injection,
and it's pretty terrifying.

**[02:06]** This is exactly why we're setting up
a virtual machine to run it

**[02:10]** on, so we can experiment with safety.

**[02:13]** now I don't want to give it all the keys
to my kingdom

**[02:15]** like Gmail, slack, notion,
and everything else.

**[02:18]** That's really a security risk.

**[02:20]** And I don't know if I trust mobile yet.

**[02:21]** I can use one secure
way called the Model Context Protocol.

**[02:25]** Think of this as a universal adapter.

**[02:27]** You log in once, and suddenly thousands
of apps become available to Moltbot.

**[02:32]** So let's set this up in my Zapier account.

**[02:34]** This works, by the way, on the free

**[02:36]** Zapier plan, which is awesome,
and Zapier has 8000+ integrations.

**[02:40]** That's plenty of hands for Moltbot,
so I'll select other for the MCP client.

**[02:44]** I can give it a name.
We can. Actually call it.

**[02:47]** Molty Server. That'll be fine.

**[02:49]** And we'll create.

**[02:50]** Okay. You'll see as I created
I can add a tool.

**[02:53]** So let's add one tool for mobile to have
just while I build up some trust.

**[02:57]** And then we can add some more later
add tool.

**[02:59]** We'll go to Gmail

**[03:01]** and I'll do something safe like creating
drafts with my Gmail account.

**[03:05]** But look, just as I was showing you
that my virtual machine has been created.

**[03:08]** So I now just hit the play button
inside this UTM app,

**[03:11]** confirm with okay,
and wait for the installation to complete.

**[03:15]** It should take just a minute or two.

**[03:17]** I'm sure many of you will be familiar
with this screen.

**[03:19]** I'm literally setting up a Mac inside
my Mac here, just as you would.

**[03:24]** This is cleaner, safer,
and infinitely easier to get working.

**[03:28]** I'll set it. Up as a new Mac.

**[03:30]** I can give my Mac
a name, let's call it Molty

**[03:33]** and give it a nice icon and continue.

**[03:36]** So here's
the prompt for the Apple account.

**[03:37]** Which will of course set up later.

**[03:39]** Yes, we do want to skip
that. Dark mode of. Course.

**[03:42]** And here it is.

**[03:43]** Our brand new clean Mac inside of Mac.

**[03:45]** Ready for Moltbot?

**[03:46]** First, I'll do something that.

**[03:47]** Most people do on a new Mac.

**[03:49]** Download Chrome.

**[03:51]** This is cool because mobile will be able
to control my Chrome.

**[03:54]** Browser later on.

**[03:55]** So I'm getting this.

**[03:56]** All set up ready for Molty. Okie.

**[03:59]** So let's get this up and running
I've gone to the website for Moltbot.

**[04:01]** And you'll find if I scroll down here,
there is just a single command to run.

**[04:06]** I copy that and I open my Mac terminal.

**[04:09]** This is,
of course, the terminal on my virtual Mac.

**[04:11]** And I just put sudo before the command
to make sure it has privileges

**[04:14]** to install, type
in my super secure password and mode.

**[04:17]** But we'll do a one line install.

**[04:20]** That's right.

**[04:21]** It's now installing everything for me,

**[04:23]** so it should be up and running in
just a minute or so.

**[04:25]** All right.

**[04:26]** Look at this.

**[04:26]** It's very nearly finished up now
installing mobile.

**[04:29]** It's done all the dependencies because
this one line command installs everything.

**[04:34]** And look at this
mobile has been installed.

**[04:37]** Now, I do have to agree this is powerful
and risky and that I want to continue.

**[04:41]** Well, thankfully I'm using an MCP
to give my keys and a virtual machine

**[04:46]** inside my Mac so that it can't touch
any of my real computer.

**[04:50]** I'll click yes.

**[04:51]** I'll also go for the quickstart,
and I need to choose an AI provider.

**[04:56]** This is the AI model
that will power my Moltbot.

**[05:00]** So I'll go for Anthropic.

**[05:02]** Now this is the only technical bit.

**[05:04]** I simply need to log in to the Claude
Console with my Claude account.

**[05:07]** Now that I've done that,
I just click into API keys.

**[05:10]** And I'll create a brand new key.

**[05:11]** I pasted that in
and it's asking me to select a model.

**[05:14]** I'll go for Claude Sonnet 4.5.

**[05:16]** And now finally for the quickstart,

**[05:18]** we'll just hook up Telegram
because it's the easiest one to do.

**[05:20]** So I can actually message my mobile
from anywhere in the world.

**[05:24]** and you'll see here it gives me
very simple setup instructions.

**[05:27]** I've just got to open Telegram, chat

**[05:29]** with the Botfather, make a new bot,
get the token and paste it in there.

**[05:33]** This is the last technical thing
you'll need to do before your mobile app

**[05:36]** will come to life.

**[05:38]** Okay, I'm inside Telegram and I'm going
to start my chat with the Botfather.

**[05:42]** I'm gonna do the forward slash
command. New bot.

**[05:44]** call it molty_dude.

**[05:47]** Okay.

**[05:47]** But father gave me a nice token
that I can now paste

**[05:51]** into Molty here and hit enter.

**[05:54]** With that done
we're nearly at the finish line.

**[05:55]** Let me make this terminal
a little bit bigger.

**[05:57]** And the text on screen even bigger.

**[05:59]** Because these are the final set up pieces.

**[06:02]** Before I can start chatting.

**[06:03]** So configuring skills I will say yes
and we'll stick with the default npm

**[06:07]** as preferred.
Now it seems overwhelming here.

**[06:10]** There are so many skills
that you can install, but the only thing

**[06:13]** we're going to need to give 8000
plus integrations is the mcporter skill.

**[06:18]** That is the way we can interface
with the Zapier MCP

**[06:22]** and talk to any application we want to.

**[06:25]** So I hit space on mcporter and hit enter.

**[06:28]** It's installing it for me now.

**[06:30]** Now it's going to ask me
a bunch of other questions.

**[06:32]** I'll say no to Google places, no
to this one, no to Gemini, no to OpenAI.

**[06:38]** No to whisper, no to ElevenLabs.

**[06:40]** We're just sticking with the Zapier MCP
integration and then finally enable hooks.

**[06:46]** We'll say skip for now,

**[06:48]** and you'll see here it's
now installing the gateway service.

**[06:51]** This is the final part that allows me
to start interacting with Molty.

**[06:55]** Okay. It says it's installed.

**[06:57]** Yeah.

**[06:57]** It's running in the background
on my new virtual Mac.

**[07:00]** And this is the final thing
the Tamagotchi moment I can hatch Moltbot.

**[07:05]** Now? Wow.

**[07:06]** Blinks awake.

**[07:07]** I just came online.
It's a fresh workspace.

**[07:09]** No memory yet. This is one of the cool
things about mobile.

**[07:12]** It remembers everything about you,
who you are and how you work.

**[07:16]** So who am I and. Who are you? Right.

**[07:18]** This is really cool.

**[07:19]** I'm going to say you,
papaya and I am Mike.

**[07:24]** If you like what you see so far,
throw a like. Subscribe.

**[07:27]** I do videos like this weekly
and if you want to follow along

**[07:30]** yourself, I'm
going to link up a tutorial down below.

**[07:33]** Okay, Mike, nice to meet you.

**[07:34]** So I'm papaya, you’re Mike.

**[07:36]** Let me figure out the rest.

**[07:37]** You.

**[07:39]** Should be super chill and talk.

**[07:43]** Only in lower.

**[07:45]** Case. Please.

**[07:47]** Oh wow. Okay.

**[07:49]** So it's updated its sole markdown
file. Wow.

**[07:53]** We're connected.

**[07:54]** Telegram is working perfectly
I can chat from here.

**[07:57]** Let's try something else. How you doing?

**[08:00]** Doing good.

**[08:00]** Woke up five minutes ago.

**[08:02]** Figured out I'm Papaya and your Mike.

**[08:04]** We're best friends. Telegram's connected.

**[08:06]** Pretty productive.

**[08:07]** First day of experience? I'd say so.

**[08:09]** So now let's
do the final piece in the puzzle

**[08:12]** and see if we can get the Zapier MCP
so we can connect to anything.

**[08:16]** With all of my secure keys stored inside

**[08:20]** Zapier and not stored inside Moltbot.

**[08:23]** I'll say, can you connect to my Zapier?

**[08:27]** MCP?

**[08:29]** Now, I'm not telling it how to do it.

**[08:31]** I'm just saying
if my new Moltbot can do it for me.

**[08:34]** Okay, it's replied to me.
It said it's checking the MCP tools.

**[08:37]** Nice MCP service already set up.

**[08:40]** This is cool.

**[08:40]** And it says no service configured yet.

**[08:42]** Okay, well this is great.

**[08:44]** Let's
go back to my configuration in Zapier.

**[08:47]** And this is where I now click the connect
details, generates a token inside Zapier.

**[08:52]** Then we're going to copy all of this.

**[08:53]** and then we'll send. It off to Molty.

**[08:56]** Give it a moment and cool.

**[08:57]** Let me add the Zapier and MCP server.

**[08:59]** It's doing it for me

**[09:01]** now I don't need to be technical
because it's figuring it all out.

**[09:05]** Nice. Let me see what tools Zapier has.

**[09:07]** This is really cool.

**[09:07]** All of this

**[09:08]** running on my virtual Mac, by the way,
which makes it super safe and secure.

**[09:13]** And it can actually see that
everything is hooked up.

**[09:15]** And I've added the Gmail create draft,
so let's give it a go.

**[09:19]** So I'll say yeah draft email about.

**[09:23]** Health benefits.

**[09:25]** Of papaya.

**[09:28]** And we'll see if multi

**[09:29]** can do this
simple task for me using the Zapier MCP.

**[09:33]** Now at this stage it said, okay,
let me draft an email about my namesake.

**[09:37]** I'm going to actually make this virtual
machine big and the coolest thing

**[09:40]** now is this is Molty working away for me.

**[09:43]** But at any time I like I can swipe
and go straight back to my main Mac.

**[09:48]** This is the Mac.

**[09:49]** I actually work on all the time.

**[09:50]** Swipe again and I'm into Molty
and I can see Molty finish the work.

**[09:54]** It's draft an email with the subject.

**[09:56]** Discover
amazing health benefits of papaya.

**[09:59]** Let's
go ahead and check my email on my real.

**[10:02]** Computer over here.

**[10:03]** And what do you know
multi has use the Zapier MCP

**[10:08]** to access the create draft feature
only of my Gmail account

**[10:12]** to create this amazing health
benefit email.

**[10:15]** About papayas.

**[10:16]** This really is absolutely incredible.

**[10:19]** So let's go ahead and add
a few more hands to my mobile

**[10:22]** and see what I can make it do.

**[10:24]** Now, in order to do this
on my real computer,

**[10:26]** I'll go back to my Molty server
and I'll have some more tools.

**[10:30]** Let's add in my Notion.
And I'm feeling brave.

**[10:32]** So I'll just select.

**[10:34]** All the tools there
and connect them up to Molty.

**[10:37]** Let's add ElevenLabs
and have some fun here. again.

**[10:39]** We'll select all the tools
for ElevenLabs and connect

**[10:42]** and look at that
in just a few easy clicks.

**[10:44]** I've connected Gmail, Notion
and ElevenLabs to my Moltbot.

**[10:48]** Let's test it out.

**[10:50]** again swiping across to my mobile
and I'll say

**[10:53]** Make me a Notion page about papayas
with nice images from the web.

**[10:56]** And then a quick ten second voiceover
about papayas using ElevenLabs.

**[11:00]** Now notice
I'm not telling you how to do that.

**[11:03]** I'm hoping it'll just know that
it has access to these tools now via the.

**[11:08]** Zapier MCP.

**[11:09]** Server.

**[11:09]** use Zapier MCP
and hopefully now Molty will understand.

**[11:15]** And the best thing is it will remember
that it has access to these tools.

**[11:19]** So I shouldn't need to tell it again
and it's discovered perfect.

**[11:22]** You've got both Notion and ElevenLabs
hooked up.

**[11:25]** Let me grab some papaya
images with the browser.

**[11:27]** And look, it's actually
opening a browser on my virtual Mac.

**[11:30]** This is insane.

**[11:32]** Now, this is crazy
because I am not touching the keyboard,

**[11:35]** but my mobile is now
searching the internet

**[11:38]** and finding images
here to use on my Notion page.

**[11:42]** let me make a voiceover. This is insane.

**[11:44]** It's just chatting to me, keeping me up
to date on everything it's doing.

**[11:47]** And look at that
with just a minute of work

**[11:49]** I messaged a minute ago
and now it's already finished.

**[11:52]** Let's go and check Molty’s work.

**[11:54]** and look at this.

**[11:55]** A papaya image, a nice Notion page
all about papayas.

**[11:59]** This is absolutely insane.

**[12:01]** And let's check my ElevenLabs account
to listen to the voiceover

**[12:04]** that was generated. Papayas.

**[12:07]** These tropical beauties are loaded
with vitamin C,

**[12:10]** packed with digestive enzymes like papain
and bursting with antioxidants.

**[12:14]** because multi remembers
everything I'm just going.

**[12:16]** To say can make a creepy voice

**[12:20]** say something for ten secs

**[12:24]** and embed in Notion page you.

**[12:28]** Made.

**[12:29]** Let's see how intelligent multi is

**[12:30]** and whether it remembers
that it already has access to those tools.

**[12:34]** Okay. It's typing away.

**[12:36]** All right let's make something spooky.

**[12:38]** And it says nice I got the creepy voice
I picked Hades.

**[12:41]** Now let me find that papaya page
and it's adding the audio.

**[12:44]** This is really cool stuff.
It's trying to add it.

**[12:47]** And it tells me it's done.

**[12:48]** It added a creepy section
to the Notion page.

**[12:51]** So let me swipe back
and have a look at my lovely papaya page.

**[12:55]** Maybe I'll need to refresh it.

**[12:56]** And then I'm going to scroll down
and look at this.

**[12:58]** Listen to the dark side of papaya.

**[13:00]** Its flesh, soft and orange, conceals
secrets from ancient times.

**[13:05]** those dark hollow seeds.

**[13:08]** They remember everything.

**[13:10]** Once you taste it, there is no escape.

**[13:14]** know, you're

**[13:14]** probably wondering how much all of that
cost me for the duration of this video.

**[13:18]** Everything I did with mobile cost
exactly $0.77,

**[13:24]** so you can see if you're

**[13:25]** using this heavily throughout the day,
those bills will add up.

**[13:28]** But if it's changing your life
and making things easier for you,

**[13:32]** it's probably worthwhile.

**[13:33]** I think you can see where this is going.

**[13:37]** So not only does Moltbot
remember everything you tell it,

**[13:41]** not only can it have secure access
to your apps using the Zapier MCP server,

**[13:46]** but you can also put it

**[13:47]** in a sandboxed environment
so it can't touch your real computer.

**[13:51]** I mean, you saw it
there just controlling Chrome.

**[13:53]** It can also access the file system.

**[13:55]** It's nice and safe using the UTM app.

**[13:58]** And needless to say, I'll link
everything I've used down below

**[14:01]** so you can follow this guide
and try it out for yourself.

**[14:03]** Let me know how you get on with mo bots
and how you'll be using it

**[14:08]** in the comments down below.

**[14:09]** I'm really curious to hear
will you be using it

**[14:12]** and how already is it improving your life?

**[14:15]** Thank you so much for watching!

**[14:17]** And YouTube is showing a video
on your screen now you should watch next.

**[14:20]** Thanks.


---

*Generated by YouTube Transcript Summarizer*
