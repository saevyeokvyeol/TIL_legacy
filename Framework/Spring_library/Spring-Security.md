# Spring Security

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d8f6814b-f106-4a3f-83fa-49432b002b10/Untitled.png)

## Spring Security 특징

- 사용자를 식별(인증)하고 기능의 사용 가능 여부를 검사(인가)해주는 오픈 소스 프레임워크
- 보편적으로 사용하는 인증, 인가, UI 처리를 제공
- 비밀번호, 결제 정보를 암호화할 수 있는 암호화 기능 제공
- 테스트 용으로 사용 가능한 in-Memory 기능 제공

## 관련 용어

### 인증Authentication

- 현재 사용자가 누구인지 사용하는 과정
- 주요 인증 종류
    - 크리덴셜Credential: ID와 비밀번호 일치 여부를 확인(로그인)
    - 이중 인증: 한 번에 2가지 방식으로 인증하는 것(로그인 + 공동인증서)
    - 물리적 인증: 지문 인식, 얼굴 인식 등 물리적인 요소로 인증받는 것

### 인가Authorization

- 현재 사용자가 접근하려는 자원에 대한 권한이 있는지 확인하는 절차

### 부여된 권한Granted Authority

- 적절한 절차를 통해 사용자가 인증되었을 때 특정 기능에 접근 가능하도록 부여되는 권한

### 리소스 권한Intercept

- 사용자의 권한 여부에 따라 자원에 접근하거나 접근할 수 없도록 외부 요청을 가로채는 것

## 사용 설정

### dependency 추가

```xml
<!--
	pom.xml에 스프링 시큐리티 dependency 추가
	Spring 버전과 맞춰서 추가함
-->
<!-- spring-security-core 추가 -->
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-core</artifactId>
    <version>5.3.13.RELEASE</version>
</dependency>

<!-- spring-security-web 추가 -->
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-web</artifactId>
    <version>5.3.13.RELEASE</version>
</dependency>

<!-- spring-security-config 추가 -->
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-config</artifactId>
    <version>5.3.13.RELEASE</version>
</dependency>

<!-- spring-security-taglibs 추가 -->
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-taglibs</artifactId>
    <version>5.3.13.RELEASE</version>
</dependency>
```

### xml 설정

```xml
<!-- web.xml -->

<!-- Spring Security는 filter 기반이기 때문에 context-param을 통해 등록 -->
<context-param>
	<param-name>contextConfigLocation</param-name>
	<param-value>
		/WEB-INF/spring/security-context.xml
	</param-value>
</context-param>

<!--
	Spring Security 등록
	: filter-name은 반드시 springSecurityFilterChain으로 사용
	  security가 등록되면 springSecurity 설정 xml 파일 필요
-->
<filter>
	<filter-name>springSecurityFilterChain</filter-name>
	<filter-class>org.springframework.web.filter.DelegatingFilterProxy</filter-class>
</filter>

<filter-mapping>
	<filter-name>springSecurityFilterChain</filter-name>
	<url-pattern>/*</url-pattern> <!-- 루트 밑의 모든 요청에 대응 -->
</filter-mapping>
```

```xml
<!--
	security-context.xml: Spring Security는 filter 기반이기 때문에 appServlet 폴더가 아닌 spring 폴더에 넣음
	namespace에서 security - http://www.springframework.org/schema/security 선택 시 태그 사용 가능
-->

<!--
	사용자 요청이 들어오면 가로챌 정보를 설정
	
	use-expressions: true 설정 시 SpringEL 사용 가능
	                 SpringEL 참고 - https://docs.spring.io/spring-security/site/docs/4.2.x/reference/html/el-access.html
	auto-config: true 설정 시 자동으로 SpringSecurity가 제공하는 loginForm과 로그인 권한을 설정
-->
<security:http use-expressions="true" auto-config="true">
	<!--
		security:intercept-url: 특정 url 패턴에 대한 권한을 설정
		                        권한이 없는 경우 403 forbidden 발생
		                        필요한 만큼 추가 작성 가능
	-->
	<security:intercept-url pattern="url 패턴(ant-style 사용 가능)" access="SpringEL"/>

	<!--
		Spring Security가 제공하는 로그인폼 대신 사용자 정의 로그인폼을 사용하고 싶을 때 사용하는 태그

		login-page: 로그인 폼 경로, 기본값="/login"
		login-processing-url: 로그인 요청 경로(로그인 폼을 보낼 경로), 기본값="/login"
		username-parameter: 로그인 요청 경로(로그인 폼을 보낼 경로), 기본값="username"
		password-parameter: 로그인 요청 경로(로그인 폼을 보낼 경로), 기본값="passowrd"
		default-target-url: 로그인 성공 시 이동 경로, 기본값="/"
		authentication-failure-url: 인증 실패 시 이동 경로, 기본값="/login?error"
	-->
	<security:form-login login-page="경로" login-processing-url="경로"/>
	
	<!--
		로그아웃 기능을 활성화하고 싶을 때 사용하는 태그

		logout-url: 로그아웃 요청 경로, 기본값="/logout"
		invalidate-session: 기존 세션 제거 여부, 기본값="true"
		delete-cookies: 로그아웃 시 삭제할 쿠키 이름, 콤마로 구분
		logout-success-url: 로그아웃 후 이동할 경로, 기본값="/"
		success-handler-ref: 로그아웃 정공 시 이동처리하는 LogoutSuccessHandler 지정
	-->
	<security:logout logout-url="경로" invalidate-session="boolean" delete-cookies="쿠키명" logout-success-url="/"/>
</security:http>

<!--
	Spring Security가 제공하는 in-memory 기능 설정
	: 테스트용 아이디와 비밀번호, 권한을 xml파일에 저장할 수 있음
	  SpringSecurity 5.x부터 PasswordEncoder는 필수 -> 비밀번호를 설정 시 필수적으로 접두어 입력
	  접두어 {noop}는 NoOpPasswordEncoder 암호화 구현체 사용을 의미(=암호화 없이 평문 사용)
-->
<security:authentication-manager>
	<security:authentication-provider>
		<security:user-service>
			<security:user name="유저 아이디" password="{접두어}비밀번호" authorities="ROLE_권한명"/>
		</security:user-service>
	</security:authentication-provider>
</security:authentication-manager>
```

## 참고

### 예약어

```html
${pageContext.request.userPrincipal} <!-- userPrincipal: 로그인 시 로그인 정보를 저장하는 예약어 -->
```

### csrf token

```html
<!--
	spring security는 기본적으로 csrf 공격을 방어하기 위한 csrf token을 서로 주고받음
  spring 5.x 이상부터 post 방식으로 form을 보낼 때 반드시 csrf token을 보내야 함
  <security:csrf> 태그로 중지는 가능하지만 보안을 위해 권장X

	form 안에 name값이 ${_csrf.parameterName}, value값이 ${_csrf.token}인 input이 없으면 폼 전송 불가능 
-->
<form action="경로" method="post">
	<input type="hidden" name="${_csrf.parameterName}" value="${_csrf.token}">
</form>
```