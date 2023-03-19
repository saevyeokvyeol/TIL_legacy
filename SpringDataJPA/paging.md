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