# QueryDSL

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