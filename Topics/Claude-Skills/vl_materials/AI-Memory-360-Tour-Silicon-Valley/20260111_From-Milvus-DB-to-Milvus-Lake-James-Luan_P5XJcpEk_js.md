# From Milvus DB to Milvus Lake - James Luan

**원본 영상**: [https://www.youtube.com/watch?v=P5XJcpEk_js](https://www.youtube.com/watch?v=P5XJcpEk_js)
**작성일**: 2026-01-11
**Video ID**: P5XJcpEk_js

---

## 요약

Milvus의 공동 창업자 James Luan이 AI 메모리 시스템 구축을 위한 인프라에 대해 발표합니다. AI 메모리 시스템 구축의 주요 과제들을 소개하고, 이를 해결하기 위한 두 가지 프로젝트인 Milvus Database(서빙용)와 Milvus Lake(배치 처리용)를 설명합니다. 대규모 멀티모달 데이터를 효율적으로 처리하고 관리하기 위한 확장 가능한 벡터 데이터베이스 솔루션을 제시합니다.

---

## 핵심 포인트

- Milvus는 LF AI 재단의 오픈소스 프로젝트로 GitHub에서 40,000+ 스타를 받은 가장 인기 있는 벡터 데이터베이스
- AI 메모리 시스템 구축의 5가지 주요 과제: 고품질 검색, 대규모 성능 유지, 멀티테넌시, 오프라인 데이터 처리, 대량 데이터셋 효율적 처리
- Milvus Database는 멀티모달 데이터 모델, 하이브리드 검색, 수천만 개의 테넌트 지원 등의 기능 제공
- 파티션 키 기반 물리적 격리를 통한 혁신적인 멀티테넌시 솔루션
- Tier Storage를 통해 S3의 저비용과 인메모리의 빠른 성능을 동시에 제공
- Milvus Lake는 Iceberg, Delta Lake 등과 통합하여 데이터 복사 없이 배치 처리 가능

---

## 주요 내용

### 섹션 1: Milvus 소개
- LF AI 재단 산하 오픈소스 프로젝트, 40,000+ GitHub 스타
- 1억 개 이상의 팟이 사용자 환경에 배포됨
- 300명 이상의 전 세계 기여자
- Zilliz Cloud는 Forrester의 리더 부문으로 선정된 완전 관리형 벡터 DB 서비스
- Nvidia, Apple 등 주요 AI 기업들이 사용 중

### 섹션 2: AI 메모리 시스템 구축의 과제
- **과제 1 - 고품질 검색**: 임베딩만으로는 부족하며, 키워드 검색, 필터 검색, 그래프와 벡터 DB의 조합 필요
- **과제 2 - 대규모 성능**: 수백만 DAU를 서빙할 수 있는 확장 가능한 인프라 필요
- **과제 3 - 멀티테넌시**: 수백만 개의 테이블/컬렉션 지원 필요, 기존 데이터베이스는 10,000개 미만만 지원
- **과제 4 - 오프라인 파이프라인**: 대량 데이터의 요약, 중복 제거, 관계 발견을 위한 분산 시스템 필요
- **과제 5 - 비용 효율성**: 대량 데이터셋을 시스템 간 이동 없이 효율적으로 처리

### 섹션 3: 이상적인 메모리 시스템 아키텍처
- 멀티모달 구조화/비구조화 데이터를 컨텍스트 메모리(벡터 DB/그래프)에 저장
- 백그라운드에서 피처 엔지니어링 및 데이터 후처리 수행
- 생성된 피처를 임베딩/그래프 변환 또는 모델 학습에 사용
- 파라메트릭 메모리(LoRA, KV 캐시)로 에이전트의 이해도 향상

### 섹션 4: Milvus Database의 특징
- **AI 특화 데이터 모델**: PDF, 웹페이지 등을 멀티모달 데이터로 쉽게 변환
- **유연한 스키마**: 고성능을 위한 정적 스키마와 유연성을 위한 동적 스키마 지원
- **하이브리드 검색**: Dense, Sparse(BM25), Binary 임베딩 등 다중 벡터 필드 지원
- **멀티벡터 지원**: ColBERT, ColPali 등 다양한 임베딩 저장
- **메타데이터**: 문자열, 숫자, 지리정보, 타임스탬프 등 고정 필드 지원

### 섹션 5: 확장성 및 아키텍처
- 완전한 클라우드 네이티브, S3와 Kubernetes 활용
- 서버리스로 쉬운 확장 가능
- Tier Storage: S3에 콜드 데이터 저장, SSD/메모리에 핫 데이터 캐싱
- 핫 데이터는 수십 밀리초 지연시간, 콜드 데이터는 200-300ms

### 섹션 6: 멀티테넌시 솔루션
- **기존 방식의 한계**:
  - 테넌트당 1개 컬렉션: 대부분 DB가 10,000개 미만만 지원
  - 모든 테넌트 1개 컬렉션: 필터링 성능 저하, 접근 제어 문제
- **Milvus의 혁신적 접근**:
  - 파티션 키 기반 물리적 격리
  - 데이터 삽입 시 하나의 컬렉션이지만 내부적으로 작은 파티션으로 분할
  - 검색 시 관련 파티션만 접근하여 성능 유지
  - 수천만 개의 테넌트 지원 가능

### 섹션 7: Milvus Lake - 배치 처리
- **목적**: 오프라인 데이터 처리 파이프라인 구축, 데이터 인사이트 발견
- **External Table 기능**: Iceberg, Delta Lake 등의 데이터를 복사 없이 Milvus 포맷으로 변환
- **인덱스 구축**: 
  - 콜드 데이터 위에 인덱스 레이어 구축
  - 데이터 복사 없이 검색 가능
  - Microsoft AI의 사례: 20일 걸리던 쿼리를 몇 시간으로 단축
- **범용 인덱스**: Spark, Ray 등 다른 시스템에서도 사용 가능
- **사용 사례**: 데이터 중복 제거, 태깅, 그래프 구축 등의 배치 작업 가속화

---

## 타임라인

- **00:00**: Yeah. So, uh I thought happy to do a little special. this um uh this morning we talked a lot about what is AI memory and uh uh how how do we build a uh application on top of AI memory but my talk is more about how do we uh build a memory system and what is the infra so uh I'm James uh co-ounder so we are vector this company so my talk will be like split into four sessions uh first part is a little bit intro introduction about male sensitives Then we talk about the challenge of how to build a memory system. Uh then we do have two different project. One is milk database for serving another one is mak for helping you to batch processing all the uh contacts. Yeah. So uh first of all mus uh we are actually open source project under n foundation. Uh we uh are like the most popular record database on the uh github. uh more than 40k stars actually uh more than 100 million uh pods actually deploying in users uh environment also we have more than 300 contributors worldwide so uh the company behind me is actually so we actually naming the company by zillion zillion this is actually a word we actually created pang so our mission is just to helping organization to make sense of uh data uh for sure including all the like AI memory datas like multi model datas or the text images audios. So uh our fully managed system those call uh is actually uh one of the best uh fully managed uh vectors DB service and according to force is actually uh in the leader segments on their first report. Okay. So uh just show quickly show our logos. Uh many of the like Nvidia, Apple, XCI, many of the AI companies and uh big companies are actually using us. So uh get uh if one day we're going to have uh your company's name on this list. Okay. So uh back to the topic, right? Uh what is the current challenge for AM memories? I think AM memory just...
- **05:00**: the second challenge and we do need some scalable infrared to handle that right and then uh your your system keeps growing uh you hit into other issues uh multi-tenency is definitely one of them uh you're definitely not building agent for yourself you're actually building for many of your application users and with the application become popular uh that is a big headache right usually what you do is just to create one uh agent in one collection or one table but the challenge is uh look at your database right is you really not be able to support uh million level tables collections right so that become a pain okay so uh if all the first three challenge has been solved uh then congratulations you have a very good uh memory systems but still uh it's not perfect right so I I think the the further challenge is uh how you going to uh convert those datas uh into a more uh efficient format and get more like details uh from the row data, right? All those chat histories, we need to do summarization, we need to do uh some dduplications or we need to find relations between knowledge base and the simple way to do that is just to write a Python code and run it in the back end. But once you have huge amount of datas that is not like really red doable then people do think using spark using ray or some kind of like um distributed system to do that and and that becomes a big headache of how you can build a reliable offline pipeline uh for your official engineering and um preparing for your training datas. Yeah. And then once you have it uh last challenge will be uh this this will cost you like like tons of machines and also uh becomes really stable. Uh I've seen a lot of big companies getting into this pains like they cannot uh they have like data sets a lot of people from different applications um but they want to serve uh them at like one one data one shot. Yeah. So how...
- **10:00**: embeddings, you can do sparse embeddings with BM25, you can do binary embedding search. Uh we also support like uh multi vector styles support like covert coali. So you can like easily store all your embeddings [clears throat] or different kinds of your uh data into one system and you can also like uh tag in your data uh and store it in in in our fixed field. Uh we do support like strings uh numeric numbers and also like geoloccation datas, timestamp data. So that is good enough for like uh people to just build a agent. Yeah. And uh also like one one of the uh fancy part for it is you can you can you can do multiodality uh data model. So uh some of them like data models actually uh fits video frame sequence and some some of them actually fit time series datas. So you can always find a way to put your ultra datas into m table. So uh second thing is like it's super scalable. So it actually helping you to solve the problem about how to scale. Uh I I know this is not a like infra so I I won't go go too deep into this. Uh but the key idea here is like uh everything is like fully fully on the cloud. Uh we actually leverage like infra s3 and kubernetes. So Mio itself is stillless make it super easy to scale and other side we can we can also push down those code datas onto uh code storage like S3 and still caching some of the hot datas. Uh that is super helpful under like multi-tenant use cases where some of your agent memories might be hot but the others could be just uh stay in the corner and don't cost you too much on AWS. Okay. So modness is definitely one big challenge. Uh I I actually see uh it actually hits several times uh in the previous talk. So there are actually multiple different data models for that. The easiest one is just a one collection per tenant but just that the limitation is how many collections or how many...
- **15:00**: it's not enough. Uh the kind key challenge is once the data accumulate we always want to build build something special uh offline processing pipeline helping us to uh like uh find keep finding insight in our like datas or in user status right uh that's some uh uh and metab data maybe just stored in S3 or maybe just stored in something like iceberg or maybe a data warehouse or data lakeink yeah so Uh originally we know a lot of people they just migrate their data from iceberg or dell lake into mus but that's definitely another challenge and also you you try to duplicate your data it cost you double maybe not double but even more than that because you do a lot of data governance and ETL uh but right now we actually support a feature which you call as internal table so no matter what kind of format you actually using it can be part can be uh vortex it can be lens uh we can just convert those datas into u uh our format and try to build another layer of index on top of it. So you can search on your uh code datas uh without even like copy to uh a lot of different places and uh what's more than that is we actually build a index on top of all the datas right uh you have all the colmer datas but remember embeddings uh sometimes you you not only imbalance but also like you do you want do some kind of regular expressions and uh run each of the queries may take you uh like minutes or even uh I think the quest query I know is from Microsoft AI so there's some kind of their internal queries take more than 20 days uh just to finding some training data set right so uh we helping them to build index on top of it and shorten the time from 20 days to couple of hours so actually uh giving their data science a lot of benefits uh from not waiting but uh also improve their like GPU usage in in house, right? So with with the index building we call it one index because...
- **20:00**: milkflake uh for sure one one of the most famous one is uh context engineering. So people do dduplications summarize visions and they can also uh structure their context for AI agents and AI memory. Uh another uh interesting use case is a model search. Uh we actually powering one of the world's largest uh uh autonomous driving company. So uh what they do is they they actually collecting huge amount of uh datas uh into their in-house data lake systems and uh uh they want to like sometimes data scientists want to uh find a subset of their datas to to quantum their model. Uh for example, if my ultimate driving car is driving and it's raining, there is a red light uh uh uh beh like a uh in front and there's actually a dog pass uh pass a road and uh my car is is not driving in the right way. And they try to find those kind of scenarios using uh uh like a neural language and uh uh like like select a bunch of images or videos just to do another round of fun tuning. Uh that's a use case. Originally they they do a lot of taggings but taggings is actually limited because you have to pre-undering what people going to ask but with embeddings then you you can cover a lot of different corner cases and uh using using index and lake helping them to accelerate. Yeah. Uh third thing is data preparation. So we also working with uh one of the uh uh leading AI companies. So they have huge amount of data uh pre-trained datas. So uh they want to uh do a very fast retrieval on the datas and they also do a lot of pre-processing using uh ray. So uh we actually uh using this uh lake solution combining it with ray so they can easily writing a lot of different udfs uh to pro processing their data. Yeah, I think that's pretty much I want to share. So glad to take questions. You found him....

---

## 전체 자막 (타임스탬프 포함)

**[00:00]** Yeah. So, uh I thought happy to do a

**[00:02]** little special. this um uh this morning

**[00:04]** we talked a lot about what is AI memory

**[00:07]** and uh uh how how do we build a uh

**[00:11]** application on top of AI memory but my

**[00:13]** talk is more about how do we uh build a

**[00:16]** memory system and what is the infra

**[00:20]** so uh I'm James uh co-ounder so we are

**[00:24]** vector this company so my talk will be

**[00:27]** like split into four sessions uh first

**[00:29]** part is a little bit intro introduction

**[00:31]** about male sensitives Then we talk about

**[00:33]** the challenge of how to build a memory

**[00:35]** system. Uh then we do have two different

**[00:38]** project. One is milk database for

**[00:40]** serving another one is mak for helping

**[00:42]** you to batch processing all the uh

**[00:45]** contacts.

**[00:48]** Yeah. So uh first of all mus uh we are

**[00:51]** actually open source project under n

**[00:53]** foundation. Uh we uh are like the most

**[00:57]** popular record database on the uh

**[00:59]** github. uh more than 40k stars actually

**[01:02]** uh more than 100 million uh pods

**[01:05]** actually deploying in users uh

**[01:09]** environment also we have more than 300

**[01:11]** contributors worldwide

**[01:15]** so uh the company behind me is actually

**[01:19]** so we actually naming the company by

**[01:21]** zillion zillion this is actually a word

**[01:23]** we actually created pang so our mission

**[01:26]** is just to helping organization to make

**[01:28]** sense of uh data uh for sure including

**[01:31]** all the like AI memory datas like multi

**[01:33]** model datas or the text images audios.

**[01:37]** So uh our fully managed system those

**[01:39]** call uh is actually uh one of the best

**[01:42]** uh fully managed uh vectors DB service

**[01:45]** and according to force is actually uh in

**[01:48]** the leader segments on their first

**[01:50]** report.

**[01:52]** Okay. So uh just show quickly show our

**[01:55]** logos. Uh many of the like Nvidia,

**[01:59]** Apple, XCI, many of the AI companies and

**[02:02]** uh big companies are actually using us.

**[02:04]** So uh get uh if one day we're going to

**[02:07]** have uh your company's name on this

**[02:10]** list. Okay. So uh back to the topic,

**[02:14]** right? Uh what is the current challenge

**[02:16]** for AM memories? I think AM memory just

**[02:18]** like teenage sex. Everybody talks about

**[02:20]** it. Everybody knows it's important.

**[02:22]** Novas knows how to do it. Everything

**[02:25]** everyone thinks every uh some some

**[02:27]** somebody else is actually doing that. So

**[02:29]** everyone claims that they also doing it

**[02:31]** right. But but but that's a challenge.

**[02:34]** Okay. Uh first of all it's it's all

**[02:37]** important. I think this morning talked a

**[02:39]** lot about how uh this is very important

**[02:42]** but just to give you one example uh if

**[02:45]** we're just trying to build an agent

**[02:46]** helping me to reply emails and u and

**[02:49]** then I receive an email say are you free

**[02:51]** tomorrow uh can we do a catch up quickly

**[02:54]** so the technical AI answer will be uh

**[02:57]** sure what's a what's a meeting what's

**[02:59]** the time available uh but uh actually

**[03:01]** tomorrow is my family day so uh I

**[03:04]** actually cannot attend right so uh we do

**[03:07]** need some kind of context information

**[03:09]** help the agent better understanding uh

**[03:12]** what's going on there uh and that is

**[03:14]** something we call as a memory

**[03:18]** uh but how you build a memory systems uh

**[03:22]** what is the challenge yeah I think from

**[03:25]** day one it seems to be pretty simple and

**[03:28]** really nothing like different from just

**[03:31]** a building a rack system so uh the first

**[03:33]** step is how you do a high quality search

**[03:36]** across our datadas, right? The simple

**[03:39]** way just to put everything into

**[03:40]** embeddings or graph and uh do uh

**[03:44]** retrieval. Uh that is simple but usually

**[03:46]** not as efficient or usually has some uh

**[03:50]** uh major limitations. That's why we are

**[03:52]** actually in this room and uh had

**[03:54]** multiple ways to fix that. Yeah. So uh

**[03:57]** from our experience only use embedding

**[04:00]** search might not be uh like the the

**[04:04]** ultimate answer. So you also need to

**[04:06]** think about doing research, filter

**[04:08]** search probably sometimes have to be uh

**[04:10]** a combination between graph and vector

**[04:13]** database. Um but yeah uh as a prototype

**[04:16]** I think it's not like uh hard like super

**[04:20]** hard to fix that. Maybe just do it in

**[04:23]** one or two weeks, build a great demo, uh

**[04:25]** get a very good uh benchmark result,

**[04:29]** then you step into challenge two, right?

**[04:32]** How do you keep uh your performance on a

**[04:36]** large scale system when you deploy your

**[04:38]** agent into your uh production

**[04:41]** environment serving like millions of

**[04:43]** your uh customers, then that becomes a

**[04:46]** big challenge, right? As far as I know

**[04:48]** most of most of the agent system or AI

**[04:51]** memory system we uh actually talked uh

**[04:54]** about this morning cannot serving like

**[04:57]** million level uh DAUs. So uh that become

**[05:01]** the second challenge and we do need some

**[05:03]** scalable infrared to handle that right

**[05:06]** and then uh your your system keeps

**[05:09]** growing uh you hit into other issues uh

**[05:12]** multi-tenency is definitely one of them

**[05:14]** uh you're definitely not building agent

**[05:16]** for yourself you're actually building

**[05:18]** for many of your application users and

**[05:21]** with the application become popular uh

**[05:23]** that is a big headache right usually

**[05:25]** what you do is just to create one uh

**[05:28]** agent in one collection or one table but

**[05:31]** the challenge is uh look at your

**[05:32]** database right is you really not be able

**[05:34]** to support uh million level tables

**[05:38]** collections right so that become a pain

**[05:41]** okay so uh if all the first three

**[05:45]** challenge has been solved uh then

**[05:47]** congratulations you have a very good uh

**[05:50]** memory systems but still uh it's not

**[05:53]** perfect right so I I think the the

**[05:56]** further challenge is uh how you going to

**[05:59]** uh convert those datas uh into a more uh

**[06:03]** efficient format and get more like

**[06:06]** details uh from the row data, right? All

**[06:09]** those chat histories, we need to do

**[06:11]** summarization, we need to do uh some

**[06:14]** dduplications or we need to find

**[06:16]** relations between knowledge base and the

**[06:20]** simple way to do that is just to write a

**[06:22]** Python code and run it in the back end.

**[06:25]** But once you have huge amount of datas

**[06:26]** that is not like really red doable then

**[06:29]** people do think using spark using ray or

**[06:32]** some kind of like um distributed system

**[06:35]** to do that and and that becomes a big

**[06:37]** headache of how you can build a reliable

**[06:40]** offline pipeline uh for your official

**[06:42]** engineering and um preparing for your

**[06:44]** training datas. Yeah. And then once you

**[06:47]** have it uh last challenge will be uh

**[06:50]** this this will cost you like like tons

**[06:53]** of machines and also uh becomes really

**[06:56]** stable. Uh I've seen a lot of big

**[06:58]** companies getting into this pains like

**[07:00]** they cannot uh they have like data sets

**[07:03]** a lot of people from different

**[07:04]** applications

**[07:06]** um but they want to serve uh them at

**[07:08]** like one one data one shot. Yeah. So how

**[07:12]** how to process massive amount of data

**[07:14]** sets very efficiently becomes a

**[07:16]** challenge and uh we don't definitely

**[07:17]** don't want to move data between

**[07:19]** different systems.

**[07:21]** Okay. So uh that's one ideal system if

**[07:26]** if I'm a application developer that's

**[07:28]** something I want to build right. So you

**[07:30]** have some uh row datas it should be

**[07:33]** modelity structure plus unstructured

**[07:36]** datas. uh first off you actually put

**[07:39]** those into your contact contextual

**[07:41]** memory. is actually your vector database

**[07:43]** or it's your graph uh whatever you do uh

**[07:47]** some simple process and uh it should be

**[07:49]** work at the very beginning but soon it

**[07:52]** hits into some problem then uh you

**[07:55]** thought maybe I I want to finetune my

**[07:57]** model to solve those problems or uh

**[07:58]** maybe I just want to uh get more deeper

**[08:01]** relationships probably at the very

**[08:03]** beginning you just had one hop per data

**[08:06]** but after certain time like we actually

**[08:08]** forgot something then we need on the

**[08:11]** other side we need to like dig deep into

**[08:14]** all the like data insights. So that's

**[08:17]** why we need all those feature

**[08:18]** engineering and uh data post processing

**[08:21]** our background and generate a lot of

**[08:24]** features. Then those features can be

**[08:26]** used either to uh like convert bing to

**[08:29]** graph again or embedding again or it can

**[08:31]** be just helping you to train those

**[08:34]** models. So uh we we uh then then with

**[08:38]** like parame that's something we call

**[08:40]** parametric memory uh just think it as a

**[08:44]** kiwi cache or just some some like Laura

**[08:47]** uh but that could also help your agent

**[08:49]** to get better understanding of yourself

**[08:52]** or your customers.

**[08:54]** >> Yeah.

**[08:57]** So uh the challenge is all all about

**[09:00]** inferest right the ideas are simple uh

**[09:02]** if you have one million datas definitely

**[09:05]** easy to do but when you have like couple

**[09:08]** millions a couple billion datas then

**[09:10]** everything become a really challenge uh

**[09:12]** that's why we introduce two of our

**[09:14]** infras one is m database

**[09:18]** so uh I uh we can't purpose build uh

**[09:21]** database for AI mainly because of the

**[09:23]** data model so uh we can easily convert

**[09:27]** any kind of PDF or any kind of like uh

**[09:31]** document whether it's a web page uh into

**[09:34]** a a matter of model. Uh we do have uh

**[09:37]** some special tricks on top of it. First

**[09:39]** of all, we actually combine dynamic uh

**[09:41]** schema and big schema. So if you want

**[09:44]** better performance, you do big schema.

**[09:45]** Uh but sometimes your a agent is like

**[09:49]** very very flexible. Your data is uh

**[09:51]** dirty. So you definitely want dynamics

**[09:53]** schema sense at some time. Yeah. Also we

**[09:56]** have multiple different vector field

**[09:57]** support. So you can easily do a hybrid

**[09:59]** search uh between either deep dense

**[10:03]** embeddings, you can do sparse embeddings

**[10:04]** with BM25, you can do binary embedding

**[10:08]** search. Uh we also support like uh multi

**[10:11]** vector styles support like covert coali.

**[10:15]** So you can like easily store all your

**[10:18]** embeddings [clears throat] or different

**[10:19]** kinds of your uh data into one system

**[10:22]** and you can also like uh tag in your

**[10:24]** data uh and store it in in in our fixed

**[10:27]** field. Uh we do support like strings uh

**[10:31]** numeric numbers and also like

**[10:33]** geoloccation datas, timestamp data. So

**[10:35]** that is good enough for like uh people

**[10:38]** to just build a agent. Yeah. And uh also

**[10:43]** like one one of the uh fancy part for it

**[10:46]** is you can you can you can do

**[10:47]** multiodality

**[10:49]** uh data model. So uh some of them like

**[10:53]** data models actually uh fits video frame

**[10:57]** sequence and some some of them actually

**[10:59]** fit time series datas. So you can always

**[11:01]** find a way to put your ultra datas into

**[11:05]** m table.

**[11:08]** So uh second thing is like it's super

**[11:11]** scalable. So it actually helping you to

**[11:12]** solve the problem about how to scale. Uh

**[11:16]** I I know this is not a like infra so I I

**[11:18]** won't go go too deep into this. Uh but

**[11:22]** the key idea here is like uh everything

**[11:25]** is like fully fully on the cloud. Uh we

**[11:30]** actually leverage like infra s3 and

**[11:33]** kubernetes. So Mio itself is stillless

**[11:35]** make it super easy to scale and other

**[11:38]** side we can we can also push down those

**[11:40]** code datas onto uh code storage like S3

**[11:44]** and still caching some of the hot datas.

**[11:46]** Uh that is super helpful under like

**[11:48]** multi-tenant use cases where some of

**[11:50]** your agent memories might be hot but the

**[11:53]** others could be just uh stay in the

**[11:56]** corner and don't cost you too much on

**[11:58]** AWS.

**[12:00]** Okay. So modness is definitely one big

**[12:05]** challenge. Uh I I actually see uh it

**[12:08]** actually hits several times uh in the

**[12:10]** previous talk. So there are actually

**[12:12]** multiple different data models for that.

**[12:14]** The easiest one is just a one collection

**[12:16]** per tenant but just that the limitation

**[12:18]** is how many collections or how many

**[12:20]** tables can create on your database. U is

**[12:22]** limited number. Uh most database I would

**[12:25]** say just less than 10k. Uh yeah it it

**[12:28]** probably don't fit if you if your

**[12:31]** application is just a uh focus on like

**[12:34]** uh business customers but if you're

**[12:36]** trying to build consumer customers then

**[12:38]** definitely like 10k is not good enough.

**[12:41]** Uh the other way to do that is uh using

**[12:44]** one collection for all your attendance

**[12:46]** but then you soon hit other issues like

**[12:48]** how do I do isolation uh you you you can

**[12:50]** definitely do filters but futures are

**[12:52]** actually kind of like slow and also uh

**[12:55]** you you get a lot of like uh access

**[12:57]** control issues uh and how like then like

**[13:01]** a lot of issue falls into uh uh on how

**[13:04]** to pre uh like uh keep that users data

**[13:07]** security and fast. So uh one innovation

**[13:10]** with us we actually uh support something

**[13:13]** in the middle. So uh when people inert

**[13:16]** data it's still one collection but we

**[13:18]** actually split all the data into smaller

**[13:19]** partitions. So uh each part uh think

**[13:23]** about each uh tenant can be one small

**[13:26]** part in the table and it's it's actually

**[13:29]** physically isolated. So uh when you

**[13:32]** ingest and when you search you still

**[13:34]** keep it as one uh collection uh not too

**[13:37]** much meta informations uh but when you

**[13:39]** when you search on it uh it actually

**[13:42]** only hits part of your data and the

**[13:45]** tendance number can be like goes to up

**[13:47]** to uh tens of millions. So that is good

**[13:49]** enough for all the consumer applications

**[13:51]** and it's extremely helpful when you when

**[13:53]** you're trying to build AI memories

**[13:54]** because you're actually building for

**[13:56]** multiple agents and each agents can be

**[13:58]** just a one partition key inside the

**[14:00]** system.

**[14:02]** Okay. Uh the other important thing

**[14:04]** definitely the uh the uh cost right. So

**[14:07]** uh we do have a special sauce we could

**[14:10]** call it pair storage. So all the data is

**[14:14]** actually uh located in in a pair storage

**[14:17]** way. So many data just stored in uh

**[14:19]** object storage. All your code datas uh

**[14:22]** cost as much as uh what S3 cost, right?

**[14:26]** But we do have several layer caching. So

**[14:28]** you can caching some of the data on your

**[14:30]** SSDs or even in memory. So hot datas can

**[14:33]** be as fast as like uh tens of millconds

**[14:37]** latency and the code code that has maybe

**[14:40]** takes much longer based on like how what

**[14:42]** kind of storage you're using 200 300

**[14:45]** millconds but still good enough for many

**[14:47]** of the AI memory use case. Yeah. So

**[14:52]** that's milk database uh mainly built for

**[14:55]** retrieving rag uh for all the serving

**[14:59]** use case. Yeah. Uh but as I just said

**[15:02]** it's not enough. Uh the kind key

**[15:04]** challenge is once the data accumulate we

**[15:06]** always want to build build something

**[15:08]** special uh offline processing pipeline

**[15:12]** helping us to uh like uh find keep

**[15:16]** finding insight in our like datas or in

**[15:18]** user status right uh that's some uh uh

**[15:22]** and metab data maybe just stored in S3

**[15:25]** or maybe just stored in something like

**[15:27]** iceberg or maybe a data warehouse or

**[15:29]** data lakeink yeah so Uh

**[15:34]** originally we know a lot of people they

**[15:35]** just migrate their data from iceberg or

**[15:38]** dell lake into mus but that's definitely

**[15:41]** another challenge and also you you try

**[15:43]** to duplicate your data it cost you

**[15:45]** double maybe not double but even more

**[15:47]** than that because you do a lot of data

**[15:49]** governance and ETL uh but right now we

**[15:52]** actually support a feature which you

**[15:53]** call as internal table so no matter what

**[15:56]** kind of format you actually using it can

**[15:58]** be part can be uh vortex it can be lens

**[16:01]** uh we can just convert those datas into

**[16:04]** u uh our format and try to build another

**[16:07]** layer of index on top of it. So you can

**[16:09]** search on your uh code datas uh without

**[16:13]** even like copy to uh a lot of different

**[16:15]** places

**[16:18]** and uh what's more than that is we

**[16:20]** actually build a index on top of all the

**[16:22]** datas right uh you have all the colmer

**[16:25]** datas but remember embeddings uh

**[16:28]** sometimes you you not only imbalance but

**[16:30]** also like you do you want do some kind

**[16:33]** of regular expressions and uh run each

**[16:36]** of the queries may take you uh like

**[16:38]** minutes or even uh I think the quest

**[16:41]** query I know is from Microsoft AI so

**[16:44]** there's some kind of their internal

**[16:46]** queries take more than 20 days uh just

**[16:50]** to finding some training data set right

**[16:52]** so uh we helping them to build index on

**[16:55]** top of it and shorten the time from 20

**[16:57]** days to couple of hours so actually uh

**[17:01]** giving their data science a lot of

**[17:02]** benefits uh from not waiting but uh also

**[17:06]** improve their like GPU usage in in

**[17:08]** house, right? So with with the index

**[17:11]** building we call it one index because

**[17:13]** the index cannot be only used for mus

**[17:15]** itself but it can also be used um in

**[17:18]** systems like spark and ray. So you can

**[17:21]** either do serving with mules but you can

**[17:23]** also do some uh like uh batch

**[17:26]** processing. You say if you want to do uh

**[17:29]** uh dduplication your datas or if you

**[17:32]** want to do uh some uh a layer uh some uh

**[17:37]** try to tag in your datas or even you

**[17:39]** want to build a graph on your datas then

**[17:42]** uh the index can help you to accelerate

**[17:44]** spark uh without need to like migrate

**[17:47]** the data to anywhere else.

**[17:50]** Okay, so with the one data and the one

**[17:55]** index design, I think the final result

**[17:57]** we get is actually one sematic layer. So

**[18:00]** you have all your unshared datas. You

**[18:02]** have your structure tables. Uh some of

**[18:05]** them is on your online system. I know a

**[18:07]** lot of people is using pg vector

**[18:08]** postgress SQL by my SQL and then your uh

**[18:13]** after a while like after you uh you you

**[18:16]** might want to do a time to leave and

**[18:18]** move those datas into your iceberg uh

**[18:21]** you might also have a like elastic for

**[18:23]** your search uh and of course you have a

**[18:26]** lot of datas people up uh upload PDFs

**[18:29]** people upload images uh a lot of colors

**[18:33]** working yeah so you put all those datas

**[18:36]** in one data leak. Um and in this inside

**[18:40]** the dialect you have vectors, you have

**[18:42]** labels, you have your data summaries,

**[18:44]** some of the some of them are blobs to

**[18:47]** store all those image and uh audio video

**[18:49]** datas and you put into one layer and uh

**[18:52]** your agent can try to uh understand it

**[18:55]** especially I think that that makes total

**[18:58]** sense uh when like models like

**[19:00]** gymnastics 3.0 Zero comes out uh because

**[19:04]** uh what we see like uh no matter it's

**[19:07]** embedding models or it's large models uh

**[19:09]** it it tends to be multiodality and try

**[19:12]** to understand uh data from different

**[19:14]** source then you should definitely store

**[19:17]** all your data in one single source uh to

**[19:20]** make sure that uh your models can be

**[19:22]** easily uh able to or your agent can be

**[19:25]** easily able to fetch all the datas right

**[19:27]** originally we see a big data silo uh

**[19:30]** because data is actually located in

**[19:31]** different places and uh uh it might

**[19:34]** maintained by different teams. So uh

**[19:37]** challenge is it's even like not possible

**[19:40]** to get access to all your datas. But

**[19:42]** right now you have one single uh

**[19:44]** semantic layer you can do arbat you can

**[19:46]** do any kind of management on top of it.

**[19:48]** Uh and you can also build index on top

**[19:51]** of it to do uh accelerations. So make

**[19:53]** your life much easier.

**[19:57]** Okay. So uh several use cases for our uh

**[20:02]** milkflake uh for sure one one of the

**[20:04]** most famous one is uh context

**[20:06]** engineering. So people do dduplications

**[20:08]** summarize visions and they can also uh

**[20:11]** structure their context for AI agents

**[20:13]** and AI memory. Uh another uh interesting

**[20:16]** use case is a model search. Uh we

**[20:18]** actually powering one of the world's

**[20:20]** largest uh uh autonomous driving

**[20:23]** company. So uh what they do is they they

**[20:25]** actually collecting huge amount of uh

**[20:28]** datas uh into their in-house data lake

**[20:31]** systems and uh uh they want to like

**[20:34]** sometimes data scientists want to uh

**[20:36]** find a subset of their datas to to

**[20:38]** quantum their model. Uh for example, if

**[20:41]** my ultimate driving car is driving and

**[20:43]** it's raining, there is a red light uh uh

**[20:47]** uh beh like a uh in front and there's

**[20:50]** actually a dog pass uh pass a road and

**[20:54]** uh my car is is not driving in the right

**[20:56]** way. And they try to find those kind of

**[20:57]** scenarios using uh uh like a neural

**[21:01]** language and uh uh like like select a

**[21:05]** bunch of images or videos just to do

**[21:08]** another round of fun tuning. Uh that's a

**[21:10]** use case. Originally they they do a lot

**[21:13]** of taggings but taggings is actually

**[21:15]** limited because you have to pre-undering

**[21:18]** what people going to ask but with

**[21:20]** embeddings then you you can cover a lot

**[21:22]** of different corner cases and uh using

**[21:25]** using index and lake helping them to

**[21:27]** accelerate. Yeah. Uh third thing is data

**[21:31]** preparation. So we also working with uh

**[21:35]** one of the uh uh leading AI companies.

**[21:39]** So they have huge amount of data uh

**[21:40]** pre-trained datas. So uh they want to uh

**[21:44]** do a very fast retrieval on the datas

**[21:47]** and they also do a lot of pre-processing

**[21:49]** using uh ray. So uh we actually uh using

**[21:53]** this uh lake solution combining it with

**[21:56]** ray so they can easily writing a lot of

**[21:58]** different udfs uh to pro processing

**[22:00]** their data.

**[22:03]** Yeah, I think that's pretty much I want

**[22:05]** to share. So glad to take questions. You

**[22:08]** found him.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
