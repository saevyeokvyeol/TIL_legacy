# Spring

## 개념

- EJB의 단점을 보완해 나온 오픈 소스 프레임워크로 자바 기반의 경량 라이브러리 덩어리
- 복잡한 엔터프라이즈 어플리케이션 개발을 간단하게 만들어줌
- 기능을 모듈로 제공하기 때문에 필요한 기능만 가져다 사용할 수 있음
- 공공부문 정보화 산업 표준인 전자정부 프레임워크(eGov)가 스프링과 마이바티스를 기반으로 하기 때문에 국내에서 활성화됨
- 현재 주류 프레임워크

## 특징

- 가벼운 경량의 라이브러리 → 현재에는 다소 무거워짐
- 기반 코드를 제공함

### Dependency Injection

- 의존 관계 주입(=제어의 역행 IoC Inversion of Control)
- 필요한 객체를 개발자가 직접 생성❌ SpringContainer(=외부 조립기)가 적절하게 객체를 생성하고 주입하기 때문에 객체와 객체 간의 결합도가 느슨해짐

### 관점 지향 프로그래밍

- 프로그램 로직을 관점에 따라 핵심 로직과 공통 로직으로 분리해 공통 로직을 재사용하는 것

### Container

- 객체들의 라이프사이클을 관리해줌

## 사용 준비 작업

1. JDK 설치
2. IDE 설치(eclipse)
3. STS(SpringSource Tool Suite) 설치
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f401e5d5-6455-4caf-9bea-5bdba1ff0a0d/Untitled.png)
    
4. Maven or Gradle 세팅: 라이브러리와 빌드 프로세스를 관리해주는 툴

## IoC = DI

### Inversion of Control

- Inversion of Control(제어의 역전)
    - 객체의 생성부터 생명주기 관리까지 객체에 대한 모든 제어권이 바뀌었음을 의미
    - 컴포넌트의 의존 관계 결정, 설정 및 생성주기을 해결하기 위한 디자인 패턴
- IoC 컨테이너
    - 객체의 생성을 책임지고 의존성을 관리함
    - POJO의 생성, 초기와, 서비스, 소멸에 대한 권한을 가짐
    - 개발자들이 직접 POJO를 생성할 수 없는 것은 아님

### Dependency Injection

- Dependency Injection(의존 관계 역전)
    - 각 클래스 간의 의존 관계를 빈 설정 정보를 바탕으로 컨테이너가 자동 연결해주는 것
    - 빈 설정 관계에 의존 관계가 필요하다는 정보만 주면 자동 연결됨
    - 객체 레퍼런스를 컨테이너에서 주입받아 실행 시 동적으로 의존관계 생성
    - 컨테이너가 흐름의 주체가 되어 어플리케이션 코드에 의존관계를 주입함
    - 코드가 단순해지고 컴포넌트 간의 결합도가 제거되는 장점이 있음
- DI 종류
    - Setter Injection: 의존성을 입력받는 setter 메소드를 만들고 이를 통해 의존성 주입
    - Construction Injection: 필요한 의존성을 포함하는 클래스 생성자를 만들고 이를 통해 의존성 주입
    - Method Injection: 의존성을 입력받는 일반 메소드를 만들고 이를 통해 의존성을 주입

### Spring DI 컨테이너

- 빈Bean
    - 스프링이 IoC 방식으로 관리하는 객체(=클래스 )
- 빈 팩토리 BeanFactory
    - 스프링의 IoC를 담당하는 핵심 컨테이너
    - 빈을 등록, 생성, 조회, 반환함
    - getBean() 메소드가 정의되어 있음
- 어플리케이션 컨텍스트ApplicationContext
    - 빈을 등록, 생성, 조회, 반환하는 것과 동시에 각종 부가 서비스를 제공함
- 설정 메타 정보
    - BeanFactory, ApplicationContext이 IoC를 적용하기 위해 사용하는 메타 정보
    - Bean 객체를 생성하고 구성할 때 사용됨

### 예시 코드: 클래스 생성

```xml
<!--
	객체 생성
	아이디값 = new 클래스파일();

	scope="singleton": 사전 초기화-미리 메모리에 생성함
	scope="prototype": 지연 초기화-필요할 때=getBean()으로 호출할 때마다 새로 생성함
-->
<bean class="경로.클래스파일명(확장자 생략)" id="아이디값" scope="singleton | prototype | request | session"/>
```

```java
ApplicationContext context = new ClassPathXmlApplicationContext("클래스 패스부터의 경로/xml파일명");
ApplicationContext context = new FileSystemXmlApplicationContext("src부터의 경로/xml파일명");

MessageBean bean = context.getBean("아이디값", 클래스파일명.class); // 클래스를 bean 객체에 저장
bean.메소드명(); // 클래스의 메소드 호출
```

### 예시 코드: 파라미터가 있는 클래스 생성

```xml
<!--
	Primitive와 String 타입은 value로 파라미터값을 입력해 파라미터가 있는 생성자를 호출할 수 있음
	순서를 바꿔 넣을 경우 index로 인수 차례를 설정할 수 있음
-->
<bean class="경로.클래스파일명(확장자 생략)" id="아이디값">

	<constructor-arg value="파라미터값" index="차례"></constructor-arg>
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
<bean class="경로.클래스파일명(확장자 생략)" id="아이디값">

	<constructor-arg ref="파라미터로 넣을 아이디값"></constructor-arg>
	<!-- 위나 아래의 코드를 사용해 파라미터값을 넣음 -->
	<constructor-arg>
			<ref bean="파라미터로 넣을 아이디값"/>
		</constructor-arg>

</bean>
```

### 예시 코드: setter가 있는 클래스 생성

```xml
<!--
	Primitive와 String 타입은 value로 세터에 변수를 입력할 수 있음
	객체 타입은 ref로 세터에 변수를 입력할 수 있음
-->
<bean class="경로.클래스파일명(확장자 생략)" id="아이디값">
	<property name="변수명" value="변수값"></property>
	<property name="변수명" ref="변수값"></property>
</bean>
```