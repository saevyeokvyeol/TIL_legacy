# JSP 내장 객체(session, application) 가져오기

```java
// HttpSession 구하기
HttpSession session = request.getSession();

// ServletContext 구하기
ServletContext application = request.getServletContext();
```