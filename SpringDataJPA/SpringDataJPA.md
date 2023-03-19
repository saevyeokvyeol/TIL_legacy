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