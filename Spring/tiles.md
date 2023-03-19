# Tiles

## 개념

- 여러 파일을 하나의 파일처럼 묶어 화면에 보여주는 것
- JSP의 include 기능과 비슷하지만 include보다 수정, 확장에 용이함

## 사용 설정

### dependency 추가

```xml
<!-- pom.xml -->

<!-- tiles를 사용하기 위해 필요한 dependency 추가 -->
<dependency>
    <groupId>org.apache.tiles</groupId>
    <artifactId>tiles-jsp</artifactId>
    <version>3.0.8</version>
</dependency>

<dependency>
    <groupId>org.apache.tiles</groupId>
    <artifactId>tiles-servlet</artifactId>
    <version>3.0.8</version>
</dependency>

<dependency>
    <groupId>org.apache.tiles</groupId>
    <artifactId>tiles-extras</artifactId>
    <version>3.0.8</version>
</dependency>
```

### Tiles Bean 등록: xml 방식

```xml
<!-- servlet-context.xml -->

<!-- Tiles 등록 -->
<beans:bean class="org.springframework.web.servlet.view.UrlBasedViewResolver" id="urlBasedViewResolver">
	<beans:property name="order" value="0"/> <!-- 순위를 높여 tiles 방식을 가장 먼저 시도하게 함 -->
	<beans:property name="viewClass" value="org.springframework.web.servlet.view.tiles3.TilesView"/>
</beans:bean>

<beans:bean class="org.springframework.web.servlet.view.tiles3.TilesConfigurer">
	<beans:property name="definitions">
		<beans:list>
			<beans:value>tiles-definitions 파일 경로</beans:value>
		</beans:list>
	</beans:property>
</beans:bean>
```

### Tiles Bean 등록: Annotation 방식

```java
/**
 * Config.java 파일
 * */

@Configuration // Bean 등록 전용 클래스를 선언하기 위한 어노테이션
public class Config {

	@Bean // Bean 등록을 위한 어노테이션
	public UrlBasedViewResolver getUrlBasedViewResolver() {
		UrlBasedViewResolver tilesViewResolver = new UrlBasedViewResolver();
		
		tilesViewResolver.setOrder(0); // 순위를 높여 tiles 방식을 가장 먼저 시도하게 함
		tilesViewResolver.setViewClass(TilesView.class);
		
		return tilesViewResolver;
	}
	
	@Bean
	public TilesConfigurer getTilesConfigurer() {
		TilesConfigurer tilesConfigurer = new TilesConfigurer();
		
		tilesConfigurer.setDefinitions(new String[] {"tiles-definitions 파일 경로"});
		
		return tilesConfigurer;
	}
}
```

## tiles 설정

- tiles-definitions 파일 설정
    
    ```xml
    <!-- tiles.xml : tiles-definitions 파일 -->
    
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE tiles-definitions PUBLIC "-//Apache Software Foundation//DTD Tiles Configuration 3.0//EN"
    	"http://tiles.apache.org/dtds/tiles-config_3_0.dtd">
    
    <tiles-definitions>
    	<definition name="문서 별칭" template="레이아웃용 파일 경로(루트 기준)">
    		<put-attribute name="속성 name값(jsp 속성 name값과 맞춰줌)" value="속성 파일 경로(루트 기준)"/>
    		<!--
    			속성 name값의 경우 뷰에 따라 달라져야 하는 메인 섹션은 템플릿 선언 태그에서 지정X
    			아래 화면 구성을 처리하는 선언 태그에서 지정
    		-->
    	</definition>
    	
    	<!-- Controller에서 return하는 뷰의 정보에 따라 화면 구성 처리 -->
    	<definition name="view 경로(와일드카드 사용 가능)" extends="문서 별칭(<definition> 태그로 선언된 문서 별칭 입력)">
    		<put-attribute name="속성 name값(jsp 속성 name값과 맞춰줌)" value="속성 파일 경로(루트 기준)"/>
    		<!--
    			view 경로에 와일드카드가 포함될 경우 속성 파일 경로에 해당 부분은 {n}으로 맞춰줌
    			1번째 와일드카드의 경우 {1}...
    			view 경로에 와일드카드를 연속해서 사용하는 경우(**) 하위의 모든 파일이 선택됨
    		-->
    	</definition>
    </tiles-definitions>
    ```
    
- 레이아웃 JSP 파일 설정
    
    ```html
    <%@ page language="java" contentType="text/html; charset=UTF-8"
        pageEncoding="UTF-8"%>
    <!-- tiles taglib 추가 -->
    <%@ taglib uri="http://tiles.apache.org/tags-tiles" prefix="tiles"%>
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="UTF-8">
    		<title></title>
    	</head>
    	<body>
    			<!-- <tiles:insertAttribute> 태그로 레이아웃 지정 -->
    			<tiles:insertAttribute name="속성 name값"/>
    	</body>
    </html>
    ```