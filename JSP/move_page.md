# WAS를 통한 이동

## forward

> 현재 request와 reponse를 유지하면서 이동하는 방식
페이지가 늘어나지 않고 현재 페이지에 포워딩됨(뒤로가기X)
> 

```html
<!-- 액션 태그로 포워드 -->
<% request.setCharacterEncoding("UTF-8"); %> <!-- 인코딩 처리하지 않으면 한글이 깨짐 -->
<jsp:forward page="url주소"></jsp:forward>
<jsp:forward page="url주소"/> <!-- 축약형 -->

<!-- 입력한 url주소 파일이 불러와지기 때문에 파일에 화면에 무언가를 출력해도 보이지 않음 -->
```

```java
/* 메소드 호출해 포워드(자바 코드) */
RequestDispatcher rd = request.getRequestDispatcher("url주소");
rd.forward(request, response)
```

```java
request.getParameter("변수명") // 보내온 파라미터 받기
```

## redirect

> 현재 request와 reponse를 버리고 새로운 request와 reponse를 생성해 이동하는 방식
> 

```java
response.sendRedirect("url주소");

// 이동할 때 넘겨주고 싶은 값이 있다면 주소에 수동 get 방식으로 넘겨줘야 함
response.sendRedirect("url주소?변수명=" + URLEncoder.encode(값, request.getCharacterEncoding()));
```