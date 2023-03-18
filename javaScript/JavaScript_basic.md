# JavaScript

## 특징

- 자바의 문법과 비슷한 부분이 많음
- 객체 기반의 언어로 객체(Object) 개념이 있음
- 이미 정의되어 호출하면 사용할 수 있는 내장 객체가 존재
- 속성, 메소드 개념이 있어 객체명.속성명 or 객체명.메소드명()의 방식으로 호출할 수 있음
- new 키워드를 이용해 새로운 객체를 생성할 수 있음
- this 키워드를 통해 현재 객체 안의 속성과 메소드에 접근할 수 있음

### Web FrontEnd로써
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

## 적용 방법

### 인라인

```html
<element onclick="">content</element>
<!--
	요소에 직접 입력하는 방식
	동작에 맞춰 CSS를 바꾸는 등의 간단한 것만 가능함
-->
```

### 내부 자바스크립트 코드

```html
<script type="text/javascript">
	document.write("<h1 style="color=blue">내부 자바스크립트 코드</h1>");
<script>
<!--
	HTML의 script 태그 안에 코드를 입력하는 방식
	script 태그 안에 HTML과 CSS 모두 사용 가능
-->
```

### 외부 자바스크립트 코드

```html
<!-- HTML -->
<script type="text/javascript" scr="JS 파일 경로">
	<!-- 내부에 입력X: 입력해도 적용안됨 -->
<script>
```

```jsx
/* JavaScript */
<element onclick="">content</element>

/* 	외부 JS파일을 가져오는 방식 */
```