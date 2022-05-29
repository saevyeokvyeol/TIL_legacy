# 특징 및 개념

- 똑같이 반복되는 기본 CRUD를 인터페이스로 제공
- 사용자는 제공되는 인터페이스를 상속받아 서브인터페이스 작성
- SpringDataJPA는 사용자가 작성한 서브인터페이스의 구현체를 자동으로 생성해 주입
- 서브인터페이스 구현체가 주입되어 실제로 CRUD 작업을 하는 DAO, Repository 클래스는 반드시 @Transational @Commit 어노테이션 입력

# 사용 설정

> 세팅은 JPA 사용 설정 참고
> 
> 
> [](https://github.com/yudaGim/TIL/blob/main/ORM_Framework/JPA/JPA.md#%EC%82%AC%EC%9A%A9-%EC%84%A4%EC%A0%95)
> 

```java
/**
 * JpaRepository를 상속받은 인터페이스 제작
 * : 해당 인터페이스 객체를 통해 CRUD 작업
 *   기본 CRUD 이외의 다양한 쿼리문을 사용하고 싶을 때에는 해당 인터페이스에 메소드 생성
 * */

public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입> {
	
}
```

```java
/**
 * @Transactional과 @Commit 어노테이션을 사용한 클래스에서 실제 CRUD 작업 가능
 * */

@Transactional
@Commit
public class DAO {
	
}
```

# 인터페이스 종류

- Repository
    - 가장 상위 부모 인터페이스
- CrudRepository
    - Repository를 상속받은 인터페이스
    - 기본 쿼리문에 충실함
- PagingAndSortingRepository
    - CrudRepository를 상속받은 인터페이스
    - 페이징 처리와 정렬 메소드가 포함되어 있음
- JpaRepository
    - PagingAndSortingRepository를 상속받은 인터페이스
    - SpringDataJPA가 제공하는 가장 하위 인터페이스로 주로 사용
    - 다양한 확장 메소드가 포함되어 있음

# 기본 SELECT, INSERT, UPDATE, DELETE

## SELECT

```java
/**
 * JpaRepository 상속 시 사용할 객체로 입력했던 테이블의 모든 레코드를 가져오고 싶을 때
 * */

List<Dto> list = repository.findAll();
```

```java
/**
 * 입력한 값과 테이블의 PK값이 같은 레코드를 가져오고 싶을 때
 * */

Dto dto = repository.findById(PK값).orElse(null);
```

### Optional

- java.util 추가 객체로 null 여부 체크를 생략할 수 있도록 관련 메소드 제공

```java
// repository.findById()의 리턴값
Optional<Dto> op = repository.findById(PK값);

// Optional 객체에 orElse() 메소드 사용 시 Repository 상속 시 입력한 객체가 반환됨
Dto dto = op.orElse(결과가 null일 때 대체할 값)
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
 * @Transactional 어노테이션이 없는 파일에서는 setter 사용해도 UPDATE X
 * */
Dto dto = repository.findById(PK값).orElse(null);
dto.setFieldColumn(수정할 값);
```

## DELETE

```java
/**
 * deleteById() 메소드의 매개변수로 PK값을 입력해 해당 레코드 삭제
 * */
boardRepository.deleteById(PK값);
```

# @Query

- 메소드로 제공되는 기본 CRUD문이 아닌 복잡하고 다양한 쿼리문을 사용하고 싶을 때 @Query 사용

## SELECT

```java
/**
 * JpaRepository 인터페이스를 상속받은 인터페이스 안에 @Query 어노테이션 사용해 메소드 선언
 * */
public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입> {
	@Query(쿼리문)
	return값 메소드명(파라미터);
}

/**
 * 예시: 입력한 숫자보다 큰 숫자를 가진 레코드 검색
 * */
@Query("select from Board b where b.bno > ?1")
List<Board> selectGrateThen(Long Id);
```

## INSERT, UPDATE, DELETE

```java
/**
 * DML 문장의 경우 @Modifying 어노테이션 추가
 * */
public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입> {
	@Query(쿼리문)
	@Modifying
	void 메소드명(파라미터);
}

/**
 * 예시: 입력한 숫자보다 큰 숫자를 가진 레코드 삭제
 * */
@Query("delete from Board b where b.bno > ?1")
@Modifying
void deleteGrateThen(Long Id);
```

## 객체 파라미터

```java
/**
 * 파라미터로 객체를 받아 그 객체의 필드명을 쿼리문에 사용하고 싶을 때
 * @Param 어노테이션과 :#{#별칭.필드명} 문법 사용
 * */
public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입> {
	@Query(쿼리문)
	return값 메소드명(@Param("별칭") 파라미터);
}

/**
 * 예시: 글번호, 제목에 해당하는 레코드 검색
 * */
@Query("select b from Board b where b.bno > :#{#bd.bno} and b.title = :#{#bd.title}")
	List<Board> selectParamBoard(@Param("bd") Board board);
```

## nativeQuery

- 순수 JPA에는 없는 문법
- DB문법으로 쿼리문을 작성하고 싶을 때에 @Query 어노테이션에 nativeQuery 속성 사용

```java
/**
 * DB문법으로 쿼리문을 작성하고 싶을 떄에는 nativeQuery = true 속성 입력
 * */
public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입> {
	@Query(value = 쿼리문, nativeQuery = true)
	return값 메소드명(파라미터);
}

/**
 * 예시: 보드 넘버가 입력한 값과 같거나 제목이 입력한 값과 같은 레코드 검색
 * */
@Query(value = "select * from board where bno = ?1 or title = ?2", nativeQuery = true)
List<Board> selectByBnoTitle(Long bno, String title);
```

## ****Query Methods****

- JpaRepository 상속 시 입력한 객체를 기반으로 조건 검색 쿼리를 자동으로 만들어주는 것
- findBy로 시작하는 메소드 생성 시 사용 가능
- @Query 어노테이션 사용X
- 사용 가능한 조건은 아래 링크 참고
    
    [Spring Data JPA - Reference Documentation](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods)
    

```java
/**
 * DB문법으로 쿼리문을 작성하고 싶을 떄에는 nativeQuery = true 속성 입력
 * */
public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입> {
	return값 findBy필드명조건...(파라미터);
}

/**
 * 예시: 보드 넘버가 입력한 값과 같거나 제목이 입력한 값과 같은 레코드 검색
 * */
List<Board> findByBnoLessThan(Long bno);
```