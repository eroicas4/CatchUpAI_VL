#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Transcript to Markdown Generator
YouTube 자막을 구조화된 마크다운 문서로 변환합니다.

필요 라이브러리:
- youtube-transcript-api
- anthropic
"""

import sys
import io
import os
import re
from datetime import datetime

# Windows 콘솔 UTF-8 인코딩 설정
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """YouTube URL에서 video ID 추출"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]+)',
        r'(?:youtube\.com\/live\/)([a-zA-Z0-9_-]+)',
        r'(?:youtu\.be\/)([a-zA-Z0-9_-]+)',
        r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return url


def get_transcript(video_id, languages=['en']):
    """YouTube 영상의 자막 추출"""
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        try:
            transcript = transcript_list.find_transcript(languages)
        except:
            print("[!] 요청한 언어를 찾을 수 없습니다. 첫 번째 사용 가능한 자막을 사용합니다.")
            transcript = next(iter(transcript_list))

        fetched = transcript.fetch()
        return fetched

    except Exception as e:
        print(f"[X] 자막 추출 실패: {e}")
        return None


def format_timestamp(seconds):
    """초를 HH:MM:SS 형식으로 변환"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def clean_subtitle_text(text):
    """
    자막 텍스트 정제 (말더듬, 이상 문자, 띄어쓰기 오류 수정)

    Args:
        text: 정제할 텍스트

    Returns:
        str: 정제된 텍스트
    """
    if not text:
        return text

    result = text

    # 1. 이상 문자 제거 (태국어 등 비한글/영문/숫자/기본 기호)
    # 한글, 영문, 숫자, 기본 구두점만 유지
    result = re.sub(r'[^\w\s가-힣a-zA-Z0-9.,!?:;\-\'\"()\[\]@#$%&*+=/<>~`]', '', result)

    # 2. 말더듬/반복 단어 제거 ("레 레퍼지토리" → "레퍼지토리")
    # 연속 반복 패턴
    result = re.sub(r'\b(\w+)\s+\1\b', r'\1', result)  # "레 레" → "레"
    result = re.sub(r'\b([\w가-힣]+)\s+\1([\w가-힣]*)', r'\1\2', result)  # "레 레퍼지토리" → "레퍼지토리"
    # 같은 단어 반복 패턴 (레퍼지토리에서 레퍼지토리를 → 레퍼지토리를)
    result = re.sub(r'([\w가-힣]+)(에서|에|를|을|이|가|은|는|의|와|과|로)\s+\1(를|을|이|가|은|는)', r'\1\3', result)

    # 3. 필러 단어 제거
    # "어" 필러 (문장 중간의 불필요한 "어")
    result = re.sub(r'\s+어\s+', ' ', result)  # " 어 " → " "
    result = re.sub(r'^어\s+', '', result)  # 문장 시작 "어 " 제거
    # "그런" 반복 제거
    result = re.sub(r'그런\s+그런', '그런', result)
    # 구어체 지시어 제거
    result = re.sub(r'\s+요거\s+', ' ', result)  # " 요거 " → " "
    result = re.sub(r'\s+이거\s+', ' ', result)  # " 이거 " → " "
    result = re.sub(r'\s+뭐\s+', ' ', result)  # " 뭐 " → " "

    # 4. 띄어쓰기 오류 수정
    # "있는이" → "있는 이", "하는이" → "하는 이" 등
    spacing_patterns = [
        (r'있는이', '있는 이'),
        (r'하는이', '하는 이'),
        (r'되는이', '되는 이'),
        (r'라는이', '라는 이'),
        (r'에서이', '에서 이'),
        (r'으로이', '으로 이'),
        (r'것은이', '것은 이'),
        (r'근데이', '근데 이'),
        (r'그런데이', '그런데 이'),
        (r'인데이', '인데 이'),
        (r'관련된이', '관련된 이'),
        (r'만든이', '만든 이'),
        (r'된이', '된 이'),
        (r'하면서이', '하면서 이'),
        (r'진행하면서이', '진행하면서 이'),
        (r'하면이', '하면 이'),
        (r'되면이', '되면 이'),
        (r'으면이', '으면 이'),
    ]
    for pattern, replacement in spacing_patterns:
        result = result.replace(pattern, replacement)

    # 중복 조사/어미 제거
    result = re.sub(r'으로\s+으로', '으로', result)  # "으로 으로" → "으로"
    result = re.sub(r'을\s+을', '을', result)  # "을 을" → "을"
    result = re.sub(r'를\s+를', '를', result)  # "를 를" → "를"
    result = re.sub(r'이\s+이', '이', result)  # "이 이" → "이"
    result = re.sub(r'가\s+가', '가', result)  # "가 가" → "가"

    # 4. 문법 오류 수정 ("~를 예정" → "~ 예정")
    result = re.sub(r'를\s*예정', ' 예정', result)
    result = re.sub(r'을\s*예정', ' 예정', result)

    # 5. 다중 공백 정리
    result = re.sub(r'\s+', ' ', result)

    return result.strip()


def convert_to_noun_ending(sentence):
    """
    문장을 명사/동명사 종결 형태로 변환
    예: "영상을 편집했습니다" → "영상 편집"
        "API를 연동하고 있습니다" → "API 연동"
        "테스트를 진행합니다" → "테스트 진행"

    Args:
        sentence: 변환할 문장

    Returns:
        str: 명사형 종결 문장
    """
    if not sentence:
        return sentence

    result = sentence.strip()

    # 1. 구어체/서술형 종결어미를 명사형으로 변환
    verb_to_noun_patterns = [
        # "~했습니다/합니다" → 제거
        (r'했습니다\.?$', ''), (r'합니다\.?$', ''), (r'됩니다\.?$', ''),
        (r'하였습니다\.?$', ''), (r'되었습니다\.?$', ''),
        (r'입니다\.?$', ''), (r'습니다\.?$', ''),
        # "~하고 있습니다" → 제거
        (r'하고\s*있습니다\.?$', ''), (r'되고\s*있습니다\.?$', ''),
        # "~를/을 했습니다" → "~"
        (r'를\s*했습니다\.?$', ''), (r'을\s*했습니다\.?$', ''),
        (r'를\s*합니다\.?$', ''), (r'을\s*합니다\.?$', ''),
        # "~하는 것" → "~"
        (r'하는\s*것$', ''), (r'되는\s*것$', ''),
        # "~예정입니다" → "~ 예정"
        (r'예정입니다\.?$', '예정'),
        # "~완료" 유지
        (r'완료했습니다\.?$', '완료'), (r'완료됐습니다\.?$', '완료'),
    ]

    for pattern, replacement in verb_to_noun_patterns:
        if re.search(pattern, result):
            result = re.sub(pattern, replacement, result)
            break

    # 2. 동사를 명사형(~함, ~됨)으로 변환
    verb_nominalization = [
        # "~했다/한다" → "~함"
        (r'했다\.?$', '함'), (r'한다\.?$', '함'), (r'했어요\.?$', '함'),
        (r'했음\.?$', '함'), (r'함\.?$', '함'),
        # "~됐다/된다" → "~됨"
        (r'됐다\.?$', '됨'), (r'된다\.?$', '됨'), (r'됐어요\.?$', '됨'),
        # "~하여/해서" → "~"
        (r'하여$', ''), (r'해서$', ''),
        # "~하기" 유지
        (r'하기$', '하기'), (r'되기$', '되기'),
        # "~만들었" → "생성"
        (r'만들었$', '생성'), (r'만들$', '생성'),
        # "~였/이었" → 제거
        (r'였$', ''), (r'이었$', ''),
        # "~받아서" → "다운로드"
        (r'다운받아서$', '다운로드'), (r'받아서$', ''),
        # "~하고" → 제거
        (r'하고$', ''), (r'되고$', ''),
    ]

    for pattern, replacement in verb_nominalization:
        if re.search(pattern, result):
            result = re.sub(pattern, replacement, result)
            break

    # 3. 조사 제거 (종결에 조사가 남은 경우)
    result = re.sub(r'[을를이가은는에의와과로]$', '', result)

    # 추가: 불완전 어미 제거
    result = re.sub(r'았$|었$|였$', '', result)

    # 4. 공백 정리
    result = re.sub(r'\s+', ' ', result).strip()

    # 5. 명사형 종결 보정 (동사 어미가 남은 경우)
    # "~하는", "~되는" 등으로 끝나면 명사 추가
    if re.search(r'하는$|되는$|되는$|있는$', result):
        result = result + " 작업"
    elif re.search(r'위한$|대한$', result):
        result = result + " 내용"

    # 6. 너무 짧으면 원본 반환
    if len(result) < 5:
        return sentence.strip()

    return result


def is_valid_bullet(sentence):
    """
    불릿으로 사용 가능한 문장인지 확인 (is_meaningless_sentence보다 완화된 기준)

    Args:
        sentence: 확인할 문장

    Returns:
        bool: 유효하면 True
    """
    if not sentence or len(sentence.strip()) < 8:
        return False

    # 명확히 제외할 패턴 (시작)
    invalid_start_patterns = [
        r'^[서어아이고는을를에]?\s',  # 조사/어미로 시작
        r'^수\s*있',  # "수 있습니다" 잔해
        r'^니다|^습니다',  # 어미 잔해
        r'^[.,;:!?]',  # 구두점으로 시작
        r'^>+',  # >> 기호
        r'^\d+\s*$',  # 숫자만
        r'^뭔가\s',  # "뭔가"로 시작
        r'^예\s+요',  # "예 요거"
        r'^그래서\s',  # "그래서"로 시작
        r'^그런데\s',  # "그런데"로 시작
        r'^근데\s',  # "근데"로 시작
        r'^저는\s',  # "저는"으로 시작
        r'^제가\s',  # "제가"으로 시작
    ]

    # 불완전한 종결 패턴 (종결)
    invalid_end_patterns = [
        r'었$|였$',  # "만들었", "했었" 등 불완전
        r'았$|았$',  # "갔았" 등 불완전
        r'는$|은$|을$|를$|이$|가$',  # 조사로 끝남
        r'에$|의$|와$|과$',  # 조사로 끝남
        r'고$|서$|면$',  # 연결어미로 끝남
        r'요$',  # 구어체
        r'죠$',  # 구어체
        r'까요$',  # 의문형
        r'볼까요$',  # 의문형
    ]

    for pattern in invalid_start_patterns:
        if re.search(pattern, sentence):
            return False

    for pattern in invalid_end_patterns:
        if re.search(pattern, sentence):
            return False

    # 포함되면 안 되는 패턴
    if '모르겠' in sentence or '어쩌고' in sentence:
        return False

    # 명사/동명사형 종결 확인 (긍정 패턴)
    valid_end_patterns = [
        r'작업$', r'진행$', r'완료$', r'예정$', r'처리$',
        r'설정$', r'구성$', r'분석$', r'테스트$', r'실습$',
        r'학습$', r'정리$', r'소개$', r'설명$', r'활용$',
        r'연동$', r'개발$', r'생성$', r'수정$', r'삭제$',
        r'확인$', r'검토$', r'비교$', r'적용$', r'배포$',
        r'업데이트$', r'다운로드$', r'업로드$',
        r'함$', r'됨$', r'임$',  # 명사형 어미
        r'기$',  # ~하기
        r'것$',  # ~하는 것
        r'내용$', r'방법$', r'과정$', r'결과$',
    ]

    for pattern in valid_end_patterns:
        if re.search(pattern, sentence):
            return True

    # 위 패턴에 해당하지 않으면 False (엄격한 명사형 체크)
    return False


def create_timeline(transcript):
    """타임라인 생성 (5분 간격으로 요약, 이상 문자 정제)"""
    timeline = []
    interval = 300  # 5분 = 300초

    current_time = 0
    current_texts = []

    for entry in transcript:
        if entry.start >= current_time + interval:
            if current_texts:
                # 현재 구간 요약 (텍스트 정제 적용)
                timestamp = format_timestamp(current_time)
                combined_text = ' '.join(current_texts[:50])
                cleaned_text = clean_subtitle_text(combined_text)
                timeline.append(f"- **{timestamp}**: {cleaned_text}...")
                current_texts = []
            current_time += interval

        # 개별 텍스트도 정제하여 추가
        cleaned_entry = clean_subtitle_text(entry.text.strip())
        if cleaned_entry:  # 빈 문자열이 아닌 경우만 추가
            current_texts.append(cleaned_entry)

    # 마지막 구간
    if current_texts:
        timestamp = format_timestamp(current_time)
        combined_text = ' '.join(current_texts[:50])
        cleaned_text = clean_subtitle_text(combined_text)
        timeline.append(f"- **{timestamp}**: {cleaned_text}...")

    return "\n".join(timeline)


def extract_keywords(text, top_n=5):
    """
    텍스트에서 핵심 키워드 추출 (빈도 기반)

    Args:
        text: 분석할 텍스트
        top_n: 추출할 키워드 수

    Returns:
        list: 상위 키워드 리스트
    """
    # 불용어 (인사말, 감탄사, 조사, 일반적인 말)
    stopwords = {
        # 인사말/감탄사
        '안녕하세요', '안녕', '예', '네', '아', '어', '음', '뭐', '그',
        '아아', '에', '오', '와', '야', '으', '이', '저', '좀', '잠깐',
        '그래서', '그러면', '그리고', '그런데', '근데', '하지만', '그냥',
        '지금', '오늘', '여기', '거기', '이거', '저거', '그거', '뭔가',
        '이렇게', '그렇게', '저렇게', '어떻게', '왜', '언제', '어디',
        '있습니다', '합니다', '됩니다', '입니다', '했습니다', '있어요',
        '해요', '되요', '거예요', '건데요', '거든요', '같아요', '있고',
        '하고', '되고', '있는', '하는', '되는', '같은', '이런', '저런',
        '그런', '많이', '조금', '아주', '정말', '너무', '굉장히', '매우',
        '것', '수', '거', '등', '중', '때', '분', '님', '시', '일', '월',
        # 영어/기호
        'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
        'to', 'of', 'and', 'in', 'that', 'have', 'for', 'it', 'with',
        # 기타 일반어
        '사람', '경우', '부분', '정도', '다음', '처음', '마지막', '계속',
        # 조사가 붙은 단어들
        '제가', '저는', '저도', '저를', '내가', '나는', '나도', '나를',
        '그것을', '이것을', '저것을', '그걸', '이걸', '저걸',
        '것을', '수가', '수를', '거를', '걸', '데를',
        '여기서', '거기서', '저기서', '어디서', '여기에', '거기에',
        # 동사 어미
        '겁니다', '됩니다', '합니다', '입니다', '봅니다', '갑니다',
        '할게요', '볼게요', '갈게요', '줄게요', '드릴게요',
        '했어요', '됐어요', '봤어요', '갔어요', '왔어요',
        '하겠습니다', '되겠습니다', '보겠습니다', '드리겠습니다',
        '시킬', '만들', '가지고', '통해서', '대해서', '위해서',
        # 추가 일반 동사/부사
        '있어서', '없어서', '돼서', '해서', '봐서', '가서', '와서',
        '있으면', '없으면', '되면', '하면', '보면', '가면', '오면',
        '있었어요', '없었어요', '됐었어요', '했었어요',
        '하려고', '보려고', '가려고', '오려고', '만들려고',
        '한번', '두번', '세번', '먼저', '나중에', '다시', '또',
        '아까', '방금', '조금', '잠깐', '금방', '바로', '곧',
        # 대명사/지시어
        '얘가', '얘를', '얘는', '얘도', '걔가', '걔를', '걔는',
        '요거', '요것', '요게', '요건', '요걸', '저거', '저것',
        '오케이', '아네', '네네', '아아', '음음',
        # 추가 일반 동사/형용사/부사
        '만든', '만들', '만들어', '만들고', '만들면', '만드는',
        '다른', '같은', '요런', '이런', '저런', '그런', '어떤',
        '좋은', '나쁜', '작은', '큰', '새로운', '오래된',
        '주는', '받는', '보는', '하는', '되는', '가는', '오는',
        '해야', '봐야', '가야', '와야', '알아야',
        '시작', '끝', '올드', '뉴', '버전',
        '그럼', '근데', '그래', '그냥', '아마', '혹시', '과연',
        '주에', '달에', '년에', '번에', '개에', '명에',
        '하는데', '되는데', '있는데', '없는데', '보는데',
        '빠른', '느린', '좋은지', '나쁜지', '있는지', '없는지',
        '요렇게', '이렇게', '저렇게', '그렇게', '어떻게',
        '기터', '기타', '페이지', '화면', '파일',
        # 추가 지시어/어미
        '이제', '있죠', '이게', '있고', '되고', '하고',
        '있어', '없어', '해서', '돼서', '봐서',
        '거고', '건데', '되죠', '하죠', '보죠', '가죠',
        '거야', '건가', '인가', '일까', '할까', '볼까',
        '보고', '가고', '오고', '나고', '되고',
        '봤고', '갔고', '왔고', '났고', '됐고',
        # 영어 일반 단어
        'or', 'but', 'so', 'if', 'when', 'how', 'what', 'why',
        'this', 'these', 'those', 'here', 'there',
        # 추가 불용어 (의미 없는 동사/조사)
        '되어', '하여', '되면', '하면', '보면',
        '일을', '것은', '것이', '것을', '것도',
        '보시면', '하시면', '되시면', '가시면',
        '같이', '때문에', '위해', '통해', '따라',
        '사용할', '만들', '보실', '하실', '되실',
        '라고', '다고', '으로', '에서', '부터',
        '싶은', '있는', '없는', '되는', '하는',
        '했던', '됐던', '봤던', '갔던', '왔던',
        # 추가 일반 동사/표현
        '사용해서', '만들어서', '해서', '가지고', '보시면',
        '거기서', '여기서', '저기서', '이용해서', '통해서',
        '경우에는', '것처럼', '것이고', '것이다', '작업을',
        # 동사 연결형
        '공부하고', '작업하고', '진행하고', '시작하고', '완료하고',
        '테스트', '다운받아서', '가져와서', '업데이트',
        # 의미없는 일반어
        '현재', '일단', '여러', '같습니다', '요렇고', '요런', '이런',
        '그런', '있는', '혹시', '어떤', '약간', '실제', '요거',
        '이쪽', '저쪽', '그쪽', '거의', '아마', '요기', '저기',
        # 구어체/불완전 어휘
        '뭐가', '달라고', '돼요', '있도록', '될까요', '뭘까요',
        '그럼요', '그래요', '해야죠', '봐야죠', '알겠죠', '있죠',
        '영어', '한글', '한국어', '영문',
        '쉽게', '얘한테', '걔한테', '비교', '얘가', '걔가',
        '다르게', '똑같이', '마찬가지', '별로', '전혀',
        '같은데', '했고', '일로', '거로', '식으로', '대로',
        '보면서', '하면서', '되면서', '가면서', '오면서',
        '말이', '메일링', '커런트', '세션', '버전', '폴더',
        '파일', '디렉토리', '패스', '경로',
    }

    # 불용어 패턴 (어미로 끝나는 단어)
    stopword_endings = ['을', '를', '이', '가', '은', '는', '에', '로', '으로',
                        '에서', '까지', '부터', '만', '도', '요', '죠', '네요']

    # 단어 추출 (2글자 이상, 한글/영문)
    words = re.findall(r'[가-힣a-zA-Z]{2,}', text)

    # 빈도 계산 (불용어 제외)
    word_count = {}
    for word in words:
        word_lower = word.lower()
        # 불용어 체크
        if word in stopwords or word_lower in stopwords:
            continue
        # 불용어 어미 체크 (3글자 이상 단어에서 조사로 끝나는 경우)
        if len(word) >= 3:
            skip = False
            for ending in stopword_endings:
                if word.endswith(ending) and len(word) > len(ending) + 1:
                    skip = True
                    break
            if skip:
                continue
        word_count[word] = word_count.get(word, 0) + 1

    # 상위 N개 추출
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_words[:top_n]]


def is_meaningless_sentence(sentence):
    """
    의미없는 문장인지 확인

    Args:
        sentence: 확인할 문장

    Returns:
        bool: 의미없으면 True
    """
    if not sentence:
        return True

    # 의미없는 문장 패턴
    meaningless_patterns = [
        r'^뭔가\s*(잘\s*)?모르겠',  # "뭔가 잘 모르겠어요"
        r'^잘\s*모르겠',
        r'^예\s*요거',  # "예 요거"
        r'^요거\s*$',
        r'^그렇\s*$',  # "그렇"으로만 끝남
        r'모르겠어요\s*$',
        r'^어\s+',  # "어"로 시작
        r'^음\s+',  # "음"으로 시작
        r'^아\s+[^니]',  # "아"로 시작 (but "아니" 제외)
        r'^\s*예\s*$',  # "예"만
        r'^\s*네\s*$',  # "네"만
        r'어쩌고저쩌고',  # 불명확한 표현
        r'뭐\s*이런\s*거',
        r'요런\s*식으로\s*$',
        # === 문장형 불릿 패턴 (구어체 시작) ===
        r'^그래서\s+',  # "그래서"로 시작
        r'^그러면\s+',  # "그러면"으로 시작
        r'^그리고\s+',  # "그리고"로 시작
        r'^그런데\s+',  # "그런데"로 시작
        r'^근데\s+',  # "근데"로 시작
        r'^저는\s+',  # "저는"으로 시작
        r'^제가\s+',  # "제가"로 시작
        r'^지금\s+',  # "지금"으로 시작 (단독)
        r'^여기\s+',  # "여기"로 시작 (단독)
        r'^이거\s+',  # "이거"로 시작
        r'^요거\s+',  # "요거"로 시작
        r'^일단\s+',  # "일단"으로 시작
        r'^방금\s+',  # "방금"으로 시작
        r'^그럼\s+',  # "그럼"으로 시작
        r'^그다음에\s+',  # "그다음에"로 시작
        r'^예,?\s+',  # "예," "예 "로 시작
        r'^이\s+템플릿',  # "이 템플릿"으로 시작
        r'^현재\s+템플릿',  # "현재 템플릿"으로 시작
        r'요렇게',  # "요렇게" 포함
        r'요렇고',  # "요렇고" 포함
        r'요거부터',  # "요거부터" 포함
        r'볼까요\s*$',  # "~볼까요"로 끝남
        r'그런.{1,50}그런',  # "그런...그런" 반복 패턴 (50자까지)
        # === 구어체 종결어미 ===
        r'거든요\s*$',  # "~거든요"로 끝남
        r'잖아요\s*$',  # "~잖아요"로 끝남
        r'같아요\s*$',  # "~같아요"로 끝남
        r'있어요\s*$',  # "~있어요"로 끝남
        r'했고요\s*$',  # "~했고요"로 끝남
        r'됐고요\s*$',  # "~됐고요"로 끝남
        r'있는데요\s*$',  # "~있는데요"로 끝남
        r'했는데요\s*$',  # "~했는데요"로 끝남
        r'있고요\s*$',  # "~있고요"로 끝남
        r'하고요\s*$',  # "~하고요"로 끝남
        r'드렸고요\s*$',  # "~드렸고요"로 끝남
        r'했어요\s*$',  # "~했어요"로 끝남
        r'봤어요\s*$',  # "~봤어요"로 끝남
        r'^어제는?\s+',  # "어제는", "어제"로 시작
        r'^오늘은?\s+',  # "오늘은", "오늘"로 시작
        r'^그게\s+',  # "그게"로 시작
        r'^하여튼\s+',  # "하여튼"으로 시작
        r'^아무튼\s+',  # "아무튼"으로 시작
        r'^어쨌든\s+',  # "어쨌든"으로 시작
        r'했죠\s*$',  # "~했죠"로 끝남
        r'됐죠\s*$',  # "~됐죠"로 끝남
        r'했는데$',  # "~했는데"로 끝남
        r'이고요\s*$',  # "~이고요"로 끝남
        r'라고\s+(하면|했)',  # "~라고 하면/했" 포함 (인용구)
        r'싶어요라고',  # "~싶어요라고" 포함
        r'중이라고',  # "~중이라고" 포함
        r'^그냥\s+',  # "그냥"으로 시작
        r'좋죠\s*$',  # "~좋죠"로 끝남
        r'되죠\s*$',  # "~되죠"로 끝남
        r'싶어\s*$',  # "~싶어"로 끝남 (불완전)
        r'할\s*거\s*$',  # "~할 거"로 끝남 (불완전)
        r'된\s*거\s*$',  # "~된 거"로 끝남 (불완전)
        r'드릴게요\s*$',  # "~드릴게요"로 끝남 (구어체)
        r'할게요\s*$',  # "~할게요"로 끝남 (구어체)
        r'볼게요\s*$',  # "~볼게요"로 끝남 (구어체)
        r'^그이\s+',  # "그이"로 시작 (이상한 패턴)
        # === 문장 중간 구어체 패턴 ===
        r'지금요\s+',  # "지금요" 포함 (구어체)
        r'있는요\s+',  # "있는요" 포함 (구어체)
        r'하는요\s+',  # "하는요" 포함 (구어체)
        r'\s+그다음에\s+',  # 중간에 "그다음에" 포함
        r'\s+근데\s+',  # 중간에 "근데" 포함
        r'\s+그런데\s+',  # 중간에 "그런데" 포함
        # === 띄어쓰기 오류 패턴 (저품질 자막) ===
        r'하면이\s+',  # "하면이" (띄어쓰기 오류)
        r'으로\s+으로',  # "으로 으로" 중복
        r'을\s+을\s+',  # "을 을" 중복
        # === 불완전한 종결 패턴 ===
        r'진행\s*$',  # "~진행"으로만 끝남 (불완전)
        r'학습\s*$',  # "~학습"으로만 끝남 (불완전)
        r'작업\s*$',  # "~작업"으로만 끝남 (불완전 - "작업을 진행" 등)
        # === 반복 패턴 ===
        r'지금.{0,20}지금.{0,20}지금',  # "지금" 3번 이상 반복
        # === 추가 구어체/비격식 패턴 ===
        r'그걸로\s+',  # "그걸로" 포함 (구어체)
        r'이걸로\s+',  # "이걸로" 포함 (구어체)
        r'저걸로\s+',  # "저걸로" 포함 (구어체)
        r'것부터\s+',  # "것부터" 포함 (비격식)
        r'거부터\s+',  # "거부터" 포함 (비격식)
        r'걸로\s+',  # "걸로" 포함 (구어체 축약)
        r'아버러닝',  # 자막 오류 패턴
        r'시작\s*예정\s*$',  # "시작 예정"으로만 끝남 (불완전)
    ]

    for pattern in meaningless_patterns:
        if re.search(pattern, sentence, re.IGNORECASE):
            return True

    # 너무 짧은 문장 (5자 미만)
    if len(sentence.strip()) < 5:
        return True

    return False


def clean_text_for_summary(text):
    """
    요약용 텍스트 정제 (인사말, 감탄사 제거)

    Args:
        text: 정제할 텍스트

    Returns:
        str: 정제된 텍스트
    """
    # 문장 분리
    sentences = re.split(r'[.!?。]\s*', text)

    # 의미 있는 문장만 선택
    meaningful_sentences = []
    skip_patterns = [
        r'^[아어음예네오와야으이저좀]+\s*[,.]?\s*$',  # 감탄사만 있는 문장
        r'^안녕하세요',  # 인사말로 시작
        r'^감사합니다',  # 감사 인사
        r'^\s*$',  # 빈 문장
        r'^[음악]',  # [음악] 태그
        r'^\[',  # 대괄호로 시작 (태그)
    ]

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 10:  # 너무 짧은 문장 제외
            continue

        skip = False
        for pattern in skip_patterns:
            if re.match(pattern, sentence, re.IGNORECASE):
                skip = True
                break

        if not skip:
            meaningful_sentences.append(sentence)

    return '. '.join(meaningful_sentences[:5])  # 최대 5문장


def extract_key_sentences(text, keywords, max_sentences=3):
    """
    키워드가 포함된 핵심 문장 추출

    Args:
        text: 분석할 텍스트
        keywords: 키워드 리스트
        max_sentences: 최대 문장 수

    Returns:
        list: 핵심 문장 리스트
    """
    sentences = re.split(r'[.!?。]\s*', text)
    scored_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 15 or len(sentence) > 200:  # 적절한 길이만
            continue

        # 키워드 포함 점수
        score = sum(1 for kw in keywords if kw in sentence)
        if score > 0:
            scored_sentences.append((sentence, score))

    # 점수순 정렬 후 상위 N개
    scored_sentences.sort(key=lambda x: x[1], reverse=True)
    return [s[0] for s in scored_sentences[:max_sentences]]


def extract_topic_from_intro(intro_text, video_title=""):
    """
    도입부 텍스트에서 영상의 실제 주제 추출

    Args:
        intro_text: 도입부 자막 텍스트 (약 5-7분 분량)
        video_title: 영상 제목 (추가 힌트)

    Returns:
        dict: {
            'main_topic': 주요 주제,
            'sub_topics': 부가 주제 리스트,
            'broadcast_info': 방송 정보 (번호, 시리즈명 등),
            'presenter': 발표자/진행자 정보
        }
    """
    result = {
        'main_topic': None,
        'sub_topics': [],
        'broadcast_info': {},
        'presenter': None
    }

    # 1. 방송 정보 추출
    broadcast_patterns = [
        r'(\d+)\s*번째\s*(?:시간|방송|라이브)',
        r'(?:재미로\s*하는\s*)?(바이브\s*코딩|라이브\s*코딩)',
        r'총\s*(\d+)\s*회\s*목표',
    ]
    for pattern in broadcast_patterns:
        match = re.search(pattern, intro_text)
        if match:
            if '번째' in pattern:
                result['broadcast_info']['episode'] = match.group(1)
            elif '목표' in pattern:
                result['broadcast_info']['total_episodes'] = match.group(1)
            else:
                result['broadcast_info']['series_name'] = match.group(1)

    # 토픽 정제 함수
    def clean_topic(topic_text):
        """토픽 텍스트를 정제하여 핵심 키워드만 추출"""
        if not topic_text:
            return None

        topic = topic_text.strip()

        # 불완전한 문장 패턴 필터링 (조사/어미로 끝나는 것)
        bad_endings = ['게', '의', '를', '을', '에', '는', '은', '가', '이', '로', '와', '과', '인', '한', '된']
        if len(topic) > 0 and topic[-1] in bad_endings:
            return None

        # "~다." 형태의 완전한 문장은 주제가 아님
        if topic.endswith('다.') or topic.endswith('요.') or topic.endswith('니다.'):
            return None

        # 의미없는 단어 제거
        skip_words = ['어', '그', '이', '저', '뭐', '좀', '아', '음', '네', '예', '뭐', '거',
                      '것', '달에', '달의', '번째', '첫', '두', '주제인', '주제는', '주제가']
        words = topic.split()
        cleaned_words = [w for w in words if w not in skip_words]

        if not cleaned_words:
            return None

        # 핵심 키워드 추출 (마지막 2개 단어)
        if len(cleaned_words) > 2:
            topic = ' '.join(cleaned_words[-2:])
        else:
            topic = ' '.join(cleaned_words)

        # 최종 길이 제한 (20자)
        if len(topic) > 20:
            topic = topic[:20].rsplit(' ', 1)[0] if ' ' in topic[:20] else topic[:20]

        # 너무 짧으면 무효
        if len(topic) < 3:
            return None

        return topic

    # 중복 체크 함수 (유사 토픽 감지)
    def is_similar_topic(topic1, topic2):
        """두 토픽이 유사한지 확인 (정규화 후 비교)"""
        if not topic1 or not topic2:
            return False
        # 정규화: 공백 제거, 소문자, 's' 제거
        def normalize(t):
            t = t.lower().replace(' ', '').replace('스', '')
            return t.replace('skills', 'skill').replace('claude', '클라우드')
        return normalize(topic1) == normalize(topic2) or topic1 in topic2 or topic2 in topic1

    # 2. 주제 패턴 매칭 (직접 언급된 주제) - 더 구체적인 패턴 사용
    topic_patterns = [
        # "클라우드 스킬스에 대해" 패턴 (구체적 키워드)
        r'(클라우드\s*스킬[스즈]?|Claude\s*Skills?|MCP|AI4?\s*PKM|바이브\s*러닝)(?:에\s*대해|를\s*다루|를\s*공부)',
        # "영상 편집 스킬" 같은 구체적 스킬명 (수량사 제외)
        r'(영상\s*편집\s*스킬|무음\s*제거\s*스킬|자막\s*스킬)',
        # "바이브러닝 방법론" 같은 구체적 방법론
        r'(바이브\s*러닝\s*방법론|파이브\s*러닝)',
    ]

    for pattern in topic_patterns:
        matches = re.findall(pattern, intro_text, re.IGNORECASE)
        for match in matches:
            topic = clean_topic(match if isinstance(match, str) else match)
            if topic:
                if not result['main_topic']:
                    result['main_topic'] = topic
                elif not is_similar_topic(topic, result['main_topic']) and topic not in result['sub_topics']:
                    # 기존 sub_topics와도 유사성 체크
                    if not any(is_similar_topic(topic, st) for st in result['sub_topics']):
                        result['sub_topics'].append(topic)

    # 3. 프로젝트/도구명 추출 (정규화된 이름 사용)
    project_mapping = {
        r'AI4\s*PKM|AI\s*포\s*PKM': 'AI4 PKM',
        r'CUA[-_]?VL|캐치업\s*AI': 'CatchUpAI',
        r'바이브\s*러닝|Vibe\s*Learning': '바이브러닝',
        r'클라우드\s*스킬[스즈]?|Claude\s*Skills?': 'Claude Skills',
        r'클라우드\s*코드|Claude\s*Code': 'Claude Code',
        r'MCP': 'MCP',
        r'워크로그|WorkLog': 'WorkLog',
    }
    for pattern, normalized_name in project_mapping.items():
        if re.search(pattern, intro_text, re.IGNORECASE):
            # main_topic과 유사하면 스킵
            if is_similar_topic(normalized_name, result['main_topic']):
                continue
            # 기존 sub_topics와 유사하면 스킵
            if any(is_similar_topic(normalized_name, st) for st in result['sub_topics']):
                continue
            result['sub_topics'].append(normalized_name)

    # 4. 발표자 정보 추출
    presenter_patterns = [
        r'저는\s*(.+?)(?:입니다|이고|에\s*있)',
        r'(.+?)(?:님이|님과)\s*(?:운영|진행|참여)',
    ]
    for pattern in presenter_patterns:
        match = re.search(pattern, intro_text)
        if match:
            result['presenter'] = match.group(1).strip()
            break

    # 5. main_topic이 없으면 영상 제목에서 핵심 키워드 추출
    if not result['main_topic'] and video_title:
        # 제목에서 의미있는 키워드만 추출
        meaningful_title_patterns = [
            r'(Claude\s*\w+)',
            r'(AI\s*[\w가-힣]+)',
            r'([\w가-힣]+\s*스킬)',
            r'([\w가-힣]+\s*방법론)',
        ]
        for pattern in meaningful_title_patterns:
            match = re.search(pattern, video_title, re.IGNORECASE)
            if match:
                result['main_topic'] = match.group(1).strip()
                break

    # sub_topics 개수 제한 (최대 3개)
    result['sub_topics'] = result['sub_topics'][:3]

    return result


def extract_meaningful_sentences(text, min_length=20, max_length=150, max_sentences=5, topic_keywords=None):
    """
    텍스트에서 의미있는 핵심 문장 추출

    Args:
        text: 분석할 텍스트
        min_length: 최소 문장 길이
        max_length: 최대 문장 길이
        max_sentences: 최대 추출 문장 수
        topic_keywords: 토픽 관련 키워드 리스트 (포함 시 가점)

    Returns:
        list: 핵심 문장 리스트
    """
    # 문장 분리
    sentences = re.split(r'[.!?。]\s*', text)

    # 의미없는 패턴
    skip_patterns = [
        r'^[아어음예네오와야으이저좀]+\s*[,.]?\s*$',
        r'^안녕하세요',
        r'^감사합니다',
        r'^\s*$',
        r'^[음악]',
        r'^\[',
        r'^잠시만요',
        r'^잠깐만요',
        r'^오케이',
        r'^예\s*$',
        r'^네\s*$',
    ]

    # 지시어로 시작하는 패턴 (감점)
    vague_start_patterns = [
        r'^그\s*프로젝트',
        r'^그\s*작업',
        r'^그것',
        r'^이것',
        r'^이거',
        r'^저거',
        r'^그래서\s*그',
        r'^근데\s*그',
    ]

    # 불완전한 문장 끝 패턴 (스킵)
    incomplete_endings = [
        r'을$', r'를$', r'이$', r'가$', r'은$', r'는$', r'에$', r'의$',
        r'와$', r'과$', r'로$', r'한$', r'된$', r'할$', r'될$',
        r'했$', r'됐$', r'한번$', r'음$',
    ]

    # 의미있는 문장 패턴 (가점)
    meaningful_patterns = [
        (r'(?:만들|개발|작업|진행|완료|시작)(?:했|합니다|하고)', 2),  # 작업 관련
        (r'(?:스킬|방법론|템플릿|프로젝트)', 2),  # 핵심 개념
        (r'(?:AI|클라우드|코딩|러닝)', 1),  # 주요 키워드
        (r'(?:중요|핵심|포인트|목표)', 1),  # 강조 표현
        (r'(?:배우|학습|공부)(?:고|했|합니다)', 2),  # 학습 관련
        (r'(?:테스트|실험|비교)', 1),  # 실험 관련
    ]

    scored_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()

        # 길이 필터
        if len(sentence) < min_length or len(sentence) > max_length:
            continue

        # 스킵 패턴 체크
        skip = False
        for pattern in skip_patterns:
            if re.match(pattern, sentence, re.IGNORECASE):
                skip = True
                break
        if skip:
            continue

        # is_meaningless_sentence 체크 (구어체 시작, 불완전 종결 등 필터링)
        if is_meaningless_sentence(sentence):
            continue

        # 불완전한 문장 끝 체크 (스킵)
        is_incomplete = False
        for pattern in incomplete_endings:
            if re.search(pattern, sentence):
                is_incomplete = True
                break
        if is_incomplete:
            continue

        # 점수 계산
        score = 1  # 기본 점수

        # 지시어로 시작하면 감점
        for pattern in vague_start_patterns:
            if re.match(pattern, sentence):
                score -= 3
                break

        # 의미있는 패턴 가점
        for pattern, points in meaningful_patterns:
            if re.search(pattern, sentence):
                score += points

        # 토픽 키워드 포함 시 높은 가점
        if topic_keywords:
            for kw in topic_keywords:
                if kw and kw.lower() in sentence.lower():
                    score += 3  # 토픽 키워드 포함 시 높은 가점
                    break

        # 점수가 양수인 경우만 추가
        if score > 0:
            scored_sentences.append((sentence, score))

    # 점수순 정렬 후 상위 N개
    scored_sentences.sort(key=lambda x: x[1], reverse=True)
    return [s[0] for s in scored_sentences[:max_sentences]]


def extract_specific_tools(text):
    """
    텍스트에서 구체적인 도구/서비스/기술명 추출

    Args:
        text: 분석할 텍스트

    Returns:
        list: 발견된 도구/서비스 리스트 (우선순위 순)
    """
    # 도구/서비스명 패턴 (구체적인 것들)
    # 주의: 순서가 중요함 - 더 구체적인 패턴을 먼저 배치
    tool_patterns = [
        # AI 서비스/모델 (구체적인 것 먼저)
        (r'클라우드\s*코드|claude\s*code|클코', 'Claude Code'),  # "클라우드"보다 먼저!
        (r'클라우드\s*스킬[스즈]?|claude\s*skills?', 'Claude Skills'),
        (r'클로드|claude(?!\s*code|\s*skill)', '클로드'),  # 단독 클로드
        (r'오픈\s*AI|openai|open\s*ai', '오픈AI'),
        (r'위스퍼|whisper', '위스퍼'),
        (r'제미나이|gemini', '제미나이'),
        (r'GPT[-\s]?4|gpt4|지피티\s*4', 'GPT-4'),
        (r'GPT[-\s]?5|gpt5|지피티\s*5', 'GPT-5'),
        (r'(?<![-\s])GPT(?![-\s]?\d)|지피티(?!\s*\d)', 'GPT'),
        (r'달리|dall[-\s]?e|dalle', 'DALL-E'),
        (r'미드저니|midjourney', '미드저니'),
        (r'스테이블\s*디퓨전|stable\s*diffusion', '스테이블 디퓨전'),
        (r'일레븐랩스|elevenlabs|eleven\s*labs', '일레븐랩스'),
        (r'노션\s*AI|notion\s*ai', '노션 AI'),
        (r'코파일럿|copilot|기업\s*코파일러', '코파일럿'),
        (r'커서\s*AI|cursor\s*ai|커서(?=\s*(?:를|로|에서|사용))', '커서 AI'),

        # 개발 도구/방법론
        (r'바이브\s*코딩|vibe\s*coding|파이브\s*코딩', '바이브 코딩'),
        (r'바이브\s*러닝|vibe\s*learning|파이브\s*러닝|파이버\s*러닝', '바이브 러닝'),
        (r'바이브\s*가이딩|vibe\s*guiding|파이브\s*가이딩', '바이브 가이딩'),
        (r'VS\s*Code|vscode|비주얼\s*스튜디오\s*코드', 'VS Code'),
        (r'깃허브|github|기타\s*레퍼지토리|기터\s*레퍼지', '깃허브'),
        (r'깃랩|gitlab', '깃랩'),
        (r'파이썬|python', '파이썬'),
        (r'자바스크립트|javascript|js', '자바스크립트'),
        (r'타입스크립트|typescript|ts', '타입스크립트'),
        (r'리액트|react', '리액트'),
        (r'노드|node\.?js|nodejs', 'Node.js'),

        # 프로젝트/커뮤니티
        (r'AI4\s*PKM|AI\s*포\s*PKM|에이아이포피케이엠', 'AI4PKM'),
        (r'캐치업\s*AI|CatchUp\s*AI|CUA[-_]?VL', 'CatchUpAI'),
        (r'고비\s*데스크탑|gobi\s*desktop', '고비 데스크탑'),
        (r'클리어리\s*앱|clearly\s*app|클리얼리', '클리어리 앱'),

        # 클라우드/플랫폼
        (r'AWS|아마존\s*웹\s*서비스', 'AWS'),
        (r'GCP|구글\s*클라우드', 'GCP'),
        (r'애저|azure', 'Azure'),
        (r'버셀|vercel', 'Vercel'),
        (r'네틀리파이|netlify', 'Netlify'),
        (r'파이어베이스|firebase', '파이어베이스'),
        (r'수파베이스|supabase', '수파베이스'),

        # 영상/미디어 도구
        (r'프리미어|premiere', '프리미어'),
        (r'파이널\s*컷|final\s*cut', '파이널 컷'),
        (r'다빈치\s*리졸브|davinci\s*resolve', '다빈치 리졸브'),
        (r'캡컷|capcut', '캡컷'),
        (r'OBS|obs\s*스튜디오', 'OBS'),
        (r'FFmpeg|ffmpeg|에프에프엠펙', 'FFmpeg'),

        # 디자인 도구
        (r'피그마|figma', '피그마'),
        (r'캔바|canva', '캔바'),
        (r'포토샵|photoshop', '포토샵'),
        (r'일러스트레이터|illustrator', '일러스트레이터'),

        # 자동화/기타
        (r'재피어|zapier', '재피어'),
        (r'메이크|make\.com|인티그로매트', '메이크'),
        (r'노션(?!\s*AI)|notion(?!\s*ai)', '노션'),
        (r'옵시디언|obsidian|옵시안', '옵시디언'),
        (r'에어테이블|airtable', '에어테이블'),
        (r'슬랙|slack', '슬랙'),
        (r'디스코드|discord', '디스코드'),
        (r'터보텍스|turbotax', '터보텍스'),
    ]

    found_tools = []
    text_lower = text.lower()

    for pattern, tool_name in tool_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            if tool_name not in found_tools:
                found_tools.append(tool_name)

    return found_tools


def extract_specific_actions(text):
    """
    텍스트에서 구체적인 작업/행위 추출

    Args:
        text: 분석할 텍스트

    Returns:
        list: 발견된 구체적 작업 리스트
    """
    # 구체적 작업 패턴
    action_patterns = [
        # 음성/오디오 관련
        (r'음성\s*(?:생성|변환|합성|추출)', '음성 생성'),
        (r'(?:TTS|tts|텍스트\s*투\s*스피치)', '음성 변환'),
        (r'(?:STT|stt|스피치\s*투\s*텍스트|자막\s*추출)', '음성 인식'),
        (r'(?:더빙|나레이션)\s*(?:생성|제작|녹음)?', '더빙 제작'),

        # 이미지/영상 관련
        (r'이미지\s*(?:생성|제작|변환)', '이미지 생성'),
        (r'(?:슬라이드|PPT|프레젠테이션)\s*(?:생성|제작|만들)', '슬라이드 제작'),
        (r'영상\s*(?:편집|제작|합성|생성)', '영상 편집'),
        (r'썸네일\s*(?:제작|생성|만들)', '썸네일 제작'),
        (r'(?:무음|침묵)\s*(?:제거|삭제|컷)', '무음 제거'),
        (r'(?:필러|음|어)\s*(?:제거|삭제)', '필러 제거'),
        (r'자막\s*(?:생성|추가|삽입)', '자막 생성'),

        # 코딩/개발 관련
        (r'코드\s*(?:생성|작성|자동화)', '코드 생성'),
        (r'API\s*(?:연동|호출|사용|통합)', 'API 연동'),
        (r'(?:배포|디플로이|deploy)', '배포'),
        (r'(?:빌드|build)', '빌드'),
        (r'(?:테스트|test)\s*(?:코드|작성)?', '테스트'),
        (r'(?:리팩토링|refactor)', '리팩토링'),
        (r'(?:디버깅|debug)', '디버깅'),

        # 문서/콘텐츠 관련
        (r'(?:문서|문서화|documentation)\s*(?:작성|생성)?', '문서 작성'),
        (r'(?:블로그|포스트)\s*(?:작성|생성)', '블로그 작성'),
        (r'(?:번역|translation)', '번역'),
        (r'(?:요약|summarize)', '요약'),
        (r'(?:마크다운|markdown)\s*(?:변환|생성)', '마크다운 변환'),

        # 자동화 관련
        (r'(?:자동화|automation)', '자동화'),
        (r'(?:워크플로우|workflow)\s*(?:구축|설정)', '워크플로우 구축'),
        (r'(?:스크립트|script)\s*(?:작성|실행)', '스크립트 작성'),
        (r'(?:스케줄|예약)\s*(?:설정|실행)', '스케줄 설정'),
    ]

    found_actions = []
    text_lower = text.lower()

    for pattern, action_name in action_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            if action_name not in found_actions:
                found_actions.append(action_name)

    return found_actions


def detect_main_action(text):
    """
    텍스트에서 주요 행위/활동 감지

    Returns:
        str: 행위 동사 (소개, 설명, 진행, 작업, 사용 등)
    """
    # 행위 패턴과 우선순위
    action_patterns = [
        (r'소개', '소개'),
        (r'설명', '설명'),
        (r'만들|제작', '제작'),
        (r'사용|활용|이용', '활용'),
        (r'작업|진행', '작업'),
        (r'분석|검토', '분석'),
        (r'설치|설정', '설정'),
        (r'테스트|실험', '테스트'),
        (r'비교', '비교'),
        (r'개발|구현', '개발'),
        (r'학습|공부', '학습'),
        (r'정리|요약', '정리'),
    ]

    text_lower = text.lower()
    for pattern, action in action_patterns:
        if re.search(pattern, text_lower):
            return action

    return "내용"


def get_particle(word, particle_type='와'):
    """
    단어에 맞는 조사 반환 (받침 유무에 따라)

    Args:
        word: 단어
        particle_type: '와'(와/과), '을'(을/를), '이'(이/가)

    Returns:
        str: 적절한 조사
    """
    if not word:
        return particle_type

    last_char = word[-1]

    # 영문/숫자는 '와' 사용
    if not ('가' <= last_char <= '힣'):
        return '와' if particle_type == '와' else particle_type

    # 받침 확인 (유니코드 계산)
    code = ord(last_char) - 0xAC00
    final = code % 28

    if particle_type == '와':
        return '과' if final > 0 else '와'
    elif particle_type == '을':
        return '을' if final > 0 else '를'
    elif particle_type == '이':
        return '이' if final > 0 else '가'

    return particle_type


def generate_topic_summary(text, keywords, max_length=40):
    """
    주제 기반 요약문 생성 (간조체)

    예: "AI를 활용한 영상 제작 방법 소개"
        "클라우드 스킬 개발 및 활용"

    Args:
        text: 요약할 텍스트
        keywords: 키워드 리스트
        max_length: 최대 길이

    Returns:
        str: 주제 기반 요약문
    """
    if not keywords:
        return "주요 내용 정리"

    # 의미있는 키워드만 필터링
    meaningful_kw = [kw for kw in keywords
                     if len(kw) >= 2 and kw not in ['것은', '것이', '일을', '이거', '저거',
                                                     '현재', '일단', '여러', '같습니다', '요렇고']]

    if not meaningful_kw:
        return "주요 내용 정리"

    # 주요 행위 감지
    action = detect_main_action(text)

    # 키워드 조합으로 요약문 생성
    main_topic = meaningful_kw[0]

    # 키워드가 2개 이상이면 조합
    if len(meaningful_kw) >= 2:
        second_topic = meaningful_kw[1]
        particle = get_particle(main_topic, '와')

        # 특정 조합 패턴
        if main_topic in ['AI', '클라우드', '오픈'] and second_topic in ['코딩', '스킬', '영상', '작업']:
            return f"{main_topic} {second_topic} {action}"
        elif action in ['활용', '사용']:
            return f"{main_topic}{particle} {second_topic} 활용 방법"
        elif action in ['제작', '개발']:
            return f"{main_topic} 기반 {second_topic} {action}"
        else:
            return f"{main_topic}{particle} {second_topic} {action}"
    else:
        # 단일 키워드
        if action in ['소개', '설명']:
            return f"{main_topic} {action}"
        else:
            return f"{main_topic} 활용 및 {action}"


def is_sentence_style_title(title):
    """
    문장형 제목인지 확인 (제목으로 부적절)

    Args:
        title: 확인할 제목

    Returns:
        bool: 문장형이면 True
    """
    if not title:
        return True

    # 문장으로 시작하는 패턴 (제목으로 부적절)
    sentence_start_patterns = [
        r'^그래서\s',
        r'^그리고\s',
        r'^그런데\s',
        r'^근데\s',
        r'^하지만\s',
        r'^그러면\s',
        r'^그럼\s',
        r'^왜냐하면\s',
        r'^저는\s',
        r'^제가\s',
        r'^우리\s',
        r'^이제\s',
        r'^지금\s',
        r'^여기\s',
        r'^요거\s',
        r'^요것\s',
    ]

    for pattern in sentence_start_patterns:
        if re.match(pattern, title):
            return True

    # 문장형 어미로 끝나는 경우
    sentence_end_patterns = [
        r'요$', r'죠$', r'네요$', r'거든요$', r'잖아요$',
        r'습니다$', r'입니다$', r'합니다$', r'됩니다$',
        r'어요$', r'아요$', r'해요$', r'돼요$',
        r'거예요$', r'건데요$', r'는데요$',
    ]

    for pattern in sentence_end_patterns:
        if re.search(pattern, title):
            return True

    return False


def generate_section_title(text, keywords):
    """
    섹션 제목 생성 (실제 내용 기반, 구체적)

    Args:
        text: 섹션 텍스트
        keywords: 키워드 리스트

    Returns:
        str: 섹션 제목
    """
    # 구체적 도구/작업 추출
    tools = extract_specific_tools(text)
    actions = extract_specific_actions(text)

    # === 개선: 의미있는 문장에서 제목 힌트 추출 ===
    meaningful = extract_meaningful_sentences(text, min_length=15, max_length=80, max_sentences=2)

    # 제목 패턴 매칭 (영상에서 직접 언급된 주제)
    title_patterns = [
        r'(.+?)(?:에\s*대해|를\s*(?:알아보|살펴보|다루|진행))',
        r'(.+?)\s*(?:작업|실습|테스트)(?:을|를)?',
        r'(.+?)\s*(?:방법|과정)(?:을|를)?',
    ]

    for pattern in title_patterns:
        match = re.search(pattern, text[:500])  # 처음 500자에서 검색
        if match:
            extracted = match.group(1).strip()
            # 너무 길거나 짧으면 스킵
            if 3 <= len(extracted) <= 25:
                # 불용어로만 이루어진 경우 스킵
                stopwords = {'그', '이', '저', '뭐', '좀', '어', '음', '예', '네', '아'}
                # 문장형 제목 체크 추가
                if extracted not in stopwords and not is_sentence_style_title(extracted):
                    return extracted

    # 구체적 도구와 작업이 있으면 조합
    if tools and actions:
        main_tool = tools[0]
        main_action = actions[0]
        # 너무 길면 축약
        if len(main_tool) + len(main_action) > 25:
            return f"{main_tool} {main_action}"
        return f"{main_tool}로 {main_action}"

    elif tools:
        main_tool = tools[0]
        # 맥락에 맞는 동사 선택
        if '테스트' in text or '실험' in text:
            return f"{main_tool} 테스트"
        elif '설정' in text or '설치' in text:
            return f"{main_tool} 설정"
        elif '비교' in text:
            return f"{main_tool} 비교 분석"
        elif '소개' in text or '안내' in text:
            return f"{main_tool} 소개"
        elif len(tools) >= 2:
            return f"{main_tool}와 {tools[1]} 활용"
        else:
            action = detect_main_action(text)
            return f"{main_tool} {action}"

    elif actions:
        main_action = actions[0]
        if len(actions) >= 2:
            return f"{main_action} 및 {actions[1]}"
        return main_action

    else:
        # 키워드 기반 (fallback)
        # 의미있는 키워드만 사용
        skip_kw = {'것은', '것이', '일을', '클라우드', '사용', '진행', '작업', '내용'}
        useful_kw = [kw for kw in keywords if kw not in skip_kw and len(kw) >= 2]

        if useful_kw:
            main_kw = useful_kw[0]
            action = detect_main_action(text)
            if len(useful_kw) >= 2:
                return f"{main_kw}와 {useful_kw[1]} {action}"
            return f"{main_kw} {action}"

        return generate_topic_summary(text, keywords, max_length=30)


def generate_section_bullets(text, keywords, max_bullets=3, global_used_bullets=None, section_index=0):
    """
    섹션 내용을 요약 불릿으로 생성 (실제 문장 기반, 전역 중복 방지)

    Args:
        text: 섹션 텍스트
        keywords: 키워드 리스트
        max_bullets: 최대 불릿 수
        global_used_bullets: 전역 사용된 불릿 set (중복 방지)
        section_index: 섹션 번호 (다양성용)

    Returns:
        list: 요약 불릿 리스트
    """
    bullets = []
    used_phrases = set()
    if global_used_bullets is None:
        global_used_bullets = set()

    # 구체적 도구/작업 추출
    tools = extract_specific_tools(text)
    actions = extract_specific_actions(text)

    # 섹션별 특화 키워드 (fallback 다양화용)
    section_keywords = keywords[:3] if keywords else []

    # === 개선: 실제 의미있는 문장에서 불릿 추출 ===
    meaningful_sentences = extract_meaningful_sentences(text, min_length=15, max_length=100, max_sentences=5)

    # 1. 의미있는 문장을 불릿으로 변환
    for sentence in meaningful_sentences:
        if len(bullets) >= max_bullets:
            break

        # 문장 정제 (간조체로 변환)
        bullet = convert_to_concise_style(sentence)

        # 너무 길면 자연스럽게 자르기
        if len(bullet) > 60:
            bullet = truncate_sentence_naturally(bullet, max_length=60, min_length=15)

        # 너무 짧거나 의미없으면 스킵
        if len(bullet) < 10:
            continue

        # 불완전한 끝 체크 및 보정
        incomplete_end_patterns = [
            # 조사로 끝나는 경우 (스킵)
            (r'을$', None), (r'를$', None), (r'이$', None), (r'가$', None),
            (r'은$', None), (r'는$', None), (r'에$', None), (r'의$', None),
            (r'와$', None), (r'과$', None), (r'로$', None), (r'에서$', None),
            # 불완전 동사 어미 (스킵)
            (r'한$', None), (r'된$', None), (r'했$', None), (r'됐$', None),
            (r'던$', None), (r'고$', None), (r'해$', None), (r'되$', None),
            (r'어$', None), (r'여$', None), (r'아$', None),
            # 연결 어미 (스킵)
            (r'하여$', None), (r'되어$', None), (r'해서$', None), (r'되서$', None),
            (r'하고$', None), (r'되고$', None), (r'면서$', None), (r'으며$', None),
            # 할/될 + 거/것 (보정)
            (r'할\s*거$', ' 예정'), (r'될\s*거$', ' 예정'),
            (r'할\s*것$', ' 예정'), (r'될\s*것$', ' 예정'),
            (r'할$', ' 예정'), (r'될$', ' 예정'),
            # 기타
            (r'한번$', None), (r'음$', None), (r'렇$', None), (r'그렇$', None),
        ]
        is_incomplete = False
        for pattern, suffix in incomplete_end_patterns:
            if re.search(pattern, bullet):
                if suffix is None:
                    # 스킵
                    is_incomplete = True
                    break
                else:
                    # 보정
                    bullet = re.sub(pattern, suffix, bullet)
                    bullet = re.sub(r'\s+', ' ', bullet)  # 이중 공백 제거
                    break

        if is_incomplete:
            continue

        # 중복 체크 (유사 문구 방지)
        is_duplicate = False
        for used in used_phrases:
            # 70% 이상 겹치면 중복으로 판단
            overlap = sum(1 for word in bullet.split() if word in used)
            if overlap > len(bullet.split()) * 0.7:
                is_duplicate = True
                break

        # 텍스트 정제 적용
        bullet = clean_subtitle_text(bullet)

        # 전역 중복 체크 추가
        if bullet in global_used_bullets:
            continue

        if not is_duplicate and bullet not in bullets:
            # 명사형 종결로 변환
            bullet = convert_to_noun_ending(bullet)

            # 유효한 불릿인지 체크 (완화된 기준)
            if not is_valid_bullet(bullet):
                continue

            if len(bullet) >= 10:  # 충분한 길이인지 확인
                bullets.append(bullet)
                used_phrases.add(bullet)
                global_used_bullets.add(bullet)  # 전역에도 추가

    # 2. 섹션 키워드 기반 내용 요약 생성 (명사형, 섹션별 다양화)
    # 섹션에서 추출된 키워드를 활용하여 해당 섹션의 고유한 내용 생성
    if len(bullets) < max_bullets and section_keywords:
        # 섹션별 고유 키워드 조합
        used_kw_in_bullets = set()
        for b in bullets:
            for kw in section_keywords:
                if kw in b:
                    used_kw_in_bullets.add(kw)

        # 섹션 인덱스에 따른 다양한 템플릿 (명사형)
        keyword_templates = [
            ["{kw} 개념 및 기초 정리", "{kw} 소개 및 개요"],
            ["{kw} 환경 설정 방법", "{kw} 구성 및 설치"],
            ["{kw} 기능 활용 실습", "{kw} 사용 방법 정리"],
            ["{kw} 심화 내용 탐구", "{kw} 고급 기능 분석"],
            ["{kw} 결과 분석 및 정리", "{kw} 출력 확인 방법"],
            ["{kw} 실제 적용 사례", "{kw} 활용 예시 정리"],
            ["{kw} 문제 해결 방안", "{kw} 오류 대응 방법"],
            ["{kw} 성능 최적화 기법", "{kw} 개선 방안 도출"],
        ]
        template_idx = section_index % len(keyword_templates)

        for kw in section_keywords:
            if len(bullets) >= max_bullets:
                break
            if kw in used_kw_in_bullets:
                continue

            # 섹션에 맞는 템플릿 적용
            templates = keyword_templates[template_idx]
            bullet = None
            for tmpl in templates:
                candidate = tmpl.format(kw=kw)
                if candidate not in global_used_bullets:
                    bullet = candidate
                    break

            if bullet is None:
                continue

            bullets.append(bullet)
            global_used_bullets.add(bullet)
            used_kw_in_bullets.add(kw)

    # 3. 도구+작업 조합 (명사형)
    if len(bullets) < max_bullets and tools and actions:
        for tool in tools[:2]:
            if len(bullets) >= max_bullets:
                break
            for action in actions[:2]:
                if len(bullets) >= max_bullets:
                    break
                # 명사형: "도구 활용 작업" 형태
                bullet = f"{tool} 기반 {action} 작업"
                # 전역 중복 체크 - 도구+작업 조합이 유사한지도 체크
                tool_action_key = f"{tool}_{action}"
                if bullet not in bullets and bullet not in global_used_bullets:
                    if not any(tool in b and action in b for b in global_used_bullets):
                        bullets.append(bullet)
                        global_used_bullets.add(bullet)
                        break

    # 섹션별 다양화를 위한 명사형 변형 패턴
    section_variants = [
        "{tool} 개념 학습",
        "{tool} 환경 구성",
        "{tool} 기능 실습",
        "{tool} 심화 활용",
        "{tool} 결과 분석",
        "{tool} 사례 연구",
        "{tool} 오류 해결",
        "{tool} 성능 최적화",
    ]

    # 4. 도구 기반 불릿 (명사형, 섹션별 다양화)
    if len(bullets) < max_bullets and tools:
        for tool in tools:
            if len(bullets) >= max_bullets:
                break
            if any(tool in b for b in bullets):
                continue

            # 맥락에 맞는 명사형 설명 생성
            if 'API' in text.upper() or '연동' in text:
                bullet = f"{tool} API 연동 설정"
            elif '테스트' in text or '실험' in text:
                bullet = f"{tool} 기능 테스트"
            elif '설치' in text or '설정' in text:
                bullet = f"{tool} 환경 설정"
            elif '비교' in text:
                bullet = f"{tool} 성능 비교"
            elif '코드' in text or '스크립트' in text:
                bullet = f"{tool} 코드 작성"
            else:
                # 섹션 인덱스 기반 다양화
                variant_idx = section_index % len(section_variants)
                bullet = section_variants[variant_idx].format(tool=tool)

            # 전역 중복 체크 - 중복이면 다른 변형 시도
            if bullet in global_used_bullets:
                for i in range(len(section_variants)):
                    alt_bullet = section_variants[(section_index + i) % len(section_variants)].format(tool=tool)
                    if alt_bullet not in global_used_bullets:
                        bullet = alt_bullet
                        break
                else:
                    continue  # 모든 변형이 사용됨, 스킵

            if bullet not in bullets and bullet not in global_used_bullets:
                bullets.append(bullet)
                global_used_bullets.add(bullet)

    # 5. 작업 기반 불릿 (명사형)
    if len(bullets) < max_bullets and actions:
        for action in actions:
            if len(bullets) >= max_bullets:
                break
            if any(action in b for b in bullets):
                continue

            # 명사형: "작업명 + 작업/처리"
            bullet = f"{action} 작업"

            # 전역 중복 체크 - 중복이면 키워드와 조합
            if bullet in global_used_bullets and section_keywords:
                for kw in section_keywords:
                    alt_bullet = f"{kw} 기반 {action}"
                    if alt_bullet not in global_used_bullets:
                        bullet = alt_bullet
                        break

            if bullet not in bullets and bullet not in global_used_bullets:
                bullets.append(bullet)
                global_used_bullets.add(bullet)

    # 6. 키워드 기반 (최후의 수단, 명사형)
    if len(bullets) < max_bullets:
        skip_words = {'것은', '것이', '일을', '이거', '저거', '현재', '일단', '여러',
                      '같습니다', '요렇고', '그런', '있는', '혹시', '요런', '이런',
                      '클라우드', '사용', '활용', '진행', '작업'}
        meaningful_kw = [kw for kw in keywords if kw not in skip_words and len(kw) >= 2]

        for kw in meaningful_kw:
            if len(bullets) >= max_bullets:
                break
            if any(kw in b for b in bullets):
                continue

            # 명사형으로 생성
            bullet = f"{kw} 관련 내용 정리"

            if bullet not in bullets and bullet not in global_used_bullets:
                bullets.append(bullet)
                global_used_bullets.add(bullet)

    # 최소 1개 보장 (명사형)
    if not bullets:
        if tools:
            fallback = f"{tools[0]} 관련 내용 설명"
            if fallback in global_used_bullets:
                fallback = f"{tools[0]} 추가 기능 소개"
            bullets.append(fallback)
        elif actions:
            bullets.append(f"{actions[0]} 작업 수행")
        else:
            bullets.append("해당 구간 주요 내용")

    return bullets[:max_bullets]


def truncate_sentence_naturally(text, max_length=60, min_length=15):
    """
    문장을 자연스러운 지점에서 자르기 (끊김 방지)

    Args:
        text: 자를 텍스트
        max_length: 최대 길이
        min_length: 최소 길이 (이보다 짧아지지 않음)

    Returns:
        str: 자연스럽게 잘린 텍스트
    """
    if len(text) <= max_length:
        return text

    # 자연스러운 끝 지점 패턴 (우선순위 순)
    natural_end_patterns = [
        # 완전한 어미 (가장 자연스러움)
        r'[^.!?]+[.!?](?=\s|$)',  # 문장 종결
        # 연결 어미 + 쉼표
        r'[^,]+하고,',
        r'[^,]+하며,',
        r'[^,]+되고,',
        # 명사형 어미
        r'[^,]+[^다]기(?=\s|,|$)',
        r'[^,]+[함됨음](?=\s|,|$)',
        # 연결 어미
        r'[^,]+(?:하고|하며|되고|하여|되어)(?=\s|$)',
    ]

    # 우선: max_length 내에서 자연스러운 끝 지점 찾기
    search_text = text[:max_length]

    # 방법 1: 완결된 문장 찾기
    for pattern in natural_end_patterns:
        matches = list(re.finditer(pattern, search_text))
        if matches:
            # 가장 긴 매치 사용
            best_match = max(matches, key=lambda m: m.end())
            if best_match.end() >= min_length:
                return text[:best_match.end()].rstrip(',').strip()

    # 방법 2: 동사/형용사 어미에서 자르기
    verb_endings = ['했', '됐', '봤', '함', '됨', '음', '임', '기', '고', '며', '어', '아', '여']
    best_cut = max_length

    for i in range(max_length - 1, min_length - 1, -1):
        if i < len(text):
            char = text[i]
            # 동사/형용사 어미 뒤에서 자르기
            if char in verb_endings:
                # 다음 문자 확인 (공백이면 좋은 지점)
                if i + 1 < len(text) and text[i + 1] in ' ,':
                    best_cut = i + 1
                    break
            # 공백에서 자르기 (단어 중간 방지)
            elif char == ' ':
                best_cut = i
                break

    # 방법 3: 공백에서 자르기 (최후의 수단)
    if best_cut == max_length:
        space_idx = text.rfind(' ', min_length, max_length)
        if space_idx > min_length:
            best_cut = space_idx

    result = text[:best_cut].rstrip(',').rstrip()

    # 불완전한 어미로 끝나면 보정
    bad_endings = ['을', '를', '이', '가', '은', '는', '에', '의', '와', '과', '로', '으로']
    if result and result[-1] in bad_endings:
        # 한 단어 더 추가 시도
        next_space = text.find(' ', best_cut + 1)
        if next_space > 0 and next_space <= max_length + 10:
            result = text[:next_space].rstrip(',').rstrip()

    return result


def convert_to_concise_style(text):
    """
    서술체를 간조체로 변환

    예: "설명합니다" → "설명"
        "진행했습니다" → "진행"
        "소개하고 있습니다" → "소개"

    Args:
        text: 변환할 텍스트

    Returns:
        str: 간조체로 변환된 텍스트
    """
    if not text:
        return text

    # 서술체 어미 → 간조체 변환 패턴 (순서 중요: 긴 패턴 먼저)
    patterns = [
        # 복합 어미
        (r'하고\s*있습니다\.?$', ''),
        (r'되고\s*있습니다\.?$', ''),
        (r'진행하고\s*있습니다\.?$', ' 진행'),
        (r'설명하고\s*있습니다\.?$', ' 설명'),
        (r'소개하고\s*있습니다\.?$', ' 소개'),
        # -겁니다 (구어체)
        (r'겁니다\.?$', ''),
        (r'거예요\.?$', ''),
        (r'거에요\.?$', ''),
        (r'거야\.?$', ''),
        (r'거고\.?$', ''),
        # -했습니다/됐습니다
        (r'했습니다\.?$', ''),
        (r'됐습니다\.?$', ''),
        (r'봤습니다\.?$', ''),
        (r'갔습니다\.?$', ''),
        (r'왔습니다\.?$', ''),
        (r'했어요\.?$', ''),
        (r'됐어요\.?$', ''),
        (r'봤어요\.?$', ''),
        (r'같습니다\.?$', ''),
        # -합니다/됩니다/입니다
        (r'합니다\.?$', ''),
        (r'됩니다\.?$', ''),
        (r'입니다\.?$', ''),
        (r'봅니다\.?$', ''),
        (r'갑니다\.?$', ''),
        (r'옵니다\.?$', ''),
        # -있어요/없어요
        (r'있어요\.?$', ' 있음'),
        (r'없어요\.?$', ' 없음'),
        (r'있습니다\.?$', ' 있음'),
        (r'없습니다\.?$', ' 없음'),
        # -해요/돼요/이에요
        (r'해요\.?$', ''),
        (r'돼요\.?$', ''),
        (r'이에요\.?$', ''),
        (r'예요\.?$', ''),
        (r'네요\.?$', ''),
        (r'죠\.?$', ''),
        (r'는데요\.?$', ''),
        (r'거든요\.?$', ''),
        (r'아니고요\.?$', ' 아님'),
        (r'이고요\.?$', ''),
        (r'고요\.?$', ''),
        # -하다/되다 (기본형)
        (r'하였다\.?$', ''),
        (r'되었다\.?$', ''),
        (r'했다\.?$', ''),
        (r'됐다\.?$', ''),
        (r'한다\.?$', ''),
        (r'된다\.?$', ''),
        # -는/은/을 것이다
        (r'을\s*것입니다\.?$', ' 예정'),
        (r'을\s*것이다\.?$', ' 예정'),
        (r'을\s*예정입니다\.?$', ' 예정'),
        (r'을\s*겁니다\.?$', ' 예정'),
        (r'을\s*거예요\.?$', ' 예정'),
    ]

    result = text.strip()
    for pattern, replacement in patterns:
        result = re.sub(pattern, replacement, result)

    # 마지막 마침표 제거
    result = result.rstrip('.')

    return result.strip()


def generate_diverse_fallback_description(topic, topic_type='general', context_text='', index=0):
    """
    토픽 유형별로 다양한 fallback 설명 생성

    Args:
        topic: 토픽/주제명
        topic_type: 유형 ('tool', 'methodology', 'action', 'concept', 'general')
        context_text: 맥락 텍스트 (추가 힌트)
        index: 인덱스 (다양성을 위해)

    Returns:
        str: 다양화된 설명
    """
    # 토픽 유형 자동 감지
    if topic_type == 'general':
        tool_keywords = ['코드', 'AI', 'API', '앱', '플랫폼', '서비스', '도구', 'Code', 'GPT']
        method_keywords = ['방법론', '러닝', '스킬', '가이딩', '코딩', '학습']
        action_keywords = ['편집', '생성', '변환', '제작', '제거', '테스트', '분석']

        topic_lower = topic.lower()
        if any(kw.lower() in topic_lower for kw in tool_keywords):
            topic_type = 'tool'
        elif any(kw in topic for kw in method_keywords):
            topic_type = 'methodology'
        elif any(kw in topic for kw in action_keywords):
            topic_type = 'action'
        else:
            topic_type = 'concept'

    # 유형별 설명 템플릿
    templates = {
        'tool': [
            f"{topic} 환경 설정 및 기본 사용법 안내",
            f"{topic}의 주요 기능과 활용 사례 소개",
            f"{topic}를 프로젝트에 적용하는 방법 설명",
            f"{topic} 설치부터 실행까지의 과정 안내",
        ],
        'methodology': [
            f"{topic}의 핵심 원리와 적용 방법 설명",
            f"{topic} 방식으로 효율적인 작업 진행",
            f"{topic}을 실제 프로젝트에 적용하는 과정",
            f"{topic}의 장점과 활용 전략 소개",
        ],
        'action': [
            f"{topic} 작업의 단계별 과정 안내",
            f"{topic} 수행을 위한 도구와 방법 설명",
            f"효율적인 {topic}을 위한 팁과 노하우",
            f"{topic} 결과물 검토 및 개선 방안",
        ],
        'concept': [
            f"{topic}에 대한 개념 설명 및 이해",
            f"{topic} 관련 주요 내용 정리",
            f"{topic}의 실제 적용 사례와 효과",
            f"{topic}을 활용한 작업 과정 소개",
        ],
    }

    # 맥락 기반 추가 커스터마이징
    selected_templates = templates.get(topic_type, templates['concept'])

    # 인덱스로 다양성 확보
    template_idx = index % len(selected_templates)
    description = selected_templates[template_idx]

    # 맥락에서 추가 힌트 추출 (선택적)
    if context_text:
        actions = extract_specific_actions(context_text)
        if actions and actions[0] not in description:
            # 특정 작업이 발견되면 설명에 반영
            if '안내' in description or '설명' in description:
                description = description.replace('안내', f"및 {actions[0]} 안내")

    return description


def generate_key_point_title(keywords, key_sentence):
    """
    핵심 포인트 제목 생성 (키워드 문장 형태)

    Args:
        keywords: 키워드 리스트
        key_sentence: 핵심 문장

    Returns:
        str: 포인트 제목
    """
    if not keywords:
        return "주요 내용"

    main_keyword = keywords[0]

    # 키워드가 포함된 문장에서 핵심 구 추출
    if key_sentence and main_keyword in key_sentence:
        # 키워드 주변 텍스트 추출 (최대 30자)
        idx = key_sentence.find(main_keyword)
        start = max(0, idx - 10)
        end = min(len(key_sentence), idx + len(main_keyword) + 20)
        excerpt = key_sentence[start:end].strip()

        # 시작/끝 정리
        if start > 0:
            excerpt = "..." + excerpt
        if end < len(key_sentence):
            excerpt = excerpt + "..."

        return excerpt

    # 기본: 키워드 + 설명 형태
    if len(keywords) >= 2:
        return f"{main_keyword}와 {keywords[1]}"
    return main_keyword


def summarize_from_timeline(transcript, video_title=""):
    """
    타임라인 기반으로 요약 생성 (API 키 불필요)
    - 도입부에서 실제 주제 추출
    - 핵심 포인트: 구체적 내용 기반 정리
    - 섹션: 실제 내용 기반 제목

    Args:
        transcript: 자막 데이터 (list of dict)
        video_title: 영상 제목

    Returns:
        dict: summary, key_points, sections
    """
    print("\n[Note] 타임라인 기반 요약 생성 중 (API 키 불필요)...")

    # 전체 텍스트 추출
    full_text = " ".join([entry['text'].strip() if isinstance(entry, dict) else entry.text.strip() for entry in transcript])

    # 영상 전체 길이 계산
    last_entry = transcript[-1]
    last_start = last_entry['start'] if isinstance(last_entry, dict) else last_entry.start
    last_duration = last_entry.get('duration', 0) if isinstance(last_entry, dict) else getattr(last_entry, 'duration', 0)
    total_duration = last_start + last_duration

    # 영상 길이에 따른 동적 간격 설정 (섹션용)
    if total_duration <= 1800:  # 30분 이하
        interval = 300  # 5분 간격
    elif total_duration <= 3600:  # 1시간 이하
        interval = 600  # 10분 간격
    elif total_duration <= 7200:  # 2시간 이하
        interval = 900  # 15분 간격
    else:  # 2시간 초과
        interval = 1200  # 20분 간격

    # 섹션 수가 6-8개가 되도록 조정
    estimated_sections = total_duration / interval
    if estimated_sections > 10:
        interval = int(total_duration / 8)  # 최대 8개 섹션
    elif estimated_sections < 4:
        interval = int(total_duration / 5)  # 최소 5개 섹션

    print(f"      영상 길이: {format_timestamp(total_duration)}, 구간 간격: {interval//60}분")

    # 전체 키워드 추출 (요약용)
    global_keywords = extract_keywords(full_text, top_n=10)
    print(f"      주요 키워드: {', '.join(global_keywords[:5])}")

    # === 개선: 도입부 확대 (50개 → 150개, 약 5-7분) ===
    intro_texts = [
        (e['text'].strip() if isinstance(e, dict) else e.text.strip())
        for e in transcript[:150]  # 처음 150개 자막 (약 5-7분)
    ]
    intro_text = " ".join(intro_texts)

    # === 개선: 도입부에서 실제 주제 추출 ===
    topic_info = extract_topic_from_intro(intro_text, video_title)
    print(f"      추출된 주제: {topic_info['main_topic'] or '(자동 감지)'}")
    if topic_info['sub_topics']:
        print(f"      부가 주제: {', '.join(topic_info['sub_topics'][:3])}")

    # 타임라인 구간별 분석
    sections_list = []
    current_time = 0
    section_num = 1
    used_section_titles = set()  # 중복 방지용 제목 추적
    global_used_bullets = set()  # 전역 불릿 중복 방지

    while current_time < total_duration:
        # 해당 구간의 텍스트 추출
        section_texts = [
            (e['text'].strip() if isinstance(e, dict) else e.text.strip())
            for e in transcript
            if current_time <= (e['start'] if isinstance(e, dict) else e.start) < current_time + interval
        ]

        if section_texts:
            section_full_text = " ".join(section_texts)

            # 구간별 키워드 추출
            section_keywords = extract_keywords(section_full_text, top_n=5)

            # 주제 기반 섹션 제목 생성 (간조체)
            section_title = generate_section_title(section_full_text, section_keywords)

            # === 섹션 제목 중복 방지 로직 ===
            original_title = section_title
            title_suffix = 1
            while section_title in used_section_titles:
                # 중복되면 대체 제목 시도
                # 1. 키워드 조합으로 대체
                if section_keywords and title_suffix == 1:
                    alt_keywords = [kw for kw in section_keywords if kw not in original_title]
                    if alt_keywords:
                        action = detect_main_action(section_full_text)
                        section_title = f"{alt_keywords[0]} {action}"
                # 2. 구체적 도구/작업 기반 대체
                elif title_suffix == 2:
                    tools = extract_specific_tools(section_full_text)
                    actions = extract_specific_actions(section_full_text)
                    if tools and original_title not in tools[0]:
                        section_title = f"{tools[0]} 활용"
                    elif actions and original_title not in actions[0]:
                        section_title = f"{actions[0]} 진행"
                # 3. 최후의 수단: 숫자 접미사
                else:
                    section_title = f"{original_title} ({title_suffix - 1})"
                title_suffix += 1
                if title_suffix > 5:  # 무한 루프 방지
                    break

            used_section_titles.add(section_title)

            # 주제 기반 요약 불릿 생성 (간조체, 전역 중복 방지)
            section_bullets = generate_section_bullets(
                section_full_text, section_keywords, max_bullets=3,
                global_used_bullets=global_used_bullets, section_index=section_num
            )

            timestamp_start = format_timestamp(current_time)
            timestamp_end = format_timestamp(min(current_time + interval, total_duration))

            sections_list.append({
                'num': section_num,
                'time_range': f"{timestamp_start} - {timestamp_end}",
                'title': section_title,
                'bullets': section_bullets,  # 요약 불릿 사용
                'keywords': section_keywords,
                'full_text': section_full_text  # 원문 보관 (핵심포인트용)
            })
            section_num += 1

        current_time += interval

    print(f"      총 {len(sections_list)}개 구간 분석 완료")

    # === 개선된 요약 생성 (실제 주제 기반) ===
    # 영상 맥락 추출 (topic_info 활용)
    video_context = ""
    if topic_info['broadcast_info'].get('episode'):
        episode = topic_info['broadcast_info']['episode']
        series = topic_info['broadcast_info'].get('series_name', '라이브 방송')
        video_context = f'"{series}" {episode}번째 방송'
    elif "방송" in intro_text or "라이브" in intro_text:
        match = re.search(r'(\d+)\s*번째', intro_text)
        if match:
            video_context = f"{match.group(1)}번째 라이브 방송"
        else:
            video_context = "라이브 방송"
    else:
        video_context = "영상"

    # === 개선: 실제 추출된 주제 우선 사용 ===
    # 1. topic_info에서 추출된 주제
    # 2. 발견된 도구/서비스
    # 3. 빈도 기반 키워드 (fallback)
    all_tools = extract_specific_tools(full_text)
    all_actions = extract_specific_actions(full_text)

    # 주제 우선순위 결정
    primary_topics = []
    if topic_info['main_topic']:
        primary_topics.append(topic_info['main_topic'])
    primary_topics.extend(topic_info['sub_topics'][:2])

    # 도구/프로젝트명 추가
    for tool in all_tools[:3]:
        if tool not in primary_topics:
            primary_topics.append(tool)

    # 키워드로 보완
    skip_topics = {'방송', '내용', '작업', '진행', '것은', '것이', '코딩', '영상',
                   '사용', '지금', '오늘', '여기', '클라우드'}  # "클라우드" 단독은 제외
    for kw in global_keywords[:5]:
        if kw not in skip_topics and kw not in primary_topics:
            primary_topics.append(kw)

    # 섹션 제목들에서 주제 파악
    section_titles = [s.get('title', '') for s in sections_list if s.get('title')]

    # === 3줄 요약 생성 (구체적 내용 기반) ===
    summary_lines = []

    # 1줄: 영상 개요 및 핵심 주제 (구체적으로)
    if topic_info['main_topic']:
        # 실제 추출된 주제 사용
        main_topic = topic_info['main_topic']
        sub_topics = topic_info['sub_topics'][:2] if topic_info['sub_topics'] else primary_topics[1:3]

        if sub_topics:
            summary_lines.append(
                f"이 {video_context}은 **{main_topic}**을 중심으로, "
                f"**{'**, **'.join(sub_topics)}** 등을 다루는 약 {format_timestamp(total_duration)} 분량의 콘텐츠입니다."
            )
        else:
            summary_lines.append(
                f"이 {video_context}은 **{main_topic}**에 대한 약 {format_timestamp(total_duration)} 분량의 콘텐츠입니다."
            )
    elif all_tools:
        # 도구 기반 요약
        main_tool = all_tools[0]
        other_tools = all_tools[1:3]
        if other_tools:
            summary_lines.append(
                f"이 {video_context}은 **{main_tool}**을 활용하여 "
                f"**{'**, **'.join(other_tools)}** 등의 작업을 진행하는 약 {format_timestamp(total_duration)} 분량입니다."
            )
        else:
            summary_lines.append(
                f"이 {video_context}은 **{main_tool}** 활용에 대한 약 {format_timestamp(total_duration)} 분량입니다."
            )
    else:
        # Fallback: 키워드 기반
        if primary_topics:
            summary_lines.append(
                f"이 {video_context}은 약 {format_timestamp(total_duration)} 분량으로, "
                f"**{primary_topics[0]}**를 중심으로 관련 내용을 다룹니다."
            )
        else:
            summary_lines.append(
                f"이 {video_context}은 약 {format_timestamp(total_duration)} 분량의 콘텐츠입니다."
            )

    # 2줄: 주요 내용 (도입부에서 추출된 의미있는 문장 활용)
    meaningful_intro = extract_meaningful_sentences(intro_text, max_sentences=3)
    if meaningful_intro:
        # 가장 의미있는 문장에서 핵심 내용 추출
        key_sentence = meaningful_intro[0]
        # 너무 길면 요약
        if len(key_sentence) > 80:
            key_sentence = key_sentence[:77] + "..."
        summary_lines.append(f"주요 내용: {key_sentence}")
    elif all_actions:
        # 작업 기반 설명
        actions_desc = ', '.join(all_actions[:3])
        summary_lines.append(f"주요 작업으로는 {actions_desc} 등이 포함됩니다.")

    # 3줄: 영상 구성 (섹션 기반)
    if len(sections_list) > 3:
        # 실제 도구/작업 기반 구성 설명
        unique_tools = list(dict.fromkeys(all_tools[:4]))  # 중복 제거
        if unique_tools:
            summary_lines.append(
                f"총 {len(sections_list)}개 섹션으로 구성되어 있으며, "
                f"{', '.join(unique_tools[:2])} 등을 활용한 실습을 포함합니다."
            )
        else:
            summary_lines.append(
                f"총 {len(sections_list)}개 섹션으로 구성되어 있습니다."
            )

    summary = " ".join(summary_lines) if summary_lines else "요약 정보 없음"

    # === 개선된 핵심 포인트 생성 (실제 내용 기반) ===
    key_points = []
    used_topics = set()
    used_descriptions = set()  # 설명 중복 방지

    # 1. 도입부에서 추출된 주제를 최우선으로 사용
    if topic_info['main_topic']:
        main_topic = topic_info['main_topic']
        # 관련 설명 찾기 - main_topic 전용 문장 (sub_topic 포함 안 된 것)
        main_desc = None
        for sentence in meaningful_intro:
            # main_topic만 포함된 문장 우선 선택
            if main_topic in sentence:
                # 텍스트 정제 적용
                cleaned_sentence = clean_subtitle_text(sentence)
                # 구어체/의미없는 문장 스킵
                if is_meaningless_sentence(cleaned_sentence):
                    continue
                # 다른 sub_topics가 없는 문장 선호
                if not any(sub in sentence for sub in topic_info['sub_topics'][:3]):
                    main_desc = cleaned_sentence[:80] + "..." if len(cleaned_sentence) > 80 else cleaned_sentence
                    break
        # 없으면 main_topic 포함 문장 사용
        if not main_desc:
            for sentence in meaningful_intro:
                if main_topic in sentence:
                    # 텍스트 정제 적용
                    cleaned_sentence = clean_subtitle_text(sentence)
                    # 구어체/의미없는 문장 스킵
                    if is_meaningless_sentence(cleaned_sentence):
                        continue
                    main_desc = cleaned_sentence[:80] + "..." if len(cleaned_sentence) > 80 else cleaned_sentence
                    break

        if not main_desc:
            # 다양한 fallback 설명 생성
            main_desc = generate_diverse_fallback_description(
                main_topic, topic_type='general', context_text=intro_text, index=0
            )

        key_points.append(f"- **{main_topic}**: {main_desc}")
        used_topics.add(main_topic)
        used_descriptions.add(main_desc[:50])  # 설명 일부만 저장 (비교용)

    # 2. 부가 주제들 추가
    for idx, sub_topic in enumerate(topic_info['sub_topics'][:3]):
        if len(key_points) >= 6:
            break
        if sub_topic in used_topics:
            continue

        # 해당 주제 관련 문장 찾기 (해당 토픽 전용 섹션에서)
        sub_desc = None
        for section in sections_list:
            section_text = section.get('full_text', '')
            if sub_topic.lower() in section_text.lower():
                # 해당 섹션에서 의미있는 문장 추출 (토픽 키워드 포함)
                section_sentences = extract_meaningful_sentences(
                    section_text, max_sentences=5, topic_keywords=[sub_topic]
                )
                # 중복되지 않은 문장 선택
                for sent in section_sentences:
                    # 텍스트 정제 적용
                    cleaned_sent = clean_subtitle_text(sent)
                    # 구어체/의미없는 문장 스킵
                    if is_meaningless_sentence(cleaned_sent):
                        continue
                    sent_key = cleaned_sent[:50]  # 비교용 키
                    if sent_key not in used_descriptions:
                        sub_desc = cleaned_sent[:80] + "..." if len(cleaned_sent) > 80 else cleaned_sent
                        used_descriptions.add(sent_key)
                        break
                if sub_desc:
                    break

        # 설명을 못 찾았거나 중복이면 다양한 fallback 사용
        if not sub_desc:
            sub_desc = generate_diverse_fallback_description(
                sub_topic, topic_type='general', context_text=full_text, index=len(key_points) + idx
            )

        key_points.append(f"- **{sub_topic}**: {sub_desc}")
        used_topics.add(sub_topic)

    # 3. 도구 기반 핵심 포인트 (중복되지 않는 것만)
    for tool in all_tools:
        if len(key_points) >= 6:
            break
        if tool in used_topics:
            continue

        # 도구 관련 작업 찾기
        tool_actions = []
        for section in sections_list:
            section_text = section.get('full_text', '')
            if tool.lower() in section_text.lower() or tool in section_text:
                section_actions = extract_specific_actions(section_text)
                tool_actions.extend(section_actions)
                break

        if tool_actions:
            description = f"{tool}을 사용하여 {tool_actions[0]} 진행"
        elif all_actions:
            description = f"{tool} 활용 및 {all_actions[0]} 작업"
        else:
            description = f"{tool} 설정 및 활용 방법 안내"

        key_points.append(f"- **{tool} 활용**: {description}")
        used_topics.add(tool)

    # 4. 작업 기반 핵심 포인트 (부족하면 추가)
    if len(key_points) < 4:
        for action in all_actions:
            if len(key_points) >= 6:
                break
            if action in used_topics:
                continue

            # 해당 작업 관련 문장 찾기
            action_desc = None
            for section in sections_list:
                section_text = section.get('full_text', '')
                if action in section_text:
                    section_sentences = extract_meaningful_sentences(section_text, max_sentences=1)
                    if section_sentences:
                        action_desc = section_sentences[0][:80] + "..." if len(section_sentences[0]) > 80 else section_sentences[0]
                    break

            if not action_desc:
                # 다양한 fallback 설명 생성 (action 유형)
                action_desc = generate_diverse_fallback_description(
                    action, topic_type='action', context_text=full_text, index=len(key_points)
                )

            key_points.append(f"- **{action}**: {action_desc}")
            used_topics.add(action)

    # 5. 섹션 기반 보완 (여전히 부족하면)
    if len(key_points) < 4:
        for section in sections_list:
            if len(key_points) >= 6:
                break

            section_text = section.get('full_text', '')
            section_tools = extract_specific_tools(section_text)
            section_actions = extract_specific_actions(section_text)

            if section_tools and section_tools[0] not in used_topics:
                tool = section_tools[0]
                if section_actions:
                    desc = f"{tool}로 {section_actions[0]} 작업 진행"
                else:
                    desc = f"{tool} 활용 방법 안내"
                key_points.append(f"- **{tool} 활용**: {desc}")
                used_topics.add(tool)
            elif section_actions and section_actions[0] not in used_topics:
                action = section_actions[0]
                desc = f"{action} 과정 및 결과 설명"
                key_points.append(f"- **{action}**: {desc}")
                used_topics.add(action)

    # 핵심 포인트 6개로 제한
    key_points = key_points[:6]

    # === 주요 섹션 생성 (주제 기반 제목, 8개 제한) ===
    sections_text = ""
    section_count = 0
    for section in sections_list[:8]:  # 최대 8개 섹션으로 제한
        section_count += 1
        title = section['title']  # 이미 간조체로 생성됨
        time_range = section['time_range']

        sections_text += f"\n### 섹션 {section_count}: {title} ({time_range})\n"

        # 요약 불릿 표시 (간조체)
        if section.get('bullets'):
            for bullet in section['bullets']:
                sections_text += f"- {bullet}\n"
        else:
            sections_text += f"- 관련 내용 다룸\n"

    return {
        'summary': summary,
        'key_points': key_points,
        'sections': sections_text.strip()
    }


def summarize_with_claude(transcript_text, video_title="", api_key=None, transcript=None):
    """
    Claude API를 사용하여 자막 요약 (API 키 없으면 타임라인 기반 요약 사용)

    Args:
        transcript_text: 전체 자막 텍스트
        video_title: 영상 제목
        api_key: Claude API 키
        transcript: 자막 데이터 (타임라인 기반 요약용)

    Returns:
        dict: summary, key_points, sections
    """
    if not api_key:
        api_key = os.getenv('ANTHROPIC_API_KEY')

    if not api_key:
        print("\n[!] Claude API 키가 없습니다. 타임라인 기반 요약을 사용합니다.")
        if transcript:
            return summarize_from_timeline(transcript, video_title)
        else:
            return {
                'summary': "요약을 생성하려면 ANTHROPIC_API_KEY 환경변수를 설정하거나 자막 데이터를 제공하세요.",
                'key_points': ["요약 없음"],
                'sections': ""
            }

    try:
        from anthropic import Anthropic

        client = Anthropic(api_key=api_key)

        # 요약 프롬프트
        prompt = f"""다음은 YouTube 영상 "{video_title}"의 자막입니다.

자막 내용:
{transcript_text[:15000]}  # 처음 15000자만 사용

다음 형식으로 요약해주세요:

## 요약
(2-3문장으로 영상 전체 내용 요약)

## 핵심 포인트
- (핵심 포인트 1)
- (핵심 포인트 2)
- (핵심 포인트 3)
- ...

## 주요 섹션
### 섹션 1: [제목]
- (핵심 내용)

### 섹션 2: [제목]
- (핵심 내용)

...

모든 내용을 한국어로 작성하세요."""

        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result_text = response.content[0].text

        # 파싱 (간단한 방식)
        summary_match = re.search(r'## 요약\n(.+?)(?=\n## |\Z)', result_text, re.DOTALL)
        key_points_match = re.search(r'## 핵심 포인트\n(.+?)(?=\n## |\Z)', result_text, re.DOTALL)
        sections_match = re.search(r'## 주요 섹션\n(.+)', result_text, re.DOTALL)

        summary = summary_match.group(1).strip() if summary_match else "요약 없음"
        key_points_text = key_points_match.group(1).strip() if key_points_match else ""
        key_points = [line.strip() for line in key_points_text.split('\n') if line.strip().startswith('-')]

        sections_text = sections_match.group(1).strip() if sections_match else ""

        return {
            'summary': summary,
            'key_points': key_points,
            'sections': sections_text
        }

    except ImportError:
        print("\n[X] anthropic 라이브러리가 설치되지 않았습니다.")
        return {
            'summary': "Claude API를 사용하려면 anthropic 라이브러리를 설치하세요.",
            'key_points': ["요약 없음"],
            'sections': ""
        }
    except Exception as e:
        print(f"\n[X] 요약 생성 실패: {e}")
        return {
            'summary': "요약 생성 중 오류가 발생했습니다.",
            'key_points': ["요약 없음"],
            'sections': ""
        }


def generate_markdown(video_id, video_url, video_title, transcript, api_key=None):
    """
    마크다운 문서 생성

    Args:
        video_id: YouTube video ID
        video_url: YouTube URL
        video_title: 영상 제목
        transcript: 자막 데이터
        api_key: Claude API 키

    Returns:
        markdown_content: 마크다운 문서 내용
    """
    # 전체 자막 텍스트 생성
    full_text = " ".join([entry.text.strip() for entry in transcript])

    # Claude로 요약 생성 (또는 타임라인 기반)
    print("\n[Note] 영상 요약 중...")
    analysis = summarize_with_claude(full_text, video_title, api_key, transcript)

    # 타임라인 생성
    timeline = create_timeline(transcript)

    # 마크다운 템플릿
    today = datetime.now().strftime("%Y-%m-%d")

    markdown = f"""# {video_title}

**원본 영상**: [{video_url}]({video_url})
**작성일**: {today}
**Video ID**: {video_id}

---

## 요약

{analysis['summary']}

---

## 핵심 포인트

"""

    for point in analysis['key_points']:
        markdown += f"{point}\n"

    markdown += f"""
---

## 주요 내용

{analysis['sections']}

---

## 타임라인

{timeline}

---

## 전체 자막 (타임스탬프 포함)

"""

    # 전체 자막 추가
    for entry in transcript:
        timestamp = format_timestamp(entry.start)
        markdown += f"**[{timestamp}]** {entry.text.strip()}\n\n"

    markdown += f"""
---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
"""

    return markdown


def main():
    """메인 함수"""
    print("=" * 60)
    print("YouTube Transcript to Markdown Generator")
    print("=" * 60)

    if len(sys.argv) < 2:
        print("\n사용법: python md-generator.py <YouTube_URL> [제목]")
        print("\n예시:")
        print("  python md-generator.py https://www.youtube.com/watch?v=VIDEO_ID \"영상 제목\"")
        return

    url = sys.argv[1]
    video_id = extract_video_id(url)
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # 제목이 주어지지 않으면 Video ID 사용
    if len(sys.argv) >= 3:
        video_title = sys.argv[2]
    else:
        video_title = f"YouTube Video {video_id}"

    print(f"\n[Video] Video ID: {video_id}")
    print(f"        제목: {video_title}")

    # 자막 추출
    print("\n[Search] 자막 추출 중...")
    transcript = get_transcript(video_id)

    if not transcript:
        print("\n[X] 자막을 가져올 수 없습니다.")
        return

    print(f"[OK] 자막 추출 성공! (총 {len(list(transcript))} 세그먼트)")

    # 마크다운 생성
    print("\n[Note] 마크다운 생성 중...")
    markdown_content = generate_markdown(
        video_id=video_id,
        video_url=video_url,
        video_title=video_title,
        transcript=transcript,
        api_key=os.getenv('ANTHROPIC_API_KEY')
    )

    # 파일 저장
    output_dir = "outputs/markdown"
    os.makedirs(output_dir, exist_ok=True)

    # 안전한 파일명 생성
    safe_title = re.sub(r'[^\w\s-]', '', video_title).strip()
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    filename = f"{datetime.now().strftime('%Y%m%d')}_{safe_title}_{video_id}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"\n[OK] 마크다운 파일 저장: {filepath}")

    # 간단한 통계
    print(f"\n[Note] 통계:")
    print(f"        자막 길이: {len(list(transcript))} 세그먼트")
    print(f"        마크다운 크기: {len(markdown_content)} 글자")

    print("\n" + "=" * 60)
    print("[OK] 변환 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
