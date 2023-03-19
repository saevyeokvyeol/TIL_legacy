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