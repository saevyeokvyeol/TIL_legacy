# Listener

## 특징

- 특정 액션이 일어나면 호출되는 메소드가 정의된 interface
- implement해 오버라이딩해 사용함

## 주요 종류

1. ServletContextListener
    - 서버가 start되거나 stop될 때 호출되는 메소드 정의
2. HttpSessionListener
    - 세션이 시작될 때(=브라우저가 시작될 때) 혹은 세션이 종료될 때(=session.invalidate() 호출될 때, session timeout 될 때, 단순 브라우저 종료 시는 호출X) 호출되는 메소드 정의
3. ServletRequestListener
    - 요청이 start될 때, 요청이 stop될 때 호출되는 메소드 정의

## 등록

```xml
<!-- 액션이 일어나면 자동으로 호출되기 때문에 매핑X -->

<!-- 리스너 등록 -->
<listener>
	<listener-class>필터 파일 경로</listener-class>
</listener>
```

```java
// 액션이 일어나면 자동으로 호출되기 때문에 매핑X

@WebListener
```