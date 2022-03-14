# Web FrontEnd

## 언어

### HTML

- Hyper Text Markup Language
- 화면 구성=구조=GUI를 담당: 주로 사용자 입력값을 받는 폼이나 사용자가 요청한 결과를 화면에 출력
- 현재는 HTML5 사용
: 다양한 API 제공(WabStorage, Drag&Drop, Audio, Video, WebSocket) → API이기 때문에 HTML, CSS, JS를 모두 알아야 함
- 대소문자를 구분하지 않고 오타가 있어도 오류가 발생하지 않음(적용되지 않은 채로 실행)

### CSS

- Cascading Style Sheets
- HTML에 디자인(화면 레이아웃)을 추가함
- 과거에는 플래시와 포토샵을 이용해 화면 구성을 시각적으로 풍부하게 만들었지만 현재는 CSS로 대부분 가능함
- 현재는 CSS3 사용
: 대소문자를 가림
  오타가 있어도 오류가 발생하지 않음(적용되지 않은 채로 실행)

### Java Script

- HTML에 기능을 부여해 Event를 처리(=동작)함
- 대소문자를 완벽하게 구분함
- 자바와 비슷한 개념: 객체 기반의 언어
- 인터프리터 언어: 실행하기 전에 한 줄씩 해석하고 오류를 보여주는 방식으로 오류 메세지가 차례대로 출력됨
- JS 관련
    - MEAN stack 개발: JS만을 사용해 전체 웹 프로그램을 개발하는 것
        1. Mongo DB: DB
        2. Express JS: Angular와 Node를 연결시키는 Controller
        3. Angular JS: View
        4. Node JS: BackEnd
    - JS기반 lib 언어가 등장: Framework(Model + View + ViewModel = MVVM구조)
        1. Angular1 → Angular2: 구글 + 개별 커뮤니티에서 제작
        2. React.js: 페이스북에서 제작
        3. Vue.js: Evan You가 제작

### 특징

- 웹 브라우저를 구성하는 언어이자 웹 브라우저가 해석할 수 있는 언어들
- 소스가 100% 공개됨
- CS(Client Side) 언어
: 클라이언트가 가지고 있는 브라우저에서 실행되는 언어로 같은 소스라도 브라우저마다 해석하는 방법이 달라 실행 결과가 달라질 수 있음
  이를 해결하기 위해 요즘은 JS기반의 라이브러리를 제공(jQuery 등)
- DB 연동 기능 없음(영속성의 문제)
HTML로 사용자가 입력한 값을 back단으로 전송할 수 있지만 페이지가 바뀌면 그 값을 받을 수 없음
웹은 페이지를 이동할 때마다 새로운 요청(request, response)이 되는 것으로 상태 정보를 유지할 수 없다
→ 때문에 웹사이트를 구축할 때는 BackEnd 기술 언어와 함께 구축해야 함(Servlet&JSP or asp or php)
- Static Wab Application: HTML, CSS, JS로 이루어진 프로그램
Dynamic Wab Application: HTML, CSS, JS + BackEnd 언어로 이루어진 프로그램

# Web BackEnd

## Java EE

> 웹 브라우저는 HTML, CSS, JS 이외의 언어를 해석할 수 없기 때문에 WebServer + WebApplication Server = WebContainer 필요
> 
- Servlet & JSP
JSP는 HTML, CSS, JS를 작성해 View의 역할을 하고, Servlet은 Controller의 역할을 함
- ASP
- PHP
- 위에 JavaSE를 통해 만든 Model을 합쳐 MVC구조의 Dynamic Wab Application 제작

# AJax기술

- 비동기화 통신
- 화면의 새로고침 없이 서버와 통신해 결과를 받아 화면의 일부분만 갱신(update) 해주는 것
- JS + XML을 사용하는 기술이었지만 요즘은 jQuery와 JSON을 사용
    - HTML과 XML
        - HTML: 이미 DTD에 의해 정의되어 있는 태그만 사용 가능
        - XML: 필요한 태그를 DTD에 선언해 사용 가능
                 서로 다른 언어 사이에서 데이터를 주고받을 때 데이터 포맷 형태로 많이 사용