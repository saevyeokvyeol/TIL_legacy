# 기본 메소드

```java
init();
/*
	서블릿 문서가 초기화될 때 최초에 자동으로 실행됨
	생성자와 비슷하게 객체가 생성된 후 반드시 해야 할 일이 있을 때 오버라이딩해 사용함
*/

service(ServletRequest request, ServletResponse response);
/*
	init이 실행된 후 호출됨(사용자 요청이 들어오면=새로고침되면 호출)
	사용자 요청이 get 방식인지 post 방식인지 구분해 doGet() | doPost() 메소드를 호출함
	요청방식에 상관없이 기능을 만들 경우 오버라이딩해 사용
*/

doGet(HttpServletRequest request , HttpServletResponse response);
/*
	사용자 요청이 get 방식일 경우 실행됨
	요청방식을 구분해 기능을 만들 경우 오버라이딩해 사용
*/

doPost(HttpServletRequest request , HttpServletResponse response);
/*
	사용자 요청이 post 방식일 경우 실행됨
	요청방식을 구분해 기능을 만들 경우 오버라이딩해 사용
*/

destory();
/*
	서블릿 문서가 종료될 때(=서버가 종료될 때, 서블릿이 리로드될 때) 호출됨
	종료할 때 반드시 해야 할 일이 있을 때 오버라이딩해 사용함
*/
```