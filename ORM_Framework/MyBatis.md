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
	
	<!-- 옵션 세팅 설정 -->
	<settings>
		<setting name="setting명" value="setting값"/>
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

# 예제 코드: 참고 문법

## include

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

## SQL문에 파라미터 입력

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

- 참고: 파라미터로 받을 객체에 별칭 주기
    
    ```xml
    <!--
    	파라미터로 받을 객체 경로가 복잡한 경우 SqlMapConfig.xml 문서에서 별칭을 부여할 수 있음
    	객체 별칭을 만들면 parameterType에 별칭 입력 가능
    	객체 별칭은 관례적으로 첫 글자를 소문자로 바꾼 객체명을 사용
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

## 컬럼명으로 파라미터 입력

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

## 파라미터를 넣지 않을 경우

> sql문에 파라미터를 지정했지만 DAO에서 파라미터를 입력하지 않는 경우 오류 발생X
> 
- 일반 select, insert, update, delete문에서는 결과값이 나오지 않음
- 동적 SQL 안에서만 파라미터를 사용할 경우 동적 SQL이 실행되지 않은 결과값이 출력됨

## DB 컬럼명과 DTO 필드명이 서로 다를 경우

> select 결과를 객체로 받을 경우 컬럼명-필드명으로 자동 매핑하기 때문에 컬럼명-필드명이 다를 경우 오류 발생
> 

### 컬럼명에 별칭 부여

```java
/* 컬럼명에 별칭을 부여해 DB 컬럼명과 DTO 필드명을 맞춰줌 */

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

### 언더스코어 표기법과 낙타 표기법 매핑 설정

```xml
<!--
	DB의 언더스코어 표기법(underscore case = snake case)과 java의 낙타 표기법(camel case)을 자동 매핑하도록 설정
-->

<!--
	SqlMapConfig.xml
	<settings> 태그는 <properties> 태그와 <typeAliases> 태그 사이에 입력
-->
<settings>
		<!-- mapUnderscoreToCamelCase을 true로 설정 -->
		<setting name="mapUnderscoreToCamelCase" value="true"/>
	</settings>
```

## RowBounds

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

## null값 입력

> insert, update 시 레코드 컬럼에 null값 입력
> 

```xml
<!--
	파라미터가 null일 경우 insert, update 시 필드에 null값을 넣도록 설정
	해당 설정이 없을 때 파라미터가 null일 경우 오류 발생
-->

<!--
	SqlMapConfig.xml
	<settings> 태그는 <properties> 태그와 <typeAliases> 태그 사이에 입력
-->
<settings>
		<!--
			파라미터에 값이 null일 때 필드에 null값으로 들어가도록 설정 변경
			value의 null은 무조건 대문자(대소문자를 가림)
		-->
		<setting name="jdbcTypeForNull" value="NULL"/>
	</settings>
```

# 예제 코드: 동적 SQL

## where

```xml
<!--
	where
	: select, insert, update, delete 태그 안에 사용함
	  where 태그 안에 문장이 있을 경우 태그 안 문장 맨 앞에 where를 추가해주고
		태그 안 문장이 and나 or로 시작한다면 and나 or를 제거함
-->
<where>
	실행문
</where>
```

## trim

```xml
<!--
	trim
	: where의 상위 버전 태그
	  trim 태그 안에 문장이 있을 경우 설정한 값에 따라 태그 안 문장 앞뒤에 문자를 삽입하거나 지워줌
		
		prefix - 태그 안에 문장이 있으면 가장 앞에 해당 문자를 붙여줌
		prefixOverrides - 태그 안 문장 중 가장 앞에 해당 문자가 있으면 자동 삭제
		suffix - 태그 안에 문장이 있으면 가장 뒤에 해당 문자 붙여줌
		suffixOverrides - 태그 안 문장 중 가장 뒤에 해당 문자가 있으면 자동 삭제

		~Overrides 속성의 경우 |(or)로 삭제할 문자 조건을 여러 개 지정하는 것도 가능
-->
<trim prefix="가장 앞에 추가할 문자" prefixOverrides="가장 앞에서 삭제할 문자"
	suffix="가장 뒤에 추가할 문자" suffixOverrides="가장 뒤에서 삭제할 문자">
	실행문
</trim>
```

## set

```xml
<!--
	set
	: update 태그 안에 사용함
	  set 태그 안에 문장이 있을 경우 태그 안 문장 맨 앞에 set를 추가해주고
	  태그 안 문장 앞이나 뒤에 붙은 필요없는 ,(콤마)를 제거함
-->
<set>
	실행문
</set>
```

## if

```xml
<!--
	if
	: select, insert, update, delete 태그 안에 사용하며 조건에 부합할 경우 태그 안에 입력한 문장을 출력함
	  조건문 안에서 파라미터를 사용할 경우 #{}, ${}로 감싸지 않음
-->

<if test="조건문">
	실행문
</if>
```

## choose

```xml
<!--
	choose
	: if의 상위 버전 태그
	  java의 if, else-if, else와 비슷함
		여러 조건 중 처음으로 부합하는 태그 안에 입력한 문장만 출력함
	  조건문 안에서 파라미터를 사용할 경우 #{}, ${}로 감싸지 않음
-->
<choose>
	<when test="조건문1">
		실행문1
	</when>
	<when test="조건문2">
		실행문2
	</when>
	<otherwise>
		실행문3
	</otherwise>
</choose>
```

## foreach

```xml
<!--
	foreach
	: select, insert, update, delete 태그 안에 사용함
	  인수로 받은 자료구조에서 요소를 하나씩 꺼내 문장 안에서 출력함
		separator, open, close 속성을 이용해 반복문 중간이나 가장 앞, 뒤에 추가할 문자를 지정할 수 있음
-->
<foreach collection="변수명(인수로 받은 자료구조)" item="item(자료구조에서 꺼낸 개별 요소)"
	separator="각 반복문 중간에 추가할 문자" open="반복문 가장 앞에 추가할 문자" close="반복문 가장 뒤에 추가할 문자">
	#{item}
</foreach>
```

# 예제 코드: join

## 1:1 관계 mapping join

```xml
<!--
	1:1 관계 데이터 매핑용 Map
	이 때 데이터 매핑용 Map != java의 Map
-->
<resultMap type="주 객체명(객체 별칭)" id="id값">
	<!-- PK 컬럼 매핑: 일반 컬럼처럼 result 태그에 입력해도 상관없음 -->
	<id column="DB 컬럼명" property="DTO 필드명"/>

	<!-- 일반 컬럼 매핑 -->
	<result column="DB 컬럼명" property="DTO 필드명"/>
	
	<!-- 객체 필드(1:1 관계) 매핑: association 태그 사용 -->
	<association property="DB 테이블명" javaType="필드 객체명(객체 별칭)">
		<!-- 컬럼 매핑 -->
		<id column="DB 컬럼명" property="DTO 필드명"/>
		<result column="DB 컬럼명" property="DTO 필드명""/>
	</association>
</resultMap>

<select id="id값" resultMap="resultMap id값">
	select join sql문
</select>
```

## 1:다 관계 mapping join

```xml
<!--
	1:다 관계 데이터 매핑용 Map
-->
<resultMap type="주 객체명(객체 별칭)" id="id값">
	<!-- PK 컬럼 매핑: 일반 컬럼처럼 result 태그에 입력해도 상관없음 -->
	<id column="DB 컬럼명" property="DTO 필드명"/>

	<!-- 일반 컬럼 매핑 -->
	<result column="DB 컬럼명" property="DTO 필드명"/>
	
	<!-- 객체 타입 리스트 필드(1:다 관계) 매핑: collection 태그 사용 -->
	<collection property="DB 테이블명" ofType="리스트 제네릭 타입(=객체명 | 객체 별칭)">
		<!-- 컬럼 매핑 -->
		<id column="DB 컬럼명" property="DTO 필드명"/>
		<result column="DB 컬럼명" property="DTO 필드명""/>
	</collection>
</resultMap>

<select id="id값" resultMap="resultMap id값">
	select join sql문
</select>
```

# 예제 코드: Annotation 방식

- xml 기반 mapper를 java 클래스에서 Annotation 방식으로 대체
- 클래스는 interface로 제작함
- 모든 멤버 필드는 public static final 상수로 제작함
- 모든 메소드는 public abstract 추상 메소드로 제작함

## SELECT

```java
/**
 * 검색
 * 
 * @return: 결과 타입 - 하나일 경우 DTO, 여러 개일 경우 List<DTO>
 * @param: 인수 타입 - 쿼리문에 입력해야 할 인수를 입력받음
 * */
@Select("select sql문")
결과타입 select(자료형 인수); // 파라미터가 하나만 들어올 때
결과타입 select(@Param("인수명") 자료형 인수, @Param("인수명") 자료형 인수); // 파라미터가 여러 개 들어올 때
```

```java
public void select() {
	SqlSession session = null;
	try {
		// 로드
		session = DbUtil.getSession();
		
		// 연결: session에서 매퍼를 가져와 
		클래스명 mepper = session.getMapper(클래스명.class);

		// interface에서 메소드 호출
		결과타입 result = mepper.select([sql문 파라미터]); // 결과가 하나일 때
		List<EmpDTO> list = mepper.select([sql문 파라미터]); // 결과가 여러 개일 때

	} finally {
		// 닫기
		// select문이므로 인수로 닫을 session만 입력
		DbUtil.sessionClose(session);
	}
}
```

## INSERT

```java
/**
 * 입력
 * 
 * @return: 추가한 레코드 갯수
 * @param: 인수 타입 - 쿼리문에 입력해야 할 인수를 입력받음
 * */
@Insert("insert sql문")
int insert(자료형 인수); // 파라미터가 하나만 들어올 때
int insert(@Param("인수명") 자료형 인수, @Param("인수명") 자료형 인수); // 파라미터가 여러 개 들어올 때
```

```java
public void insert() {
	SqlSession session = null;
	boolean state = false; // commit, rollback 여부 변수

	try {
		// 로드
		session = DbUtil.getSession();
		
		// 연결: session에서 매퍼를 가져와 
		클래스명 mepper = session.getMapper(클래스명.class);

		// interface에서 메소드 호출
		state = mepper.insert([sql문 파라미터]) > 0 ? true : false;
		// 삼항 연산자를 이용해 변경된 레코드의 갯수에 따라 commit, rollback 여부를 변경해줌

	} finally {
		// 닫기
		// insert문이므로 commit, rollback 할 수 있도록 결과를 나타내는 변수 state를 인수로 입력
		DbUtil.sessionClose(session);
	}
}
```

## UPDATE

```java
/**
 * 수정
 * 
 * @return: 변경한 레코드 갯수
 * @param: 인수 타입 - 쿼리문에 입력해야 할 인수를 입력받음
 * */
@Update("update sql문")
int update(자료형 인수); // 파라미터가 하나만 들어올 때
int update(@Param("인수명") 자료형 인수, @Param("인수명") 자료형 인수); // 파라미터가 여러 개 들어올 때
```

```java
public void update() {
	SqlSession session = null;
	boolean state = false; // commit, rollback 여부 변수

	try {
		// 로드
		session = DbUtil.getSession();
		
		// 연결: session에서 매퍼를 가져와 
		클래스명 mepper = session.getMapper(클래스명.class);

		// interface에서 메소드 호출
		state = mepper.update([sql문 파라미터]) > 0 ? true : false;
		// 삼항 연산자를 이용해 변경된 레코드의 갯수에 따라 commit, rollback 여부를 변경해줌

	} finally {
		// 닫기
		// update문이므로 commit, rollback 할 수 있도록 결과를 나타내는 변수 state를 인수로 입력
		DbUtil.sessionClose(session);
	}
}
```

## DELETE

```java
/**
 * 삭제
 * 
 * @return: 삭제한 레코드 갯수
 * @param: 인수 타입 - 쿼리문에 입력해야 할 인수를 입력받음
 * */
@Delete("delete sql문")
int delete(자료형 인수); // 파라미터가 하나만 들어올 때
int delete(@Param("인수명") 자료형 인수, @Param("인수명") 자료형 인수); // 파라미터가 여러 개 들어올 때
```

```java
public void insert() {
	SqlSession session = null;
	boolean state = false; // commit, rollback 여부 변수

	try {
		// 로드
		session = DbUtil.getSession();
		
		// 연결: session에서 매퍼를 가져와 
		클래스명 mepper = session.getMapper(클래스명.class);

		// interface에서 메소드 호출
		state = mepper.delete([sql문 파라미터]) > 0 ? true : false;
		// 삼항 연산자를 이용해 삭제된 레코드의 갯수에 따라 commit, rollback 여부를 변경해줌

	} finally {
		// 닫기
		// delete문이므로 commit, rollback 할 수 있도록 결과를 나타내는 변수 state를 인수로 입력
		DbUtil.sessionClose(session);
	}
}
```

## include

> 자주 사용하는 문장의 경우 멤버 필드에 저장해 재사용
> 

```java
String SELECT_SQL = "select sql문";

@Select(SELECT_SQL)
결과타입 select(인수);
```

## 동적 SQL

> 동적 쿼리는 <script> 태그 사이에 입력함
> 

```java
@Select("<script>동적 sql문</script>")
결과타입 select(인수);
```

- Annotation 방식 동적 쿼리는 복잡하고 가독성이 나쁘기 때문에 xml 방식 권장