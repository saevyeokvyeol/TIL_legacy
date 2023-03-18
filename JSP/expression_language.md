# 표현언어(Expression Language: EL)

## 특징

- jsp 2.0부터 새롭게 추가된 스크립팅 요소
- 자바 객체와 속성값을 쉽게 가져올 수 있는 방법
- ${표현식 | 속성명.메소드} 형태로 사용함
- 표현식에는 정수형, 실수형, 문자열형, 논리형, null이 올 수 있으며 연산이 가능함

## 연산자

```html
<!-- 산술 연산자 -->

${A + B}
<!-- A와 B를 더함 -->

${A - B}
<!-- A에서 B를 뺌 -->

${A * B}
<!-- A와 B를 곱함 -->

${A / | div B}
<!-- A를 B로 나눔 -->

${A % | mod B}
<!-- A를 B로 나눈 나머지 -->
```

```html
<!-- 문자열 연결 -->

${문자열.concat("문자열")}
<!-- +로 문자열을 연결할 경우 NumberFormatException -->
```

```html
<!-- 산술 연산자 -->

${A == | eq B}
<!-- A와 B가 같으면 true -->

${A != | ne B}
<!-- A와 B가 다르면 true -->

${A > | gt B}
<!-- A보다 B가 작으면 true -->

${A < | lt B}
<!-- A보다 B가 크면 true -->

${A >= | ge B}
<!-- A보다 B가 작거나 같으면 true -->

${A <= | le B}
<!-- A보다 B가 크거나 같으면 true -->
```

```html
<!-- 삼항 연산자(조건 연산자) -->

${조건식 ? 참 : 거짓}
```

```html
<!-- 논리 연산자 -->

${A && | and B}
<!-- A와 B 둘 다 true면 true -->

${A || | or B}
<!-- A와 B 둘 중 하나가 true면 true -->

${! | not A}
<!-- A가 true면 false, false면 true-->
```

## 값 가져오기

```html
${pageScope.name값}
<!-- page 기본 객체에 저장된 속성 가져오기 -->

${requestScope.name값}
<!-- request 기본 객체에 저장된 속성 가져오기 -->

${sessionScope.name값}
<!-- session 기본 객체에 저장된 속성 가져오기 -->

${applicationScope.name값}
<!-- application 기본 객체에 저장된 속성 가져오기 -->

<!--
	xxxScope 생략하고 name값만 써도 속성값 호출 가능
	이 경우 우선순위(pageScope < requestScope < sessionScope < applicationScope)가 높은 속성이 호출됨
-->
```

```html
<!-- param 가져오기 -->

${param.name값}
<!-- request.getParameter("name값"); -->
```

## 메소드 호출

```html
<!-- 객체 생성 -->
<jsp:useBean id="객체명" class="클래스 경로"></jsp:useBean>
<jsp:useBean id="객체명" class="클래스 경로"/>
```

```html
${객체명.변수명}
<!-- 객체 내의 get변수명()(=getter) 메소드를 호출 -->
```

## 주요 메소드

- 경로 출력
    
    ```html
    ${pageContext.request.contextPath}
    
    <!-- a태그 등에서 경로 앞에 붙여 경로가 엉키는 것을 방지함 -->
    ```