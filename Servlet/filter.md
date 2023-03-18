# Filter

## 특징

- 사용자의 요청을 가로채 자동으로 사전 혹은 사후에 처리하는 것
- 한글 인코딩 처리, 세션 유무 체크, log 기록, spring security 인증/권한, 유효성 체크 등에 사용
- 필터는 여러 개 사용할 수 있으며, 모든 필터가 사전처리 된 후 사전처리 역순으로 사후처리됨
- interface로 제공되어 implement하고 함수를 오버라이딩 해 사용함

## 등록 및 매핑

```xml
<!-- 필터 파일을 생성해 작성한 뒤 등록 및 매핑을 완료해야 필터링 가능 -->

<!-- 필터 등록 -->
<filter>
	<filter-name>필터 이름</filter-name>
	<filter-class>필터 파일 경로</filter-class>
</filter>

<!-- 필터 매핑 -->
<filter-mapping>
	<filter-name>필터 이름</filter-name>
	<url-pattern>필터링할 파일 url 경로1(루트 기준, 와일드카드 사용 가능, 여러 개)</url-pattern>
	<url-pattern>필터링할 파일 url 경로2(여러 줄 입력 가능)</url-pattern>
</filter-mapping>
```

```java
// 필터 파일을 생성해 작성한 뒤 등록 및 매핑을 완료해야 필터링 가능

@WebFilter(urlPatterns = { "필터링할 파일 url 경로" })
```

## 사용법

```java
// init() 메소드 오버라이딩

@Override
public void init(FilterConfig filterConfig) throws ServletException {
	System.out.println("SampleFilter init() call");
}
// 파일이 열릴 때 호출됨
```

```java
// doFilter() 메소드 오버라이딩

@Override
public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
		throws IOException, ServletException {
	// 사전 처리
	
	// 실제 타겟 대상 호출: 타겟 대상 호출을 중심으로 사전 처리와 사후 처리가 나뉨
	chain.doFilter(request, response);
	
	// 사후 처리
}
// 타겟 대상이 호출될 때 호출됨
```

```java
// destroy() 메소드 오버라이딩

@Override
public void destroy() {
	System.out.println("SampleFilter destroy() call");
}
// 파일이 재컴파일되거나 서버가 종료될 때 호출됨
```

## init-param

### web.xml에서 생성
    
```xml
<!-- 한 서블릿에서만 사용할 init-param 생성 -->

<filter>
    <filter-name>필터 이름</filter-name>
    <filter-class>필터 파일 경로</filter-class>

    <init-param>
        <param-name>init변수명</param-name>
        <param-value>값</param-value>
    </init-param>
    <!-- filter 등록 시 변수 등록 -->

</filter>
```
    
### @annotation에서 생성
    
```java
@WebFilter(
        urlPatterns = { "/*" }, 

        initParams = { 
                @WebInitParam(name = "init변수명", value = "값"),
                @WebInitParam(name = "init변수명", value = "값")...
        }

)
```
    
### 호출 방법
    
```java
public class 클래스명 implements Filter {

    String 변수명;
    
    @Override
    public void init(FilterConfig filterConfig) throws ServletException{
        변수명= super.getInitParameter("init변수명");
        // initParam을 호출해 전역 변수로 저장해 사용
    }
}
```