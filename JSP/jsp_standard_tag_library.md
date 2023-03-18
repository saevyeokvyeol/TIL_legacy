# jsp Standard Tag Library

## 특징

- jsp 2.0부터 새롭게 추가된 스크립팅 요소
- 자바 객체와 속성값을 쉽게 가져올 수 있는 방법
- ${표현식 | 속성명.메소드} 형태로 사용함
- 표현식에는 정수형, 실수형, 문자열형, 논리형, null이 올 수 있으며 연산이 가능함

## 주요 JSTL 태그

### 문자 출력
    
```html
<%@ taglib uri="http://java.sun.com/jsp/jstl/core"  prefix="c"%>

<c:out value"값 | 변수명"></c:out>
<c:out value"값 | 변수명" excapeXml="true | false"/>
<!-- excapeXml값이 true(기본값)일 경우 값에 태그가 있으면 문자로 출력됨 -->
```
    
### 변수 선언 및 삭제
    
```html
<%@ taglib uri="http://java.sun.com/jsp/jstl/core"  prefix="c"%>

<!-- 변수 선언 -->
<c:set var="변수명" value="값"></c:set>
<c:set var="변수명" value="값" scope="page|request|session|application"/>
<!-- scope값을 입력하면 해당 scope에 저장됨 -->

<!-- 변수 삭제 -->
<c:set var="변수명"></c:set>
<c:set var="변수명"/>
```
    
### 조건문
    
```html
<%@ taglib uri="http://java.sun.com/jsp/jstl/core"  prefix="c"%>

<!-- if -->
<c:if test="${ 조건식 }" var="결과를 저장할 변수명">
    실행문
</c:if>
<!-- var에 변수명을 입력하면 해당 변수에 조건식의 결과값이 저장됨 -->

<!-- choose -->
<c:choose>
    <c:when test="${ 조건식1 }">
        실행문1
    </c:when>
    <c:when test="${ 조건식2 }">
        실행문2
    </c:when>
    <c:otherwise>
        실행문3
    </c:otherwise>
</c:choose>
<!-- 
    자바 if문처럼 조건식이 true인 실행문만 실행됨
    조건식이 모두 false일 때 otherwise가 실행됨
-->
```
    
### 반복문
    
```html
<%@ taglib uri="http://java.sun.com/jsp/jstl/core"  prefix="c"%>

<!-- forEach -->
<c:forEach var="변수" begin="초기값" end="종료"[ step="증가치"]>
    실행문
</c:forEach>
<!--
    변수에 담긴 초기값이 1씩 증가하며 실행문을 반복함
    증가치를 입력하면 한 번 실행될 때마다 변수에 담긴 숫자가 증가치만큼 증가함
-->

<c:forEach items="배열 | 자료구조" var="변수" [ varStatus="status변수"]>
    ${변수}
</c:forEach>
<!--
    배열에 담긴 요소를 하나씩 꺼내옴
    varStatus를 설정할 경우 status변수.index로 번지수를, status변수.count로 꺼내온 갯수를 가져올 수 있음
-->
```
    
### 문자 출력 형식
    
```html
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt"  prefix="fmt"%>

<fmt:formatNumber value="숫자값"></fmt:formatNumber>
<fmt:formatNumber value="숫자값"/>
<!-- 입력한 숫자값에 세 자리마다 콤마를 찍어 출력함 -->
```