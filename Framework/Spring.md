# 개념

- 자바 기반의 경량 라이브러리 덩어리
- EJB(Enterprise Java Bean)의 단점을 보완해 나온 오픈 소스 프레임워크
- 복잡한 엔터프라이즈 어플리케이션 개발을 간단하게 만들어줌
- 기능을 모듈로 제공하기 때문에 필요한 기능만 가져다 사용할 수 있음
- 공공부문 정보화 산업 표준인 전자정부 프레임워크(eGov)가 Spring과 MyBatis를 기반으로 하기 때문에 국내에서 활성화됨
- 현재 주류 프레임워크

# 특징

- 가벼운 경량의 라이브러리 → 현재에는 다소 무거워짐
- 기반 코드를 제공함
- xml 기반으로 컴포넌트를 개발함
- Maven( or Gradle) 기반 프로젝트 사용: Maven이 pom(Project Object Model).xml 파일을 통해 의존 관계 라이브러리를 관리함

## Spring의 전략

> 복잡한 엔터프라이즈 개발을 간단하게 만들고자 Spring이 사용하는 전략
> 

### Potable Service Abstraction

- 추상화된 기반 코드(=인터페이스) 제공

### Dependency Injection

- 의존 관계 주입(=제어의 역행 IoC Inversion of Control 개념을 문법으로 적용한 것)
- 필요한 객체를 개발자가 직접 생성❌
- SpringContainer(=외부 조립기)가 적절하게 객체를 생성하고 주입해 객체와 객체 간의 결합도를 느슨하게 만듦

### Aspect Oriented Programming

- 관점 지향 프로그래밍
- 프로그램 로직을 관점에 따라 핵심 로직과 공통 로직으로 분리해 공통 로직을 재사용함

# 사용 준비 작업

1. JDK 설치
2. IDE 설치(eclipse)
3. STS(SpringSource Tool Suite) 설치
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f401e5d5-6455-4caf-9bea-5bdba1ff0a0d/Untitled.png)
    
4. Maven or Gradle 세팅: 라이브러리와 빌드 프로세스를 관리해주는 툴

# Dependency Injection

## Inversion of Control

- = 제어의 역전
- 컴포넌트의 의존 관계 결정, 설정 및 생성주기 문제를 해결하기 위한 디자인 패턴
- 객체의 생성부터 생명주기 관리까지 객체에 대한 모든 제어권을 개발자→프로그램으로 넘기는 것

## Dependency Injection

### Dependency Injection(의존 관계 주입)

- Inversion of Control 개념을 문법화한 것
- 각 클래스 간의 의존 관계를 빈Bean 설정 정보를 바탕으로 컨테이너가 자동 연결해줌
- 객체 레퍼런스를 컨테이너에서 주입받아 실행 시 동적으로 의존관계 생성
- 컨테이너가 흐름의 주체가 되어 어플리케이션 코드에 의존관계를 주입함
- 코드가 단순해지고 컴포넌트 간의 결합도가 제거되는 장점이 있음

### DI 유형

- Setter Injection: 의존성을 입력받는 setter 메소드를 만들고 이를 통해 의존성 주입
- Construction Injection: 필요한 의존성을 포함하는 클래스 생성자를 만들고 이를 통해 의존성 주입
- Method Injection: 의존성을 입력받는 일반 메소드를 만들고 이를 통해 의존성을 주입

## Spring DI 컨테이너

### 개념

- DI 컨테이너 = IoC 컨테이너
- 객체의 생성을 책임지고 의존성을 관리함
- POJO의 생성, 초기화, 서비스, 소멸에 대한 권한을 가짐
- 개발자들이 직접 POJO를 생성할 수 없는 것은 아님

### 빈Bean

- 스프링이 IoC 방식으로 관리하는 객체(=클래스)

### 빈 팩토리BeanFactory

- 스프링의 IoC를 담당하는 핵심 컨테이너
- 빈을 등록, 생성, 조회, 반환함(객체의 라이프사이클 관리)

### 어플리케이션 컨텍스트ApplicationContext

- 빈 팩토리 기능 + 다국어 지원, 메시지 처리 등 각종 부가 서비스 제공

### 웹 어플리케이션 컨텍스트WebApplicationContext

- Spring WEB MVC Container
- 웹 어플리케이션을 위한 어플리케이션 컨텍스트

### 설정 메타 정보

- BeanFactory, ApplicationContext이 IoC를 적용하기 위해 사용하는 메타 정보
- Bean 객체를 생성하고 구성할 때 사용됨

## 예시 코드: 클래스 생성

```xml
<!-- xml 파일 -->

<!-- 
	객체 생성

	scope="singleton": 사전 초기화-미리 메모리에 생성한 뒤 싱글톤으로 이용함(기본값)
	scope="prototype": 지연 초기화-필요할 때(=getBean()으로 호출할 때)마다 새로 생성해 
	scope="request": 웹에서 사용, 사용자 요청이 들어오는 동안 bean 유지
	scope="session": 웹에서 사용, 세션이 유지되는 동안 bean 유지
 -->
<bean class="경로.클래스파일명(확장자 생략)" id="id값" scope="singleton | prototype | request | session"/>
```

```java
// java 파일

ApplicationContext context = new ClassPathXmlApplicationContext("클래스 패스부터의 경로/xml파일명");
ApplicationContext context = new FileSystemXmlApplicationContext("src부터의 경로/xml파일명");
// 위의 둘 중 하나를 사용해 context 생성

MessageBean bean = context.getBean("아이디값", 클래스파일명.class); // 생성된 객체를 가져와 저장
bean.메소드명(); // 클래스의 메소드 호출
```

## 예시 코드: 생성자 주입

```xml
<!--
	Primitive와 String 타입은 value로 파라미터값을 입력해 파라미터가 있는 생성자를 호출할 수 있음
	순서를 바꿔 넣을 경우 index로 인수 차례를 설정할 수 있음
-->
<bean class="경로.클래스파일명(확장자 생략)" id="id값">

	<constructor-arg value="파라미터값" index="차례"/>
	<!-- 위나 아래의 코드를 사용해 파라미터값을 넣음 -->
	<constructor-arg>
		<value>파라미터값</value>
	</constructor-arg>

</bean>
```

```xml
<!--
	객체 타입은 ref로 파라미터값을 입력해 파라미터가 있는 생성자를 호출할 수 있음
-->
<bean class="경로.클래스파일명(확장자 생략)" id="id값">

	<constructor-arg ref="bean id값"></constructor-arg>
	<!-- 위나 아래의 코드를 사용해 파라미터값을 넣음 -->
	<constructor-arg>
			<ref bean="bean id값"/>
		</constructor-arg>

</bean>
```

## 예시 코드: setter 주입

```xml
<!--
	Primitive와 String 타입은 value로, 객체 타입은 ref로 세터를 주입할 수 있음
-->
<bean class="경로.클래스파일명(확장자 생략)" id="id값">
	<property name="필드명" value="파라미터값"></property>
	<property name="필드명" ref="bean id값"></property>
</bean>
```

```xml
<!--
	namespace에서 p - http://www.springframework.org/schema/p를 추가하면 p:필드명 속성을 이용해 세터를 주입할 수 있음
-->
xmlns:p="http://www.springframework.org/schema/p"

<bean class="경로.클래스파일명(확장자 생략)" id="id값" p:필드명="파라미터값"/>
```

## 예시 코드: collection 주입

```xml
<!--
	<list> 태그를 이용해 객체의 자료구조형 필드에 요소을 입력할 수 있음를
-->

<bean class="경로.클래스파일명(확장자 생략)" id="id값">
		<property name="필드명(자료구조)">
			<list>
				<value>값</value> <!-- primitive 타입 입력 -->
				<ref bean="c4"/> <!-- 생성된 객체 타입 입력 -->
				<bean class="경로.클래스파일명(확장자 생략)"/> <!-- 객체 타입 생성해 입력 -->
				...
			</list>
		</property>
	</bean>
```

## 예시 코드: 외부 properties 파일에서 값 가져오기

```xml

<!-- 외부 ~.properties 파일 위치를 설정하는 클래스 선언 -->
<bean class="org.springframework.context.support.PropertySourcesPlaceholderConfigurer">
	<property name="location">
		<value>classpath:경로/~.properties</value>
	</property>
</bean>

<!--
	두 개 이상의 properties 파일을 가져올 때
	property name값 변화에 주의
-->
<bean class="org.springframework.context.support.PropertySourcesPlaceholderConfigurer">
	<property name="locations">
		<array>
			<value>classpath:경로/~.properties</value>
			<value>classpath:경로/~.properties</value>
		</array>
	</property>
</bean>

<!-- ${key값}으로 외부 ~.properties 파일에 저장한 value값 호출 -->
<bean class="경로.클래스파일명(확장자 생략)" id="아이디값">
	<property name="필드명" value="경로.${key값}"/>
</bean>
```

```xml
<!--
	namespace에서 context - http://www.springframework.org/schema/context를 추가하면
	PropertySourcesPlaceholderConfigurer 자동 등록 설정할 수 있음
-->
xmlns:context="http://www.springframework.org/schema/context"

<context:property-placeholder location="classpath:경로/~.properties, classpath:경로/~.properties..."/>
```

## 예시 코드: 외부 xml 파일에서 값 가져오기

```xml
<!--
	외부 ~.xml 문서 import하기
	임포트 한 뒤에는 현재 xml 파일에 존재하는 것처럼 호출하면 호출됨
-->
<import resource="classpath:경로/~.xml"/>
```

## 예시 코드: autowire

```xml
<!--
	세터나 생성자에 주입시킬 객체를 자동으로 찾아내 xml 태그를 간소화시키는 것
	
	byType: 타입이 같은 객체를 자동으로 찾아 setter를 주입
	        없으면 생략, 동일한 타입이 2개 이상 있을 때에는 오류 발생
	byName: xml id와 java property 이름이 동일한 객체를 찾아 setter를 주입
	        이름이 달라도 오류가 나지는 않지만 주입되지 않음
	constructor: 생성자 파라미터를 주입함
	             먼저 byType으로 객체를 찾고, 동일한 타입이 2개 이상일 경우 byName으로 찾음
	             이 때 byName의 경우 xml의 id와 생성자의 parameter 이름과 동일해야 함(필드명X)
	             - 이름이 다르면 생성자 주입X
-->
<bean class="경로.클래스파일명(확장자 생략)" id="아이디값" autowire="default | byType | byName | constructor"/>

```

## 예시 코드: 생성 어노테이션 @Component, @Repository, @Service, @Controller

```xml
<!--
	Bean을 등록하는 어노테이션
	
	@Component: 컴포넌트를 나타내는 일반적인 스테레오 타입, <Bean> 태그와 동일한 역할
	@Repository: 퍼시스턴스 레이어, 영속성을 가지는 속성(파일, 데이터베이스)를 가진 클래스에 사용
	@Service: 서비스 레이어, 비즈니스 로직을 가진 클래스에 사용
	@Controller: 프레젠테이션 레이어, 웹 어플리케이션 웹 요청과 응답을 처리하는 클래스에 사용

	@Repository, @Service, @Controller는 @Component를 구체화한 형태
	기본적으로 객체를 singleton으로 관리하기 때문에 두 번 입력해 객체 두 개를 생성하는 건 불가능
	@Scope 어노테이션으로 설정을 바꿀 수 있음
-->

<!--
	클래스를 스캔해 Bean으로 등록하기 위한 태그
	<context:annotation-config/> 기능을 포괄함
-->
<context:component-scan base-package="패키지 경로"/>
```

```java
/*
* 클래스 선언부 위에서 어노테이션 입력
* */ 

@Component | @Repository | @Service | @Controller("id값") // id 기본값: 첫 글자를 소문자로 바꾼 클래스명
@Scope("singleton | prototype | request | session") // bean의 scope와 같은 역할
public class 클래스명{}
```

## 예시 코드: 주입 어노테이션 @Autowired, @Qualifier, @Value, @Resource

### @Autowired, @Qualifier

```xml
<!--
	주입시킬 객체를 자동으로 찾아내는 어노테이션
	
	@Autowired: spring에서 제공하는 어노테이션
	            프로퍼티, 세터, 생성자, 일반 메소드에 적용 가능하며 타입 > 이름으로 주입함
	@Qualifier: 동일한 타입이 여러 개 있을 경우 특정 Bean을 찾음
	            @Autowired와 함께 사용
-->

<!-- @Autowired를 자바에서 사용하기 위해 필요한 객체 등록 -->
<bean class="org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor"/>

<!-- Spring Annotation들을 사용하기 위해 필요한 객체 전체 등록 -->
<context:annotation-config/>
```

```java
// 자바 파일 필드 선언부 윗줄에 @Autowired 작성(Autowired를 사용할 모든 필드마다 작성)
@Autowired
@Qualifier("xml 파일 value값") // xml 파일에서 생성한 id와 필드명이 다를 때 호출해올 값을 알려주기 위해 사용
private 필드타입 필드명;
```

### @Value

```java
/**
 * primitive 멤버 필드에 값을 초기화할 때 사용하는 어노테이션
 * 
 * @Value: spring에서 제공하는 어노테이션
 *         primitive 멤버 필드에 값을 주입함
 * */

// 자바 파일 필드 선언부 윗줄에 @Value작성(초기화할 모든 필드에 작성)
@Value("초기화할 값")
private 필드타입 필드명;
```

### @Resource

```xml
<!--
	@Resource: javax에서 제공하는 어노테이션
	           프로퍼티와 세터에 적용 가능하며 이름으로 주입함
-->

<!-- @Resource를 자바에서 사용하기 위해 pom.xml에 dependency 추가 -->
<dependency>
    <groupId>javax.annotation</groupId>
    <artifactId>javax.annotation-api</artifactId>
    <version>1.3.2</version>
</dependency>
```

```java
// 자바 파일 필드 선언부 윗줄에 @Resource 작성(Resource를 사용할 모든 필드마다 작성)
@Resource(name = "name값")
```

# AOP

## Aspect Oriented Programming

- 관점 지향 프로그래밍
- 프로그램의 기능 중 핵심 기능과 중복되는 공통 기능을 완전히 분리한 뒤 공통 기능을 따로 제작해 재사용하는 것
- ex) 보안, 트랜잭션, 로그, 세션 유무 처리, 한글 인코딩 처리 등

## 용어 정리

- Advice: Spring에서 AOP에 의한 공통 기능(=공통 관심 사항)을 부르는 용어, Joinpoint에 삽입되어 동작할 수 있는 코드
- target: Advice를 적용해야 하는 각각의 클래스, 핵심 기능을 구현한 클래스
- JoinPoint : 어플리케이션을 실행할 때 특정 작업이 시작되는 시점, 특정 메소드가 시작되는 지점, Advice를 삽입하는 지점
- Pointcut: 여러 개의 Joinpoint를 하나로 묶은 것, 정규식 표현식을 사용해 묶음
- Advisor: Pointcut + Advice = Advisor
- Aspect: 하나의 advice가 타겟 대상에 적용되는 전체 과정(advice 하나 당 하나의 Aspect)
- AOP Proxy Server: joinpoint에 advice를 삽입해주는 도구
- Weaving: AOP Proxy Server에서 joinpoint에 advice를 삽입해주는 것

## Advice

- Spring에서 AOP에 의한 공통 기능(=공통 관심 사항)을 부르는 용어
- 직접 호출 ❌ AOP Proxy Server에서 자동으로 joinpoint가 호출되기 전이나 후에 advice를 삽입해줌(=Weaving)
- around: 사전, 사후 처리를 모두 하는 advice
- before: 사전 처리만 하는 advice
- after: 예외 발생 여부와 관계없이 무조건 사후 처리 하는 advice
- after-returning: 정상 동작 시에만 사후 처리하는 advice
- after-throwing: 예외가 발생했을 때만 사후 처리하는 advice

## AOP Proxy Server

- joinpoint에 advice를 삽입해주는 도구
- 물리적으로 존재하는 서버 ❌ 개념적으로 존재
- 생성 방법
    - J2SE: 디폴트 방식. 자바 기본 문법을 사용. 인터페이스가 있을 경우 인터페이스에서 작업해야 함
    - CGLIB: 사전 처리만 하는 advice
- 적용 방법
    - xml 기반 설정:
    - JavaBase설정(=Annotation)

## JoinPoint

- 어플리케이션을 실행할 때 특정 작업이 시작되는 시점, 특정 메소드가 시작되는 지점, Advice를 삽입하는 지점

## 예제코드: Around 방식 Advice

```xml
<!--
	AOP를 위한 추가 dependency
	모든 Advise는 pom.xml에 해당 dependency를 추가해야 사용 가능함
-->
<!-- https://mvnrepository.com/artifact/org.aspectj/aspectjweaver -->
<dependency>
  	<groupId>org.aspectj</groupId>
  	<artifactId>aspectjweaver</artifactId>
  	<version>1.9.6</version>
  	<scope>compile</scope><!-- 디폴트값은 runtime, compile로 바꿔줘야 임포트 가능 -->
</dependency>
```

```java
/**
* Around 방식 Advice 기본 패턴
* */
public Object around(ProceedingJoinPoint joinPoint) throws Throwable {
	// 사전 처리
	
	// 실제 타겟 대상을 호출
	Object obj = joinPoint.proceed();
	
	// 사후 처리
	
	return obj;
}
```

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
    
    	@ModelAttribute("{템플릿변수}")
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
        

## restful 서비스

> url 주소를 간소화해 데이터로 사용하는 것
> 

### 설정 방법

- Controller에 @ExceptionHandler 어노테이션 사용

```java
import org.springframework.web.servlet.mvc.Controller;

@Controller // Controller 어노테이션
@RestController // @Controller + @ResponseBody, AJAX 전용 컨트롤러 선언 시 사용
public class ~Controller {

	public void method(HttpServletRequest request, HttpServletResponse response) {
	} // Spring이나 자바에서 제공하는 클래스가 매개 변수로 필요한 경우 인수로 입력하면 Spring이 호출할 때 자동으로 입력해줌

}
```

# Upload, Download

## Upload

### 준비 작업

```xml
<!-- pom.xml에 파일 업로드 dependency 추가 -->
<dependency>
	<groupId>org.apache.commons</groupId>
	<artifactId>commons-io</artifactId>
	<version>1.3.2</version>
</dependency>
<dependency>
	<groupId>commons-fileupload</groupId>
	<artifactId>commons-fileupload</artifactId>
	<version>1.3.1</version>
</dependency>
```

```xml
<!-- servlet-context.xml에 파일 업로드에 필요한 Bean 생성 -->
<bean class="org.springframework.web.multipart.commons.CommonsMultipartResolver" id="multipartResolver"/>
```

### JSP(HTML) 마크업

```html
<form action="이동 경로" method="post" enctype="multipart/form-data">
<!-- 업로드 폼은 반드시 post 방식, enctype="multipart/form-data" 설정해야 함 -->
	<input type="file" name="file">
	<input type="submit" value="전송">
</form>
```

### Java 예제 코드

```java
/**
 * 폼 정보를 각 객체로 나누어 받을 경우
 * */

@RequestMapping("요청 경로")
// 인수의 MultipartFile 변수명은 input type="file" name과 맞춰야 함
// java 프로젝트 실제 경로를 가져오기 위해 인수로 HttpSession을 받음
public void upload(MultipartFile file, HttpSession session) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 저장할 경로 설정
	
	try {
		file.transferTo(new File(path + "/" + file.getOriginalFilename())); // 저장 경로 아래에 파일 저장
	} catch (Exception e) {
		e.printStackTrace();
	}

	// Model 객체로 넘길 수 있는 정보: file.get~()으로 받을 수 있는 정보
}
```

```java
/**
 * DTO로 파일을 받을 경우 
 * */

@RequestMapping("요청 경로")
// 인수로 받는 DTO의 객체 필드 이름은 input name과 맞춰야 함
// java 프로젝트 실제 경로를 가져오기 위해 인수로 HttpSession을 받음
public void upload(UploadDTO dto, HttpSession session) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 저장할 경로 설정
	
	try {
		dto.getFile().transferTo(new File(path + "/" + dto.getFile().getOriginalFilename()));
		// 저장 경로 아래에 파일 저장
	} catch (Exception e) {
		e.printStackTrace();
	}

	// Model이나 ModelAndView로 넘겨주지 않아도 자동으로 DTO에 저장된 정보가 view로 넘어감
}
```

## Download

### 준비 작업

```xml
<!-- servlet-context.xml에 파일 업로드에 필요한 Bean 생성 -->
<bean class="org.springframework.web.servlet.view.BeanNameViewResolver">
	<property name="order" value="1"/> <!-- 우선순위를 높여 가장 먼저 시도하게 함 -->
</bean>
```

### JSP(HTML) 마크업

```html
<!-- 다운로드 기능 구현 마크업 -->

<a href="${pageContext.request.contextPath}/이동할 경로?fileName=${fileName}">${fileName}</a>
```

### Java 예제 코드

```java
/**
 * 다운로드 목록 가져오기
 * */
@RequestMapping("/downList.do")
// java 프로젝트 실제 경로를 가져오기 위해 인수로 HttpSession을 받음
public void download(HttpSession session, Model model) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 파일을 저장한 경로 설정
	File file = new File(path); // 저장 경로를 파일 객체로 저장
	String[] fileNames = file.list(); // file 안에 있는 파일 리스트 이름을 배열로 저장
	
	model.addAttribute("fileNames", fileNames);
	// Model이나 ModelAndView로 리스트 넘겨주기
}
```

```java
/**
 * 다운로드 기능 구현용 view
 * : 페이지 이동 없이 현재 화면에서 다운로드 할 수 있도록 제작
 * */
@Component
public class DownLoadCustomView extends AbstractView{
// AbstractView를 상속받아 오버라이딩한 클래스 자체가 view 역할을 함

	@Override
	protected void renderMergedOutputModel(Map<String, Object> map,
		HttpServletRequest request, HttpServletResponse response) throws Exception {
		
		File file = (File)map.get("fname"); // 다운로드 할 파일을 fname으로 꺼냄
		
		response.setContentType("application/download;charset-UTF-8");
		response.setContentLength((int)file.length());
		
		String userAgent = request.getHeader("User-Agent");
		
		boolean isInternetExplorer = userAgent.indexOf("MSIE") > -1;
		String fileName = null;
		
		// 브라우저 종류에 맞춰 인코딩
		if(isInternetExplorer) {
			fileName = URLEncoder.encode(file.getName() , "UTF-8");
		} else {
			fileName = new String(file.getName().getBytes("UTF-8") , "iso-8859-1");
		}
		
		response.setHeader("Content-Disposition","attachment;filename=\"" + fileName.replace("+", "%20") + "\";");
		//response.setHeader("Content-Transfer-Encoding", "binary");
		
		OutputStream out = response.getOutputStream();
		FileInputStream fis = null;

		try {
			fis = new FileInputStream(file);
			FileCopyUtils.copy(fis, out); // inputStream 정보를 읽어 outputStream에 저장
		} catch(Exception e) {
			//map.put("error", e.toString());
			e.printStackTrace();
		} finally {
			if(fis != null) {
				try {
					fis.close();
				} catch(IOException ex) {}
			}
		}

		out.flush();
	}
}
```

```java
/**
 * 실제 다운로드 기능 구현
 * */
@RequestMapping("/down.do")
public ModelAndView down(String fileName, HttpSession session) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 파일을 저장한 경로 설정
	File file = new File(path + "/" + fileName); // 요청된 파일 이름으로 해당 파일 경로 설정
	
	return new ModelAndView("DownLoadCustomView", "fname", file);
	// 다운로드 기능 구현용 뷰에서 경로를 사용할 수 있도록 넘겨줌
	// 여기서 modelName은 구현 view에서 객체를 꺼낼 때 사용하는 이름과 맞춰줌
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

## 한글 인코딩

```xml
<!--
	Spring에서 인코딩 필터 처리를 제공한 것을 web.xml에 입력하면 한글 인코딩 처리 완료
-->
<filter>
	<filter-name>charaterEncoding</filter-name>
	<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
	<init-param>
		<param-name>encoding</param-name>
		<param-value>UTF-8</param-value>
	</init-param>
</filter>

<filter-mapping>
	<filter-name>charaterEncoding</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
```