# Reflection

## 개념

- 어떤 객체가 가지고 있는 필드, 생성자, 메소드의 정보를 동적으로 가져올 수 있도록 하는 것
- 객체를 미리 만들어 사용하는 것이 아니라 실행 도중에 필요한 객체를 생성하고 호출할 수 있도록 도움
- Class<?> API를 이용함

## Class<?>

```java
Class<?> clz = Class.forName(String className); // 문자열로 된 클래스 경로를 입력
Object obj = className.getDeclaredConstructor(클래스 생성 시 필요한 매개변수).newInstance(); // 객체 생성
// 매개변수로 클래스 생성 시 필요한 매개변수 입력, 없을 시 비워둠
// 생성된 객체를 다운캐스팅해 해당 클래스 객체로 생성해 사용할 수 있음
```