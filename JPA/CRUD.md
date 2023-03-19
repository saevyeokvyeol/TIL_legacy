# 기본 SELECT, INSERT, UPDATE, DELETE

## SELECT

```java
/**
 * 입력한 객체 = 입력한 테이블, 입력한 pk값 = DB에 저장된 pk값인 레코드를 객체에 매핑해 가져옴
 * 만일 관계가 있는 테이블일 경우 모든 관계를 자동 조인해 가져옴
 * */
Table table = entityManager.find(Table.class, pk값);
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
 * */
Table table = entityManager.find(Table.class, pk값);
table.setFieldColumn("수정할 내용");
```

## DELETE

```java
/**
 * SELECT해 가져온 객체를 entityManager.remove() 메소드 파라미터로 넘겨 DELETE
 * */
Table table = entityManager.find(Table.class, pk값);
entityManager.remove(table);
```