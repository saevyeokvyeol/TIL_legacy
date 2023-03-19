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