> @Setter, @Getter 등의 어노테이션을 지원해 개발을 빠르게 만들어주는 라이브러리
> 

# 주요 어노테이션

```xml
<!-- Lombok을 사용하기 위해 설치 후 pom.xml에 dependency 추가 -->
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

@Setter // 세터 생성
@Getter // 게터 생성
@NoArgsConstructor // 아무 인수도 들어가지 않는 생성자 생성
@AllArgsConstructor // 모든 인수가 들어가는 생성자 생성
@ToString(exclude = "필드명") // toString 메소드 오버라이딩, 출력하고 싶지 않은 필드가 있을 경우 exclude 속성 추가
@RequiredArgsConstructor // final 필드를 기반으로 생성자를 만들어 초기화: @Autowired 대신 사용
public class 클래스명{

	/*
	 * 생성자를 통해 반드시 생성해야 하는 필드
	 * RequiredArgsConstructor 사용 시 @NonNull을 사용한 필드만 생성하는 생성자 생성
	 * */
	@NonNull
	private int number;
}
```

# 주의: @ToString

- 서로를 멤버 필드를 가진 클래스에 @ToString 어노테이션을 사용하면 스택오버플로우가 일어날 수 있음

```java
@ToString
public class A {
	B b;
}

@ToString
public class B {
	A a;
}

public static void main(String[] args) {
	A a = new A();
	System.out.println(A);
	/*
	 * 결과: A가 출력되며 A안에 있는 B가, B를 출력하며 B 안에 있는 A가 출력되며 스택오버플로우가 일어남
	 * */
}
```

```java
@ToString(exclude = "b")
public class A {
	B b;
}

@ToString(exclude = "a") // a는 제외하고 toString 메소드 오버라이딩
public class B {
	A a;
}

public static void main(String[] args) {
	A a = new A();
	System.out.println(A);
	/*
	 * 결과: A가 출력될 때 A 안에 있는 B가 출력되지만 B가 출력될 때에는 A가 출력되지 않아 A와 B가 한 번씩 출력되고 종료
	 * */
}
```