# Spring Transaction

> Spring에서 제공하는 Advice를 이용해 여러 작업을 하나로 묶어 결과에 따라 한 번에 commit, rollback(트랜잭션 처리) 할 수 있음
> 

## API 종류

> Spring 트랜잭션 API는 같은 인터페이스(Platform Transaction Manager)를 구현한 구현체이기 때문에 다른 종류의 API로 바꿔도 정상 작동함
> 
- Java Transaction API(JTA): Jta Transaction Manager
- Hibernate: Hibernate Transaction Manager
- JDBC: DataSource Transaction Manager
- Java Persistence API(JPA): Jpa Transaction Manager

## 작동 원리

1. advice가 적용된 target 메소드를 호출하면 AOP Proxy가 호출됨
2. Transaction Advisor가 새로운 트랜잭션을 생성함
3. Custom interceptor들이 Transaction Advisor 전 후로 호출되어 target 메소드를 실행함
4. Transaction Advisor가 작업 결과에 따라 커밋, 롤백을 결정함
5. AOP Proxy가 결과를 받아 호출자에게 넘김

## 사용 설정

### dependency 추가

- MyBatis-Spring 사용 설정을 기반으로 dependency 추가
    
    [https://github.com/yudaGim/TIL/blob/main/Framework/Spring_library/MyBatis-Spring.md#](https://github.com/yudaGim/TIL/blob/main/Framework/Spring_library/MyBatis-Spring.md#%EC%82%AC%EC%9A%A9-%EC%84%A4%EC%A0%95)dependency-추가
    

```xml
<!-- pom.xml -->

<!-- Advice를 사용하기 위해 aspectjweaver 준비 -->
<dependency>
  	<groupId>org.aspectj</groupId>
  	<artifactId>aspectjweaver</artifactId>
  	<version>1.9.6</version>
  	<scope>compile</scope>
</dependency>
```

### Bean 등록

- MyBatis-Spring 사용 설정을 기반으로 dependency 추가
    
    [https://github.com/yudaGim/TIL/blob/main/Framework/Spring_library/MyBatis-Spring.md#Bean-](https://github.com/yudaGim/TIL/blob/main/Framework/Spring_library/MyBatis-Spring.md#%EC%82%AC%EC%9A%A9-%EC%84%A4%EC%A0%95)등록
    
- xml 방식
    
    ```xml
    <!-- mybatis-context.xml -->
    
    <!-- transaction 옵션 설정: xml 방식 사용 시 -->
    <tx:advice transaction-manager="transactionManager" id="txAdvice">
    	<tx:attributes>
    		<tx:method name="트랜잭션 적용할 메소드"/><!-- <tx:method/> 태그 속성은 아래 필기 참고 -->
    		<!-- 와일드카드로 묶이지 않는 여러 메소드에 적용하고 싶을 경우 <tx:method> 태그 추가 작성 가능 -->
    	</tx:attributes>
    </tx:advice>
    
    <aop:config>
    	<!-- 트랜잭션 advice 등록 -->
    	<aop:advisor advice-ref="txAdvice" pointcut="정규 표현식"/> 
    </aop:config>
    
    <!-- transaction 옵션 설정: annotation 방식 사용 시 -->
    <tx:annotation-driven transaction-manager="transactionManager"/>
    ```
    
- Annotation 방식
    
    ```java
    /**
     * Config.java
     * */
    
    /**
     * <tx:annotation-driven transaction-manager="transactionManager"/> 태그를 대신하기 위해
     * TransactionManagementConfigurer 구현하고 @EnableTransactionManagement 어노테이션 입력
     * */
    @EnableTransactionManagement
    public class Config implements TransactionManagementConfigurer {
    	
    /**
    	 * transaction 옵션 설정
    	 * */
    	@Bean // Bean 등록을 위한 어노테이션
    	public DataSourceTransactionManager getTransactionManager() {
    		DataSourceTransactionManager transactionManager = new DataSourceTransactionManager();
    		
    		transactionManager.setDataSource(getBasicDataSource());
    		
    		return transactionManager;
    	}
    	
    	/**
    	 * TransactionManagementConfigurer 인터페이스를 구현해 오버라이딩된 메소드
    	 * TransactionManager를 확장한 DataSourceTransactionManager를 사용할 것이기 때문에
    	 * DataSourceTransactionManager를 리턴하는 getTransactionManager() 메소드를 리턴
    	 * */
    	@Override
    	public TransactionManager annotationDrivenTransactionManager() {
    		return this.getTransactionManager();
    	}
    }
    ```
    

### 트랜잭션 전파

- 트랜잭션 처리 시 트랜잭션(커넥션) 생성, 유지 등 트랜잭션 전파를 설정할 수 있음
- <tx:method> 태그의 propagation 속성에서 설정 가능
- REQUIRED
    - 기본값
    - 메소드를 수행하는 데 트랜잭션 ⭕
    - 현재 진행 중인 트랜잭션이 존재하면 해당 트랜잭션을 사용하고, 존재하지 않으면 새로운 트랜잭션을 생성함
- MANDATORY
    - 메소드를 수행하는 데 트랜잭션 ⭕
    - 진행 중인 트랜잭션이 존재하지 않을 경우 Exception 발생
- REQUIRES_NEW
    - 메소드를 수행하는 데 트랜잭션 ⭕
    - 항상 새로운 트랜잭션을 시작함
    - 진행 중인 트랜잭션이 존재하면 기존 트랜잭션을 일시 중지하고 새로운 트랜잭션을 시작한 뒤, 새로운 트랜잭션이 종료되면 기존 트랜잭션을 계속함
- SUPPORTS
    - 메소드를 수행하는데 트랜잭션 ❌
    - 진행 중인 트랜잭션이 존재하면 해당 트랜잭션 사용, 진행 중인 트랜잭션이 존재하지 않더라도 메소드 정상 동작
- NOT_SUPPORTS
    - 메소드를 수행하는데 트랜잭션 ❌
    - 진행 중인 트랜잭션이 존재하면 메소드가 실행되는 동안 기존 트랜잭션을 일시 중지하고 메소드가 종료되면 기존 트랜잭션을 계속함
- NEVER
    - 메소드를 수행하는데 트랜잭션 ❌
    - 진행 중인 트랜잭션이 존재할 경우 Exception 발생
- NESTED
    - 메소드를 수행하는 데 트랜잭션 ⭕
    - 기존 트랜잭션이 존재하면 기존 트랜잭션과 중첩해 메소드 실행
    - 기존 트랜잭션이 존재하지 않으면 REQUIRED와 동일하게 동작
    - JDBC 3.0 이상이거나 JTA Provider가 기능을 지원할 때에만 사용 가능

### 트랜잭션 격리 레벨

- 다른 사용자가 테이블을 변경하고 있을 때 변경 내용에 대한 반영 여부 설정
- <tx:method> 태그의 isolation 속성에서 설정 가능
- DEFUALT
    - 기본 설정
    - Oracle의 경우 DEFUALT=READ_COMMITED
- READ_UNCOMMITED
    - 트랜잭션에서 처리되는 중이거나 아직 커밋되지 않은 데이터를 읽을 수 있음
- READ_COMMITED
    - 트랜잭션이 처리되는 동안 해당 데이터를 읽을 수 없음
    - = 커밋이 완료된 트랜잭션만 읽을 수 있음
- REPEATABLE_READ
    - 트랜잭션이 시작되기 전에 커밋한 데이터만 읽을 수 있음
    - 처음 읽어 온 데이터와 두 번째 읽어 온 데이터가 동일한 값을 가짐
- SERIALIZABLE
    - 동일한 데이터에 대해 동시에 두 개 이상의 트랜잭션 수행 ❌

### 기타 설정

- <tx:method> 태그 속성으로 설정 가능
- name
    - 트랜잭션을 적용할 메소드 이름 작성
    - 와일드카드 사용 가능
- rollback-for
    - 트랜잭션을 rollback할 exception 타입 설정
    - 기본적으로 비체크 예외가 일어났을 때만 rollback: 체크 예외는 실행된 곳까지 commit
- no-rollback-for
    - 트랜잭션을 rollback하지 않을 exception 타입 설정
    - 기본적으로 비체크 예외가 일어났을 때만 rollback: 체크 예외는 실행된 곳까지 commit

## 예제 코드

### xml 방식

```java
@Service
public class Service {
	public int method(TransferDTO transfer) {
		트랜잭션 실행문;
	}
}
```

### Annotation 방식

```java
// annotation 방식

@Service
// 클래스 안의 모든 메소드에 트랜잭션 처리를 하고 싶을 때 클래스명 위에 어노테이션 사용
@Transactional(속성 = "속성값", 속성 = "속성값"...)
public class Service {

	// 클래스 안의 특정 메소드에만 트랜잭션 처리를 하고 싶을 때 메소드명 위에 어노테이션 사용
	@Transactional(속성 = "속성값", 속성 = "속성값"...)
	public int method(TransferDTO transfer) {
		트랜잭션 실행문;
	}
}
```