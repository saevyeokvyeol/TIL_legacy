# 한글 인코딩

```xml
<!--
	Spring에서 인코딩 필터 처리를 제공한 것을 web.xml에 입력하면 한글 인코딩 처리 완료
-->
<filter>
	<filter-name>charaterEncoding</filter-name>
	<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
	<init-param>
		<param-name>encoding</param-name>
		<param-value>UTF-8</param-value>
	</init-param>
</filter>

<filter-mapping>
	<filter-name>charaterEncoding</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
```