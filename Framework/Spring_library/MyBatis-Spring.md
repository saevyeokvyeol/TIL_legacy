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

## dependency 설정

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

## Bean 등록

### xml 방식

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

<!-- SqlSessionTemplate 등록 -->
<bean id="sqlSession"	class="org.mybatis.spring.SqlSessionTemplate">
	<constructor-arg index="0" ref="sqlSessionFactory"/>
<bean>
```

### Annotation 방식

```java
/**
 * Config.java
 * */

@Configuration // Bean 등록 전용 클래스를 선언하기 위한 어노테이션
@PropertySource("/WEB-INF/spring/appServlet/dbInfo.properties") // properties 파일이 필요한 경우 가져옴
public class Config implements {
	
	@Autowired
	private Environment env; // properties 파일에 있는 모든 key와 value를 저장하는 객체
	
	@Value("${key값}")
	private String value;
	
	/**
	 * PropertySourcesPlaceholderConfigurer 등록
	 * 프로퍼티 파일을 가져오는 객체이기 때문에 다른 빈보다 더 먼저 실행되어야 함
	 * 때문에 객체 생성 시 가장 먼저 실행되는 static 메소드로 제작
	 * */
	@Bean // Bean 등록을 위한 어노테이션
	public static PropertySourcesPlaceholderConfigurer getPlaceholderConfigurer() {
		PropertySourcesPlaceholderConfigurer placeholderConfigurer = new PropertySourcesPlaceholderConfigurer();
		
		return placeholderConfigurer;
	}
	
	/**
	 * SqlSessionFactoryBean 등록
	 * */
	@Bean // Bean 등록을 위한 어노테이션
	public SqlSessionFactoryBean getFactoryBean() throws Exception {
		SqlSessionFactoryBean factoryBean = new SqlSessionFactoryBean();
		
		// DataSource 등록
		factoryBean.setDataSource(getBasicDataSource());
		
		/**
		 * PropertySourcesPlaceholderConfigurer 등록
		 * 프로퍼티 파일을 가져오는 객체이기 때문에 다른 빈보다 더 먼저 실행되어야 함
		 * 때문에 객체 생성 시 가장 먼저 실행되는 static 메소드로 제작
		 * */
		PathMatchingResourcePatternResolver patternResolver = new PathMatchingResourcePatternResolver();
		Resource[] resources = patternResolver.getResources("classpath:mapper/*Mapper.xml");
		factoryBean.setMapperLocations(resources);
		
		// 클래스 별칭 등록: yuda.mvc.dto 팩토리 안의 모든 클래스를 첫 글자를 소문자로 바꾼 클래스명으로
		factoryBean.setTypeAliasesPackage("yuda.web.mvc.*.dto");
		
		// 필요할 경우 SqlMapConfig.xml 등록
		PathMatchingResourcePatternResolver patternResolver2 = new PathMatchingResourcePatternResolver();
		Resource resource = patternResolver.getResource("classpath:SqlMapConfig.xml");
		factoryBean.setConfigLocation(resource);
		
		return factoryBean;
	}
	
	/**
	 * SqlSessionTemplate 등록
	 * */
	@Bean // Bean 등록을 위한 어노테이션
	public SqlSessionTemplate getSqlSessionTemplate() throws Exception {
		SqlSessionTemplate sqlSessionTemplate = new SqlSessionTemplate(getFactoryBean().getObject());
		
		return sqlSessionTemplate;
	}
	
	/**
	 * 인터페이스 기반 매퍼 등록
	 * */
	@Bean // Bean 등록을 위한 어노테이션
	public MapperFactoryBean<UserMapper> getUserMapper() throws Exception {
		MapperFactoryBean<UserMapper> userMapper = new MapperFactoryBean<UserMapper>();
		
		userMapper.setMapperInterface(UserMapper.class);
		userMapper.setSqlSessionFactory(getFactoryBean().getObject());
		
		return userMapper;
	}
		
	/**
	 * DataSource(DB 정보) 등록
	 * 임포트 시 org.apache.commons.dbcp.BasicDataSource로 임포트 해야 함
	 * */
	@Bean // Bean 등록을 위한 어노테이션
	public BasicDataSource getBasicDataSource() {
		BasicDataSource dataSource = new BasicDataSource();
		
		// Environment를 통해 value값을 가져옴
		dataSource.setDriverClassName(env.getProperty("driveName"));
		dataSource.setUrl(env.getProperty("url"));
		dataSource.setUsername(env.getProperty("dbUserName"));
		dataSource.setPassword(env.getProperty("password"));
		dataSource.setMaxActive(10);
		
		return dataSource;
	}
```

## dependency 설정

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