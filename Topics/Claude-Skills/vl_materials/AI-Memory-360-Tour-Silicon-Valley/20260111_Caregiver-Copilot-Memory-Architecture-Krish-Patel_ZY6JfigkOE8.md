# Caregiver Copilot Memory Architecture - Krish Patel

**원본 영상**: [https://www.youtube.com/watch?v=ZY6JfigkOE8](https://www.youtube.com/watch?v=ZY6JfigkOE8)
**작성일**: 2026-01-11
**Video ID**: ZY6JfigkOE8

---

## 요약

Caregiver Copilot은 치매 환자를 돌보는 간병인을 위한 AI 파트너로, 개인화된 기억 저장 기능과 AI 지식을 결합하여 일지, 약물, 진료 예약 등을 추적하고 맞춤형 조언을 제공합니다. 전 세계 5,500만 명의 치매 환자와 그들을 돌보는 간병인들의 우울증(75%)과 부담을 줄이기 위해 개발된 이 시스템은 6가지 건강 기둥(수면, 영양, 운동 등)을 기반으로 환자의 전체 케어 여정을 기억하고 분석합니다. 공개 의료 지식과 환자의 개인 기록을 통합하여 실시간 맞춤형 가이드를 제공하는 새로운 시대의 간병 솔루션입니다.

---

## 핵심 포인트

- 치매 환자 간병인의 75%가 우울증을 경험하며, 2025년까지 환자 수가 3배 증가 예상
- AI와 개인화된 메모리를 결합하여 환자의 전체 케어 여정을 기억하고 분석
- 6가지 건강 기둥(수면, 영양, 신체운동, 정신운동, 사회적 교류, 의료 관리) 기반 프레임워크
- 일일 저널, 약물 관리, 일정 관리, 대시보드, AI 챗봇 등 통합 기능 제공
- 미국 시장만 800만 간병인, 8억 4천만 달러 규모의 잠재 시장
- 간병인뿐 아니라 가족 구성원과 의사도 환자 정보에 접근 가능
- MemE Machine(벡터 검색, 메모리 통합)과 OpenAI GPT-4를 활용한 기술 아키텍처

---

## 주요 내용

### 섹션 1: 문제 인식과 프로젝트 탄생
- 인간은 3일 내 97%를 망각하며, 치매 환자를 돌보는 간병인은 환자의 '기억' 역할을 해야 함
- 한 달 전 AI 해커톤에서 치매 환자용 AI 동반자로 1등 수상
- 실제 가족들과 대화 후, 환자보다는 간병인을 돕는 것이 더 효과적임을 깨닫고 Caregiver Copilot으로 전환
- 대부분의 AI는 환자에 대한 개인 정보가 없어 실질적 도움을 주지 못함

### 섹션 2: 시장 규모와 타겟
- 전 세계 5,500만 명의 치매 환자, 향후 25년간 3배 증가 예상
- 70%의 환자가 가족 구성원에 의해 집에서 돌봄 받음
- 간병인의 75%가 우울증 경험, 후기 단계에서는 24/7 전담 간호 필요
- 미국 시장: 800만 가정 간병인 중 25%(200만 명)를 타겟으로 1인당 $480, 총 $8.4억 시장 규모
- 주요 타겟: 사랑하는 사람(loved one)과 그들을 돌보는 간병인, 가족, 의사

### 섹션 3: 6가지 건강 기둥 프레임워크
- 치매 7단계 전반에 걸쳐 환자의 기억, 이동성, 행동, 간병인 역할이 변화
- 증거 기반 6가지 정신 건강 기둥 적용: 수면, 영양, 신체운동, 정신운동, 사회적 교류, 의료 관리
- 각 기둥은 환자의 건강 상태와 컨디션에 대한 귀중한 정보 제공
- 모든 단계에서 학습하고 기억하며 가이드하여 간병인이 혼자라고 느끼지 않도록 지원

### 섹션 4: 주요 기능
- **온보딩**: 신규 간병인 및 대체 간병인을 위한 포괄적 프레임워크
- **조직화된 케어 관리**: 의사, 보험, 기본 케어 필요사항 조율
- **효과적인 커뮤니케이션**: 간병인, 가족, 의사 간 환자 정보 공유로 통합 케어 팀 구성
- **AI 챗봇**: 개인 기록과 공개 지식에 접근하여 간병인 질문 답변, 인사이트, 리소스, 번아웃 예방 팁 제공

### 섹션 5: 기술 아키텍처
- **프론트엔드**: Streamlit 웹앱
- **백엔드**: API 호출, CORS 보안, JWT 인증
- **LLM 클라이언트**: OpenAI GPT-4 (자연어 이해, 커스텀 프롬프트, 함수 호출)
- **MemE Machine 클라이언트**: PostgreSQL + Neo4j 환경에서 실행
- **벡터 메트릭스**: 시맨틱 검색, 대화 간 지속적 컨텍스트 유지, 자동 메모리 통합
- **스케줄러**: 일일 약속 및 약물 알림
- 챗봇이 모든 기능에 대한 중앙 제어권 보유

### 섹션 6: 일일 저널 (Daily Journal)
- 6가지 건강 기둥에 기반한 강력한 간병 도구
- 간병인이 매일 5분 이내 체크리스트 작성: 활동 참여, 각 기둥별 평가, 자유 형식 노트
- AI가 시간에 따른 패턴 식별, 일일 항목에서 중요한 인사이트 제공
- 데이터 기반 심층 분석으로 더 명확하고 풍부한 일상 경험 이해

### 섹션 7: 사용자 친화적 대시보드
- 간병인, 가족, 의사 모두 접근 가능한 시스템의 심장부
- **상단**: 6가지 건강 기둥 관련 환자 진행 상황 및 이력 시각화 (가족과 의사가 처음으로 확인 가능)
- **우측**: 약물 일정(복용량, 시간, 지침)
- **좌측**: 예정된 진료 예약 및 연체된 예약(설명, 위치, 날짜, 시간)
- **하단**: 최근 며칠~90일 선택 가능한 인터랙티브 그래프로 6가지 건강 기둥과 일일 저널 시각화
- 버튼 클릭만으로 환자 건강 진행 상황을 시각화하는 AI 시대의 새로운 기능

### 섹션 8: 약물 관리 페이지
- 간병인이 환자의 약물 추가 가능
- 복용량, 빈도, 복용 시간 설정
- 의사와 간병인이 약물 비활성화/삭제 가능
- **가장 중요**: 전체 약물 이력 접근 가능

### 섹션 9: 캘린더 및 진료 예약 페이지
- 효과적인 일정 관리를 위한 필수 기능
- '이벤트 추가' 기능으로 환자 일정 직접 예약
- 캘린더 보기 페이지로 모든 이벤트 간편하게 확인 (대시보드에도 표시)
- **진료 예약 관리**: 예정/과거 예약 확인, 진료 중/후 의사 노트 및 관찰 사항 기록으로 다음 방문 준비

### 섹션 10: 리포트 기능
- 의사, 간병인, 가족 구성원을 위한 데이터 기반 리포트
- 전날 또는 선택한 날짜의 약물 순응도, 일일 저널, 환자 관련 대화 체크 제공
- 평가, 요약, 환자 일상 및 건강 기둥 개선을 위한 피드백 제공
- **예시**: 수면 부족 시 취침 전 화면 시간 줄이기, 명상 권장 등 맞춤형 조언

### 섹션 11: AI 어시스턴트 (핵심 기능)
- 시스템의 '두뇌' 역할
- **공개 지식**: AI의 방대한 증거 기반 가이드, 의료 연구, 간병 모범 사례
- **개인 기록**: 일일 저널, 약물 로그, 진료 노트, 챗봇 대화 등 환자의 개인 이력
- 시간에 따른 실제 패턴 식별 및 상세한 응답 생성
- 6가지 건강 기둥의 트렌드 강조 및 의미 있는 가이드 제공
- **예시**: "지난주 Trisha의 수면은 어땠나요?" → 지난주 수면 완전 개요, 노트와 평가, 다음 주 점수 개선을 위한 전략 제시
- 데이터가 누적될수록 챗봇의 응답이 더욱 정교해짐
- Reddit, Facebook 그룹, 온라인 기사를 몇 시간 동안 검색하던 것을 한곳에 모아 실시간 맞춤형 교육적 응답 제공

### 섹션 12: 결론 및 비전
- LLM 지식과 개인화된 개인 메모리 결합으로 새로운 간병 시대 개막
- 사람들이 이미 ChatGPT에서 정보를 찾기 시작했으나, 개인 메모리 추가로 완전히 새로운 수준으로 발전
- 치매 환자나 간병인을 아는 사람들에게 베타 사용자로 등록 권장
- QR 코드 스캔으로 연락 및 설정 가능
- AI Memory Forum에 감사 표현

---

## 타임라인

- **00:00**: So, I want to start off by kind of talking about some of the things that Charles mentioned earlier about how humans tend to forget and how Gabriel emphasized as well that up to 97% within 3 days. When it comes to caring for someone with memory loss, that means that you become their memory. Tracking medications, behaviors, doctor's appointments while exhausted and overwhelmed. Most AI can't help because it knows nothing about your loved one. Caregiver Copilot changes that. There's a new era of caregiving where people are already looking to chat GPT for information. But we have taken it to a new level by combining AI knowledge with personalized and private memory. Caregiver Co-opilot is an AI partner that remembers the entire journey. Every journal entry, every pattern, every detail, and it combines that personal history with deep knowledge of memory care. So today we're going to show you how we built it. My name is Chris Patel >> and I'm Danala >> and we're the found co-founding uh engineers behind Caregiver Co-Pilot and we're really excited to be here today. So let's just get right into it. So, taking a step back to where it all began, about a month ago, we went to Members's Memories that last AI agents hackathon and we came up with memory care, an AI companion that remembers everything for dementia patients from tracking their medications and routines to their life stories. And it was also someone that they could talk to that has the information that they might have forgotten. We won first place at the hackathon, but once we sat down and talked to real families such as Franks, we found that the best way we can help dementia patients is by helping their caregivers thrive at their jobs. So, Caregiver Copilot was born. Now, if you look at the slide behind me, every number on the slide tells the same story. Caregiving is overwhelming with...
- **05:00**: now so we integrating machine and open so me machine help us to ve with vector metics for cementing search and it help us to keep persistent context across the conversation and it also provide us with a automatic consolidation memory and for opening as we're using GB4 for natural language understanding and we designed some custom fonts for higher context and we also implement a function calling for tool integration and our chatbot has control over commercial control over all our features >> and then uh moving on to our core entities we're going to start with the daily journal which is a powerful caregiving tool built upon the foundational six pillars of health which are once again sleep, nutrition, mental exercise, physical exercise, social interaction and medical care. Every single day, the caregiver can log in and fill out a quick validated evaluation framework in within five minutes where they can check off boxes for any activities that the loved one participated in as well as provide ratings for each of the pillars and free form notes incorporate any specific details or observations for a clear, richer understanding of daily experiences. Our AI identifies patterns over time, offering crucial insights from the daily entries and providing deeper datadriven analysis. Now this is our user friendly dashboard which is kind of like the heart of our system which can be accessed by the caregiver but it can also be accessed by the family members and doctors. This is the top half. Um for the first time ever family members and doctors can peer into their loved ones progression and their history regarding all six pillars of health. On the right hand side we have a medications tab where you can see the upcoming medication schedule with any doses, timings and instructions. On the lefth hand side, we have the upcoming...
- **10:00**: the last week along with the notes and ratings. And then it provides guidance as well as potentially beneficial strategies to improve the score for the upcoming week. Um, and this is just based off of one week's input, but as we keep adding data, as we keep filling out journal entries, and keep having conversations, the chat will grow with all the data that it gets. So, as kind of Frank mentioned earlier, hours of combing through Reddit posts, Facebook groups, online articles, looking for your very specific issue is now simplified with all the data in one place along with the loved one's private personal history for real time personalized educated responses. If you sum it all up, combining LLM knowledge with personalized and private memory is going to open the door to a new era of caregiving. As I mentioned earlier, people have already began to look to Chat GBT for information. But now, the addition of private memory is going to take it to a whole new level. If any of you know a caregiver or have a loved one with dementia and believe that Caregiver Copilot could be a useful tool to assist them, please scan our QR code. It's on the screen. It's also on the banner over there. we'd love to get in touch and get them set up as a beta user. Um, thank you guys so much for listening and thank you to the AI memory forum for giving us this opportunity. We hope you guys enjoyed and please feel free to ask any questions....

---

## 전체 자막 (타임스탬프 포함)

**[00:01]** So, I want to start off by kind of

**[00:03]** talking about some of the things that

**[00:05]** Charles mentioned earlier about how

**[00:06]** humans tend to forget and how Gabriel

**[00:09]** emphasized as well that up to 97% within

**[00:11]** 3 days. When it comes to caring for

**[00:13]** someone with memory loss, that means

**[00:15]** that you become their memory. Tracking

**[00:17]** medications, behaviors, doctor's

**[00:19]** appointments while exhausted and

**[00:20]** overwhelmed. Most AI can't help because

**[00:23]** it knows nothing about your loved one.

**[00:25]** Caregiver Copilot changes that. There's

**[00:27]** a new era of caregiving where people are

**[00:29]** already looking to chat GPT for

**[00:31]** information. But we have taken it to a

**[00:33]** new level by combining AI knowledge with

**[00:35]** personalized and private memory.

**[00:38]** Caregiver Co-opilot is an AI partner

**[00:39]** that remembers the entire journey. Every

**[00:41]** journal entry, every pattern, every

**[00:43]** detail, and it combines that personal

**[00:45]** history with deep knowledge of memory

**[00:47]** care. So today we're going to show you

**[00:49]** how we built it. My name is Chris Patel

**[00:51]** >> and I'm Danala

**[00:53]** >> and we're the found co-founding uh

**[00:54]** engineers behind Caregiver Co-Pilot and

**[00:57]** we're really excited to be here today.

**[00:58]** So let's just get right into it.

**[01:03]** So, taking a step back to where it all

**[01:05]** began, about a month ago, we went to

**[01:08]** Members's Memories that last AI agents

**[01:10]** hackathon and we came up with memory

**[01:13]** care, an AI companion that remembers

**[01:15]** everything for dementia patients from

**[01:17]** tracking their medications and routines

**[01:19]** to their life stories. And it was also

**[01:21]** someone that they could talk to that has

**[01:23]** the information that they might have

**[01:24]** forgotten. We won first place at the

**[01:26]** hackathon, but once we sat down and

**[01:28]** talked to real families such as Franks,

**[01:30]** we found that the best way we can help

**[01:32]** dementia patients is by helping their

**[01:34]** caregivers thrive at their jobs. So,

**[01:36]** Caregiver Copilot was born. Now, if you

**[01:39]** look at the slide behind me, every

**[01:41]** number on the slide tells the same

**[01:42]** story. Caregiving is overwhelming with

**[01:45]** over 55 million people worldwide living

**[01:47]** with dementia. And that number is

**[01:49]** projected to triple within the next 25

**[01:51]** years. 70% of these dementia patients or

**[01:53]** as they refer to as loved ones are cared

**[01:56]** for at home by their family members. Yet

**[01:58]** up to 75% of caregivers report

**[02:01]** experiencing depression at some point

**[02:02]** during their journey. This could be due

**[02:05]** to the fact that oftent times in the

**[02:06]** later stages it becomes a 247

**[02:08]** roundthe-clock job.

**[02:12]** So we are looking at billion dollar per

**[02:14]** industry in only US because there are

**[02:17]** around 8 million home caregivers and if

**[02:19]** we are able to around 25% of them which

**[02:22]** is around 2 million we can estimate per

**[02:25]** caregiver around $480 which going to

**[02:28]** generate our total of $840 million and

**[02:31]** it is just like 25%. We are looking at

**[02:34]** bigger picture now.

**[02:37]** So when we talk about dementia, we often

**[02:39]** focus on the patient. But for

**[02:40]** caregivers, the journey is just as

**[02:42]** intense. Across the seven stages of

**[02:44]** dementia, everything changes from

**[02:46]** memory, mobility, behavior to even the

**[02:48]** caregivers's role. So we implemented the

**[02:51]** evidencebacked six pillars of mental

**[02:52]** health, which are sleep, nutrition,

**[02:55]** physical exercise, mental exercise,

**[02:57]** social interaction, and medical care.

**[03:00]** Each of these pillars can provide

**[03:02]** valuable information regarding a loved

**[03:03]** one's health and their condition. By the

**[03:06]** late stages, caregiving becomes a

**[03:08]** full-time 247 supervision, physical

**[03:11]** assistance, and constant vigilance. It's

**[03:13]** continuous adaptation, and caregiver

**[03:15]** co-pilot is going to be there for every

**[03:17]** stage, learning, remembering, and

**[03:19]** guiding so that the caregiver never

**[03:20]** feels alone.

**[03:23]** So with care co-pilot, our primary

**[03:25]** target audience is a loved one. We are

**[03:27]** providing them help by helping that

**[03:29]** caregivers to reduce their stress and

**[03:31]** providing them with the right guidance.

**[03:33]** And we are also providing meaningful

**[03:34]** insight for the families and doctor as

**[03:36]** well which can make their doctors visit

**[03:38]** enriched and impactful.

**[03:43]** So let's talk about some of our key

**[03:45]** features. First off, we have a

**[03:47]** comprehensive framework that facilitates

**[03:48]** smooth onboarding for both new

**[03:50]** caregivers as well as substitute

**[03:51]** caregivers. We also have organized care

**[03:54]** management that coordinates all the

**[03:56]** doctors, insuranceances and basic care

**[03:58]** needs so that there's nothing that we

**[04:00]** don't oversight everything anything. We

**[04:02]** provide effective communication about

**[04:04]** the loved one, not only to the

**[04:05]** caregiver, but also to their family

**[04:07]** members and the doctors, fostering a

**[04:09]** cohesive care team. Our AI chatbot has

**[04:12]** access to both private history as well

**[04:14]** as public knowledge, addressing common

**[04:16]** caregiver questions, sharing insights,

**[04:18]** resources, burnout prevention tips once

**[04:21]** again to ensure that caregivers are

**[04:22]** never alone.

**[04:25]** Let me walk through care technical

**[04:27]** overview. As you see in the left, we are

**[04:30]** using stream as a web app which connects

**[04:33]** with a back end which is using API calls

**[04:35]** and course as a security measurement and

**[04:38]** JD authentication for password

**[04:40]** authentication and all. So our back end

**[04:42]** we are using LLM client which is J GBD

**[04:45]** for now and M machine client as well as

**[04:47]** scheduleuler foruling daily appointments

**[04:49]** and medications and me machine client is

**[04:53]** now running on main machine environment

**[04:55]** which is basically post SQL and neoforj

**[04:59]** and our system is running on postgra for

**[05:01]** now

**[05:05]** so we integrating machine and open so me

**[05:07]** machine help us to ve with vector metics

**[05:10]** for cementing search and it help us to

**[05:13]** keep persistent context across the

**[05:15]** conversation and it also provide us with

**[05:17]** a automatic consolidation memory and for

**[05:21]** opening as we're using GB4 for natural

**[05:23]** language understanding and we designed

**[05:25]** some custom fonts for higher context and

**[05:28]** we also implement a function calling for

**[05:30]** tool integration and our chatbot has

**[05:32]** control over commercial control over all

**[05:35]** our features

**[05:37]** >> and then uh moving on to our core

**[05:39]** entities we're going to start with the

**[05:41]** daily journal which is a powerful

**[05:43]** caregiving tool built upon the

**[05:44]** foundational six pillars of health which

**[05:46]** are once again sleep, nutrition, mental

**[05:49]** exercise, physical exercise, social

**[05:50]** interaction and medical care. Every

**[05:52]** single day, the caregiver can log in and

**[05:54]** fill out a quick validated evaluation

**[05:56]** framework in within five minutes where

**[05:58]** they can check off boxes for any

**[05:59]** activities that the loved one

**[06:00]** participated in as well as provide

**[06:02]** ratings for each of the pillars and free

**[06:04]** form notes incorporate any specific

**[06:06]** details or observations for a clear,

**[06:09]** richer understanding of daily

**[06:10]** experiences. Our AI identifies patterns

**[06:13]** over time, offering crucial insights

**[06:15]** from the daily entries and providing

**[06:17]** deeper datadriven analysis.

**[06:20]** Now this is our user friendly dashboard

**[06:22]** which is kind of like the heart of our

**[06:24]** system which can be accessed by the

**[06:25]** caregiver but it can also be accessed by

**[06:28]** the family members and doctors. This is

**[06:30]** the top half. Um for the first time ever

**[06:32]** family members and doctors can peer into

**[06:34]** their loved ones progression and their

**[06:36]** history regarding all six pillars of

**[06:38]** health. On the right hand side we have a

**[06:40]** medications tab where you can see the

**[06:41]** upcoming medication schedule with any

**[06:43]** doses, timings and instructions. On the

**[06:46]** lefth hand side, we have the upcoming

**[06:47]** appointments as well as overdue

**[06:48]** appointments with again descriptions,

**[06:51]** locations, dates, and times. But if you

**[06:53]** scroll down to the bottom half of our

**[06:55]** dashboard here, the user can select uh

**[06:59]** time frame anywhere from the last couple

**[07:01]** of days to even the last 90 days, and

**[07:03]** they'll see an interactive graph

**[07:05]** showcasing the six pillars of health and

**[07:07]** the daily journal entries. This type of

**[07:09]** information can be vital to families in

**[07:11]** order to visualize the progression of a

**[07:12]** loved one's health. And in this new era

**[07:15]** of AI, it's available at the click of a

**[07:16]** button.

**[07:20]** >> This is a medication page designed for

**[07:21]** caregivers. So they can add medication

**[07:23]** for their loved ones. They can also

**[07:25]** limit dosages, frequencies and the time

**[07:28]** which uh user has to take medicines. And

**[07:32]** this is a m medication page where

**[07:34]** designed for caregivers as well as

**[07:36]** doctors. So they can deactivate or

**[07:38]** delete a medication and important most

**[07:40]** importantly they can have access for

**[07:42]** full medication history.

**[07:45]** >> And then we have the calendar and

**[07:47]** appointment page which is essential for

**[07:48]** effective schedule management.

**[07:50]** Caregivers can easily mark appointments

**[07:52]** using the add event feature allowing

**[07:54]** direct scheduling for loved ones. The

**[07:56]** view calendar page provides a seamless

**[07:58]** overview of all the events designed for

**[07:59]** simplicity but you still have it on the

**[08:01]** dashboard as well. And then right here,

**[08:03]** the manage appointments tab allows a

**[08:05]** user to not not only view upcoming

**[08:07]** appointments as well as past

**[08:08]** appointments, but the cool thing is the

**[08:10]** caregiver can also come in during or

**[08:12]** after an appointment. They can write in

**[08:13]** any doctor's notes, any observations to

**[08:16]** keep in mind for the next time.

**[08:23]** This is a report designed for doctors,

**[08:25]** caregiver and family members. It

**[08:28]** provides with uh such a datadriven

**[08:30]** report from previous day or selected

**[08:31]** dates with insights such as medication

**[08:34]** arhance daily journal as well as check

**[08:36]** converation which career did about the

**[08:39]** loved ones. It presents the rating and

**[08:41]** summaries as well as feedback for the

**[08:43]** loved ones and routine in order to

**[08:46]** enhance their health pillars. Example,

**[08:49]** if lover has not gotten enough good

**[08:52]** sleep in past few days, it can give some

**[08:54]** recommendations like a user should like

**[08:58]** avoid using a reduced screen time before

**[09:00]** going to bed or do some medication

**[09:02]** before going to bed.

**[09:05]** >> Um and then now finally let's talk about

**[09:08]** our caregiver co-pilot AI assistant.

**[09:10]** This is kind of like the brain of our

**[09:12]** system. Um here we have combined two

**[09:14]** very powerful things. The first is the

**[09:16]** vast public knowledge of AI which

**[09:18]** includes evidence-based guidance. It

**[09:20]** includes medical research and simply

**[09:22]** just caregiving best practices. Second

**[09:25]** is the private personal history of for a

**[09:27]** loved one including their daily journal

**[09:28]** entries, their medication logs,

**[09:30]** appointment notes, and basically any

**[09:32]** conversation had with the chatbot as

**[09:34]** well. It identifies real patterns over

**[09:36]** time

**[09:37]** which the caregiver can utilize to

**[09:39]** produce detailed responses such as this

**[09:41]** one. Our chatbot highlights any trends

**[09:44]** in any of the six pillars for the loved

**[09:45]** one and then provides meaningful

**[09:47]** guidance. And honestly, there's no limit

**[09:49]** to where you can ask it. For example, if

**[09:51]** you look at the conversation on screen,

**[09:53]** um the caregiver asks, "How has Trisha's

**[09:55]** sleep been this past week?" And the

**[09:57]** caregiver co-pilot responds with a

**[09:59]** complete overview of Trisha's sleep for

**[10:01]** the last week along with the notes and

**[10:03]** ratings. And then it provides guidance

**[10:05]** as well as potentially beneficial

**[10:07]** strategies to improve the score for the

**[10:08]** upcoming week.

**[10:10]** Um, and this is just based off of one

**[10:12]** week's input, but as we keep adding

**[10:15]** data, as we keep filling out journal

**[10:17]** entries, and keep having conversations,

**[10:18]** the chat will grow with all the data

**[10:19]** that it gets. So, as kind of Frank

**[10:22]** mentioned earlier, hours of combing

**[10:24]** through Reddit posts, Facebook groups,

**[10:26]** online articles, looking for your very

**[10:28]** specific issue is now simplified with

**[10:30]** all the data in one place along with the

**[10:32]** loved one's private personal history for

**[10:35]** real time personalized educated

**[10:37]** responses.

**[10:39]** If you sum it all up, combining LLM

**[10:41]** knowledge with personalized and private

**[10:43]** memory is going to open the door to a

**[10:44]** new era of caregiving. As I mentioned

**[10:47]** earlier, people have already began to

**[10:48]** look to Chat GBT for information. But

**[10:51]** now, the addition of private memory is

**[10:52]** going to take it to a whole new level.

**[10:54]** If any of you know a caregiver or have a

**[10:57]** loved one with dementia and believe that

**[10:59]** Caregiver Copilot could be a useful tool

**[11:01]** to assist them, please scan our QR code.

**[11:03]** It's on the screen. It's also on the

**[11:04]** banner over there. we'd love to get in

**[11:06]** touch and get them set up as a beta

**[11:08]** user. Um, thank you guys so much for

**[11:10]** listening and thank you to the AI memory

**[11:12]** forum for giving us this opportunity. We

**[11:14]** hope you guys enjoyed and please feel

**[11:16]** free to ask any questions.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
