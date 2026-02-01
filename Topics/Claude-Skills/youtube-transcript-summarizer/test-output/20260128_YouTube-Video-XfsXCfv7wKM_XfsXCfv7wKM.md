# YouTube Video XfsXCfv7wKM

**Original Video**: [https://www.youtube.com/watch?v=XfsXCfv7wKM](https://www.youtube.com/watch?v=XfsXCfv7wKM)
**Generated**: 2026-01-28
**Video ID**: XfsXCfv7wKM
**Language**: English -> Korean

---

## Summary

이 영상은 React, Angular, Svelte 같은 모던 웹 프레임워크를 사용하여 Chrome 확장 프로그램을 개발하는 방법에 대해 설명합니다. Manifest v3에서도 프레임워크 사용이 가능하지만, 확장 프로그램의 각 컨텍스트(팝업, 콘텐츠 스크립트, 옵션 페이지)에 따라 적절한 프레임워크를 선택하는 것이 중요합니다. 외부 CDN에서 스크립트를 로드할 수 없고, 보안 정책으로 인해 번들러를 사용해야 한다는 제약사항도 함께 다룹니다.

---

## Key Points

- Chrome 확장 프로그램에서 React, Angular, Svelte 등 모던 웹 프레임워크 사용 가능
- Manifest v3에서도 프레임워크 사용 지원
- 확장 프로그램의 컨텍스트에 따라 적절한 프레임워크 선택 필요
- 팝업(popup)은 격리된 환경으로 복잡한 프레임워크 사용 가능
- 페이지 내 콘텐츠 주입은 빠른 렌더링을 위해 가벼운 프레임워크 권장
- 옵션 페이지도 격리된 환경으로 원하는 프레임워크 자유롭게 사용 가능
- 서버사이드 렌더링 중심 프레임워크는 확장 프로그램에 부적합
- CDN에서 스크립트 로드 불가능 - CSP(Content Security Policy) 제약
- ESBuild, Rollup, Webpack 같은 번들러 필수
- JSX 같은 템플릿 언어는 컴파일 단계 필요

---

## Main Content

### Section 1: 기본 개념 및 가능성
- Chrome 확장 프로그램에서 React, Angular, Svelte 등 모던 웹 프레임워크 사용 가능
- Manifest v3 버전에서도 문제없이 작동
- 다만 상황에 따라 좋은 선택과 나쁜 선택이 존재하며, 고려사항이 있음
- 실제 동작 예제: background.js가 index.html을 열고, index.html이 index.jsx 파일을 로드하는 구조

### Section 2: React 기본 예제
- 간단한 React 앱 구현 예제 제시
- JSX 템플릿 사용으로 컴파일 단계 필요
- ESBuild를 사용하여 빌드
- 브라우저에서 로드하면 "Hello World" 정상 표시
- 기본적인 프레임워크 통합이 잘 작동함을 증명

### Section 3: 팝업(Popup) UI 컨텍스트
- Google Dictionary 확장 프로그램을 예시로 사용
- 액션 아이콘 클릭 시 나타나는 팝업은 HTML과 JavaScript로 구성
- 완전히 격리된(isolated) 환경으로 페이지에 영향 주지 않음
- 복잡한 애플리케이션이 필요할 수 있어 강력한 프레임워크 사용이 합리적
- 성능을 고려해야 하지만 다른 컨텍스트보다 덜 민감함
- React는 부트스트랩 시간이 길 수 있지만 이 경우 합리적인 선택

### Section 4: 콘텐츠 주입(Content Injection) 컨텍스트
- 페이지에서 단어를 하이라이트하면 나타나는 팝업
- 매우 빠르게 표시되어야 하며, 여러 번 표시될 수 있음
- 무거운 프레임워크는 적절하지 않음
- Svelte나 바닐라 JavaScript가 좋은 선택
- Google Dictionary는 Mustache 템플릿 엔진 사용 (프레임워크 아님)
- 코드 구조화를 돕고 최종적으로 HTML을 페이지에 추가
- 주의사항: 페이지에 콘텐츠를 주입하면 페이지가 접근 가능
- 보안이 중요하다면 최소한 iframe 사용, 가능하면 아예 피하는 것이 좋음

### Section 5: 옵션 페이지(Options Page) 컨텍스트
- 완전히 격리된 페이지 환경
- script 태그 추가 가능하며 원하는 프레임워크 자유롭게 사용
- 팝업 케이스와 유사하게 개발자가 선호하는 것 사용 가능
- 성능 제약이 상대적으로 덜함

### Section 6: 피해야 할 프레임워크
- 서버사이드 렌더링(SSR)에 중점을 둔 프레임워크
- 복잡한 HTTP 라우팅 기능 중심 프레임워크
- 이유: 확장 프로그램은 완전히 클라이언트 사이드이기 때문
- 프레임워크 자체에 문제가 있는 것이 아니라 확장 프로그램 특성과 맞지 않음

### Section 7: CDN 및 보안 정책 제약사항
- 많은 웹사이트가 CDN에서 스크립트를 로드하는 script 태그 사용
- 개발자에게는 편리하지만 확장 프로그램에서는 작동하지 않음
- 엄격한 CSP(Content Security Policy)로 인해 외부 리소스에서 스크립트 로드 불가
- Web Extension Playground 예제: TypeScript 웹사이트에서 스크립트 로드
- 웹에서는 작동하지만 확장 프로그램으로 빌드 시 불가능
- 해당 스크립트를 번들링해야 함

### Section 8: 번들러의 필요성
- ESBuild, Rollup, Webpack 같은 번들러 사용 필수
- 외부 콘텐츠 로드의 보안 위험을 피하기 위한 요구사항
- Patrick Kentner의 관련 영상에서 더 자세한 정보 확인 가능
- 번들러를 통해 모든 의존성을 확장 프로그램 패키지에 포함시켜야 함

### Section 9: 결론 및 추가 리소스
- Chrome 확장 프로그램에서 프레임워크 사용 완전히 가능
- 추가 질문이나 특정 프레임워크에 대한 심화 내용 요청 환영
- Chrome for Developers 채널 구독 권장
- Developer Mode 시리즈에서 Chrome 확장 및 웹 확장 플랫폼 관련 질문 답변 제공

---

## Timeline

- **00:00**: You can build a Chrome extension with any modern web framework like React, Angular or Spelt. That's true even in manifest v3, but there are good and b...

---

## Full Transcript

**[00:00]** You can build a Chrome extension with

**[00:02]** any modern web framework like React,

**[00:04]** Angular or Spelt. That's true even in

**[00:06]** manifest v3, but there are good and bad

**[00:09]** choices and some interesting

**[00:11]** considerations. So, let's talk about

**[00:13]** that.

**[00:16]** [music]

**[00:19]** Welcome back to developer mode. This is

**[00:22]** the series where we answer your

**[00:23]** questions with a focus on Chrome

**[00:25]** extensions and the web extensions

**[00:27]** platform more broadly. Really quickly

**[00:29]** before we jump in, consider subscribing

**[00:31]** to the Chrome for Developers channel if

**[00:33]** you haven't already. We don't usually

**[00:35]** ask for that here, but it's a good way

**[00:36]** to see new videos in this series, new

**[00:39]** videos about other things happening in

**[00:40]** Chrome, and also to see YouTube shorts

**[00:42]** for some of the shorter or more fun

**[00:44]** content that we make. Getting back to

**[00:46]** frameworks, the easy answer is yes, you

**[00:49]** can absolutely use frameworks to build a

**[00:51]** Chrome extension. Let me actually give

**[00:53]** you a really quick example. So, I have a

**[00:56]** basic extension here. It has a

**[00:58]** background.js file that opens

**[01:00]** index.html.

**[01:01]** And then index.html has a script tag

**[01:04]** which is loading this index.jsx file.

**[01:07]** And this is a really simple react app

**[01:09]** which is just rendering hello world to

**[01:10]** the page. And then I have ES build since

**[01:13]** I'm using JSX for templating and that

**[01:15]** needs a compile step. And then I can go

**[01:18]** ahead and I can run this. I can load

**[01:20]** this in the browser. And you can see

**[01:22]** that the page opens and we see the hello

**[01:24]** world. So this works great. Now, there

**[01:27]** are lots of different contexts where an

**[01:28]** extension might want to show UI and

**[01:30]** there are some different considerations

**[01:31]** for the framework that you might pick in

**[01:33]** each case. So, let's talk through each

**[01:35]** of those. I have the Google dictionary

**[01:38]** extension installed in my browser. So,

**[01:40]** we can use that as quite a nice example.

**[01:42]** This is actually one that I helped to

**[01:44]** migrate to manifest v3 and I know how it

**[01:46]** works quite well.

**[01:48]** If I click the action icon, we can see

**[01:51]** the popup. And if I inspect the pop-up,

**[01:54]** you can see that this is just HTML and

**[01:56]** JavaScript. It's fully isolated, so

**[01:59]** whatever you run isn't going to bloat

**[02:01]** the page. And you might want a pretty

**[02:02]** complex application here. So using a

**[02:05]** framework which is very capable makes a

**[02:07]** lot of sense. Now, you still want to be

**[02:09]** mindful of performance, but I would say

**[02:10]** you don't need to worry as much here. My

**[02:13]** experience is that React can take longer

**[02:14]** to bootstrap than other options, for

**[02:16]** example, but I think it would be a

**[02:18]** reasonable choice here. If I go to a

**[02:20]** page and highlight a word, you can see

**[02:22]** this pop-up. This pop-up we want to show

**[02:25]** really quickly, and we might be showing

**[02:27]** multiple of these pop-ups over time, so

**[02:30]** a heavy framework probably isn't the

**[02:32]** right choice. Something like spelt would

**[02:34]** be great here, or even just vanilla

**[02:36]** JavaScript. In the case of the Google

**[02:38]** dictionary extension, we're using the

**[02:40]** mustache templating engine. So, actually

**[02:42]** not a framework at all, but it makes it

**[02:44]** a little easier to structure our code

**[02:45]** and ultimately just gives us HTML that

**[02:48]** we can add to the page. By the way,

**[02:50]** injecting content into the page means

**[02:52]** that the page has access to it. If

**[02:55]** that's a concern, consider iframes at

**[02:57]** the very least, or honestly, just try to

**[02:59]** avoid it entirely. That's a whole rabbit

**[03:01]** hole in itself. It could be a whole

**[03:03]** video, but if you're interested in

**[03:04]** hearing more about that, feel free to

**[03:06]** let me know in the comments. Let's also

**[03:08]** go to the extension and open up the

**[03:11]** options page. And this is again a fully

**[03:13]** isolated page. So I can add script tags

**[03:15]** and use whatever framework I prefer. I'd

**[03:18]** say this is more similar to the pop-up

**[03:19]** case where whatever works for you is

**[03:21]** probably okay. Now, there are some

**[03:24]** frameworks that you probably shouldn't

**[03:25]** pick. Not because there's anything wrong

**[03:27]** with them, but just because they don't

**[03:28]** make as much sense for extensions. For

**[03:31]** example, any framework that's focused

**[03:32]** heavily on serverside rendering or

**[03:34]** complex HTTP routting probably isn't a

**[03:37]** good fit since extensions are entirely

**[03:39]** client side. If you look at a lot of

**[03:41]** websites that include frameworks by

**[03:43]** adding a script tag that loads the

**[03:45]** framework from a CDN or content

**[03:47]** distribution network, that makes things

**[03:49]** easy for us as developers, but it

**[03:51]** doesn't work in extensions because we

**[03:53]** have a strict content security policy

**[03:55]** that prevents loading scripts from

**[03:56]** external resources. So, I have the web

**[04:00]** extension playground here, and it's

**[04:01]** loading a script from the TypeScript

**[04:03]** website. This works great here, but if I

**[04:05]** was building this as an extension, that

**[04:06]** wouldn't work, and I'd need to make sure

**[04:08]** I bundled that script. A bundler like

**[04:11]** ESB build, rollup, or Webpack can help

**[04:13]** with this. The reason we require it is

**[04:15]** to avoid the security risks with loading

**[04:17]** external content. Patrick Kentner from

**[04:20]** our team has a great video on that which

**[04:21]** you can watch if you want to learn more.

**[04:25]** Hopefully that answers the question. You

**[04:26]** can absolutely use frameworks to build a

**[04:29]** Chrome extension. If you have further

**[04:31]** questions about this, feel free to leave

**[04:33]** them below. I could also talk a lot more

**[04:35]** about specific frameworks if that would

**[04:37]** be interesting. Just let us know. Until

**[04:40]** next time.

**[04:42]** [music]

**[04:48]** >> [music]


---

*Generated by YouTube Transcript Summarizer*
