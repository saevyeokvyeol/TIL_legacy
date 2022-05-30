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

# 객체-테이블 매핑

```java
@Entity // hibernate.hbm2ddl.auto 설정에 따라 객체와 대응하는 테이블 생성
@Table(name = "table_test") // 생성할 테이블 이름 변경
public class Table {
	
	@Id // Primary Key 설정
	
	/*
	 * @GeneratedValue: 생성된 컬럼에 자동으로 값을 넣어줄 때 사용
	 * 
	 * strategy: persistence provider가 엔티티 기본키를 생성할 때 사용할 PK 생성 전략
	 *           GenerationType.AUTO - 벤더에 맞춰 hibernate 내부에서 시퀀스를 생성해 할당(기본값)
	 *                                 동일한 hibernate로 생성한 모든 테이블에서 같은 시퀀스 공유
	 *                                 Oracle-SEQUENCE, MySQL-AUTOINCREMENT, MSSQL-IDENTITY
	 *           GenerationType.SEQUENCE - Oracle 시퀀스 사용(Oracle 전용)
	 *                                     반드시 @SequenceGenerator와 함께 사용하지 않으면 
	 *           GenerationType.TABLE - 테이블이 직접 키를 만들어 사용하는 방법(MySQL, MSSQL 전용)
	 *           GenerationType.IDENTITY - MySQL, MSSQL의 IDENTITY 사용(MySQL, MSSQL 전용)
	 * */
	@GeneratedValue(strategy = GenerationType.AUTO)

	/*
	 * @SequenceGenerator: 시퀀스를 생성하는 어노테이션
	 * name: SequenceGenerator 이름
	 *       @GeneratedValue의 strategy 속성이 GenerationType.SEQUENCE일 경우
   *       @GeneratedValue의 generator 속성에 SequenceGenerator 이름을 동일하게 주어야 시퀀스 작동
	 * allocationSize: 시퀀스 숫자 증가치
	 * sequenceName: 실제로 생성될 시퀀스 이름
	 * */
	@SequenceGenerator(name = "SequenceGenerator 이름", allocationSize = 증가치, sequenceName = "시퀀스명")
	private Long pk;

	// 컬럼명, null 허용 여부, 컬럼의 데이터 크기 등 컬럼 설정 변경
	@Column(name = "field_column", nullable = false, length = 100)
	private String fieldColumn;

	/*
	 * @@UpdateTimestamp: insert, update될 때 자동으로 현재 날짜와 시간 설정
	 *                    Date와 LocalDateTime 형식 사용 가능 -> Oracle에 생성될 때는 둘 다 timestamp 타입으로 생성
	 * */
	@CreationTimestamp
	private Date dateColumn;
	
	@UpdateTimestamp // insert, update될 때 자동으로 현재 날짜와 시간 설정, Date와 LocalDateTime 형식 사용 가능
	private LocalDateTime dateColumn; // JAVA LocalDateTime(JDK 1.8 추가) == Oracle timestamp	

	/*
	 * @Temporal: 특정 날짜 입력 시 사용 가능, Date 형식만 사용 가능
	 *            TemporalType.DATE - Date 타입(연/월/일만 입력)으로 컬럼 생성
	 *            TemporalType.TIMESTAMP - TIMESTAMP 타입(연/월/일 시:분:초 입력)으로 컬럼 생성
	 * */
	@Temporal(TemporalType.DATE)
	private Date dateColumn;

	/*
	 * 연관관계 생성 어노테이션: 테이블끼리의 연관관계를 생성하는 어노테이션
	 * 
	 * @ManyToOne - 다:1 연관관계, 즉시 로딩(select 할 때 연관관계 테이블 자동 조인)
	 * @OneToOne - 1:1 연관관계, 즉시 로딩
	 * @OneToMany - 1:다 연관관계, 지연 로딩(필요할 때만 연관관계 테이블 조인, 권장)
	 *              mappedBy = "부모 테이블명=현재 객체의 테이블명" 속성 입력해야 조인 가능
	 * 
	 * 즉시 로딩을 지연 로딩으로 만들기: fetch = FetchType.LAZY 속성 입력(권장)
	 * 지연 로딩을 즉시 로딩으로 만들기: fetch = FetchType.EAGER 속성 입력
	 * */
		@OneToMany(mappedBy = "자식 객체에 생성된 부모 객체 필드명") // 1:다 연관관계 생성
	@JoinColumn(name = "컬럼명") // Foreign Key 이름 변경
	private List<ChildTable> list;

	@ManyToOne(fetch = FetchType.LAZY) // 다:1 연관관계 생성, 지연 로딩 설정
	private Team team;
}
```

# 기본 SELECT, INSERT, UPDATE, DELETE

## SELECT

```java
/**
 * 입력한 객체 = 입력한 테이블, 입력한 pk값 = DB에 저장된 pk값인 레코드를 객체에 매핑해 가져옴
 * 만일 관계가 있는 테이블일 경우 모든 관계를 자동 조인해 가져옴
 * */
Table table = entityManager.find(Table.class, pk값);
```

## INSERT

```java
/**
 * 객체를 생성해 entityManager.persist() 메소드 파라미터로 입력하면 해당 객체가 테이블에 INSERT
 * */
entityManager.persist(new Table(null, "첫 번째 레코드", new Date(), new Date(), new Date()));
```

```java
/**
 * 연관관계가 있을 경우 해당 파라미터로 연관관계 객체 입력
 * : 테이블의 FK에는 해당 객체의 PK값이 INSERT
 * */
Team team = entityManager.find(Team.class, pk값);
entityManager.persist(new Table(null, team));

Team team = new Team().setPk(pk값);
entityManager.persist(new Table(null, team));
```

## UPDATE

```java
/**
 * SELECT해 가져온 객체의 필드를 setter를 이용해 변경하면 자동 UPDATE
 * */
Table table = entityManager.find(Table.class, pk값);
table.setFieldColumn("수정할 내용");
```

## DELETE

```java
/**
 * SELECT해 가져온 객체를 entityManager.remove() 메소드 파라미터로 넘겨 DELETE
 * */
Table table = entityManager.find(Table.class, pk값);
entityManager.remove(table);
```

# JPQL

- 자바 객체 중심으로 쿼리를 작성하는 문법(테이블명, 컬럼명❌ 클래스 객체명, 필드명⭕)
- 사용자가 쿼리를 작성하면 JPA가 데이터베이스에 맞는 언어로 자동 변환해줌
- 조건이 다양하고 복잡한 SELECT문에 주로 사용
- SQL 문법과 유사하게 SELECT, FROM, WHERE, GROUP BY, HAVING, JOIN 지원
- 자바 객체 기반이기 때문에 대소문자 구분, 별칭 반드시 작성

## 예시 코드

### 기본 형태

```java
/**
 * 형식
 * */
String sql = "sql문";
List<클래스명> list = entityManager.createQuery(sql, 클래스명.class).getResultList();

/**
 * 예시
 * */
String sql = "select c from Customer c where c.userName = '김유다'";
List<Customer> list = entityManager.createQuery(sql, Customer.class).getResultList();
// 모든 컬럼을 가져올 때에는 *이 아니라 객체 별칭을 입력해 객체의 모든 필드에 매핑해 가져옴
// 테이블명, 컬럼명이 아니라 객체명, 필드명을 입력해야 하기 때문에 대소문자 구분해 입력
```

### 변수 입력

```java
/**
 * 변수명 입력 방식
 * */

// :변수명 형태로 SQL문에 변수 추가
String sql = "select c from Customer where c.userName = :name or c.addr = :addr";

// 메소드 체인 기법으로 파라미터 입력
List<Customer> list =
	entityManager.createQuery(sql, Customer.class).setParameter("name", "김유다").setParameter("addr", "센트럴파크").getResultList();
```

```java
/**
 * 파라미터 인덱스 방식
 * : like 연산자 사용 가능
 * */

// ?n 형태로 SQL문에 변수 추가
String sql = "select c from Customer c where c.userName = ?1 or c.addr like '%' || ?2 || '%'";

// 메소드 체인 기법으로 파라미터 입력
List<Customer> list =
	entityManager.createQuery(sql, Customer.class).setParameter(1, "김유다").setParameter(2, "센트럴파크").getResultList();
```