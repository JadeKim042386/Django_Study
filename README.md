목차
=====
[1. What is Django?](#What-is-Django?)  
[2. Django vs Flask](#Django-vs-Flask)  
[3. 장고 개발 환경 준비](#장고-개발-환경-준비)  
## Wiki  
### 기본 요소
[1. URL과 View](https://github.com/JadeKim042386/Django_Study/wiki/URL%EA%B3%BC-View)  
[2. Model](https://github.com/JadeKim042386/Django_Study/wiki/Model)  
[3. Admin](https://github.com/JadeKim042386/Django_Study/wiki/Admin)  
[4. Question list & detail 구현](https://github.com/JadeKim042386/Django_Study/wiki/Question-list-&-detail-%EA%B5%AC%ED%98%84)  
[5. Remove URL hard coding](https://github.com/JadeKim042386/Django_Study/wiki/Remove-URL-hard-coding)  
[6. Create Answer](https://github.com/JadeKim042386/Django_Study/wiki/Create-Answer)  
[7. CSS 파일 적용](https://github.com/JadeKim042386/Django_Study/wiki/CSS-%ED%8C%8C%EC%9D%BC-%EC%A0%81%EC%9A%A9)  
[8. Bootstrap](https://github.com/JadeKim042386/Django_Study/wiki/Bootstrap)  
[9. 표준 HTML](https://github.com/JadeKim042386/Django_Study/wiki/%ED%91%9C%EC%A4%80-HTML)  
[10. question create 구현 & form 적용](https://github.com/JadeKim042386/Django_Study/wiki/question-create-&-form-%EA%B5%AC%ED%98%84) 
### 서비스 개발  
[1. 내비게이션 기능 & include 기능](https://github.com/JadeKim042386/Django_Study/wiki/Add-navbar(%EB%82%B4%EB%B9%84%EA%B2%8C%EC%9D%B4%EC%85%98-%EA%B8%B0%EB%8A%A5)-&-include)  
[2. Pagination](https://github.com/JadeKim042386/Django_Study/wiki/Pagination)  
[3. Template Filter](https://github.com/JadeKim042386/Django_Study/wiki/Template-Filter)  
[4. Answer Count Marking](https://github.com/JadeKim042386/Django_Study/wiki/answer-count-marking)  
[5. login & logout](https://github.com/JadeKim042386/Django_Study/wiki/Implement-login-&-logout)

[출처](#출처)  


# What is Django?

  1. 장고는 웹 프로그램을 쉽고 빠르게 만들어 주는 웹 프레임워크다.
  
  예를 들어 쿠키나 세션 처리, 로그인/로그아웃 처리, 권한 처리, 데이터베이스 처리 등 웹 프로그램을 위해 만들어야 할 기능이 정말 산더미처럼 많다.
  하지만 웹 프레임워크를 사용하면 이런 기능들을 여러분이 일일이 만들 필요가 없다. 왜냐하면 웹 프레임워크에는 그런 기능들이 이미 만들어져 있기 때문이다. 
  그저 웹 프레임워크에 있는 기능을 익혀서 사용하기만 하면 된다. 쉽게 말해 웹 프레임워크는 웹 프로그램을 만들기 위한 스타터 키트라고 생각하면 된다. 
  그리고 파이썬으로 만들어진 웹 프레임워크 중 하나가 바로 장고이다.
  
  2. 장고는 튼튼한 웹 프레임워크이다
  
  개발자가 웹 프로그램을 만들 때 가장 어렵게 느끼는 기능 중 하나는 바로 보안 기능이다. 이 세상에는 기상천외한 방법으로 웹 사이트를 괴롭히는 사람들이 있다.
  이런 공격에 개발자 홀로 신속하게 대응하기는 무척 어려운 일이다. 하지만 걱정하지 마라. 장고는 이런 보안 공격을 기본으로 아주 잘 막아 준다.
  그만큼 장고는 튼튼한 웹 프레임워크다. 예를 들어 SQL 인젝션, XSS(cross-site scripting), CSRF(cross-site request forgery), 클릭재킹(clickjacking)과 같은
  보안 공격을 기본으로 막아 준다. 즉, 장고를 사용하면 이런 보안 공격에 대한 코드를 여러분이 짤 필요가 없다.
  
  + Note
    - SQL 인젝션은 악의적인 SQL을 주입하여 공격하는 방법이다.
    - XSS는 자바스크립트를 삽입해 공격하는 방법이다.
    - CSRF는 위조된 요청을 보내는 공격 방법이다.
    - 클릭재킹은 사용자의 의도하지 않은 클릭을 유도하는 공격 방법이다.
    
   3. 장고에는 여러 기능이 준비되어 있다
   
   장고는 2005년에 등장하여 10년 이상의 세월을 감내한 베테랑 웹 프레임워크이다. 그동안 정말 무수히 많은 기능이 추가되고 또 다듬어졌다. 혹시 로그인 기능을
   원하는가? 관리자 기능을 원하는가? 이미 장고에 있다. 이미 있을 뿐 아니라 너무나도 잘 만들어져 있다. 한마디로 장고에는 여러분이 필요로 하는 웹 프로그램 개발을
   위한 도구와 기능이 대부분 준비되어 있다. 필자는 장고를 공부할 여러분에게 '이미 만들어져 있는 기능을 새로 만드느라 애써 고생하지 말라'는 이야기를 꼭 해 주고
   싶다.
   
   4. 장고의 구조
   
   
      ![Django Architecture](https://mdn.mozillademos.org/files/13931/basic-django.png)
  
  
  - URLs: 단일 함수를 통해 모든 URL 요청을 처리하는 것이 가능하지만, 분리된 뷰 함수를 작성하는 것이 각각의 리소스를 유지보수하기 훨씬 쉽습니다. 
  URL mapper는 요청 URL을 기준으로 HTTP 요청을 적절한 뷰(view)로 보내주기 위해 사용됩니다. 또한 URL mapper는 URL에 나타나는 특정한 문자열이나 
  숫자의 패턴을 일치시켜 데이터로서 뷰 함수에 전달할 수 있습니다.
  
  - View: 뷰는 HTTP 요청을 수신하고 HTTP 응답을 반환하는 요청 처리 함수입니다. 뷰는 Model을 통해 요청을 충족시키는데 필요한 데이터에 접근합니다.
  그리고 탬플릿에게 응답의 서식 설정을 맡깁니다.
  
  - Models: 모델은 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)하고 쿼리하는 방법을 제공하는 파이썬 객체입니다.
  
  - Templates: 탬플릿은 파일의 구조나 레이아웃을 정의하고(예: HTML 페이지), 실제 내용을 보여주는 데 사용되는 플레이스홀더를 가진 텍스트 파일입니다.
  뷰는 HTML 탬플릿을 이용하여 동적으로 HTML 페이지를 만들고 모델에서 가져온 데이터로 채웁니다. 탬플릿으로 모든 파일의 구조를 정의할 수 있습니다.
  탬플릿이 꼭 HTML 타입일 필요는 없습니다!
  
    Note: 장고는 이 구조를 "모델 뷰 템플릿(Model View Template)(MVT)" 아키텍처라고 부릅니다. 이것은 더 익숙한 Model View Controller 아키텍처와
    많은 유사점을 가지고 있습니다.
  
      ![Django Diagram](https://w.namu.la/s/dea675fca9120cdee8331049e318113fd8b7e1b72b75cbc46854b809784a73c434e9b9abe59be0a41f1b59ace410fc7247db918a595ef5b804799c0bdfedf865e7ea11e1b1044d40ff0fae41a3f27036482abdfe1801a3873cf8f18b2f425f1a)
  
  - Django의 동작 순서 예시
  
    1. 사용자가 1번 강의를 보겠다고 요청을 보냄 (URL 주소 입력)
    2. View (중간관리자)는 받은 요청을 확인하고, Model (데이터 관리)에 1번강의를 찾아달라고 지시를 내림
    3. Model (데이터 관리)은 Database에서 1번 강의를 찾아서 View (중간관리자)에 전달
    4. View (중간관리자)는 1번강의를 Template에 전달하여, HTML 파일과 조합하여 화면을 사용자에게 전달
    
# Django vs Flask

Python에서 django와 Flask는 가장 널리 사용되는 오픈소스 기반 웹 프레임워크입니다.  
django는 Python의 full stack web framework인 반면 Flask는 가볍고 확장 가능한 web framework입니다. 즉 django는 기능이 훨씬 뛰어나지만 복
잡하고, Flask는 매우 단순하고 가볍습니다.

## Django

django는 python기반 web framework 중 가장 많이 사용되고 있는 web framework이며, Flask보다 약 10배 많은 코드 라인으로 개발이 되어있습니다. (code 290,087 
lines) 구글 앱 엔진에서 django를 사용하게 되면서 많은 사람들이 사용하게 되었으며, web application을 개발하기 위한 대부분의 기능들이 갖추어져 있기 때문에 외
부 도구 및 라이브러리를 사용하지 않고도 어느 정도 규모가 있는 web application 개발에도 문제가 없습니다.  

django는 ORM (Object relational mapping) 기능이 내장되어있습니다.  
객체 관계 매핑이라고도 하며 데이터베이스 시스템과 데이터 모델 클래스를 연결하는 역할을 합니다.  
ORM을 이용해 다양한 데이터베이스를 지원하고 있으며, SQL 의존적인 코드를 벗어나 생산적인 코딩이 가능하게 되어 유지보수가 편하게 됩니다.  

django는 자동으로 관리자 화면을 구성해줍니다.  
django는 데이터베이스에 대한 관리 기능을 위하여 프로젝트를 시작하는 시점에 관리자 화면을 제공합니다. 이런 관리자 화면을 이용하여 web application에서 사용하는 
데이터들을 쉽게 생성하거나 변경이 가능합니다.  

# Flask

Flask는 Python의 Micro framework를 기반으로 단순하고 매우 가벼운 web framework입니다.  
URL 라우팅, Template, Cookie, Debugger 및 개발서버 등 기본 기능만을 제공합니다.  
그러기 때문에 django의 1/10밖에 안 되는 코드 (code 28,677 lines)로 구현되어있으며, 직접 소스코드를 분석하여 내부적으로 일어나는 확인할 수 있으며 권장되고 있습니다.  
Flask의 구조는 크게 WSGI용 Library인 Werkzeug와 HTML 렌더링 엔진인 Jinja2 template으로 구성되어있습니다.  
즉 Flask는 기본 기능 제공에 다양한 확장 모듈을 이용할 수 있는 구조 입니다.  
django에서는 특수한경우 내부 로직에서 어떠한 기능을 지원하지 않거나 장애가 발생했을 때 이를 해결하기위해 큰 비용이 들게되지만 Flask는 정해진 확장 모듈이 없기
때문에 다양한 방법으로 해결이 가능합니다.  

Flask는 단 10줄도 안되는 코드로 웹 서버를 구동할 수 있습니다.  
from flask import Flask 를 시작으로 서버를 시작하는 코드까지 10줄이 되지 않습니다.  
물론 그만큼 최소한의 패키지로 구성되어있기때문에 Hello World는 간단히 구현 되지만, 상용 웹 서버를 구현할때는 단순하지만은 않습니다.  

Flask에는 ORM (Object relational mapping) 기능이 제공되지 않습니다.  
그렇기 때문에 개발자가 직접 SQLAlchemy 등 개발자에게 편하거나 익숙한 패키지를 설치하여 사용할 수 있습니다.  
위에서 언급한대로 Flask는 최소한의 기능만을 제공합니다. 데이터 베이스 연결 외에도 양식 처리, 보안, 인증 등 모두 개발자가 직접 처리해주어야 합니다.  
즉, django에서는 탄탄한 framework 안에서 다른 설계 패턴으로 벗어날 수 없다는 점을 Flask에서는 직접 새로운 framework로 설계할 수 있다는 장점이 있지만 이제 막 
파이썬 웹 프레임워크에 진입하는 입장에서는 신경써야할게 한두가지가 아니기때문에 최대 단점으로 다가올 수 있습니다.  

[Google Trends에서의 Django와 Flask 비교](https://trends.google.com/trends/explore?q=Django,Flask)

Note: [ORM 이란?](https://gmlwjd9405.github.io/2019/02/01/orm.html)

# 장고 개발 환경 준비

## 가상 환경 사용
파이썬 가상 환경은 파이썬 프로젝트를 진행할 때 독립된 환경을 만들어 주는 고마운 도구다. 예를 들어 파이썬 개발자 A가 2개의 파이썬 프로젝트를 개발하고 관리한다고 가정하자. 파이썬 프로젝트를 각각 P-1, P-2라고 부르겠다. 이때 P-1, P-2에 필요한 파이썬 또는 파이썬 라이브러리의 버전이 다를 수 있다. 이를테면 P-1에는 파이썬 2.7 버전이, P-2에는 파이썬 3.8 버전이 필요할 수 있다. 이때 하나의 데스크톱에 서로 다른 버전의 파이썬을 설치해야 하는 문제가 생긴다. 이처럼 가상 환경을 이용하면 하나의 데스크톱에 서로 다른 버전의 파이썬과 라이브러리를 쉽게 설치해 사용할 수 있다.  
### 가상 환경 Directory 생성
```
C:\Users\pahkey> cd \
C:\> mkdir venvs
C:\> cd venvs
```

### 가상 환경 만들기
```
C:\venvs> python -m venv mysite
```
venv : python Module  
mysite : 가상 환경 이름

### 가상 환경 진입 & 탈출
```
#진입
C:\venvs>cd C:\venvs\mysite\Scripts
C:\venvs\mysite\Scripts> activate
(mysite) C:\venvs\mysite\Scripts>

#탈출
(mysite) C:\venvs\mysite\Scripts> deactivate
```

### 장고 설치
만들어진 가상 환경 mysite에 장고를 설치한다.
```
C:\venvs\mysite\Scripts> activate
(mysite) C:\venvs\mysite\Scripts> pip install django==3.1.3
(mysite) C:\venvs\mysite\Scripts> python -m pip install --upgrade pip
```
(업데이트 실습을 위해 3.1.3으로 설치 후 최신 버전으로 업데이트)

### Root Directory 생성
장고 프로젝트는 여러 개가 될 수 있으므로 프로젝트를 모아 둘 프로젝트 루트 디렉터리 생성은 필수다.
```
C:\Users\pahke>cd \
C:\>mkdir projects
C:\>cd projects
C:\projects>
```

### Django Project 생성
```
C:\projects>C:\venvs\mysite\Scripts\activate
(mysite) C:\projects>mkdir mysite
(mysite) C:\projects>cd mysite
(mysite) C:\projects\mysite>django-admin startproject config .
```
가상 환경 진입 -> mysite Directory 생성 -> mysite Directory 이동 -> 현재 Directory를 Project Directory로 만듬

생성 후 Directory 구조
```
C:\projects\mysite
├── config/
│      ├─ asgi.py
│      ├─ settings.py
│      ├─ urls.py
│      ├─ wsgi.py
│      └─ __init__.py
└── manage.py
```

### 개발 서버 구동
```
(mysite) C:\projects\mysite>python manage.py runserver
```
<Ctrl + C> : Exit

### 배치 파일을 사용한 가상 환경 진입
메모장에 다음과 같이 작성하여 mysite.cmd로 저장한다.
```
@echo off
cd c:/projects/mysite
c:/venvs/mysite/scripts/activate
```

PATH 환경 변수 추가  
![환경 변수 1](https://wikidocs.net/images/page/72377/1-04_4.png)  
![환경 변수 2](https://wikidocs.net/images/page/72377/1-04_5.png)  
![환경 변수 3](https://wikidocs.net/images/page/72377/1-04_7.png)  

환경 변수 확인 후 진입
```
C:\Users\pahkey>set path
C:\Users\pahkey> mysite
(mysite) C:\projects\mysite>
```

### Pycharm Setting
![envset1](https://wikidocs.net/images/page/72407/1-05_7.png)  
![envset2](https://wikidocs.net/images/page/72407/1-05_8.png)  
![envset3](https://wikidocs.net/images/page/72407/1-05_9.png)  

  *settings.py 파일 수정
  ./config/settings.py
  ```
  (... 생략 ...)
  # ---------------------------------- [edit] ---------------------------------- #
  LANGUAGE_CODE = 'ko-kr'

  TIME_ZONE = 'Asia/Seoul'
  # ---------------------------------------------------------------------------- #
  (... 생략 ...)
  ```

# 출처

[점프 투 장고](https://wikidocs.net/78004)  
[mozilla_Django 소개](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#%EC%9A%94%EC%B2%AD%EC%9D%84_%EC%95%8C%EB%A7%9E%EC%9D%80_%EB%B7%B0%EB%A1%9C_%EC%A0%84%EB%8B%AC_urls.py)  
[Django 01 - Introduction, 동작원리, 기본설정](https://tothefullest08.github.io/django/2019/02/11/django01/)  
[Python django vs Flask. web framework 무엇을 선택해야할까?](https://wendys.tistory.com/172)
