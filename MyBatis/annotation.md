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