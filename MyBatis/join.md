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