# Aspect Oriented Programming

- = 관점 지향 프로그래밍
- 프로그램의 기능 중 핵심 기능과 중복되는 공통 기능을 완전히 분리한 뒤 공통 기능을 따로 제작해 재사용하는 것
- ex) 보안, 트랜잭션, 로그, 세션 유무 처리, 한글 인코딩 처리 등

## 용어 정리

### Advice

- Spring에서 AOP에 의한 공통 기능(=공통 관심 사항)을 부르는 용어

### target

- Advice를 적용해야 하는 핵심 기능을 구현한 메소드

### JoinPoint

- 어플리케이션을 실행할 때 특정 작업이 시작되는 시점
- = Advice를 삽입하는 지점
- ≠ JoinPoint, proceedingJoinPoint 인터페이스

### Pointcut

- 여러 개의 Joinpoint를 하나로 묶은 것
- 정규 표현식을 사용해 패턴화함

### JoinPoint Interface

- Advice에서 핵심 기능을 구현한 메소드에 대해 알 수 있도록 정보를 제공하는 인터페이스
- JoinPoint: 실제 타겟 대상(=메소드)의 정보를 가져오는 메소드 제공
- proceedingJoinPoint: JoinPoint의 확장 개념, 메소드에 대한 정보를 가져오거나 타겟 대상을 호출하는 메소드 제공

### Advisor

- Spring에서 Pointcut과 Advice를 묶어 부르는 용어

### Aspect

- 하나의 advice가 타겟 대상에 적용되는 전체 과정
- advice 하나 당 하나의 Aspect

### AOP Proxy Server

- joinpoint에 advice를 삽입해주는 도구

### Weaving

- AOP Proxy Server에서 joinpoint에 advice를 삽입해주는 것

## 사용 설정

```xml
<!-- AOP 사용하기 위해 dependency 추가 -->
<dependency>
  	<groupId>org.aspectj</groupId>
  	<artifactId>aspectjweaver</artifactId>
  	<version>1.9.6</version>
  	<scope>compile</scope> <!-- 기본값 runtime: java 베이스로 테스트하고 싶다면 compile로 변경 -->
</dependency>
```

## AOP Proxy Server

- joinpoint에 advice를 삽입(=weaving)해주는 도구
- 물리적으로 존재하는 서버 ❌ 개념적으로 존재

### 종류

- J2SE
    - 디폴트, 권장 방식
    - 타겟 대상에게 인터페이스가 있을 경우 구현체가 아닌 인터페이스로 접근해야 적용됨(=자바 규칙을 맞춰야 적용)
    
    ```java
    ApplicationContext context = new ClassPathXmlApplicationContext("xml 파일 경로");
    ControllerImpl controller= context.getBean("target", ControllerImpl.class); // 적용X
    Controller controller= context.getBean("target", Controller.class); // 적용O
    ```
    
- CGLIB
    - 타겟 대상에게 인터페이스가 있어도 구현체로 접근 가능
    
    ```java
    ApplicationContext context = new ClassPathXmlApplicationContext("xml 파일 경로");
    ControllerImpl controller= context.getBean("target", ControllerImpl.class); // 적용O
    Controller controller= context.getBean("target", Controller.class); // 적용O
    ```
    

### 생성 방법

```xml
<!--
	servlet-context.xml에 AOP Proxy Server 생성

	proxy-target-class: true일 경우 CGLIB, false일 경우 J2SE 방식으로 생성(기본값)
	expose-proxy: AopContext를 통해 메소드를 호출할 경우 사전/사후 처리 여부 선택
	              true일 경우 사전/사후 처리O, false일 경우 사전/사후 처리X -> 에러 발생(기본값)
-->

<!-- xml 방식 사용 시 -->
<aop:config proxy-target-class="boolean" expose-proxy="boolean">
</aop:config>

<!-- Annotation 방식 사용 시 -->
<aop:aspectj-autoproxy proxy-target-class="boolean" expose-proxy="boolean"/>
```

```java
// expose-proxy="true" 설정 후 AopContext를 사용하면 직접 호출 시 사전/사후 처리O
Controller controller = (Controller)AopContext.currentProxy();
controller.method();
```

### Weaving 적용 방법

- xml 기반 설정
    
    ```xml
    <!--
    	xml 기반 weaving 설정
    	: servlet-context.xml에 등록한 <aop:config> 태그 내에 <aop:aspect> 태그 입력
    	  aspect 갯수만큼 <aop:aspect> 태그 작성 가능
    		하나의 aspect에서 실행할 advice의 갯수만큼 advice 작성 가능
    -->
    
    <aop:config>
    	<!-- 같은 포인트컷을 여러 aspect에서 사용하고 싶다면 미리 저장해두고 참조할 수 있음 -->
    	<aop:pointcut expression="정규 표현식" id="pointCut id값"/>
    
    	<!--
    		ref: bean으로 등록한 advice 객체의 id값
    		order: 하나의 타겟 대상(=비즈니스 로직 메소드)에 여러 애스펙트를 적용하고 싶을 경우 실행 순서 설정 가능
    	-->
    	<aop:aspect id="aspect id값" ref="advice bean id값" order="n(실행 순서)">
    
    		<!-- around 방식 advice일 때 -->
    		<aop:around method="메소드명" pointcut="정규 표현식" or pointcut-ref="pointCut id값"/>
    		
    		<!-- before 방식 advice일 때 -->
    		<aop:before method="메소드명" pointcut="정규 표현식" or pointcut-ref="pointCut id값"/>
    
    		<!-- afterReturning 방식 advice일 때 -->
    		<aop:afterReturning method="메소드명" pointcut="정규 표현식" or pointcut-ref="pointCut id값"
    		returning="변수명"/> <!-- return값을 인수로 받고싶을 때 return값을 받을 Object 인수 변수명을 입력 -->
    		
    		<!-- afterThrowing 방식 advice일 때 -->
    		<aop:afterThrowing method="메소드명" pointcut="정규 표현식" or pointcut-ref="pointCut id값"
    		throwing="변수명"/> <!-- 예외 정보를 받고 싶을 때 예외 정보를 받을 Throwable 인수 변수명을 입력 -->
    
    		<!-- after 방식 advice일 때 -->
    		<aop:after method="메소드명" pointcut="정규 표현식" or pointcut-ref="pointCut id값"/>
    
    	</aop:aspect>
    </aop:config>
    ```
    
- JavaBase 설정 = Annotation 방식
    
    ```xml
    <!--
    	Annotation 방식 weaving 설정
    	: <aop:aspectj-autoproxy> 태그를 사용해 AOP Proxy Server 생성
    -->
    
    <aop:aspectj-autoproxy/> <!-- AOP 어노테이션 자동 스캔 -->
    ```
    
    ```java
    /**
     * 클래스명 위에 어노테이션 추가
     * */
    @Component// 객체 생성
    @Aspect // 공통 관심 사항 생성
    @Order(n) // 하나의 타겟 대상에 실행할 애스팩트가 두 개 이상인 경우 실행 순서 설정 가능
    public class Advice {
    
    	// advice 메소드 상단에 사용할 방식의 어노테이션 입력
    	@Around("정규 표현식 | pointCut클래스명.메소드명()")
    	@Before("정규 표현식 | pointCut클래스명.메소드명()")
    	@AfterReturning(pointcut = "정규 표현식 | pointCut클래스명.메소드명()", returning = "변수명") // 리턴값을 받을 변수명 입력
    	@AfterThrowing(pointcut = "정규 표현식 | pointCut클래스명.메소드명()", throwing = "변수명") // 예외 정보를 받을 변수명 입력
    	@After("정규 표현식 | pointCut클래스명.메소드명()")
    	public 리턴타입 메소드명(파라미터) {}
    
    }
    ```
    
    ```java
    /**
     * 같은 포인트컷을 여러 aspect에서 사용하고 싶다면 클래스 내의 메소드에서 미리 선언해두고 참조할 수 있음
     * */
    
    public class PointCutClass{
    
    	@Pointcut("정규 표현식")
    	public void pointCutMethod() {}
    
    }
    ```
    
- 참고: pointcut 정규 표현식
    
    ```xml
    <!--
    	pointcut 정규 표현식
    	: 와일드 카드 사용 가능, 대소문자 구분
    
    	0개 이상의 모든 파라미터를 입력받는 메소드를 표현하고 싶을 경우 메소드명(..) 형태로 작성
    -->
    pointcut="execution(접근제한자 리턴타입 패키지경로.클래스명.메소드명(인수 형태))"
    ```
    

## Advice

- Spring에서 AOP에 의한 공통 기능(=공통 관심 사항)을 부르는 용어
- 공통 관심 사항을 구현한 메소드
- 직접 호출 ❌ AOP Proxy Server에서 자동으로 joinpoint가 호출되기 전이나 후에 advice를 삽입해줌(=Weaving)

### Around Advice

- 사전, 사후 처리를 모두 하는 advice

```java
/**
 * Around 방식 Advice 기본 패턴
 * : 사전 처리와 사후 처리를 나눌 지점을 명시하기 위해 중간에 타겟을 호출하는 방식으로 제작
 * 
 * @return: 타겟 대상의 리턴값을 리턴: 어떤 type으로 리턴될 지 알 수 없기 때문에 Object type으로 리턴
 * @param: ProceedingJoinPoint
 *         - 타겟 대상의 정보를 제공하는 JoinPoint를 확장해 타겟 대상을 실행시키는 proceed() 메소드를 추가한 객체
 *           proceed()를 이용해 타겟 대상 호출(=비즈니스 로직 실행)시킴
 * @throws: Throwable - 타겟 대상 호출(=비즈니스 로직 실행)했을 때 발생할 수 있는 예외/에러를 던짐
 * */

@Around("정규 표현식") // 어노테이션 방식으로 생성할 때 입력, xml 방식 사용 시 X
public Object around(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
	// 사전 처리
	
	// 실제 타겟 대상 or 다음에 처리할 advice 호출 (=비즈니스 로직 실행)
	Object obj = proceedingJoinPoint.proceed();
	
	// 사후 처리
	
	return obj;
}
```

### Before Advice

- 사전 처리만 하는 advice

```java
/**
 * Before 방식 Advice 기본 패턴
 * : 사전 처리만 진행하기 때문에 타겟 대상 호출 X 사전 처리 종료 후 자동으로 타겟 대상이 실행됨
 * 
 * @param: JoinPoint - 타겟 대상의 정보를 제공하는 JoinPoint 객체를 이용해 필요한 타겟 대상 정보를 가져옴
 * */

@Before("정규 표현식") // 어노테이션 방식으로 생성할 때 입력, xml 방식 사용 시 X
public void before(JoinPoint joinPoint) {
	// 사전 처리
}
```

### After-returning Advice

- 정상 동작 시에만 사후 처리하는 advice

```java
/**
 * After-returning 방식 Advice 기본 패턴
 * : 타겟 대상이 실행되고 난 뒤에 실행되기 때문에 타겟 대상 호출 X
 * 
 * @param: JoinPoint - 타겟 대상의 정보를 제공하는 JoinPoint 객체를 이용해 필요한 타겟 대상 정보를 가져옴
 *         Object obj - Weaving에서 설정 시 타겟 대상의 리턴값이 자동으로 입력되어 들어옴
 * */

@AfterReturning("정규 표현식") // 어노테이션 방식으로 생성할 때 입력, xml 방식 사용 시 X
public void afterReturning(JoinPoint joinPoint) {
	// 사후 처리
}
```

### After-throwing Advice

- 예외가 발생했을 때만 사후 처리하는 advice

```java
/**
 * After-throwing 방식 Advice 기본 패턴
 * : 타겟 대상이 실행되고 난 뒤에 실행되기 때문에 타겟 대상 호출 X
 * 
 * @param: JoinPoint - 타겟 대상의 정보를 제공하는 JoinPoint 객체를 이용해 필요한 타겟 대상 정보를 가져옴
 *         Throwable - 예외가 발생했을 때 해당 예외 정보를 Throwable을 통해 받음
 * */

@AfterThrowing("정규 표현식") // 어노테이션 방식으로 생성할 때 입력, xml 방식 사용 시 X
public void afterThrowing(JoinPoint joinPoint, Throwable e) {
	// 사후 처리
}
```

### After Advice

- 예외 발생 여부와 관계없이 무조건 사후 처리 하는 advice

```java
/**
 * After 방식 Advice 기본 패턴
 * : 타겟 대상이 실행되고 난 뒤에 실행되기 때문에 타겟 대상 호출 X
 * 
 * @param: JoinPoint - 타겟 대상의 정보를 제공하는 JoinPoint 객체를 이용해 필요한 타겟 대상 정보를 가져옴
 * */

@After("정규 표현식") // 어노테이션 방식으로 생성할 때 입력, xml 방식 사용 시 X
public void around(JoinPoint joinPoint) {
	// 사후 처리
}
```

### 참고: JoinPoint와 ProceedingJoinPoint 주요 메소드

- JoinPoint
    
    ```java
    Object obj = joinPoint.getSignature(); // 타겟 대상(=비즈니스 로직을 구현한 메소드)를 리턴함
    
    String methodName = joinPoint.getSignature().getName(); // 타겟 대상의 이름을 가져옴
    
    Object[] params = joinPoint.getArgs(); // 타겟 대상의 파라미터들을 리턴함
    ```
    
- ProceedingJoinPoint
    
    ```java
    /**
     * 타겟 대상(=비즈니스 로직을 구현한 메소드)를 호출해 실행하고 결과값을 리턴함
     * */
    Object obj = proceedingJoinPoint.proceed();
    ```
    

## 예제 코드: 메소드 내에서 호출한 메소드에서 advice 적용하는 방법

```java
public void method() {

	/**
	 * 1. AOP Proxy Server 생성 시 expose-proxy 속성을 true로 지정
	 * 2. AopContext 객체를 이용해 AOP Proxy Server로부터 메소드 호출
	 * */
	LogicClass logicClass = (LogicClass)AopContext.currentProxy();
	logicClass.logicMethod();

}
```