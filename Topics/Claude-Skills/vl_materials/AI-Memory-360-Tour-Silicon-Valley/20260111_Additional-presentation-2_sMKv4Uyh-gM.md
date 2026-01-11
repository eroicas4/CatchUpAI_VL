# Additional presentation 2

**원본 영상**: [https://www.youtube.com/watch?v=sMKv4Uyh-gM](https://www.youtube.com/watch?v=sMKv4Uyh-gM)
**작성일**: 2026-01-11
**Video ID**: sMKv4Uyh-gM

---

## 요약

NebulaGraph(Voft)의 Hal W가 그래프 데이터베이스 기반 AI 플랫폼과 'Fusion Graph RAG'를 소개하는 발표입니다. 기존 벡터 RAG의 한계를 지적하고, 그래프 RAG와 벡터 RAG의 장점을 결합한 Fusion Graph 개념을 통해 더 정확하고 효율적인 지식 검색 및 답변 생성이 가능함을 설명합니다.

---

## 핵심 포인트

- NebulaGraph는 세계 2위 그래프 데이터베이스로, 1000억 개 버텍스, 1조 개 엣지 처리 가능
- 전통적인 벡터 RAG는 세밀한 사실 구분, 문맥 연결, 전역 검색에서 한계가 있음
- 그래프 RAG는 문서 간 관계와 계층 구조를 보존하여 복잡한 질문에 효과적
- Fusion Graph는 그래프 RAG와 벡터 RAG의 장점을 결합한 NebulaGraph의 독자적 발명
- 인덱싱 속도가 자사 그래프 RAG 대비 5배, Microsoft 그래프 RAG 대비 100배 빠름

---

## 주요 내용

### 섹션 1: NebulaGraph 회사 소개
- 2018년 설립, Meta와 Alibaba 출신 창업자들
- DB-Engines 랭킹 그래프 데이터베이스 부문 2위
- ISO GQL 표준 최초 구현 벤더 (데이터베이스 분야 SQL 이후 40년 만의 두 번째 ISO 표준)
- 최대 100억 버텍스, 1조 엣지, 200TB 데이터 처리 실적

### 섹션 2: LLM 활용 방법론 비교
- **재학습(Retraining)**: 내부 지식으로 모델 재학습, 비용이 매우 높고 문서 업데이트마다 재학습 필요
- **프롬프트 엔지니어링**: 재학습 없이 프롬프트만 조정, 내부 지식 접근 불가로 환각 문제 해결 못함
- **RAG(추천)**: 비용 효율적이며 내부 비공개 지식에 접근 가능, 인덱스 생성 후 검색-생성 파이프라인

### 섹션 3: 벡터 RAG의 한계
- **세밀한 사실 구분 어려움**: "2023년 GDP"와 "2024년 GDP"가 벡터 공간에서 매우 유사
- **문맥 및 다중홉 연결 부족**: 문서 간 관계 파악 불가
- **수학적 유사도 ≠ 의미적 관련성**: "Apple(과일)"과 "Apple(회사)"이 벡터상 유사
- **전역 검색 및 추론 제한**: "모든 자료에서 상위 5개 중요 포인트"같은 질문에 약함

### 섹션 4: 벡터 RAG의 구체적 문제점
- **청킹 문제**: 
  - 청크 크기가 너무 작으면 문장 의미 왜곡 또는 반대 의미 생성
  - 청크 크기가 너무 크면 실제 정보가 묻혀 유사도 낮아짐
  - 최적 청크 크기는 예측 불가능하거나 존재하지 않을 수 있음
- **문맥 누락**: 계층적 문서 구조(L1, L2, L3 부서)에서 부서 레벨, 인용, 참조 정보 보존 안됨

### 섹션 5: 그래프 RAG의 장점
- **문서 관계 보존**: 부서별 문서를 노드로, 발행/참조 관계를 엣지로 표현
- **복잡한 질문 처리**:
  - 단순 질문: 벡터 RAG와 동일하게 처리
  - 관계 질문: "문서 A와 문서 C의 관계는?" → 서브그래프 매칭으로 연결 경로 발견
  - 전역 질문: "상위 5개 중요 메시지는?" → 커뮤니티 탐지 알고리즘으로 그래프 분할 및 요약

### 섹션 6: 그래프 RAG의 한계
- 인덱싱 단계가 더 비싸고 시간 소요
- 멀티모달 컨텍스트 처리 약함 (벡터는 모든 것을 임베딩 가능)
- **데이터 토픽 불일치 문제**: 서로 다른 버전의 보고서에서 상충되는 정보를 병합할 수 있음

### 섹션 7: Fusion Graph - NebulaGraph의 혁신
- **개념**: 그래프 RAG + 벡터 RAG + 전문 검색(Full-text) 통합
- **구조**: 
  - 기본 레이어: Knowledge Block
  - 상위 레이어: 문서 메타데이터 및 계층 구조(섹션, 챕터, 청크) 인덱싱
- **성능**: 
  - 자사 그래프 RAG 대비 인덱싱 5배 빠름
  - Microsoft 그래프 RAG 대비 100배 빠름 (20×5)
  - 답변 정확도 향상
- **기술 스택**: 그래프 인덱스 + 벡터 인덱스 + 전문 검색 인덱스 통합 활용

### 섹션 8: NebulaGraph 아키텍처
- **컴퓨팅-스토리지 분리 구조**:
  - 컴퓨팅 노드(Graph)와 스토리지 노드(Storage) 독립 확장
  - 유연성, 탄력성, 확장성 향상
- **Shared-Nothing 스토리지**: 
  - 데이터를 다수의 작은 파티션으로 분할
  - 각 파티션은 여러 복제본으로 복제
  - 복제본은 스토리지 노드에 분산 배치
- **쿼리 처리**: 컴퓨팅 노드가 해당 파티션 식별 → 스토리지 노드에서 데이터 검색
- **합의 계층**: Raft 합의 메커니즘 기반

### 섹션 9: 제품 라인업
- **NebulaGraph Database**: 기반 그래프 데이터베이스
- **Neo Application SDK**: 개발자용 Fusion Graph 기능 호출 SDK
- **Neo AI Application Platform**: 엔드투엔드 즉시 사용 가능한 제품
- **Cloud Service**: Neo AI 애플리케이션 플랫폼의 클라우드 버전

---

## 타임라인

- **00:00**: All right. So, hello everyone. Uh, my name is Hal W and I'm from Never and our company is called Voft. And, um, let me introduce a little bit about our company. It's our company was founded in 20 uh 2018 and our founders are from uh like Meta, Alibaba essentially and our vision is to become the number number one graph database uh in the world and currently we are reing ranking number two uh on DBMS on DB engine in terms of the uh graph database native uh database. And um uh here's a a little bit um introduction about the uh the features of network database. Um so first of all um we are aim we are targeting large scale and high performance uh scenarios and we support super large scale uh data set. So the maximum data set that we see on our customers are 100 billion vertices uh one hitting edging and 200 terabytes of data in terms of the data science and we are the leader leaders and uh we are among the first vendors uh who implement the ISO standard and ISO standard is the second uh ISO standard in the database area and the first one is ISS is SQL which was already 40 years ago and ISO standard was released uh April last year and we also talk about MCP and the component is our comp is what we are confident about. So we talk about um very high Q 1 million and latency very low and we also provide open source version that you can try out. Okay. So today I'm going to maybe talk about our new product called um our graph red or our uh AI platform based on graph red. I will introduce um a little bit of like why graph red and not red and what we invented uh in in this graph field. So first of all um the question uh that many enterprise will have when um trying to apply the large large language model is how to use the large language model. So here are several...
- **05:00**: digit but uh in in vector space they are very similar and the second uh issue of vector uh vector rag is lack lacking of contextual and multihop connections. So the vector uh right is not good at questioning like what's the relationship between these two document right and the third question the third issue is um the back the the vector approach is heavily depends on the similarity comparison but mathematical similarity doesn't equal to semantic ras I will provide an example of this later and and the last one is um vector rag is very limited in answering those global search or reasoning intensive questions. For example, a question like uh how do we think how do you like all the materials that are uploaded? What's what are top five important uh uh points that you can summarize from the documents that have just uploaded? So these kind of questions is not some traditional vector rack is good at. So since pure vector based rack has these limitations what else can we do? So an an alternative is graph rack. So on the left side is the uh the paper published by Microsoft research last year and actually uh our Neograph um proposed this idea actually even earlier than Microsoft and they cited our work in their inside their paper. Um I will walk through uh the limitations of the vector uh rack and discuss how graph can address this. So the first one is the the chunking selection. So the first the very first step of creating index in uh vector databases is to uh chunk to slice the document into chunks. Then the very the first question that you then you need to answer is what's the chunk size? The size of the chunk affects the quality of the text segmentation. If the chunk size is too small uh just like the example over here uh at the top you you may slice you may cut the sentence into very small...
- **10:00**: department document and these are the level two department documents and these are the level three department documents and they will reference um to each other like a level two department document will reference some contents in the level one department document. Okay. So if I use better database to store them, I will just slice the document into chunks and these chunks in different departments are just equal. They are just chunks. They don't preserve any information like whether it's from like a level one or level two or it doesn't preserve the citation information or it doesn't preserve any reference information. They are just equal charts. Okay. But if we use a graph database, we we can create a a graph like this. For example, I will create first of all, I'll create a node called L1 department and also a node called L2 department and a node called L3 department. And then I will create all the all the nodes for I will create a note for each document and create a link or edge uh called publish to links the department and the documents published by this department. Okay. So I will then I will create a um two three groups the documents of department one documents of department two and documents of department three. And let's say I uh this document C published from uh published by L2 shell some common entities with this document D from U department one then I can create an edge like this saying that these two documents are related because they share the same entity. Okay. So by this means I can create a a relationship between different uh uh documents very easily. It's very natural. So what's the impact of of the of the difference? So the impact lies in this global search and community level reasoning. So assuming on the right side assuming we have three different type of questions. Okay. So the first question is what is the main content of the doc...
- **15:00**: inconsistent data topics uh also have issues when they are inconsistent data topics um for example when you when when answering a global or multiple question uh graph rag may unintentionally merge information from two different document versions for example uh I'm trying to ask a question about apple apple.com uh financial status analysis right then I can got two different an analysis report from two different companies they may have conflicting results or conflicting information then by using graph red I may the the general answer may combine find these completing numbers from both of the documents and then send you the result and and generate and send the results to human beings. This is something that is very hard for a graph rack to to to to avoid. So um that's why we introduced this con this concept of called fusion graph. This is our invention uh by negraph. So fusion graph leverage the document metad data and hierarchical structures. So our our base layer of m of our uh foundation is still knowledge block but we build another layer um to index document level metad data and document structure like sections, chapters and chunks. And with um with this uh fusion graph our indexing can be faster than our own version of graph rack uh like five time five five times faster and our own version of graph rack is already 20 times faster than uh the Microsoft graph rack in terms of the index building stage and we are also more accurate in question answering and our graph rack fusion grapher is built upon our underlying network graph database which is which which which supports not only graph index but also supports vector index and full text index. So we have a capability to utilize all all the advantage of these three indexes factor index and vortex index and graph index to generate the...
- **20:00**: And and this is the architecture of our fusion graph rack. So you can see graph is sitting in the middle of the structure. So we allow users to update to upload all kinds of documents. So yes uh uh fusion our fusion graph network graph is multimodel. So we support not only documents but also image tables and all kinds of document documents and based on the index that people want to create right. So we create with never graph support vector index for text index and and graph index. So based on the index that people choose uh we can create a graph or embeddings and then we will store either graph or embeddings inside network graph and when people ask a question we will either create a embedding of the question or split the question into multiple nodes and then we will create a query plan to answer this question and this query plan is main about how to search the backup database and how to search the network graph using factor and how to search network graph using uh a graph index and then we'll achieve the the data being stored in the network graph database and send to generate the answers and this is the um um overview of our network graph application platform. So this is the interface and you can see you can create an app um on this interface. So it requires zero code to build AI application and inside each app you can reference which documents or which knowledge which knowledge set that you want to use to answer this question and we also have an interface to show the indexes. Right? So here is a visualized graph index and it's with this with this visualized index is explainable and auditable. You can you can tell why the answers is generate is generated like this and this is the interface of the...

---

## 전체 자막 (타임스탬프 포함)

**[00:00]** All right. So, hello everyone. Uh, my

**[00:03]** name is Hal W and I'm from Never and our

**[00:06]** company is called Voft.

**[00:09]** And, um, let me introduce a little bit

**[00:11]** about our company. It's our company was

**[00:14]** founded in 20 uh 2018 and our founders

**[00:18]** are from uh like Meta, Alibaba

**[00:20]** essentially and our vision is to become

**[00:22]** the number number one graph database uh

**[00:26]** in the world and currently we are reing

**[00:28]** ranking number two uh on DBMS on DB

**[00:32]** engine in terms of the uh graph database

**[00:37]** native uh database.

**[00:42]** And um uh here's a a little bit um

**[00:46]** introduction about the uh the features

**[00:48]** of network database. Um so first of all

**[00:52]** um we are aim we are targeting large

**[00:55]** scale and high performance uh scenarios

**[00:59]** and we support super large scale uh data

**[01:02]** set. So the maximum data set that we see

**[01:04]** on our customers are 100 billion

**[01:07]** vertices uh one hitting edging and 200

**[01:10]** terabytes of data in terms of the data

**[01:13]** science and we are the leader leaders

**[01:15]** and uh we are among the first vendors uh

**[01:19]** who implement the ISO standard and ISO

**[01:23]** standard is the second uh ISO standard

**[01:27]** in the database area and the first one

**[01:30]** is ISS is SQL which was already 40 years

**[01:32]** ago and ISO standard was released uh

**[01:36]** April last year and we also talk about

**[01:39]** MCP

**[01:40]** and the component is our comp

**[01:44]** is what we are confident about. So we

**[01:47]** talk about um very high Q

**[01:50]** 1 million and latency very low

**[01:54]** and we also provide open source version

**[01:56]** that you can try out.

**[02:01]** Okay. So today I'm going to maybe talk

**[02:03]** about our new product called um our

**[02:07]** graph red or our uh AI platform based on

**[02:12]** graph red. I will introduce um a little

**[02:15]** bit of like why graph red and not red

**[02:18]** and what we invented uh in in this graph

**[02:22]** field.

**[02:25]** So first of all um the question uh that

**[02:28]** many enterprise will have when

**[02:31]** um trying to apply the large large

**[02:34]** language model is how to use the large

**[02:37]** language model. So here are several

**[02:39]** methods. The first method is bun. Okay.

**[02:42]** So this is kind of an extreme. Um

**[02:47]** people will retrain their model based on

**[02:50]** their internal target knowledge and uh

**[02:54]** and then they will uh they will be a the

**[02:58]** the retrained model will be able to

**[03:01]** answer their uh answer the questions

**[03:03]** based on their internal knowledge. But

**[03:05]** the issue is this is very expensive not

**[03:07]** like no for all companies and it's also

**[03:12]** um it also requires to return every time

**[03:16]** you update your documents. Okay. And the

**[03:20]** other uh extreme is uh prompt engineer

**[03:23]** is basically don't do any return but

**[03:25]** directly um you need to your prompts to

**[03:30]** try to get answer from the uh uh from

**[03:35]** but the issue is the prompt we prompt

**[03:38]** engineer the last model have access to

**[03:42]** internal knowledge so it cannot solve

**[03:44]** the hallucination issues. So between

**[03:47]** these we usually recommend using rack

**[03:50]** yeah because it's um it's cheap right

**[03:54]** you don't need to retain any model and

**[03:56]** it has it has access to your uh internal

**[03:59]** private knowledge

**[04:04]** and this is the paradigm of the uh rack.

**[04:08]** So usually it will uh create index of

**[04:10]** your internal knowledge and during the

**[04:13]** query process it will retrieve the

**[04:15]** knowledge from your database and then

**[04:18]** send the retrieve uh the retrieved the

**[04:20]** knowledge to the LRM to generate the

**[04:22]** final answers. Um when people talk about

**[04:25]** the red people usually talk about u the

**[04:28]** vector database. Okay. But we find

**[04:31]** actually there are several uh issues or

**[04:34]** challenges

**[04:35]** uh

**[04:37]** of the traditional vector database. The

**[04:40]** first one is uh ve the vector database

**[04:42]** is hard to differentiate fine grain

**[04:45]** factual difference. Uh for example here

**[04:48]** I have two questions. One question is uh

**[04:50]** what's the GDP of the United States in

**[04:53]** 2024 and the second question is what is

**[04:55]** the uh GDP of United States in 2023.

**[04:59]** These two sentences only differs in one

**[05:01]** digit but uh in in vector space they are

**[05:04]** very similar

**[05:07]** and the second uh issue of vector uh

**[05:11]** vector rag is lack lacking of contextual

**[05:14]** and multihop connections. So the vector

**[05:18]** uh right is not good at questioning like

**[05:21]** what's the relationship between these

**[05:23]** two document right

**[05:26]** and the third question the third issue

**[05:28]** is um the back the the vector approach

**[05:32]** is heavily depends on the similarity

**[05:34]** comparison but mathematical similarity

**[05:37]** doesn't equal to semantic ras I will

**[05:40]** provide an example of this later and and

**[05:43]** the last one is um vector rag is very

**[05:46]** limited in answering those global search

**[05:49]** or reasoning intensive questions. For

**[05:51]** example, a question like uh how do we

**[05:54]** think how do you like all the materials

**[05:57]** that are uploaded? What's what are top

**[05:59]** five important uh uh points that you can

**[06:02]** summarize from the documents that have

**[06:05]** just uploaded? So these kind of

**[06:06]** questions is not some traditional vector

**[06:10]** rack is good at.

**[06:14]** So since pure vector based rack has

**[06:16]** these limitations what else can we do?

**[06:18]** So an an alternative is graph rack. So

**[06:21]** on the left side is the uh the paper

**[06:24]** published by Microsoft research last

**[06:26]** year and actually uh our Neograph um

**[06:30]** proposed this idea actually even earlier

**[06:32]** than Microsoft and they cited our work

**[06:35]** in their inside their paper.

**[06:39]** Um I will walk through uh the

**[06:42]** limitations of the vector uh rack and

**[06:46]** discuss how graph can address this. So

**[06:50]** the first one is the the chunking

**[06:52]** selection. So the first the very first

**[06:55]** step of creating index in uh vector

**[06:58]** databases is to uh chunk to slice the

**[07:01]** document into chunks. Then the very the

**[07:05]** first question that you then you need to

**[07:07]** answer is what's the chunk size? The

**[07:10]** size of the chunk affects the quality of

**[07:11]** the text

**[07:13]** segmentation. If the chunk size is too

**[07:16]** small uh just like the example over here

**[07:19]** uh at the top you you may slice you may

**[07:23]** cut the sentence into very small

**[07:25]** fragmentations and this may not

**[07:28]** represent the real meaning of the

**[07:29]** original sentence and may even you will

**[07:32]** may even end up with an opposite meaning

**[07:34]** of the original sentence. And if the

**[07:37]** chunk is too large just like the example

**[07:39]** over here

**[07:41]** is almost the whole paragraph then the

**[07:44]** real information will be buried. Uh for

**[07:47]** example I I'm trying to ask a question

**[07:49]** and the person the the answer matching

**[07:51]** this question is just a few words in a

**[07:55]** large chunk then the similarity that you

**[07:57]** get between my question and this large

**[08:00]** chunk is very small.

**[08:03]** So the optimal chunk size for different

**[08:05]** types of tags is unpredictable and may

**[08:07]** not even exist.

**[08:11]** And the next uh the next issue that I

**[08:13]** I've already mentioned is the vector

**[08:15]** relevance doesn't means semantic

**[08:18]** relevance. So let's take a look at a

**[08:20]** example over here. So here I have two

**[08:23]** sentence. The first sentence is apple is

**[08:25]** valuable because it provides the

**[08:26]** vitamins that people need and human

**[08:30]** being can easily tell this apple means a

**[08:33]** fruit.

**[08:35]** And the second question is apple is

**[08:37]** valuable because it provides intelligent

**[08:39]** experience that people need. After some

**[08:42]** thinking people can also easily guess

**[08:45]** have a high confidence guess this apple

**[08:49]** means Apple

**[08:51]** all the products from Apple right

**[08:55]** but if we trans transfer these two

**[08:57]** sentences into vectors you will end up

**[09:00]** the embeddings like this this I'm just

**[09:02]** here to provide illustration the actual

**[09:06]** dimension of the embedding should be

**[09:08]** larger than this but you can see uh

**[09:11]** income uh in terms of the vector uh

**[09:14]** these two sanities will be very similar

**[09:18]** and the similar another example is is a

**[09:21]** two graphs over here like coral and uh

**[09:25]** and correct these two

**[09:29]** words are representing exactly totally

**[09:31]** two different things but in terms of

**[09:33]** vector space uh they are

**[09:38]** okay and the third challenge is the the

**[09:41]** contextual leakage and multi-document

**[09:43]** relationship that I mentioned that um

**[09:46]** earlier that a vector rag is not is not

**[09:49]** good at to preserve the relationship

**[09:52]** between documents. So assuming I have a

**[09:55]** um a multi-level hierarchical document

**[09:58]** like like here. So this is the level one

**[10:01]** department document and these are the

**[10:03]** level two department documents and these

**[10:05]** are the level three department documents

**[10:08]** and they will reference

**[10:10]** um to each other like a level two

**[10:12]** department document will reference some

**[10:13]** contents in the level one department

**[10:15]** document. Okay. So if I use better

**[10:18]** database to store them, I will

**[10:22]** just slice the document into chunks and

**[10:24]** these chunks in different departments

**[10:27]** are just equal. They are just chunks.

**[10:30]** They don't preserve any information like

**[10:33]** whether it's from like a level one or

**[10:35]** level two or it doesn't preserve the

**[10:38]** citation information or it doesn't

**[10:40]** preserve any reference information. They

**[10:42]** are just equal charts.

**[10:46]** Okay. But if we use a graph database, we

**[10:50]** we can create a a graph like this. For

**[10:52]** example, I will create first of all,

**[10:54]** I'll create a node called L1 department

**[10:57]** and also a node called L2 department and

**[11:00]** a node called L3 department. And then I

**[11:03]** will create all the all the nodes for I

**[11:08]** will create a note for each document and

**[11:10]** create a link or edge uh called publish

**[11:14]** to links the department and the

**[11:16]** documents published by this department.

**[11:19]** Okay. So I will then I will create a um

**[11:22]** two three groups the documents of

**[11:25]** department one documents of department

**[11:27]** two and documents of department three.

**[11:30]** And let's say I uh this document

**[11:34]** C published from uh published by L2

**[11:38]** shell some common entities with this

**[11:41]** document D from U department one then I

**[11:45]** can create an edge like this saying that

**[11:49]** these two documents are related because

**[11:52]** they share the same entity. Okay. So by

**[11:55]** this means I can create a a relationship

**[11:58]** between different uh uh documents very

**[12:01]** easily. It's very natural.

**[12:06]** So what's the impact of of the of the

**[12:10]** difference? So the impact lies in this

**[12:12]** global search and community level

**[12:14]** reasoning. So assuming on the right side

**[12:17]** assuming we have three different type of

**[12:19]** questions. Okay. So the first question

**[12:22]** is what is the main content of the doc

**[12:24]** from the level one department? This

**[12:26]** question is very direct. It's it's it's

**[12:29]** just a single question. A very simple

**[12:32]** question. And if you use a vector

**[12:34]** database, it can achieve it can answer

**[12:37]** this question really well. Okay, because

**[12:40]** it just need to find the chance related

**[12:42]** to this uh this document. And and what

**[12:46]** if I have this question like what is the

**[12:48]** relationship between doc A from level

**[12:49]** one department and doc C from level two

**[12:52]** department. Uh it can find the documents

**[12:55]** the the related chunks of of level one

**[12:59]** department and and the related chunks of

**[13:02]** doc from level two department but you

**[13:04]** cannot find the relationship because

**[13:06]** it's just not there. It's not in the

**[13:08]** vector database.

**[13:10]** And how about the third question like

**[13:12]** what are top five important messages

**[13:14]** then it's really hard because the

**[13:17]** database doesn't just know how to do

**[13:19]** this

**[13:22]** then what if we have a graph database

**[13:24]** right we have a graph record uh for this

**[13:28]** question number two like what's the

**[13:30]** relationship between doc a from level

**[13:32]** one department and doc c from level two

**[13:35]** department it can easily first it can

**[13:38]** easily achieve this search by locating

**[13:40]** between these two document right this

**[13:43]** document and this document and then

**[13:45]** apply by doing some like subraph match

**[13:49]** or uh some very mature establish graph

**[13:54]** algorithm it can easily find the

**[13:56]** connections between this who knows who

**[13:59]** by exploring uh this graph okay and how

**[14:03]** about this question like what are the

**[14:04]** top five important messages this

**[14:07]** question also be answered easily by

**[14:09]** applying some graph algorithm like a uh

**[14:12]** later community detection to summarize

**[14:16]** to divide a graph into several

**[14:17]** communities and then summarize of each

**[14:21]** community and then after basaries

**[14:27]** but

**[14:29]** this graph rag enough no the graph rack

**[14:32]** still also have some uh issues comparing

**[14:35]** with better rack the index stage of

**[14:38]** graph rack is more expensive and takes

**[14:40]** more time

**[14:42]** and it's also not good at multiodel

**[14:45]** contexts like vector actually can uh

**[14:48]** transfer transform everything on the

**[14:50]** word into embeddings but not every all

**[14:53]** not all data can be transformed into

**[14:55]** graph and also uh graph has issues of

**[15:00]** inconsistent data topics uh also have

**[15:03]** issues when they are inconsistent data

**[15:05]** topics um for example when you when when

**[15:08]** answering a global or multiple question

**[15:11]** uh graph rag may unintentionally merge

**[15:13]** information from two different document

**[15:15]** versions for example uh I'm trying to

**[15:17]** ask a question about apple apple.com uh

**[15:22]** financial

**[15:24]** status analysis right then I can got two

**[15:27]** different an analysis report from two

**[15:29]** different companies they may have

**[15:31]** conflicting results or conflicting

**[15:33]** information then by using graph red I

**[15:36]** may the the general answer may combine

**[15:38]** find these completing numbers from both

**[15:41]** of the documents and then send you the

**[15:42]** result and and generate and send the

**[15:45]** results to human beings. This is

**[15:47]** something that is very hard for a graph

**[15:49]** rack to to to to avoid.

**[15:53]** So um

**[15:56]** that's why we introduced this con this

**[15:58]** concept of called fusion graph. This is

**[16:01]** our invention uh by negraph. So fusion

**[16:05]** graph leverage the document metad data

**[16:07]** and hierarchical structures. So our our

**[16:11]** base layer of m of our uh foundation is

**[16:15]** still knowledge block but we build

**[16:18]** another layer um to index document level

**[16:22]** metad data and document structure like

**[16:24]** sections, chapters and chunks.

**[16:28]** And with um with this uh fusion graph

**[16:33]** our indexing can be faster than our own

**[16:37]** version of graph rack uh like five time

**[16:40]** five five times faster and our own

**[16:42]** version of graph rack is already 20

**[16:44]** times faster than uh the Microsoft graph

**[16:47]** rack in terms of the index building

**[16:49]** stage and we are also more accurate in

**[16:51]** question answering

**[16:53]** and our graph rack fusion grapher is

**[16:55]** built upon our underlying network graph

**[16:58]** database which is which which which

**[17:01]** supports not only graph index but also

**[17:03]** supports vector index and full text

**[17:06]** index. So we have a capability to

**[17:09]** utilize all all the advantage of these

**[17:11]** three indexes factor index and vortex

**[17:13]** index and graph index to generate the

**[17:16]** results

**[17:17]** the to generate the best result and we

**[17:20]** also enhance those multiple graph

**[17:22]** algorithm to help the search to help the

**[17:26]** retrieval of knowledge.

**[17:29]** So I've mentioned that uh um uh this

**[17:32]** fusion block is kind of our invention

**[17:34]** and upon that we build our nei

**[17:37]** application SDK for developers to call

**[17:40]** the functions of to of our fusion graph

**[17:43]** and we also have a neo AI application

**[17:46]** platform which is an end toend product

**[17:48]** uh for user to uh to use uh from open

**[17:52]** box and we also uh have a cloud service

**[17:55]** of this neo air application platform.

**[17:58]** Yeah, I've already mentioned that the

**[18:00]** foundation of uh our graph rack product

**[18:03]** is network graph database. Then maybe I

**[18:06]** can introduce a little bit about the uh

**[18:09]** our network graph database and see how

**[18:11]** it can and why it can support the our

**[18:15]** graph product. Yes. First of all, our

**[18:18]** network graph database is a separated

**[18:20]** compute and storage architecture and our

**[18:22]** compute node is called graph and storage

**[18:24]** node is storage. Since it's set a

**[18:28]** separated architecture rather than to

**[18:30]** collated architecture, um we can achieve

**[18:33]** a more flexibility and more elasticity

**[18:37]** and we can have a better scalability

**[18:42]** and and this computer node and storage

**[18:45]** node can scale independently

**[18:48]** and the storage are using shell nothing

**[18:51]** structure so it's easy to scale and and

**[18:53]** also for tolerate

**[18:55]** and data have been partitioned into a

**[18:57]** lot of small partitions and the

**[18:58]** partitions are way more than the number

**[19:00]** of the number of partitions is way more

**[19:02]** than the number of storage nodes and

**[19:05]** each partition is replicated into

**[19:07]** multiple replicas and each replicated

**[19:11]** partition will be assigned to a storage

**[19:12]** node. When uh serving a quary uh the

**[19:16]** computer node will find the the

**[19:19]** corresponding partitions uh will find

**[19:21]** the partitions responsible for um retrie

**[19:25]** for for achieving this query and then

**[19:28]** access the corresponding storage node to

**[19:30]** retrieve the data

**[19:32]** and we have a consensus consensus layer

**[19:35]** built upon uh uh rough consensus rec

**[19:40]** mechanism to ensure the strong

**[19:42]** consistency. between replicas and high

**[19:45]** availability and high durability. And we

**[19:48]** have a centralized meta span data

**[19:49]** service which is also distributed to

**[19:52]** store the metadata information like

**[19:53]** schema leader information, user

**[19:56]** information and etc.

**[20:00]** And and

**[20:03]** this is the architecture of our fusion

**[20:05]** graph rack. So you can see graph is

**[20:08]** sitting in the middle of the structure.

**[20:10]** So we allow users to update to upload

**[20:13]** all kinds of documents. So yes uh uh

**[20:16]** fusion our fusion graph network graph is

**[20:19]** multimodel. So we support not only

**[20:21]** documents but also image tables and all

**[20:24]** kinds of document documents and based on

**[20:26]** the index that people want to create

**[20:29]** right. So we create with never graph

**[20:31]** support vector index for text index and

**[20:34]** and graph index. So based on the index

**[20:37]** that people choose uh we can create a

**[20:40]** graph or embeddings

**[20:42]** and then we will store either graph or

**[20:44]** embeddings inside network graph

**[20:47]** and when people ask a question we will

**[20:50]** either create a embedding of the

**[20:52]** question or split the question into

**[20:54]** multiple nodes and then we will create a

**[20:58]** query plan to answer this question and

**[21:00]** this query plan is main about how to

**[21:03]** search the backup database and

**[21:06]** how to search the network graph using

**[21:08]** factor and how to search network graph

**[21:10]** using uh a graph index and then we'll

**[21:13]** achieve the the data being stored in the

**[21:16]** network graph database and send to

**[21:18]** generate the answers

**[21:22]** and this is the um

**[21:27]** um overview of our network graph

**[21:30]** application platform. So this is the

**[21:32]** interface and you can see you can create

**[21:35]** an app

**[21:37]** um on this interface. So it requires

**[21:40]** zero code to build AI application and

**[21:43]** inside each app you can reference which

**[21:46]** documents or which knowledge which

**[21:48]** knowledge set that you want to use to

**[21:51]** answer this question

**[21:53]** and we also have an interface to show

**[21:55]** the indexes. Right? So here is a

**[21:58]** visualized graph index and it's with

**[22:02]** this with this visualized index is

**[22:04]** explainable and auditable. You can you

**[22:07]** can tell why the answers is generate is

**[22:10]** generated like this

**[22:14]** and this is the interface of the

**[22:15]** question answering uh it's similar to

**[22:19]** chat GPT um so it's you can use natural

**[22:22]** language uh to ask questions and our uh

**[22:27]** question answering accuracy is uh is

**[22:30]** high as of October 1st our question

**[22:32]** answering accuracy it can reach uh 0.81

**[22:35]** 81 on benchmark data set and the

**[22:39]** question is not is not like question

**[22:41]** it's complicated multiple question when

**[22:43]** you when we when we evaluate this and uh

**[22:47]** even some customer data set we can reach

**[22:49]** 95% accuracy it's better than the best

**[22:53]** open source solution which is which can

**[22:55]** only achieve uh 0 71 accuracy


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
