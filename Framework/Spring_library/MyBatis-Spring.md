> MyBatis를 대신해주는 library
> 

# 주요 컴포넌트

## SqlSessionFactoryBean

- Spring의 Bean 클래스: xml에 등록해야 사용 가능
- SqlSessionFactoryBuilder를 대신해 SqlSessionFactory 생성
- DataSource(DB 정보), mybatis-context.xml(환경 설정 문서), mapper

## SqlSessionTemplate

- Spring의 Bean 클래스: xml에 등록해야 사용 가능
- SqlSession의 구현체로 SQL을 실행하고 트랜잭션을 관리하는 역할

# 사용 설정

```xml
<!-- MyBatis-Spring이 사용할 jdbc 준비 -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc8</artifactId>
    <version>21.1.0.0</version>
</dependency>

<!-- MyBatis-Spring이 사용할 MyBatis 준비 -->
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.7</version>
</dependency>

<!-- MyBatis-Spring을 사용하기 위한 mybatis-spring 준비 -->
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis-spring</artifactId>
    <version>2.0.6</version>
</dependency>

<!-- db 프로그래밍을 위한 jdbc 준비 -->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-jdbc</artifactId>
    <version>5.3.13</version>
</dependency>

<!-- 데이터베이스와 연결하기 위해 dbcp 준비 -->
<dependency>
    <groupId>commons-dbcp</groupId>
    <artifactId>commons-dbcp</artifactId>
    <version>1.4</version>
</dependency>

<!-- DTO에서 어노테이션을 사용하기 위해 lombok 준비(선택 사항) -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
    <scope>provided</scope>
</dependency>

<!-- Spring-MyBatis 실행 과정을 보기 위해 log4j 준비(선택 사항) -->
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>

<!-- 주입 어노테이션을 사용하기 위해 javax.annotation 준비(선택 사항) -->
<dependency>
    <groupId>javax.annotation</groupId>
    <artifactId>javax.annotation-api</artifactId>
    <version>1.3.2</version>
</dependency>
```

```xml
<!--
	mybatis-context.xml: 환경 설정 문서
-->

<!-- 필요한 경우 property 파일 등록 -->
<context:property-placeholder location="/WEB-INF/spring/appServlet/*.properties"/>

<!-- DataSource(DB 정보) 등록 -->
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource"
		p:driverClassName="oracle.jdbc.driver.OracleDriver"
		p:url="jdbc:oracle:thin:@127.0.0.1:1521:xe"
		p:username="c##scott"
		p:password="tiger"
		p:maxActive="10"/>

<!-- SqlSessionFactoryBean 등록 -->
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">

	<!-- DataSource 등록 -->
	<property name="dataSource" ref="dataSource"/>

	<!-- mapper 등록: src/main/resources/mapper 폴더 안에 있는 모든 ~Mapper.xml 파일 -->
	<property name="mapperLocations" value="classpath:mapper/*Mapper.xml"/>

	<!-- 클래스 별칭 등록: yuda.mvc.dto 팩토리 안의 모든 클래스를 첫 글자를 소문자로 바꾼 클래스명으로 -->
	<property name="typeAliasesPackage" value="yuda.mvc.dto"/>
	
	<!-- 필요할 경우 SqlMapConfig.xml 등록 -->
	<property name="configLocation" value="classpath:SqlMapConfig.xml"/>
</bean>
```

```java
@Repository
@RequiredArgsConstructor
public class DAOImpl implements DAO {
	/**
	 * 어노테이션으로 주입한 뒤 사용
	 * : 자동으로 생성하고 닫기 때문에 메소드별로 새로 생성하고 닫을 필요X
	 * */
	private final SqlSession session;
}
```