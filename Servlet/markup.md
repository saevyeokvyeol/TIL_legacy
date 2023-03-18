# 웹페이지 구성

```java
// Servlet으로 웹페이지 문서를 만들기 위해서는 jsp와 달리 아래처럼 직접 마크업을 입력해야 함

// 문자 인코딩 처리
response.setContentType("text/html;charset=UTF-8");
		
// 브라우저 출력
PrintWriter out = response.getWriter();

out.println("<html>");
out.println("<head><title>servlet</title></head>");

out.println("<body>");
out.println("<h1>빰빰빰</h1>");
out.println("<h1>nununu</h1>");
out.println("</body>");

out.println("</html>");
```