# 특징 및 개념

- 스프링 기반 프로젝트를 기반으로 자주 사용되는 설정을 자동으로 세팅해주는 라이브러리
    - XML 설정 파일 작성❌ → 기본 설정 수정 필요시 application.properties나 application.yml로 설정
    - 스프링 부트 버전 선택 시 가장 호환성이 좋은 라이브러리 버전을 자동으로 가져옴
    - 스프링 부트의 부모 객체인 Starter 라이브러리를 등록해 의존성 관리
    - @EnableAutoContiguration 어노테이션으로 스프링에서 자주 사용하는 설정을 자동 세팅
    - Tomcat이 내장되어 있어 @SpringBootApplication 어노테이션이 선언된 클래스의 main() 메소드를 실행하면 서버 구동
    - 내장 Tomcat이 존재하기 때문에 웹 어플리케이션을 WAR가 아닌 JAR 파일로 패키징 가능
- 기존 모놀리식 구조 프로젝트는 유지보수가 어려움 → MSA 구조로 변화하며 SpringBoot가 활성화됨
- MSA 구조와 JPA 기술을 기반으로 개발할 때 주로 사용
- 벤처기업, 스타트업에서 주로 사용

# 사용 준비 작업

## 설치

1. JDK 설치
2. IDE 설치(eclipse)
3. STS(SpringSource Tool Suite) 설치
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f401e5d5-6455-4caf-9bea-5bdba1ff0a0d/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e8d826cc-bd48-40dd-b3b8-8b35626e1d17/Untitled.png)
    

## 생성

![제목 없음-1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/60e6df72-82f0-44d5-8829-180361e1fdac/제목_없음-1.png)

![화면 캡처 2022-05-26 222229.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fc4295b-533c-444d-a795-de5f49b9b210/화면_캡처_2022-05-26_222229.png)

![제목 없음-2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4e1d9584-6c59-4252-b3bb-6976fd5f9237/제목_없음-2.png)

## 추가 dependency

```xml
<!-- pom.xml -->

<!-- SpringBoot 프로젝트에서 jsp 파일을 사용하기 위해 필요한 dependency -->
<dependency>
	<groupId>org.apache.tomcat.embed</groupId>
	<artifactId>tomcat-embed-jasper</artifactId>
	<version>9.0.46</version>
</dependency>

<!-- jstl을 사용하기 위한 dependency -->
<dependency>
	<groupId>javax.servlet</groupId>
	<artifactId>jstl</artifactId>
	<version>1.2</version>
</dependency>
```

## 기본 설정 문서

### application.properties

- SpringBoot의 설정 변경 기본 문서
- 추가 설정이나 기본 설정 변경이 필요한 경우 key=value 형태로 설정 입력

```python
# 서버 포트 번호 변경
server.port=8888

# 요청이 들어왔을 때 뷰 파일을 찾을 경로
spring.mvc.view.prefix=경로

# 요청이 들어왔을 때 가져올 뷰 파일 확장자
spring.mvc.view.suffix=.확장자명
```

### application.yml

- SpringBoot의 확장형 설정 변경 문서
- application.properties 파일이 존재하지 않아야 사용 가능
- 콜론(:)으로 설정 요소를 구분해 입력
- 비슷한 설정끼리 모아둘 수 있어 유지보수가 편리함

```python
# 서버 포트 번호 변경
server:
  port: 9000

spring:
  mvc:
    view:
      prefix: /WEB-INF/views/ # 요청이 들어왔을 때 뷰 파일을 찾을 경로
      suffix: .jsp # 요청이 들어왔을 때 가져올 뷰 파일 확장자
```

# 구조

- src/main/resources/static → html, css, img, js 문서

# 단위 테스트

- 스프링과 스프링부트는 단위테스트를 위한 어노테이션 제공
- 테스트를 위한 메소드 실행 시 서버가 해당 메소드 내부에 있는 코드만 실행한 뒤 자동으로 종료됨
- 단위테스트 클래스 위치: src/test/java/루트 패키지/

```java
@SpringBootTest // 테스트용 클래스 선언을 위한 어노테이션
class TestClass {

	@Test // 테스트용 메소드 선언을 위한 어노테이션
	void contextLoads() { // 메소드 작성 후 Run As -> JUnit Test
		System.out.println("TEST");
	}

}
```