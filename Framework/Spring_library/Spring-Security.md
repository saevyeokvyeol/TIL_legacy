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

<!-- UI 처리를 위한 spring-security-taglibs 추가 -->
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-taglibs</artifactId>
    <version>5.3.13.RELEASE</version>
</dependency>

<!-- DB 사용 시 DB dependency도 추가 -->
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
		authentication-failure-handler-ref: 인증 실패 시 실행할 핸들러 등록
	-->
	<security:form-login login-page="경로" login-processing-url="경로"/>
	
	<!--
		로그아웃 기능을 활성화하고 싶을 때 사용하는 태그

		logout-url: 로그아웃 요청 경로, 기본값="/logout"
		invalidate-session: 기존 세션 제거 여부, 기본값="true"
		delete-cookies: 로그아웃 시 삭제할 쿠키 이름, 콤마로 구분
		logout-success-url: 로그아웃 후 이동할 경로, 기본값="/login?logout"
		success-handler-ref: 로그아웃 정공 시 이동처리하는 LogoutSuccessHandler 지정
	-->
	<security:logout logout-url="경로" invalidate-session="boolean" delete-cookies="쿠키명" logout-success-url="/"/>
</security:http>

<security:authentication-manager>
	<!--
		Spring Security가 제공하는 in-memory 기능 설정 방식
		: 테스트용 아이디와 비밀번호, 권한을 xml파일에 저장할 수 있음
		  SpringSecurity 5.x부터 PasswordEncoder는 필수 -> 비밀번호를 설정 시 필수적으로 접두어 입력
		  {noop} - NoOpPasswordEncoder(=암호화 없이 평문 사용)
		  {bcrypt} - BCryptPasswordEncoder
		  {} - BCryptPasswordEncoder
	-->
	<security:authentication-provider>
		<security:user-service>
			<security:user name="유저 아이디" password="{접두어}비밀번호" authorities="ROLE_권한명"/>
		</security:user-service>
	</security:authentication-provider>

	<!--
		authentication-provider 구현체 등록 방식
		: DB에 저장된 정보를 바탕으로 인증 시행
	-->
	<security:authentication-provider ref="객체 id값"/>
</security:authentication-manager>
```

```xml
<!--
	root-context.xml
	: 필터 기반 Spring Security가 사용할 객체를 스캔하고 클래스를 등록
-->

<!-- filter 기반 Spring Security가 사용해야 하는 service, repository, annotation 기반 DB 문서 등록 -->
<context:component-scan base-package="경로"/>

<!-- 암호화 사용할 경우 비밀번호를 암호화하는 PasswordEncoder 구현체 클래스 등록 -->
<bean class="org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder" id="passwordEncoder"/>
<bean class="org.springframework.security.crypto.password.StandardPasswordEncoder"  id="passwordEncoder"/>
<!-- 둘 중 원하는 것 하나만 등록 -->
```

## 예제 코드: 설정 레퍼런스

### authentication-failure-handler-ref

```java
/**
 * AuthenticationFailureHandler를 구현해 인증에 실패했을 때 호출될 메소드를 담은 핸들러 제작
 * : 제작 후 경로를 스캔한 뒤 security:form-login 태그의 authentication-failure-handler-ref 속성값으로 입력해야 사용 가능
 * */
@Service
public class AuthenticationFailureHandler implements AuthenticationFailureHandler {

	@Override
	public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response,
			AuthenticationException exception) throws IOException, ServletException {
		/**
		 * 인증에 실패했을 때 할 일 제작
		 * DispatcherServlet 이전에 동작하기 때문에 ModelAndView 사용 불가
		 * : 이동하고 싶을 때에는 request를 이용해 리다이렉트나 포워드 방식으로 이동해야 함
		 * */
	}

}
```

### security:authentication-provider ref

```java
/**
 * 인증 시 사용할 정보를 DB에서 가져오고 인증 성공 시 정보를 저장하기 위한 객체
 * 제작 후 경로를 스캔한 뒤 security:authentication-provider 태그의 ref 속성값으로 입력해야 사용 가능
 * */
@Service
@RequiredArgsConstructor
public class AuthenticationProvider implements AuthenticationProvider {
	
	private final MemberDAO memberDAO; // 인증 시 DB와 연결되어 아이디와 비밀번호(=계정 정보)를 가져올 DAO
	private final AuthoritiesDAO authoritiesDAO; // 인증 성공 시 DB와 연결되어 해당 아이디가 가지고있는 권한을 가져올 DAO
	private final PasswordEncoder passwordEncoder; // 비밀번호를 암호화할 인코더(암호화 인코더 객체가 등록되지 않으면 주입X, 에러 발생)
	
	/**
	 * 로그인 폼에서 username, password가 전송되면 UsernamePasswordAuthenticationToken 객체를 만들어 인수로 전달
	 * -> 전달된 인수에서 username(=아이디)과 credentials(=비밀번호)를 꺼내 인증처리(로그인)
	 *    성공 시 인증된 사용자의 정보와 권한을 가져와 Authentication에 저장해 리턴
	 *    실패 시 예외(AuthenticationException)를 발생
	 * */
	@Override
	public Authentication authenticate(Authentication authentication) throws AuthenticationException {
		// 1. username(=id)를 꺼내 Member 테이블의 사용자 정보와 비교
		String id = authentication.getName();
		Member member = memberDAO.selectMemberById(id);
		
		// 2. 1이 없으면 예외 발생
		if(member == null) throw new UsernameNotFoundException(에러 메세지);
		
		// 3. 1이 있으면 인수로 전달된 평문과 DB에 저장된 암호화 비밀번호를 비교
		String password = authentication.getCredentials().toString();
		boolean result = passwordEncoder.matches(password, member.getPassword());
		
		// 4. 3이 일치하지 않으면 예외 발생
		if(!result) throw new UsernameNotFoundException(에러 메세지);
		
		// 5-1. 일치하면 DB에서 List<Authority> 타입을 꺼냄
		List<Authority> authoritiesList = authoritiesDAO.selectAuthorityByUserName(id);
		
		// 5-2. 꺼낸 List<Authority> 타입을 security에서 사용하는 권한 타입으로 변환
		List<SimpleGrantedAuthority> simpleGrantedList = new ArrayList<SimpleGrantedAuthority>();
		for(Authority authority : authoritiesList) {
			simpleGrantedList.add(new SimpleGrantedAuthority(authority.getRole()));
		}
		
		// 5-3. Authentication 구현체를 생성해 객체 안에 사용자 정보와 권한을 저장
		//      UsernamePasswordAuthenticationToken에 저장하는 정보는 차례로 계정 정보(principal), 비밀번호, 권한 리스트
		UsernamePasswordAuthenticationToken usernamePasswordAuthenticationToken
			= new UsernamePasswordAuthenticationToken(member, null, simpleGrantedList);
		
		// 6. 생성된 Authentication 객체 리턴
		return usernamePasswordAuthenticationToken;
	}

	/**
	 * 인수로 전달된 인증 정보(=사용자가 입력한 로그인 정보)가 유효한 객체인지 판단해주는 메소드
	 * : authenticate보다 먼저 호출되며 해당 메소드가 true를 리턴해야 authenticate 메소드 호출
	 * */
	@Override
	public boolean supports(Class<?> authentication) {
		return UsernamePasswordAuthenticationToken.class.isAssignableFrom(authentication);
	}
}
```

## 예제 코드: 기타 참고 코드

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

## taglib

> JSP에서 권한, 로그인 여부에 따라 UI를 변경할 수 있도록 태그 라이브러리 지원
> 

```html
<!--
	sec:authorize
	: access 속성에 springEL에 대응하는 권한이 있을 경우 태그 내부에 작성한 코드를 출력함
	  springEL 참고 - https://docs.spring.io/spring-security/site/docs/4.2.x/reference/html/el-access.html
-->
<sec:authorize></sec:authorize>

<!--
	sec:authentication
	: Authentication에 저장한 principal을 출력하는 객체
	  property 속성에 principal이나 principal.필드를 입력하면 principal로 저장된 객체를 출력함
-->
<sec:authentication property=""/>
```