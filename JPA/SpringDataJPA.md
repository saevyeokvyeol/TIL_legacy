# 특징 및 개념

- 똑같이 반복되는 기본 CRUD를 인터페이스로 제공
- 사용자는 제공되는 인터페이스를 상속받아 서브인터페이스 작성
- SpringDataJPA는 사용자가 작성한 서브인터페이스의 구현체를 자동으로 생성해 주입
- 서브인터페이스 구현체가 주입되어 실제로 CRUD 작업을 하는 DAO, Repository 클래스는 반드시 @Transational @Commit 어노테이션 입력

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

# ****Query Methods****

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

# 페이징 처리

- PageRequest 객체를 이용해 자동으로 테이블의 레코드를 페이징 처리해 가져올 수 있음

## 기본 코드

```java
// 페이징 방식 생성
Pageable page = PageRequest.of(가져올 페이지 수(0부터 시작), 한 페이지 당 존재하는 레코드 수, 정렬 방식, 정렬 기준 컬럼);

// 위에서 생성한 페이징 방식을 이용해 페이징 처리
Page<Dto> pageList = boardRepository.findAll(page);

// 페이징 처리된 레코드를 리스트 형태로 변환
List<Dto> list = pageList.getContent();
```

## 주요 메소드

```java
pageList.getNumber() // 현재 객체의 페이지 번호(0부터 시작)

pageList.getSize() // 현재 객체의 레코드 수

pageList.getTotalPages() // 가져온 테이블의 전체 페이지 수

pageList.previousPageable() // 이전 페이지의 페이지 번호, 레코드 수, 정렬 방식

pageList.nextPageable() // 다음 페이지의 페이지 번호, 레코드 수, 정렬 방식

pageList.isFirst() // 현재 객체의 첫 번째 페이지 여부

pageList.isLast() // 현재 객체의 마지막 페이지 여부

pageList.hasPrevious() // 현재 객체의 이전 페이지 존재 여부

pageList.hasNext() // 현재 객체의 다음 페이지 존재 여부
```

# ****QueryDSL****

## 특징 및 개념

- DSL = Domain Specific Language
- 자바를 이용해 쿼리 조건을 처리할 때 사용하는 라이브러리
- 정적 쿼리만 사용 가능한 JPA와 다르게 동적 쿼리 작성이 가능
- 작동 방식
    - QueryDSL로 쿼리를 작성하면 내부에서 JPQL로 변환해 SQL로 보내줌

## 사용 설정

```xml
<!-- pom.xml -->

<!-- QueryDSL을 사용하기 위한 QueryDSL APT dependency 추가 -->
<dependency>
	<groupId>com.querydsl</groupId>
	<artifactId>querydsl-apt</artifactId>
	<!-- 뷰 템플릿이 jsp일 경우 jasper와 충돌을 방지하기 위한 추가 설정 -->
	<exclusions>
		<exclusion>
			<groupId>org.eclipse.jdt.core.compiler</groupId>
			<artifactId>ecj</artifactId>
		</exclusion>
	</exclusions>
</dependency>

<!-- QueryDSL을 사용하기 위한 QueryDSL JPA dependency 추가 -->
<dependency>
	<groupId>com.querydsl</groupId>
	<artifactId>querydsl-jpa</artifactId>
</dependency>

<!-- QueryDSL를 사용하기 위한 plugin 등록 -->
<plugin>
	<groupId>com.mysema.maven</groupId>
	<artifactId>apt-maven-plugin</artifactId>
	<version>1.1.3</version>
	<executions>
		<execution>
			<goals>
				<goal>process</goal>
			</goals>
			<configuration>
				<!-- @Entity 어노테이션을 사용한 객체를 Q파일명 객체로 변환해 아래 경로에 저장 -->
				<outputDirectory>target/generated-sources/java</outputDirectory>
				<processor>com.querydsl.apt.jpa.JPAAnnotationProcessor</processor>
			</configuration>
		</execution>
	</executions>
</plugin>
```

```java
/**
 * JpaRepository와 QuerydslPredicateExecutor를 상속받은 인터페이스 제작
 * : 인터페이스는 인터페이스 다중 상속 가능
 * */

public interface Repository extends JpaRepository<사용할 객체, PK 데이터 타입>, QuerydslPredicateExecutor<사용할 객체> {
	
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

## 예제 코드

### 기본 형태

```java
/**
 * @Transactional과 @Commit 어노테이션을 사용한 클래스에서 실제 CRUD 작업 가능
 * */

@Transactional
@Commit
public class DAO {
	public void test() {
		// BooleanBuilder 객체 생성
		BooleanBuilder booleanBuilder = new BooleanBuilder();

		// QDomain 객체 생성
		QDomain domain = QDomain.domain;
		
		// 조건 입력
		booleanBuilder.논리연산메소드(board.검색할필드.검색조건(검색어));
		
		// 조건에 맞는 레코드 검색해 Iterable 객체로 저장
		Iterable<Domain> iterable = boardRepository.findAll(booleanBuilder);

		// Iterable 객체를 list로 변환
		List<Domain> list = Lists.newArrayList(iterable);
	}
}
```

```java
/**
 * 예시: board 테이블의 bno 컬럼이 130이 넘지 않고 title에 30이 포함된 레코드 검색
 * */

@Transactional
@Commit
public class DAO {
	public void test() {
		// BooleanBuilder 객체 생성
		BooleanBuilder booleanBuilder = new BooleanBuilder();

		// QDomain 객체 생성
		QBoard board = QBoard.board;
		
		// 조건 1: 첫 번째 조건은 and/or 상관없이 사용 가능
		booleanBuilder.andNot(board.bno.gt(130L));
		
		// 조건 2
		booleanBuilder.and(board.title.like("%30%"));
		
		// 조건에 맞는 레코드 검색해 Iterable 객체로 저장
		Iterable<Domain> iterable = boardRepository.findAll(booleanBuilder);

		// Iterable 객체를 list로 변환
		List<Domain> list = Lists.newArrayList(iterable);
	}
}
```

### 주요 조건

```java
/**
 * 날짜로 검색
 * */

LocalDateTime from = LocalDateTime.of(2022, 5, 30, 0, 0);
LocalDateTime to = LocalDateTime.of(2022, 5, 31, 0, 0);
booleanBuilder.and(domain.date.between(from, to));
```

```java
/**
 * 대소문자 구분없이 검색
 * */

booleanBuilder.and(domain.field.equalsIgnoreCase("A"));
```