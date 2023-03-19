# SpringMVC

## DispatcherServlet

> Spring MVC Framework의 Front Controller, 웹 요청-응답 Life Cycle을 주관
> 

### 설정 방법

- 기존 방식
    1. HttpServlet을 상속받아 DispatcherServlet 파일 생성
        1. HandlerMapping을 통해 key값에 대응되는 controller를 받음
        2. controller에서 메소드를 호출해 ModelAndView를 리턴받음
        3. 리턴받은 ModelAndView 값에 따라 이동시킴
    2. 제작한 DispatcherServlet 파일을 wep.xml 문서에 등록함
- Spring 사용 시(xml 방식)
    1. springframework에서 제공하는 DispatcherServlet을 wep.xml 문서에 등록
    2. dispatcher-servlet.xml 파일을 제작(DispatcherServlet 등록 시 자동 탐색 및 실행)
        1. handlerMapping 등록
        2. viewResolver 등록
        3. ~Controller 등록
    
    ```xml
    <!-- web.xml -->
    
    <!--
    	서블릿 등록
    	두 개 이상의 서블릿을 등록하는 것도 가능함
    	두 개 이상의 서블릿이 등록된 경우 서로의 HandlerMapping, Controller, viewResolver 공유X
    	각자에게 등록된 HandlerMapping, Controller, viewResolver만 사용 가능함
    -->
    <servlet>
    	<servlet-name>dispatcher</servlet-name>
    	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    	<load-on-startup>1</load-on-startup>
    
    	<!--
    		기본으로 설정된 경로/파일명 대신 다른 경로/파일명을 사용하고 싶을 때 init-param 등록\
    		기본 경로/파일명: /WEB-INF/(servlet-name)-servlet.xml
    	-->
    	<init-param>
    		<param-name>appServlet</param-name>
    		<param-value>경로/파일명.xml</param-value>
    		<!-- 두 개 이상의 xml 파일을 연결하고 싶을 때에는 콤마나 줄바꿈으로 연결 -->
    	</init-param>
    
    </servlet>
    
    <servlet-mapping>
    	<servlet-name>appServlet</servlet-name>
    	<url-pattern>url 주소 설정(루트 기준 or *.확장자)</url-pattern>
    </servlet-mapping>
    ```
    
    ```xml
    <!--
    	dispatcher-servlet.xml
    	springContainer 개념인 WebApplicationContext 역할로 spring 내부의 모든 객체의 생성과 소멸을 관리
    -->
    
    <!-- HandlerMapping 등록 -->
    <bean id="handlerMapping" class="org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping"/>
    
    <!-- viewResolver 등록-->
    <bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    	<property name="prefix" value="이동할 경로"/>
    	<property name="suffix" value="호출할 파일 확장자"/>
    	<property name="order" value="n"/>
    	<!--
    		viewResolver가 여러 개 있을 경우 우선 순위를 설정하기 위해 사용
    		숫자가 낮을 수록 우선순위가 높음
    	-->
    </bean>
    
    <!-- Controller 등록 -->
    <bean name="/메소드 호출 후 이동시킬 경로" class="경로.~Controller"/>
    ```
    
- Spring 사용 시(Annotation 방식)
    1. springframework에서 제공하는 DispatcherServlet을 wep.xml 문서에 등록함
    2. servlet-context.xml(=dispatcher-servlet.xml) 파일을 제작(DispatcherServlet 등록 시 자동 탐색 및 실행, maven 사용 시 자동 제작 및 탐색)
    
    ```xml
    <!-- web.xml -->
    
    <!--
    	ContextLoaderListener 등록
    	기본 경로/파일명: /WEB-INF/applicationContext.xml
    	Maven 프로젝트에서는 /WEB-INF/spring/root-context.xml로 자동 설정
    -->
    <listener>
    	<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
    </listener>
    
    <!--
    	서블릿 등록
    	두 개 이상의 서블릿을 등록하는 것도 가능함
    	두 개 이상의 서블릿이 등록된 경우 서로의 HandlerMapping, Controller, viewResolver 공유X
    	각자에게 등록된 HandlerMapping, Controller, viewResolver만 사용 가능함
    -->
    <servlet>
    	<servlet-name>dispatcher</servlet-name>
    	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    	<load-on-startup>1</load-on-startup>
    
    	<!--
    		기본으로 설정된 경로/파일명 대신 다른 경로/파일명을 사용하고 싶을 때 init-param 등록\
    		기본 경로/파일명: /WEB-INF/(servlet-name)-servlet.xml
    	-->
    	<init-param>
    		<param-name>appServlet</param-name>
    		<param-value>경로/파일명.xml</param-value>
    		<!-- 두 개 이상의 xml 파일을 연결하고 싶을 때에는 콤마나 줄바꿈으로 연결 -->
    	</init-param>
    
    </servlet>
    
    <servlet-mapping>
    	<servlet-name>appServlet</servlet-name>
    	<url-pattern>url 주소 설정(루트 기준 or *.확장자)</url-pattern>
    </servlet-mapping>
    ```
    
    ```xml
    <!--
    	servlet-context.xml(=dispatcher-servlet.xml)
    	springContainer 개념인 WebApplicationContext 역할로 spring 내부의 모든 객체의 생성과 소멸을 관리
    -->
    
    <!-- 정적 문서 매핑 -->
    <resources mapping="/resources/**" location="/resources/"/>
    
    <!-- viewResolver 등록-->
    <bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    	<property name="prefix" value="이동할 경로"/>
    	<property name="suffix" value="호출할 파일 확장자"/>
    </bean>
    
    <!-- Controller 등록 -->
    <annotation-driven/>
    <context:component-scan base-package="패키지"/>
    ```
    
    ```xml
    <!--
    	root-context.xml(=applicationContext.xml)
    	모든 서블릿과 필터에서 공유할 영역을 등록함
    -->
    
    <context:component-scan base-package="패키지"/>
    ```

## HandlerMapping

> 웹 요청 시 해당 URL을 어떤 Controller가 처리할 지 결정
> 

### 설정 방법

- 기존 방식
    1. HandlerMapping 파일 제작
        1. key값을 받아 대응하는 controller를 넘겨줌
    2. DispatcherServlet에서 호출해 사용
- Spring 사용 시(xml 방식)
    1. springframework에서 지원하는 BeanNameUrlHandlerMapping을 dispatcher-servlet.xml 파일에 등록함
    
    ```xml
    <!-- HandlerMapping 등록 -->
    <bean id="handlerMapping" class="org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping"/>
    ```
    
- Spring 사용 시(Annotation 방식)
    1. 각 컨트롤러의 메소드 선언부 위에서 어노테이션을 사용해 매핑
    
    ```java
    @RequestMapping("/경로")
    /*
     * 특정 경로 내부로 진입하는 url을 가져오기 위해 사용
     * 해당 Controller 내부의 메소드는 해당 경로 아래로 처리됨
     * */
    public class ~Controller {
    	
    	@RequestMapping("요청 경로") // 특정 경로를 요청할 때 메소드 호출
    	public void method() {}
    	
    	@RequestMapping(value = {"요청 경로", "요청 경로"}) // 여러 개의 요청이 하나의 메소드를 실행할 때 메소드 호출
    	public void method() {}
    	
    	@RequestMapping(value = "요청 경로", method = RequestMethod.GET | POST) // 특정 요청 방식만 받고 싶을 때
    	public void method() {}
    	
    	@GetMapping("요청 경로") // get 방식만 받고 싶을 때(4.3 버전 이상부터 사용 가능한 축약형)
    	public void method() {}
    	
    	@PostMapping("요청 경로") // post 방식만 받고 싶을 때(4.3 버전 이상부터 사용 가능한 축약형)
    	// 축약형의 경우 @RequestMapping과 함께 사용X
    	public void method() {}
    	
    	@RequestMapping(value = "요청 경로", params = {"key값"}) // 특정 파라미터를 받을 때에만 메소드 호출
    	public void method() {}
    	
    	@RequestMapping(value = "요청 경로", produces = "text/html;charset=UTF-8")
    	@ResponseBody // AJAX처럼 이동하지 않고 리턴값을 해당 페이지로 돌려줄 때 사용
    	// 이 경우 produces로 인코딩 처리해야 한글이 깨지지 않음
    	public String method() {
    		return "문자열";
    	}
    
    	@RequestMapping("{템플릿변수}")
    	/*
    	 * restful 방식
    	 * 루트 바로 아래 경로에 대한 모든 요청 중 다른 메소드와 연결되지 않은 요청을 모두 가져옴
    	 * {템플릿변수1}/{템플릿변수2}... 으로 depth의 길이를 조절해 요청을 가져올 수도 있음
    	 * */
    	public void method(@PathVariable String 템플릿변수명) {}
    	// @PathVariable 어노테이션을 사용해 경로를 변수로 가져올 수 있음
    
    }
    ```

## Controller

> 비즈니스 로직을 수행하고 결과 데이터를 ModelAndView에 반영
> 

### 설정 방법

- 기존 방식
    1. Controller 인터페이스 제작
    2. 제작한 Controller 인터페이스를 구현해 세부 Controller 제작
- Spring 사용 시(xml 방식)
    1. springframework에서 제공하는 Controller를 구현해 세부 Controller 제작
    
    ```java
    import org.springframework.web.servlet.mvc.Controller;
    
    public class ~Controller implements Controller {
    	@Override
    	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    		ModelAndView mv = new ModelAndView();
    		return mv;
    	}
    }
    ```
    
- Spring 사용 시(Annotation 방식)
    1. Controller 선언부 위에 @Controller 어노테이션 입력해 Controller 제작
    
    ```java
    import org.springframework.web.servlet.mvc.Controller;
    
    @Controller // Controller 어노테이션
    @RestController // @Controller + @ResponseBody, AJAX 전용 컨트롤러 선언 시 사용
    public class ~Controller {
    
    	public void method(HttpServletRequest request, HttpServletResponse response) {
    	} // Spring이나 자바에서 제공하는 클래스가 매개 변수로 필요한 경우 인수로 입력하면 Spring이 호출할 때 자동으로 입력해줌
    
    	public void method(Model model) {
    		model.addAttribute(key, value);
    	} // 리턴이 void나 String일 때 결과뷰로 변수를 넘기고 싶을 때에는 Model을 인수로 받은 뒤 사용
    
    	public void method(String str, Integer i) {
    	} // 요청 경로에 변수가 포함될 경우 인수로 key를 입력하면 자동으로 들어옴
    	// int의 경우 입력하지 않으면 null로 오류가 발생하기 때문에 null값이 허용되는 Integer로 받음
    
    	public void method(@RequestParam(value = "string", required = false, defaultValue = "디폴트값") String str) {
    	} /*
    	 * 들어오는 key값과 받는 인수 변수명이 다를 경우 둘을 묶기 위해 사용
    	 * 아무 값도 들어오지 않을 경우 required = false가 없으면 에러 발생
    	 * defaultValue를 입력할 경우 해당 인수가 들어오지 않을 때 디폴트값을 입력함
    	 * */
    
    	public void method(@ModalAttribute("m"), Member m) {
    	} /*
    	 * form을 받을 경우 대응하는 dto를 인수로 넣으면 자동으로 setter에 입력되어 들어옴
    	 * 
    	 * 이렇게 받은 객체는 결과뷰로 자동으로 넘어감
    	 * 이 때, key값은 첫 글자를 소문자로 바꾼 클래스명 ex)${member}
    	 * @ModalAttribute를 메소드 인수에 선언한 경우 뷰로 전달되는 객체의 별칭을 만듦 ex) ${m}
    	 * 
    	 * 단, List<객체> 형식으로 특정 객체를 리스트 형태로 받을 수는 없음
    	 * 객체를 리스트 형태로 받고 싶은 경우 리스트를 저장하는 DTO를 만들어 해당 객체를 인수로 받아야 함
    	 * */
    
    	public void method(MemberListDTO list) {
    	} /*
    	 * 객체를 리스트 형태로 받고 싶은 경우 리스트를 저장하는 DTO를 만들어 해당 객체를 인수로 받아야 함
    	 * List<객체> 형태로 인수 받는 건 불가능
    	 * */
    
    	@RequestMapping("key값")
    	public 리턴타입 method() {
    		return value값;
    	} /*
    	 * 현재 컨트롤러를 호출하는 모든 요청에 공통으로 넘겨줄 정보 설정
    	 * 괄호 안의 값이 key, 리턴값이 value로 처리됨
    	 * */
    }
    ```
    
- Controller 메소드 리턴 타입별 이동할 viewName 규칙
    - return String: 리턴값 = viewName
    - return void: 요청된 주소 = viewName = prefix + 요청된 주소(확장자 생략) + suffix

## ModelAndView

> Controller가 수행 결과를 반영하는 Model 데이터 객체와 이동할 페이지 정보(또는 View 객체)를 담은 객체
> 

### 설정 방법

- 기존 방식
    1. ModelAndView 클래스 제작
    2. 제작한 ModelAndView를 임포트해 Controller에서 리턴값으로 사용
- Spring 사용 시
    1. springframework에서 제공하는 ModelAndView를 임포트해 Controller에서 리턴값으로 사용
    
    ```java
    import org.springframework.web.servlet.ModelAndView;
    
    public class ~Controller {
    	public ModelAndView method() {
    		return new ModelAndView(viewName, modelName, modelObject);
    		// 이동할 뷰 이름, key, value를 입력받는 생성자(가장 자주 사용됨)
    	}
    }
    ```
    

## View

> 결과 데이터인 Model 객체를 보여줌
> 

### 설정 방법

- 기존 방식
    1. ModelAndView 클래스 제작
    2. 제작한 ModelAndView를 임포트해 Controller에서 이동할 뷰 입력
    3. 리턴값으로 넘겨줌
- Spring 사용 시
    1. ModelAndView를 리턴할 경우
        1. springframework에서 제공하는 ModelAndView를 임포트해 Controller에서 이동할 뷰 입력
        2. 리턴값으로 넘겨줌
    2. String을 리턴할 경우: 리턴한 String으로 뷰를 이동시킴
    3. void를 리턴할 경우: 요청 경로로 이동함
    
    ```java
    public class ~Controller {
    
    	public ModelAndView method() {
    		return new ModelAndView();
    	} // 리턴 ModelAndView의 경우 = ModelAndView().getViewName() = viewName = prefix + ModelAndView().getViewName() + suffix
    	
    	public String method() {
    		return "result";
    	} // 리턴 String의 경우: 리턴값 = viewName = prefix + 리턴값 + suffix
    
    	public void method() {
    	} // 리턴 void의 경우: 요청 경로(@RequestMapping 요청 경로) = viewName = prefix + 요청 경로(확장자 생략) + suffix
    
    }
    ```
    
## Exception

> 에러가 발생할 경우 에러 처리
> 

### 설정 방법

- 기존 방식
    - 페이지에서 errorPage=”에러 처리용 페이지” 설정: 한 페이지에서 일어나는 에러는 모두 한 페이지로 이동함
    - web.xml에 에러 페이지 등록: 각 에러에 따라 다른 페이지로 이동 가능
- Spring 사용 시
    - Controller에 @ExceptionHandler 어노테이션 사용
        
        ```java
        public class ~Controller {
        
        	@ExceptionHandler(처리할 Exception.class) // Controller에서 입력한 Exception 발생 시 이동
        	public ModelAndView error(Exception e) { // 발생한 Exception 정보가 필요한 경우 인수로 입력하면 자동 삽입됨
        		// 예외가 발생했을 때 해야할 일 작성
        		return new ModelAndView();
        	}
        
        	@ExceptionHandler(value = {처리할 Exception1.class, 처리할 Exception2.class})
        	// 여러 Exception을 한 번에 처리하고 싶은 경우 value값으로 여러 Exception을 받음
        	public ModelAndView error() {
        		return new ModelAndView();
        	}
        }
        ```
        
    - springBean 설정에 SimpleMappingExcepeionResolver 세팅
        
        ```xml
        <bean class="org.springframework.web.servlet.handler.SimpleMappingExceptionResolver">
        	<property name="exceptionMappings">
        		<props>
        			<!-- Exception 처리가 필요한 만큼 prop 추가 -->
        			<prop key="처리할 exception"> 
        				이동할 페이지
        			</prop>
        		</props>
        	</property>
        </bean>
        
        <!-- @ExceptionHandler과 SimpleMappingExcepeionResolver를 동시에 사용하고 싶을 때 아래 태그 필요 -->
        <annotation-driven/>
        ```
        
    - Annotation 방식으로 SimpleMappingExcepeionResolver 세팅
        
        ```java
        /**
         * Config.java 파일
         * */
        
        @Configuration // Bean 등록 전용 클래스를 선언하기 위한 어노테이션
        public class Config {
        
        	@Bean // Bean 등록을 위한 어노테이션
        	public SimpleMappingExceptionResolver getSimpleMappingExceptionResolver() {
        		SimpleMappingExceptionResolver exceptionResolver = new SimpleMappingExceptionResolver();
        		
        		Properties pro = new Properties(); // 처리할 exception과 이동할 페이지를 매핑할 프로퍼티 생성
        		pro.put("처리할 exception", "이동할 페이지"); // 처리할 exception과 이동할 페이지 입력
        		
        		exceptionResolver.setExceptionMappings(pro); // exceptionResolver에 매핑한 프로퍼티 입력
        		
        		return exceptionResolver;
        	}
				}
        ```

# Maven 기반 SpringMVC

## 디렉토리 구조

### 루트

- src/main/java  → controller, service, dao, dto 등 java 파일
- src/main/resources  → mapper, config 등 설정 관련 xml, properties 파일
- src/main/test  → 단위 테스트용 폴더

### webapp

- src/main/webapp/  → root (= WebContent)
- src/main/webapp/resources  → css, js, img 등 정적 문서

### WEB-INF

- src/main/webapp/WEB-INF/  → web.xml
- src/main/webapp/WEB-INF/spring  → root-context.xml, spring-context.xml 등 springContainer 설정 문서
- src/main/webapp/WEB-INF/views  → ~.jsp문서