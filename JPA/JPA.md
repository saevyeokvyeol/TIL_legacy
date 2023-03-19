# 개념과 특징

- = Java Persistence API
- MyBatis처럼 영속성과 관련된 API
- JDBC를 대신해 DB와 연결되어 JDBC 코드와 파라미터 설정, 결과 매핑을 해줌
- 관계형 데이터베이스와 자바의 패러다임의 불일치로 인해 객체 지향 프로그래밍의 장점이 유실되는 것을 막아줌
- 각 데이터베이스 언어에 맞춰 SQL 쿼리문을 생성해주기 때문에 벤더에 독립적임
- JPA를 구현한 Hibernate, EclipseLink, DataNucleus 라이브러리를 통해 사용
- 도메인과 DTO을 자동으로 변환해줌
    - 도메인: DB와 1:1 매칭하는 객체, 서비스와 DAO가 주고받는 객체
    - DTO: view에서 사용할 수 있도록 변환된 객체, 컨트롤과 서비스가 주고받는 객체

# 사용 설정

## pom.xml 설정

```xml
<!-- pom.xml에 필요한 dependency 추가 -->

<!-- JPA가 사용하기 위한 JDBC 추가 -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc8</artifactId>
    <version>21.1.0.0</version>
</dependency>
	
<!-- 어노테이션을 사용하기 위해 lombok 추가 -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
    <scope>provided</scope>
</dependency>

<!-- JPA의 구현체 중 하나인 hibernate 추가 -->
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-entitymanager</artifactId>
    <version>5.6.9.Final</version>
</dependency>
```

## persistence.xml 설정

```xml
<!--
	persistence.xml 파일 설정
	src/main/java/META-INF 폴더 안에 위치해야함
-->

<?xml version="1.0" encoding="UTF-8"?>

<persistence version="2.1"
	xmlns="http://xmlns.jcp.org/xml/ns/persistence"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
	<persistence-unit name="JPAProject"> <!-- entityManagerFactory 이름 설정 -->
		<properties>

			<!-- 필수 속성 -->
			<property name="javax.persistence.jdbc.driver" value="oracle.jdbc.driver.OracleDriver"/>
			<property name="javax.persistence.jdbc.user" value="c##scott" />
			<property name="javax.persistence.jdbc.password" value="tiger" />
			<property name="javax.persistence.jdbc.url" value="jdbc:oracle:thin:@localhost:1521:XE"/>
			<property name="hibernate.dialect" value="org.hibernate.dialect.Oracle10gDialect"/> <!-- SQL문을 생성할 DB 방언 -->

			<!-- 옵션 -->
			<property name="hibernate.show_sql" value="true"/> <!-- 콘솔창에 SQL문 출력 여부 -->
			<property name="hibernate.format_sql" value="true"/>
			<property name="hibernate.use_sql_comments" value="false"/>
			<property name="hibernate.id.new_generator_mappings" value="true"/> <!-- sequence 설정 -->

			<!--
				@Entity 어노테이션이 입력된 객체를 찾았을 때 할 일 설정

				create: 테이블 생성
				create-drop: 테이블 드롭 후 생성
				update: 수정 사항이 있다면 반영
				none: 테이블 생성or수정 X
			-->
			<property name="hibernate.hbm2ddl.auto" value="none"/>
		</properties>

	</persistence-unit>
</persistence>
```

## 주요 컴포넌트 생성 및 닫기

```java
// EntityManagerFactory 생성(한 번 생성해 singleton으로 관리하며 재활용)
EntityManagerFactory entityManagerFactory = Persistence.createEntityManagerFactory(persistence-unit name값);

// EntityManager 생성(트랜잭션이 필요할 때마다 새로 생성)
EntityManager entityManager = entityManagerFactory.createEntityManager();

// 트랜잭션 생성
EntityTransaction entityTransaction = entityManager.getTransaction();

// 트랜잭션 시작
entityTransaction.begin();

// 트랜잭션 커밋
entityTransaction.commit();

// EntityManager 종료(트랜잭션이 종료되면 함께 종료)
entityManager.close();

// EntityManagerFactory 종료(모든 작업이 종료되면 함께 종료)
entityManagerFactory.close();
```