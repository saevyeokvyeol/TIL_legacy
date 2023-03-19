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