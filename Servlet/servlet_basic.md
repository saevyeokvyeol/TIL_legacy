# 문서 작성 및 사용 방법

## 문서 작성

```java
public class 클래스명 extends HttpServlet { }
// 반드시 public class여야 하며, HttpServlet 상속받아 필요한 메소드를 재정의해 작성함
```

## 문서 사용

- web.xml 문서 설정

```xml
<!-- 서블릿 개체 생성 -->
<servlet>
	<servlet-name>서블릿 개체명 설정</servlet-name>
	<servlet-class>자바 파일 경로</servlet-class>
	<load-on-startup>n(제작 순서)</load-on-startup>
	<!-- load-on-startup 옵션을 설정하면 tomcat이 start될 때 미리 생성함 -->
</servlet>

<!-- 생성한 서블릿을 url에서 호출 -->
<servlet-mapping>
	<servlet-name>서블릿 개체명</servlet-name>
  <url-pattern>url 주소 설정(루트 기준 or *.확장자)</url-pattern>
	<!-- 여기서 설정한 url 주소를 호출하면 서블릿 개체가 출력됨 -->
</servlet-mapping>
```

- @annotation 설정

```java
import javax.servlet.annotation.WebServlet;

@WebServlet (loadOnStartup = 1, urlPatterns = "url 주소 설정(루트 기준 or *.확장자)")
public class 클래스명 extends HttpServlet { }
```