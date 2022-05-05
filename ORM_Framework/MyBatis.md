# 개념 및 특징

- ORM(Object Relation Mapping) Framework로 DB와 연결되어 JDBC 코드와 파라미터 설정, 결과 매핑을 해줌
- 3.x 버전부터 IBatis → MyBatis로 명칭이 변경되며 동적 쿼리를 지원함
- 조인 쿼리를 자동으로 DTO와 필드에 매핑해줌

# 주요 Component

## SqlSessionFactoryBuilder

- 최초에 단 한 번 만들어진 뒤 사라짐
- 최초에 한 번 SqlSessionFactory를 생성해줌
- SqlSessionFactory 생성을 위해 환경 설정 문서인 ~.xml 문서가 필요함

## SqlSessionFactory

- 최초에 단 한 번 만들어져 싱글톤으로 계속 사용됨
- 필요할 때마다 SqlSession을 새롭게 생성해줌

## SqlSession

- 필요할 때마다 생성해 사용한 뒤 닫음
- Connection과 동일한 개념
- CRUD 작업에 관련된 method를 제공
- transaction에 관련된 method를 제공

# 설정 및 사용 방법

## lib 준비

```xml
<!-- pom.xml -->

<!-- MyBatis가 사용할 jdbc 준비 -->
<dependency>
    <groupId>com.oracle.database.jdbc</groupId>
    <artifactId>ojdbc8</artifactId>
    <version>21.1.0.0</version>
</dependency>

<!-- MyBatis를 사용하기 위해 MyBatis 준비 -->
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.7</version>
</dependency>

<!-- DTO에서 어노테이션을 사용하기 위해 lombok 준비(선택 사항) -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
    <scope>provided</scope>
</dependency>

<!-- MyBatis 실행 과정을 보기 위해 log4j 준비(선택 사항) -->
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

## 설정 문서(~.xml) 준비

### SqlMapConfig.xml 생성 및 작성

> MyBatis 기본 환경 설정을 담당
> 

```xml
<!--
	SqlMapConfig.xml
	DbUtil.java 파일에서 사용하는 경로와 이름이 같으면 네이밍은 마음대로 해도 무관
-->

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd"> 

<configuration>
	<!--
		외부 ~.properties 파일을 이용해 key와 value값을 가져오고 싶을 때 설정
		경로 기준: src/main/java ( = classes)
	-->
	<properties resource="properties 파일 경로"/>
	
	<settings>
		<!--
			#{ename}에 값이 없을 때 null값으로 들어가도록 설정 변경
			value의 null은 무조건 대문자()
		-->
		<setting name="jdbcTypeForNull" value="NULL"/>

		<!-- 자바의 camel 표기법과 db의 snake 표기법을 매핑해주는 설정 -->
		<setting name="mapUnderscoreToCamelCase" value="true"/>
	</settings>
	
	<!-- 객체 별칭 만들기 -->
	<typeAliases>
		<typeAlias type="패키지 경로.객체명" alias="객체 별칭"/>
	</typeAliases>
	
	<environments default="development">
		<environment id="development">
			<transactionManager type="JDBC"/>
			<!--
				dataSource
				POOLED: 일정량의 커넥션을 확보해두는 방식(웹에서 사용)
				UNPOOLED: 커넥션 확보X(순수 자바 프로젝트에서 사용)
			-->
			<dataSource type="POOLED">
				<!--
					property value는 유지보수를 위해 외부 ~.properties 파일을 끌어와 ${key값}을 많이 사용함
				-->
				<property name="driver" value="드라이버 이름"/>
				<property name="url" value="url"/>
				<property name="username" value="DB 계정명"/>
				<property name="password" value="DB 비밀번호"/>
			</dataSource>
		</environment>
	</environments>
	
	<!--
		실제 CRUD SQL 문장을 작성하는 매퍼 등록
		여러 개의 매퍼를 등록하고 싶은 경우 <mappers> 태그 안에 <mapper> 태그 추가
	-->
	<mappers>
		<mapper resource="매퍼 경로"/>
	</mappers>
	
</configuration>
```

### ~Mapper.xml 생성

> 실제 CRUD SQL 문장을 작성
> 

```xml
<!--
	~Mapper.xml
	실제 CRUD SQL 문장을 작성함
-->

<?xml version="1.0" encoding="UTF-8" ?> 
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"> 

<!--
	namespace: 어떤 mapper에서 가져온 SQL 문장인지 식별하기 위해 생성
-->
<mapper namespace="별칭"> 
	<!-- 필요한 쿼리 작성(CRUD 작업) -->
</mapper>
```

## DbUtil.java 생성 및 작성

> MyBatis ORM 설정 세팅
> 

```java
/**
 * MyBatis ORM 설정 세팅
 * : 필드와 메소드를 static으로 제작해 모든 DAO 영역에서 생성 없이 사용
 * */
public class DbUtil {

	// 최초에 단 한 번 생성하고 싱글톤으로 사용하기 위해 static으로 static 필드로 생성
	private static SqlSessionFactory factory;
	
	/**
	 * SqlSessionFactoryBuilder를 이용해 SqlSessionFactory 생성
	 * */
	static {
		try {
			/**
			 * 환경 설정 문서 위치 저장
			 * 환경 설정한 xml 파일과 이름이 같으면 네이밍은 마음대로 해도 무관
			 * */
			String resource = "config/SqlMapConfig.xml";
			
			/**
			 * 환경 설정 문서를 Reader로 읽어옴
			 * */
			Reader reader = Resources.getResourceAsReader(resource);
			
			/**
			 * Reader로 읽은 환경 설정 문서로 SqlSessionFactory 생성
			 * */
			factory = new SqlSessionFactoryBuilder().build(reader);
		} catch (Exception e) {
			e.printStackTrace();
		}
	} // static block 종료
	
	/**
	 * SqlSession 객체를 리턴해주는 메소드 작성 - JDBC의 Connection과 동일한 역할
	 * : SqlSession은 CRUD 작업을 할 때마다 새롭게 생성하고 닫음
	 *   commit 또는 rollback을 이용해 transaction 처리를 함
	 *   자동 커밋X - DML(insert, update, delete) 작업 시 반드시 commit 또는 rollback 필수
	 * */
	public static SqlSession getSession() {
		// SqlSessionFactory에서 SqlSession을 열어 리턴해줌
		return factory.openSession();
	}
	
	/**
	 * 닫기 기능(DQL: select 전용)
	 * */
	public static void sessionClose(SqlSession session) {
		if(session != null) {
			session.close(); // session.close() 메소드에서 자동으로 예외처리
		}
	}
	
	/**
	 * 닫기 기능(DML:insert, update, delete 전용)
	 * @param: boolean state가 true인 경우 commit(), false인 경우 rollback()
	 * */
	public static void sessionClose(SqlSession session, boolean state) {
		if(session != null) {
			if(state) session.commit();
			else session.rollback();
			
			session.close(); // session.close() 메소드에서 자동으로 예외처리
		}
	} // sessionClose(SqlSession session, boolean state) 종료
}
```

## DAO 작성

> DbUtil.java과 ~Mapper.xml 문서를 이용해 CRUD 작업 실행
> 

```java
public class ~DAO {
	
	public void method() {
		SqlSession session = null;

		try {
			// 세션 로드
			session = DbUtil.getSession();

			/**
			 * ~Mapper.xml에 입력한 SQL문 실행
			 * */
			session.실행 메소드("mapper namespace값.SQL문 id값", 인수(필요한 경우 입력));

			// 필요한 추가 작업

		} finally {
			// 세션 종료
			DbUtil.sessionClose(session); // select문일 경우
			DbUtil.sessionClose(session, state); // insert, update, delete문일 경우
		}
	}
```

# 예제 코드: 기본 SELECT, INSERT, UPDATE, DELETE

## SELECT

```xml
<!--
	기본 select sql문
	id: DAO에서 매퍼의 namespace과 <select> 태그의 id값으로 SQL문을 호출할 때 사용
	parameterType: sql문에서 인수를 입력받을 경우 인수 타입 작성(옵션), 기본 타입과 객체 타입 모두 사용 가능
	resultType: sql문 결과로 출력될 타입을 입력(필수), 기본 타입과 객체 타입 모두 사용 가능
-->
<select id="id값" parameterType="인수 타입" resultType="결과 타입">
	select sql문
</select>
```

```java
public void select() {
	SqlSession session = null;
	try {
		// 로드
		session = DbUtil.getSession();

		// 연결
		결과타입 result = session.selectOne("mapper namespace값.select문 id값"[, sql문 파라미터]);
		// 결과가 하나인 경우

		List<결과타입> list = session.selectList("mapper namespace값.select문 id값"[, sql문 파라미터, RowBound rows]);
		// 결과가 여러 개인 경우
		// RowBound: 
		// session.select~() 메소드는 자동 캐스팅되기 때문에 캐스팅할 필요X

	} finally {
		// 닫기
		// select문이므로 인수로 닫을 session만 입력
		DbUtil.sessionClose(session);
	}
}
```

## INSERT

```xml

<!--
	기본 insert sql문
	id: DAO에서 매퍼의 namespace과 <insert> 태그의 id값으로 SQL문을 호출할 때 사용
	parameterType: sql문에서 인수를 입력받을 경우 인수 타입 작성(옵션), 기본 타입과 객체 타입 모두 사용 가능
-->
<insert id="id값" parameterType="인수 타입">
	insert sql문
</insert>
```

```java
public void insert() {
	SqlSession session = null;
	boolean state = false; // commit, rollback 여부 변수
	try {
		// 로드
		session = DbUtil.getSession();

		// 연결
		state = session.insert("mapper namespace값.insert문 id값"[, sql문 파라미터]) > 0 ? true : false;
		/*
		 * session.insert() 메소드는 변경한 레코드 갯수를 리턴함
		 * 삼항 연산자를 이용해 변경한 값이 0보다 크다면(=변경한 값이 있다면) true(=commit)
		 * 변경한 값이 0이라면(=변경한 값이 없다면) false(=rollback)
		 * */
	} finally {
		// 닫기
		// insert문이므로 commit, rollback 할 수 있도록 결과를 나타내는 변수 state를 인수로 입력
		DbUtil.sessionClose(session, state);
	}
}
```

## UPDATE

```xml

<!--
	기본 update sql문
	id: DAO에서 매퍼의 namespace과 <update> 태그의 id값으로 SQL문을 호출할 때 사용
	parameterType: sql문에서 인수를 입력받을 경우 인수 타입 작성(옵션), 기본 타입과 객체 타입 모두 사용 가능
-->
<update id="id값" parameterType="인수 타입">
	update sql문
</update>
```

```java
public void update() {
	SqlSession session = null;
	boolean state = false; // commit, rollback 여부 변수
	try {
		// 로드
		session = DbUtil.getSession();

		// 연결
		state = session.update("mapper namespace값.update문 id값"[, sql문 파라미터]) > 0 ? true : false;
		/*
		 * session.update() 메소드는 변경한 레코드 갯수를 리턴함
		 * 삼항 연산자를 이용해 변경한 값이 0보다 크다면(=변경한 값이 있다면) true(=commit)
		 * 변경한 값이 0이라면(=변경한 값이 없다면) false(=rollback)
		 * */
	} finally {
		// 닫기
		// update문이므로 commit, rollback 할 수 있도록 결과를 나타내는 변수 state를 인수로 입력
		DbUtil.sessionClose(session, state);
	}
}
```

## DELETE

```xml

<!--
	기본 delete sql문
	id: DAO에서 매퍼의 namespace과 <delete> 태그의 id값으로 SQL문을 호출할 때 사용
	parameterType: sql문에서 인수를 입력받을 경우 인수 타입 작성(옵션), 기본 타입과 객체 타입 모두 사용 가능
-->
<delete id="id값" parameterType="인수 타입">
	delete sql문
</delete>
```

```java
public void delete() {
	SqlSession session = null;
	boolean state = false; // commit, rollback 여부 변수
	try {
		// 로드
		session = DbUtil.getSession();

		// 연결
		state = session.delete("mapper namespace값.delete문 id값"[, sql문 파라미터]) > 0 ? true : false;
		/*
		 * session.delete() 메소드는 변경한 레코드 갯수를 리턴함
		 * 삼항 연산자를 이용해 변경한 값이 0보다 크다면(=변경한 값이 있다면) true(=commit)
		 * 변경한 값이 0이라면(=변경한 값이 없다면) false(=rollback)
		 * */
	} finally {
		// 닫기
		// delete문이므로 commit, rollback 할 수 있도록 결과를 나타내는 변수 state를 인수로 입력
		DbUtil.sessionClose(session, state);
	}
}
```

## 참고: include

> 자주 사용되는 문장의 경우 미리 선언한 뒤 include를 이용해 참조함
> 

```xml
<sql id="id값">
	SQL문
</sql>

<select id="id값" parameterType="인수 타입" resultType="결과 타입">
	<!--
		앞에서 선언한 sql문의 id값으로 찾아 sql문 가져옴
		다른 xml 문서에 있는 sql문을 include하고 싶은 경우 id값 앞에 해당 문서의 namespace값. 입력
	-->
	<include refid="[namespace값.]id값"/>
	<!-- include로 들어온 문장 뒤에 추가해야 하는 문장이 있을 경우 추가 작성 -->
	추가 SQL문
</select>
```

## 참고: SQL문에 파라미터 입력

### 파라미터: 기본 타입

```xml
<!--
	파라미터 자리에 #{_parameter} 입력 - #{} 안에 어떤 값을 넣어도 상관없지만 편의상 _parameter 입력
	내장된 타입 별칭이 따로 있기 때문에 parameterType 작성 시 참고
-->
<select id="id값" parameterType="기본 타입" resultType="결과 타입">
	select * from emp where 컬럼명 = #{_parameter}

	<!-- 파라미터가 포함된 문자열을 검색하고 싶은 경우 -->
	select * from emp where 컬럼명 = '%' || #{_parameter} || '%'
</select>
```

### 파라미터: 객체 타입

```xml
<!--
	파라미터 자리에 #{필드명} 입력
	getter를 사용하기 때문에 getter가 없으면 오류 발생
	파라미터는 한 개만 받을 수 있기 때문에 여러 개의 파라미터를 입력해야 할 경우 사용
-->
<select id="id값" parameterType="패키지 경로.객체명" resultType="결과 타입">
	select * from emp where 컬럼명 = #{필드명}, 컬럼명 = #{필드명}
</select>
```

- 파라미터로 받을 객체에 별칭 주기
    
    ```xml
    <!--
    	파라미터가 객체의 경로와 이름이 복잡한 경우 SqlMapConfig.xml 문서에서 별칭을 부여할 수 있음
    	객체 별칭을 만들면 parameterType에 별칭 입력 가능
    -->
    
    <!-- SqlMapConfig.xml -->
    <typeAliases>
    	<typeAlias type="패키지 경로.객체명" alias="객체 별칭"/>
    </typeAliases>
    ```
    
    ```xml
    <!-- ~Mapper.xml -->
    <select id="id값" parameterType="객체 별칭" resultType="결과 타입">
    	select * from emp where 컬럼명 = #{필드명}, 컬럼명 = #{필드명}
    </select>
    ```
    

### 파라미터: Map

```xml
<!--
	파라미터 자리에 #{key값} 입력
	Map의 내장된 타입 별칭은 map이기 때문에 첫 글자를 대문자로 쓰지 않도록 주의
	필요한 파라미터를 모두 담을 수 있는 객체가 없을 경우, 여러 객체를 함께 받아야 할 경우,
	객체와 다른 파라미터를 함께 받아야 할 경우에 사용
-->
<select id="id값" parameterType="map" resultType="결과 타입">
	select * from emp where 컬럼명 = #{key값}, 컬럼명 = #{key값.필드명(객체를 담은 경우)}
</select>
```

## 참고: 컬럼명으로 파라미터 입력

```xml
<!--
	#{}는 prepareStatement 방식처럼 자동으로 파라미터를 single quotation으로 감싸기 때문에 컬럼명에 #{}를 사용하면 오류 발생
	${}가 Statement 방식처럼 파라미터를 있는 그대로 넣어주기 때문에 컬럼명에는 ${} 사용
	but Statement의 보안 문제 역시 동일하기 때문에 주의

	${} 안에 입력하는 값 형식은 #{}와 동일
-->
<select id="id값" parameterType="string" resultType="결과 타입">
	select * from emp order by ${_parameter}
</select>
```

## 참고: DB 컬럼명과 DTO 필드명이 서로 다를 경우

```java
/*
 * select문 결과를 객체로 받을 경우 컬럼명-필드명을 인식해 자동 매핑함
 * 때문에 DB 컬럼명과 DTO 필드명이 서로 다를 경우 오류 발생
 * 해당 오류를 방지하기 위해 컬럼명에 별칭 부여
 * */

// DTO
public class EmpDTO {
	private String empName;
}
```

```xml
<!-- ~Mapper.xml -->
<select id="id값" resultType="EmpDTO">
	select ename as empName from emp
</select>
```

## 참고: RowBounds

> RowBounds 객체를 이용해 결과를 제한해 가져올 수 있음
> 

```java
public void select() {
	SqlSession session = null;
	try {
		session = DbUtil.getSession();

		
		List<결과타입> list = session.selectList("mapper namespace값.select문 id값", null, new RowBounds(i, j));
		/**
		 * RowBounds: 결과값으로 나온 레코드 중 일부분만 제한해 가져올 때 사용
		 * new RowBounds(i, j): 결과 레코드 중 i번째 레코드부터 j개만 가져옴(i: 0부터 시작)
		 * 
		 * session.selectList(sql문 id값, sql문 인수, RowBounds) 메소드만 RowBounds 사용 가능
		 * session.selectList(sql문 id값, RowBounds) 메소드는 존재하지 않기 때문에 주의
		 * */

	} finally {
		DbUtil.sessionClose(session);
	}
}
```