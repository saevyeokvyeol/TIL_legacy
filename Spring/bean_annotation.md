
# Bean Annotation

- 프레임워크에서 제공하는 라이브러리 속 객체를 메소드를 통해 어노테이션으로 선언

```java
/**
 * @Configuration
 * : 어노테이션 기반 환경 설정을 돕는 annotation
 * : 이 클래스 내부에 @Bean 선언한 메소드가 리턴하는 객체를 bean으로 등록해줌
 * */
@Configuration
public class Configuration {
	/**
	 * 라이브러리 객체를 리턴하는 클래스로 만든 뒤 @Bean 어노테이션으로 선언함
	 * */
	@Bean
	public 라이브러리객체(리턴타입) method() {
		라이브러리객체 result = new 라이브러리객체();
		// 라이브러리 객체에 값을 지정해야 하는 필드(=beans:property or property 태그)가 있을 경우 세터 이용
		result.setField(field값);
		return result;
	}
}
```