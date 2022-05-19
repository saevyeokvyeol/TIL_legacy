# 개념과 특징

- = Java Persistence API
- MyBatis처럼 영속성과 관련된 API
- JDBC를 대신해 DB와 연결되어 JDBC 코드와 파라미터 설정, 결과 매핑을 해줌
- 관계형 데이터베이스와 자바의 패러다임의 불일치로 인해 객체 지향 프로그래밍의 장점이 유실되는 것을 막아줌
- 각 데이터베이스 언어에 맞춰 SQL 기본 query문을 자동 생성해줌

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

## persistence.xml

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
			<property name="hibernate.dialect" value="org.hibernate.dialect.Oracle10gDialect"/> <!-- SQL문을 생성할 언어 -->

			<!-- 옵션 -->
			<property name="hibernate.show_sql" value="true"/> <!-- 콘솔창에 SQL문 출력 여부 -->
			<property name="hibernate.format_sql" value="true"/> <!-- 콘솔창에 SQL문 출력 여부 -->
			<property name="hibernate.use_sql_comments" value="false"/> <!-- 콘솔창에 SQL문 출력 여부 -->
			<property name="hibernate.id.new_generator_mappings" value="true"/> <!-- 콘솔창에 SQL문 출력 여부 -->

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