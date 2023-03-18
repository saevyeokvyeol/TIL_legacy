# include

> top, footer 영역 등 많은 페이지에 동일한 형식으로 들어가는 영역을 따로 파일로 만들어 삽입하기 위해 사용
> 

```html
<!-- 스크립팅 요소로 include하기 -->
<%@ include file="url주소" %>
<!--
	WAS에서 변환될 때 소스가 하나의 페이지로 통합돼 Servlet이 하나만 만들어짐
	(=변수를 공유해 사용할 수 있음)
-->

<!-- 액션태그로 include하기 -->
<jsp:include page="url주소"></jsp:include>
<jsp:include page="url주소"/>
<!--
	모든 파일이 각각의 Servlet으로 생성된 후 하나로 합쳐짐
	(=변수 공유 불가)
-->
```

## 액션태그 include로 변수 받기

```html
<% request.setCharacterEncoding("UTF-8"); %> <!-- 인코딩 처리하지 않으면 한글이 깨짐 -->
<jsp:include page="url주소">
	<jsp:param value="값" name="변수명"/>
</jsp:include>
```

```java
<%
	request.getParameter("변수명");
	 // 보내온 파라미터 받기
%>
```