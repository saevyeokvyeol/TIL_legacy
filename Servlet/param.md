# init-param

## web.xml에서 생성
    
```xml
<!-- 한 서블릿에서만 사용할 init-param 생성 -->
<servlet>
    <servlet-name></servlet-name>
    <servlet-class></servlet-class>

    <init-param>
        <param-name>init변수명</param-name>
        <param-value>값</param-value>
    </init-param>
    <!-- servlet 등록 시 변수 등록 -->

</servlet>
```
    
## @annotation에서 생성
    
```java
import javax.servlet.annotation.WebServlet;

@WebServlet (loadOnStartup = 1, urlPatterns = "url 주소 설정(루트 기준)"
    initParams = {
            @WebInitParam(name = "init변수명", value ="값"),
            @WebInitParam(name = "init변수명", value ="값")...
    })
public class 클래스명 extends HttpServlet { }
```
    
## 호출 방법
    
```java
public class 클래스명 extends HttpServlet {

    String 변수명;
    
    @Override
    public void init() throws ServletException {
        변수명= super.getInitParameter("init변수명");
        // initParam을 호출해 전역 변수로 저장해 사용
    }
}
```
    

# context-param

```xml
<!-- ServletContext 영역에 저장되는(=모든 서블릿 문서가 공유하는) context-param 생성 -->
<context-param>
	<param-name>context변수명</param-name>
	<param-value>값</param-value>
</context-param>
```

```java
public class 클래스명 extends HttpServlet {

	String 변수명;
	
	@Override
	public void init() throws ServletException {
		ServletContext application = super.getServletContext();
		application.getInitParameter("context변수명");
		변수명= super.getInitParameter("context변수명");
		// contextParam을 호출해 전역 변수로 저장해 사용
	}
}
```

```html
<%= application.getInitParameter("fileName") %>
<!-- JSP 문서에서 application을 이용해 꺼내 사용할 수 있음 -->
```