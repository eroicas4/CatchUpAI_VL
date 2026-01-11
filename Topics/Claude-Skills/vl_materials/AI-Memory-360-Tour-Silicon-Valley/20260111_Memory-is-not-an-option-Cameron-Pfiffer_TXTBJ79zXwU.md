# Memory is not an option - Cameron Pfiffer

**원본 영상**: [https://www.youtube.com/watch?v=TXTBJ79zXwU](https://www.youtube.com/watch?v=TXTBJ79zXwU)
**작성일**: 2026-01-11
**Video ID**: TXTBJ79zXwU

---

## 요약

Cameron Pfiffer는 인간의 기억을 완벽하게 보존하고 증강하는 "Memory Machines" 프로젝트를 소개합니다. 뇌과학 연구를 기반으로 개인의 모든 경험을 기록하는 'Memome(기억체)'을 구축하고, 인간이 모든 것을 기억할 수 있는 '기억 특이점(Memory Singularity)'을 실현하고자 합니다.

---

## 핵심 포인트

- 인간은 일상적으로 많은 정보를 망각하며, 핵심 문제는 저장이 아닌 '회상(recall)'에 있음
- 해마(hippocampus)의 신경세포들이 사건의 시간 순서를 어떻게 인코딩하는지 실험으로 입증
- AI 모델로 사람들이 무엇을 기억하고 잊을지 75% 정도 예측 가능
- 'Memome'은 개인의 모든 디지털 경험(대화, 이메일, 영상 등)을 포함하는 완전한 기억 기록
- 대규모 기억 모델(LMM) 개발을 위한 새로운 벤치마크와 데이터셋 구축 필요

---

## 주요 내용

### 섹션 1: 기억 상실의 보편성
- 기억 상실은 노인뿐만 아니라 모든 사람에게 일상적으로 발생
- '망각'은 정보 소실이 아니라 회상 실패인 경우가 많음
- 적절한 트리거를 통해 기억을 회상하도록 돕는 것이 인지 증강의 핵심

### 섹션 2: 뇌과학 기반 기억 메커니즘
- **시간 순서 인코딩 실험**: 해마의 개별 뉴런들이 사건의 순서(첫 번째, 두 번째 등)를 각각 담당
- 간질 환자의 뇌에 전극을 삽입해 개별 신경세포의 활동을 실시간 기록
- 특정 뉴런이 특정 순서의 이벤트에만 반응하는 패턴 발견

### 섹션 3: 기억 예측 AI 모델
- TV 시리즈 '24'를 시청한 51명의 참가자 대상 실험
- 프레임 단위로 무엇을 기억하고 잊는지 측정
- 컴퓨터 비전과 언어 모델을 결합해 단일 사건/개인에 대해 75% 정확도로 기억 여부 예측

### 섹션 4: Memome(기억체) 구축
- 개인의 모든 기억을 담는 완전한 조직화된 기록 시스템
- 게놈(Genome)과 유사한 개념으로, 모든 대화, 만남, 이메일, 책, 영화 등 포함
- 뇌의 정보 인코딩 메커니즘에서 영감을 받은 멀티모달 방식
- 모든 디지털 파일과 경험을 통합

### 섹션 5: 새로운 벤치마크의 필요성
- **컴퓨터 비전의 교훈**: MNIST에서 ImageNet으로의 발전이 분야를 변혁
- 현재 메모리 분야는 ImageNet 이전의 초기 단계
- 대규모 언어 모델(LLM)의 성공 요인은 방대한 데이터 활용
- 대규모 기억 모델(LMM) 개발을 위한 유사한 데이터셋과 벤치마크 부재

### 섹션 6: 벤치마크 설계 원칙
- **Ground Truth 접근**: 검증 가능한 정답 필요
- **개인화(Personal)**: 인간 기억 증강에 초점 (에이전트 메모리가 아님)
- **동적(Dynamic)**: 시간에 따른 변화 반영
- **접근 가능(Accessible)**: 개인 정보 보호하면서 커뮤니티 전체가 테스트 가능
- **대규모(Large)**: 소량의 샘플이 아닌 방대한 데이터셋

### 섹션 7: 개발 중인 데이터셋
- Abraham Lincoln Memome (역사적 인물 기반)
- 유명인 기반 Memome
- 개인 기반 Memome
- 광범위한 질문-답변 세트
- NeurIPS 워크숍에 벤치마크 관련 제안서 제출 예정

### 섹션 8: 비전과 목표
- **궁극적 목표**: 인간에게 완벽하고 무한한 기억 능력 부여
- **기억 특이점(Memory Singularity)**: 모든 것을 진정으로 기억할 수 있는 날
- 페니실린, DNA 이중나선, 달 착륙에 비견되는 혁명적 변화 예상
- 이미 필요한 도구들을 보유하고 있으며 실현 가능한 목표로 판단

---

## 타임라인

- **00:00**: All right, thank you very much for the organiz very very exciting. I hope that a few years from now we'll look back on this day as when everything really uh got started in the eyes. Uh I also want to give a a quick note to Charles and this world we converge on the memory machines a few weeks ago and it turns out that he's been using machines for for for many many years but anyway we'll uh we'll get to that. Um I want to talk about the the memory in garden and perhaps to give you a little bit of a different perspective on how uh we are thinking about memory uh together with who are here in the audience and are the true architects of everything that I'm going to be uh talking about. So um humans uh forget we forget things every day and our key goal is to augment human cognition and the memory similarity. I think we are not that far from the notion that uh very very soon we will be able to actually uh remember uh everything and that's our goal uh uh at memory machines. So uh first of all and this is uh basically stated several times already you are your memories Charles already said at the beginning in the morning and this is this is who you are basically. If I ask you about uh give me a recommendation for a good restaurant or if you think about the code that you've been read you've been writing uh or what you're going to do tomorrow. Uh this is the very essence of uh who you are and loss of memory uh is uh devastating uh both for uh the person themselves as well as uh for the uh loved ones. But memory loss is not just restricted to um all people. It turns out that uh all of us uh forget uh things constantly. In fact uh there are many quantitative studies that argue that we forget a huge amount of the information that we uh interact with uh on a on a daily basis. So it turns out that the word forgetting uh is a little bit of a misnomer. Sometimes we really...
- **05:00**: uh things uh happen and this is I just gave you a few examples. Here's a whole population of neurons. Some neurons encode what happens first, what happens next etc. So there are fundamental uh units in the brain that are encoding uh the temporal order in which uh things happen. So this is the kind of inspiration that goes behind some of the algorithms that we're building to represent uh uh the fundamental structures of uh memory uh based on uh neuroscience. I'll jump gears now to another vignette where we studied what people do and do not remember and this was a behavioral study where we built uh very simple machine learning algorithms to actually predict what people will remember or not under different circumstances. So in one of these experiments we had people watch a TV series in this particular case a TV series called 24 and we registered with very high uh resolution uh basically every part of the movie what people do or do not remember at different time points after watching this TV series. So what you're looking at here is a particular fragment of that movie from of that one of the episodes of this TV series from frame 55,000 to 56,000 or so. And each of the ticks corresponds to one particular event and whether people do remember that or not. This is participant 51. Here are 51 participants. And you can see that there's a huge amount of consistency from one participant to another in terms of what they remember or not. So here uh uh in this case this is the average across different participants. This is for another episode. And so we can measure very densely what will be remember and what will be uh forgot. And then we can build basic AI models to predict what's memorable or not. This is uh basically uh I won't go into a lot of the details but basically this is a combination of computer vision language uh trying to decode from the content and...
- **10:00**: time and be dynamic uh and incorporate the changes over time that are fundamental to memory. Uh they need to be accessible. So uh I cannot quite share my entire personal history uh with everyone. So we need memor that are accessible for testing for the entire community. Uh and importantly they have to be large right. So we cannot work with data set that has you know a hundred snippets of conversation and then few questions and answers on on on that. So here's a couple of things that we're developing. One is the Abraham Lincoln uh memor uh another one is celebrity based memors uh personal based memors and fundamental list of uh uh extensive questions and answers that we can all test our algorithms uh uh on. So we're going to be submitting a proposal for Europe's workshop uh on benchmarks for memory and would like to invite everyone who's interested in collaborating with us on this. Uh uh I think this is going to benefit all of us uh first of all in defining what data sets we need for training models. Second in evaluating uh rigorous uh benchmarks uh that that we can all uh then compare uh nodes uh with. So uh just to close our vision is to endow humans with perfect and infinite memory. We want to augment uh human condition. We want to make you uh superhuman. Uh and to go back to the title, uh we think that we're not very far from uh what I call the memory singularity. Uh perhaps it's a bit grandiose to put that on par with peniselline, the DNA double helix, and the moon landing. But I do think that all of our lives and the world will be transformed in a fundamental way uh the way the day we can actually uh truly remember uh everything. And I think that we actually have the tools to build that and to allow uh and enable all of you to uh remember absolutely everything. Uh here's part of our team, half of which is actually here and and I'd like to encourage all of you to talk to to them...

---

## 전체 자막 (타임스탬프 포함)

**[00:04]** All right, thank you very much for the

**[00:06]** organiz

**[00:08]** very very exciting. I hope that a few

**[00:09]** years from now we'll look back on this

**[00:11]** day as when everything really uh got

**[00:13]** started in the eyes. Uh I also want to

**[00:16]** give a a quick note to Charles and this

**[00:19]** world we converge on the memory machines

**[00:22]** a few weeks ago and it turns out that

**[00:24]** he's been using machines for for for

**[00:26]** many many years but anyway we'll uh

**[00:28]** we'll get to that. Um I want to talk

**[00:30]** about the the memory in garden and

**[00:32]** perhaps to give you a little bit of a

**[00:33]** different perspective on how uh we are

**[00:36]** thinking about memory uh together with

**[00:39]** who are here in the audience and are the

**[00:41]** true architects of everything that I'm

**[00:43]** going to be uh talking about. So um

**[00:47]** humans uh forget we forget things every

**[00:50]** day and our key goal is to augment human

**[00:53]** cognition and the memory similarity. I

**[00:56]** think we are not that far from the

**[00:59]** notion that uh very very soon we will be

**[01:01]** able to actually uh remember uh

**[01:04]** everything and that's our goal uh uh at

**[01:07]** memory machines. So uh first of all and

**[01:09]** this is uh basically stated several

**[01:12]** times already you are your memories

**[01:14]** Charles already said at the beginning in

**[01:16]** the morning and this is this is who you

**[01:18]** are basically. If I ask you about uh

**[01:20]** give me a recommendation for a good

**[01:22]** restaurant or if you think about the

**[01:24]** code that you've been read you've been

**[01:26]** writing uh or what you're going to do

**[01:29]** tomorrow. Uh this is the very essence of

**[01:31]** uh who you are and loss of memory uh is

**[01:36]** uh devastating uh both for uh the person

**[01:39]** themselves as well as uh for the uh

**[01:42]** loved ones. But memory loss is not just

**[01:44]** restricted to um all people. It turns

**[01:47]** out that uh all of us uh forget uh

**[01:50]** things constantly. In fact uh there are

**[01:53]** many quantitative studies that argue

**[01:55]** that we forget a huge amount of the

**[01:57]** information that we uh interact with uh

**[02:01]** on a on a daily basis. So it turns out

**[02:04]** that the word forgetting uh is a little

**[02:07]** bit of a misnomer. Sometimes we really

**[02:09]** forget things that are things that

**[02:10]** really disappear. But often times

**[02:11]** information is in our brains. it's just

**[02:13]** that we cannot recall it. So the key

**[02:15]** problem in memory uh is about uh being

**[02:18]** able to recall that information and if I

**[02:20]** can trigger that information you then

**[02:23]** are key arguments that we will be able

**[02:24]** to augment your cognition and help you

**[02:27]** truly remember uh everything. So I'd

**[02:30]** like to spend a few minutes now with

**[02:31]** something that's a little bit different

**[02:32]** from what you're normally used to which

**[02:34]** is telling you about what we know about

**[02:36]** how our brains encode and retrieve

**[02:38]** memories. I mean there have been many

**[02:40]** people that have been working for

**[02:41]** decades trying to understand at the

**[02:43]** behavioral level what we do remember and

**[02:46]** what we forget and also the mechanisms

**[02:48]** actually the neural circuit mechanisms

**[02:50]** that orchestrate what we remember or

**[02:52]** not. So I'll give you a quick uh glimpse

**[02:55]** on on that with two quick uh two two

**[02:58]** brief vignettes on on on on this uh

**[03:00]** problem. So the first one I think about

**[03:02]** neurons in a particular part of the

**[03:04]** brain called the human media temporal

**[03:06]** lobe. Many of you may have heard about

**[03:07]** the hippocampus. Uh if you don't have

**[03:09]** the hippocampi in both hemispheres, uh

**[03:11]** it turns out that you cannot consolidate

**[03:13]** memory. So I'll tell you what neurons do

**[03:15]** and how they uh represent information

**[03:17]** with a very quick experiment where we

**[03:19]** showed people uh u uh short video clips

**[03:24]** uh and then uh they they uh they were

**[03:27]** exposed to uh these different videos

**[03:29]** that had different orders. And I'll tell

**[03:30]** you about how the brain encodes one of

**[03:32]** the fundamental aspects of memory which

**[03:34]** is the temple order the sequence uh with

**[03:37]** which things happen. So we show these

**[03:39]** video clips to people and then we ask

**[03:41]** them uh in two different tasks what they

**[03:44]** remember and what they forget. One is a

**[03:46]** scene recognition task. Have you seen

**[03:47]** this scene before? Yes or no? Or we show

**[03:50]** you two frames and say which one

**[03:51]** happened uh before. And we did this work

**[03:53]** with patients that have epilepsy that

**[03:56]** have electrodes implanted in their

**[03:57]** brains. And this allowed us to give uh

**[03:59]** to get a unique glimpse with

**[04:01]** unprecedented spatial temporal

**[04:03]** resolution to record the activity of

**[04:04]** individual neurons. So we can look at

**[04:06]** the individual fundamental components of

**[04:08]** memory in the human brain. So let me

**[04:10]** give you a quick glimpse of what happens

**[04:12]** in the brain when you're trying to

**[04:14]** remember uh short snippets of the video.

**[04:16]** So what you're seeing here, many of you

**[04:18]** may not be familiar with this format.

**[04:20]** Each of the tiny dots over there

**[04:22]** corresponds to the action potential.

**[04:24]** that is the fundamental unit of activity

**[04:26]** of a neuron in the hypocampus of one of

**[04:28]** these patients while they're looking at

**[04:31]** the first event order one in one of

**[04:34]** these movies. Okay. And so you see that

**[04:36]** this neuron was activated after that

**[04:39]** dash line which corresponds to the onset

**[04:41]** of a new event uh in memory. When we

**[04:43]** look at other events uh event number

**[04:46]** two, event number three, this neuron was

**[04:48]** not activated at all. And similarly we

**[04:51]** have other neurons that represent order

**[04:53]** two, order three etc. So here's the

**[04:56]** fundamental mechanism by which the brain

**[04:58]** can encode the sequential order by which

**[05:02]** uh things uh happen and this is I just

**[05:05]** gave you a few examples. Here's a whole

**[05:07]** population of neurons. Some neurons

**[05:09]** encode what happens first, what happens

**[05:11]** next etc. So there are fundamental uh

**[05:14]** units in the brain that are encoding uh

**[05:16]** the temporal order in which uh things

**[05:18]** happen. So this is the kind of

**[05:20]** inspiration that goes behind some of the

**[05:22]** algorithms that we're building to

**[05:24]** represent uh uh the fundamental

**[05:26]** structures of uh memory uh based on uh

**[05:29]** neuroscience. I'll jump gears now to

**[05:32]** another vignette where we studied what

**[05:35]** people do and do not remember and this

**[05:37]** was a behavioral study where we built uh

**[05:39]** very simple machine learning algorithms

**[05:41]** to actually predict what people will

**[05:43]** remember or not under different

**[05:45]** circumstances. So in one of these

**[05:46]** experiments we had people watch a TV

**[05:49]** series in this particular case a TV

**[05:50]** series called 24 and we registered with

**[05:54]** very high uh resolution uh basically

**[05:57]** every part of the movie what people do

**[05:59]** or do not remember at different time

**[06:00]** points after watching this TV series. So

**[06:03]** what you're looking at here is a

**[06:05]** particular fragment of that movie from

**[06:07]** of that one of the episodes of this TV

**[06:09]** series from frame 55,000 to 56,000 or

**[06:13]** so. And each of the ticks corresponds to

**[06:16]** one particular event and whether people

**[06:17]** do remember that or not. This is

**[06:19]** participant 51. Here are 51

**[06:21]** participants. And you can see that

**[06:22]** there's a huge amount of consistency

**[06:24]** from one participant to another in terms

**[06:26]** of what they remember or not. So here uh

**[06:28]** uh in this case this is the average

**[06:30]** across different participants. This is

**[06:32]** for another episode. And so we can

**[06:34]** measure very densely what will be

**[06:36]** remember and what will be uh forgot. And

**[06:38]** then we can build basic AI models to

**[06:42]** predict what's memorable or not. This is

**[06:44]** uh basically uh I won't go into a lot of

**[06:46]** the details but basically this is a

**[06:48]** combination of computer vision language

**[06:52]** uh trying to decode from the content and

**[06:54]** predict exactly what will be remembered

**[06:56]** or not. Here we can predict with about

**[06:58]** 75% accuracy uh for a single event and

**[07:01]** for a single person what's memorable and

**[07:03]** what isn't uh memorable.

**[07:06]** So um back to u trying to build

**[07:09]** algorithms that would augment uh human

**[07:11]** cognition. The first step is building

**[07:14]** what we call the memor. The memor is the

**[07:16]** complete organized record of an

**[07:18]** individual's memory. It's like a u it's

**[07:20]** like a genome but containing all your

**[07:22]** memory. So think about uh every

**[07:24]** conversation you've ever had, every

**[07:25]** person you've ever met, every email

**[07:27]** you've written, every book, every movie,

**[07:29]** uh everything is part of your memor. We

**[07:31]** want to be able to encode that and we

**[07:33]** want to be able to encode that in a way

**[07:35]** that uh is inspired by what we

**[07:37]** understand about the mechanisms by which

**[07:38]** the brain and people actually encode

**[07:40]** information.

**[07:42]** So this has to be uh multimodal. We

**[07:44]** extract all of the experiences uh from

**[07:46]** uh all the the sources. Uh in principle

**[07:50]** we'd like to incorporate uh every single

**[07:52]** file, everything that's digital uh

**[07:54]** incorporated into the uh memor. And um

**[07:59]** one thing that I want to uh emphasize

**[08:02]** and talk a little bit more about now and

**[08:03]** this was alluded to in some of the

**[08:05]** previous talks is that we need new ways

**[08:07]** of evaluating humanlike memory. And I

**[08:09]** look forward to seeing uh where was it

**[08:11]** the the previous talk uh from Tanka the

**[08:14]** the new benchmark that they are created.

**[08:16]** I think creating new benchmarks is

**[08:17]** essential for us to make progress in our

**[08:19]** field and I'd like to invite our whole

**[08:21]** community to collaborate uh on that. So

**[08:24]** perhaps I'm preaching to the converted

**[08:25]** here. Many of you are probably familiar

**[08:27]** with the story of computer vision. Uh

**[08:29]** emnest was quite exciting you know uh it

**[08:32]** sort of started the whole discussion. Um

**[08:35]** but I think in the memory field we are

**[08:37]** kind of in the preeminent stage in terms

**[08:39]** of how we are evaluating uh uh memories.

**[08:42]** Uh so imageet with all the caveats we

**[08:45]** can criticize uh image net in a lot of

**[08:47]** ways but imageet has been quite

**[08:48]** transformative uh in terms of being able

**[08:50]** to push the frontiers of uh computer

**[08:53]** vision uh and that sort of ignited a

**[08:55]** whole era uh that transforms sensory uh

**[08:59]** intelligence. So if we think about large

**[09:01]** language models, one of the reasons they

**[09:02]** have been so successful is because

**[09:04]** they've been able to capitalize on uh

**[09:07]** enormous amounts of data that they have

**[09:09]** been uh using for uh for training. We

**[09:12]** just don't have that for uh uh LM. So

**[09:14]** LMMs are large memory models. Uh that's

**[09:18]** what we are building. That's what many

**[09:19]** of you are interested in building as

**[09:20]** well. And for to build large memory

**[09:22]** models, we need uh fundamental uh

**[09:25]** benchmarks and data sets that we can u

**[09:27]** build upon. And so uh we'd like to

**[09:30]** invite all of you to uh uh collaborate

**[09:33]** with us if you're interested in building

**[09:35]** better data sets and benchmarks uh for

**[09:37]** humanlike uh memory. And here's a basic

**[09:40]** decider of what those what those

**[09:42]** benchmarks should look like. So first of

**[09:44]** all we need to have access to ground

**[09:46]** truth. They need to be personal. Uh we

**[09:48]** are in particular interested in our case

**[09:50]** in human memory not in memory for agents

**[09:53]** but actually in augmenting you

**[09:55]** augmenting human cognition. Um they need

**[09:57]** to be uh uh to be able to incorporate uh

**[10:00]** time and be dynamic uh and incorporate

**[10:03]** the changes over time that are

**[10:04]** fundamental to memory. Uh they need to

**[10:06]** be accessible. So uh I cannot quite

**[10:08]** share my entire personal history uh with

**[10:11]** everyone. So we need memor that are

**[10:14]** accessible for testing for the entire

**[10:15]** community. Uh and importantly they have

**[10:18]** to be large right. So we cannot work

**[10:19]** with data set that has you know a

**[10:22]** hundred snippets of conversation and

**[10:23]** then few questions and answers on on on

**[10:26]** that. So here's a couple of things that

**[10:28]** we're developing. One is the Abraham

**[10:30]** Lincoln uh memor uh another one is

**[10:34]** celebrity based memors uh personal based

**[10:38]** memors and fundamental list of uh uh

**[10:41]** extensive questions and answers that we

**[10:43]** can all test our algorithms uh uh on. So

**[10:46]** we're going to be submitting a proposal

**[10:48]** for Europe's workshop uh on benchmarks

**[10:51]** for memory and would like to invite

**[10:52]** everyone who's interested in

**[10:54]** collaborating with us on this. Uh uh I

**[10:56]** think this is going to benefit all of us

**[10:58]** uh first of all in defining what data

**[11:00]** sets we need for training models. Second

**[11:02]** in evaluating uh rigorous uh benchmarks

**[11:06]** uh that that we can all uh then compare

**[11:08]** uh nodes uh with. So uh just to close

**[11:11]** our vision is to endow humans with

**[11:13]** perfect and infinite memory. We want to

**[11:15]** augment uh human condition. We want to

**[11:17]** make you uh superhuman. Uh and to go

**[11:21]** back to the title, uh we think that

**[11:23]** we're not very far from uh what I call

**[11:25]** the memory singularity. Uh perhaps it's

**[11:28]** a bit grandiose to put that on par with

**[11:30]** peniselline, the DNA double helix, and

**[11:33]** the moon landing. But I do think that

**[11:34]** all of our lives and the world will be

**[11:37]** transformed in a fundamental way uh the

**[11:40]** way the day we can actually uh truly

**[11:42]** remember uh everything. And I think that

**[11:44]** we actually have the tools to build that

**[11:46]** and to allow uh and enable all of you to

**[11:49]** uh remember absolutely everything. Uh

**[11:51]** here's part of our team, half of which

**[11:54]** is actually here and and I'd like to

**[11:56]** encourage all of you to talk to to them

**[11:58]** and and I'll stop there. So, thank you.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
