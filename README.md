# IITP 크롤러

bloomberg.com, investing.com, mining.com 뉴스 기사를 크롤링하는 python code입니다.

## 설치법

1. [Python 3.9](https://www.python.org/downloads/release/python-3913/) 설치

2. [Playwright](https://playwright.dev/python/docs/library) 설치

3. 라이브러리 다운로드 및 디펜던시 설치\
   cmd 실행 및 콘솔창 입력

```
git clone "https://github.com/kimjaewon96/iitp-crawl"
pip install -r requirements.txt
```

4. 실행\
   각 크롤러에 맞게 명령줄을 입력

##(1) Bloomberg 크롤러

지정한 연도-달의 모든 Bloomberg 뉴스 기사를 수집하여 bloomberg_crawl.json 파일로 결과를 저장

## 실행법

type: 'bloomberg'\
date: 크롤링을 진행할 연도와 달은 20xx-xx 형식으로 입력

예시: bloomberg.com 2022년 9월 기사 크롤링을 진행하려면 다음과 같이 입력

```
python main.py --type bloomberg --date 2022-09
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
![bloomberg_df](https://user-images.githubusercontent.com/101622378/196018537-9bc0c224-5d01-4259-b673-c45d830d0fa7.PNG)

※ 만일 기사 크롤링이 잘 진행되지 않는다면, [1.1.1.1 WARP](https://1.1.1.1) 등의 VPN 서비스를 사용을 추천

##(2) Investing 크롤러

지정한 페이지까지의 copper 관련 모든 investing.com 뉴스 기사를 수집하여 investing_crawl.json 파일로 결과를 저장

## 실행법

type: 'investing'\
page: 크롤링을 진행할 페이지 수를 지정

예시: 1 ~ 30 페이지까지 investing.com 크롤링을 진행하려면

```
python main.py --type investing --page 30
```

### 데이터 형식

title: 제목\
date: 기사 날짜\
body: 기사 텍스트

### 데이터 예시
![investing_df](https://user-images.githubusercontent.com/101622378/196018541-fd4c0e92-9620-42db-92ab-c81169821314.PNG)

## (3) Mining 크롤러

지정한 페이지까지의 copper 관련 모든 mining.com 뉴스 기사를 수집하여 mining_crawl.json 파일로 결과를 저장

## 실행법

type: 'mining'\
page: 크롤링을 진행할 페이지 수를 지정

예시: 1 ~ 30 페이지까지 mining.com 크롤링을 진행하려면

```
python main.py --type mining --page 30
```

### 데이터 형식

title: 제목\
date: 기사 날짜\
body: 기사 텍스트

### 데이터 예시
![mining_df](https://user-images.githubusercontent.com/101622378/196018547-4733b124-a88d-44f7-b6fc-bdc8456902ec.PNG)
