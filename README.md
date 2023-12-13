## 중앙대학교 예술공학과 오픈소스프로그래밍 [BCAA]팀 프로젝트


### 프로젝트 소개
> 프로젝트: PROTECT는 서울특별시, 경기도 및 한국환경공단 API 등의 오픈소스를 활용하여 제작한 기상정보 및 미세먼지 현황 조회 프로그램입니다. 

## 1. 팀 BCAA
> 팀장, 개발자: 예술공학부 23학번 이주형

## 2. 개발환경
> 파이썬을 이용하여 제작하였기에 실행환경에 파이썬 프로그램이 설치되어있어야 합니다. 설치주소: https://www.python.org/downloads/

## 3. 참고 레퍼런스
> 외부 환경공단 API
> 
> 오픈소스 프로젝트 pypubdata: https://github.com/gomgom/pypubdata


-----------------------------------------------------------------------------------


## 4. PROTECT 사용 전 설치
> 프로그램 다운로드 전 공공데이터 포탈에서 개인 API를 발급받으시는 것을 추천드립니다.
> pypubdata의 pdairp 패키지와 geopy를 사용하기 위해 다음과 같은 과정이 필요합니다.
```
For Windows: C:\Users\sample> pip install pypubdata
For Linux/Unix: sample@ip-123-12-3-45:~$ sudo pip3 install pypubdata
```
```
pip install pdarip
pip install geopy
```

## 5. PROTECT 사용법
```
채널 URL: http://pf.kakao.com/_TpExfG
채팅 URL: http://pf.kakao.com/_TpExfG/chat  
```
> 해당 URL를 입력하신 후 채널을 추가하신 뒤, 챗봇을 이용하시면 됩니다. 

> 현재 하나의 기능밖에 지원하지 않고 있습니다.

## 6. PROTECT 기능
> 미세먼지: 사용자가 원하는 지역을 검색하여 해당 지역에 대한 미세먼지 정보를 출력합니다.
