# Ajax

## 설정

```xml
<!-- 자바 자료형을 프론트로 가져올 때 json으로 변환하기 위해 jackson dependency 추가 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.13.0</version>
</dependency>
```

## 예제 코드

### HTML/JSP(JavaScript)

```jsx
$.ajax({
	url : "서버 요청 주소",
	type : "요청 방식(method방식 : get | post | put | delete)",
	dateType : "서버가 보내온 데이터(응답) 타입(text | html | xml | json)",
	data : "서버에게 보낼 데이터 정보(parameter 정보)",
	success : function(서버가 가져온 데이터를 저장할 변수명) {
		성공했을 때 실행할 함수;
	},
	error : function(서버가 가져온 데이터를 저장할 변수명) {
		실패했을 때 실행할 함수;
	}
});
```

### Controller

```java
/**
 * void / primitive 타입을 리턴할 경우
 * */
@RequestMapping(value = "/서버 요청 주소", produces = "text/html;charset=UTF-8") // 인코딩 변환
public String ajax(서버에게 보낼 데이터 정보(parameter 정보)) {
	return "string";
}

/**
 * 객체, 자료구조를 리턴할 경우
 * : json으로 변환해 리턴해주기 위해 jackson 라이브러리 필요
 * */
@RequestMapping("/서버 요청 주소") // 인코딩 방식 선언 시 jackson과 충돌해 오류 발생
public List<String> ajax(서버에게 보낼 데이터 정보(parameter 정보)) {
	List<String> list = new ArrayList<>();
	return list;
}
```