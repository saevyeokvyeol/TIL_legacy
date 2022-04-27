# Lombok

- @Setter, @Getter 등의 어노테이션을 지원해 개발을 빠르게 만들어주는 라이브러리

## 예제코드 @Setter, @Getter

```xml
<!--
	@Setter: 세터를 자동으로 생성해줌
	@Getter: 게터를 자동으로 생성해줌
-->

<!-- Lombok을 사용하기 위해 pom.xml에 dependency 추가 -->
<!-- https://mvnrepository.com/artifact/org.projectlombok/lombok -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
    <scope>provided</scope>
</dependency>
```

```java
/*
* 클래스 선언부 위에서 어노테이션 입력
* 자바 파일에서는 보이지 않지만 컴파일 시 인수를 기반으로 세터와 게터 자동 생성
* */ 
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Setter // 세터 생성
@Getter // 게터 생성
@AllArgsConstructor // 모든 인수가 들어가는 생성자 생성
@NoArgsConstructor // 아무 인수도 들어가지 않는 생성자 생성
@ToString // toString 메소드 오버라이딩
public class 클래스명{}
```