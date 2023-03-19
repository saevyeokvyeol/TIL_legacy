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