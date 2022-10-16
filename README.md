# IITP 크롤러

뉴스 기사를 크롤링하는 프로그램입니다.
bloomberg.com, investing.com, mining.com 3가지 사이트에 대한 크롤러입니다.

## 설치법

1. [Python 3.9](https://www.python.org/downloads/release/python-3913/) 설치

2. [Playwright](https://playwright.dev/python/docs/library) 설치

3. 라이브러리 다운로드 및 디펜던시 설치\
   cmd 실행 및 콘솔창 입력

```
git clone "https://github.com/kimjaewon96/iitp-crawl"
pip install requirements.txt
```

4. 실행\
   각 크롤러에 맞게 명령줄을 입력

## Bloomberg 크롤러

지정한 연도-달의 모든 Bloomberg 뉴스 기사를 수집하여 json 파일로 결과를 저장합니다.

## 실행법

type: 'bloomberg'\
date: 크롤링을 진행할 연도와 달은 20xx-xx 형식으로 입력

예시: 2022년 9월 기사 크롤링을 진행하려면 다음과 같이 입력

```
pip main.py --type bloomberg --date 2022-09
```

### 데이터 형식

title: 제목\
title_sub: 부제목\
point1, point2: 소제목\
date: 기사 날짜\
category: 기사 대분류\
category_sub: 기사 소분류\
body: 기사 텍스트

### 데이터 예시

![블룸버그 데이터 예시](bloomberg_df.png "블룸버그 데이터 예시")

만일 데이터 다운로드가 잘 이뤄지지 않는다면, [1.1.1.1 WARP](https://1.1.1.1) 등의 VPN 서비스를 사용하세요.

## Investing 크롤러

지정한 페이지까지의 copper 관련 모든 investing.com 뉴스 기사를 수집하여 json 파일로 결과를 저장합니다.

## 실행법

type: 'investing'\
page: 크롤링을 진행할 페이지 수를 지정

예시: 1 ~ 30 페이지까지 크롤링을 진행하려면

```
pip main.py --type investing --page 30
```

### 데이터 형식

title: 제목\
date: 기사 날짜\
body: 기사 텍스트

### 데이터 예시

![인베스팅 데이터 예시](investing_df.png "인베스팅 데이터 예시")

## Mining 크롤러

지정한 페이지까지의 copper 관련 모든 mining.com 뉴스 기사를 수집하여 json 파일로 결과를 저장합니다.

## 실행법

type: 'mining'\
page: 크롤링을 진행할 페이지 수를 지정

예시: 1 ~ 30 페이지까지 크롤링을 진행하려면

```
pip main.py --type mining --page 30
```

### 데이터 형식

title: 제목\
date: 기사 날짜\
body: 기사 텍스트

### 데이터 예시

![마이닝 데이터 예시](mining_df.png "마이닝 데이터 예시")
