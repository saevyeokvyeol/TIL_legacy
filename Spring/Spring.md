# 개념

- 자바 기반의 경량 라이브러리 덩어리
- EJB(Enterprise Java Bean)의 단점을 보완해 나온 오픈 소스 프레임워크
- 복잡한 엔터프라이즈 어플리케이션 개발을 간단하게 만들어줌
- 기능을 모듈로 제공하기 때문에 필요한 기능만 가져다 사용할 수 있음
- 공공부문 정보화 산업 표준인 전자정부 프레임워크(eGov)가 Spring과 MyBatis를 기반으로 하기 때문에 국내에서 활성화됨
- 현재 주류 프레임워크

# 특징

- 가벼운 경량의 라이브러리 → 현재에는 다소 무거워짐
- 기반 코드를 제공함
- xml 기반으로 컴포넌트를 개발함
- Maven( or Gradle) 기반 프로젝트 사용: Maven이 pom(Project Object Model).xml 파일을 통해 의존 관계 라이브러리를 관리함

## Spring의 전략

> 복잡한 엔터프라이즈 개발을 간단하게 만들고자 Spring이 사용하는 전략
> 

### Potable Service Abstraction

- 추상화된 기반 코드(=인터페이스) 제공

### Dependency Injection

- 의존 관계 주입(=제어의 역행 IoC Inversion of Control 개념을 문법으로 적용한 것)
- 필요한 객체를 개발자가 직접 생성❌
- SpringContainer(=외부 조립기)가 적절하게 객체를 생성하고 주입해 객체와 객체 간의 결합도를 느슨하게 만듦

### Aspect Oriented Programming

- 관점 지향 프로그래밍
- 프로그램 로직을 관점에 따라 핵심 로직과 공통 로직으로 분리해 공통 로직을 재사용함

# 사용 준비 작업

1. JDK 설치
2. IDE 설치(eclipse)
3. STS(SpringSource Tool Suite) 설치
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f401e5d5-6455-4caf-9bea-5bdba1ff0a0d/Untitled.png)
    
4. Maven or Gradle 세팅: 라이브러리와 빌드 프로세스를 관리해주는 툴