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