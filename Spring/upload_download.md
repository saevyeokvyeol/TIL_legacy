# Upload, Download

## Upload

### 준비 작업

- dependency 추가
    
    ```xml
    <!-- pom.xml에 파일 업로드 dependency 추가 -->
    <dependency>
    	<groupId>org.apache.commons</groupId>
    	<artifactId>commons-io</artifactId>
    	<version>1.3.2</version>
    </dependency>
    
    <dependency>
    	<groupId>commons-fileupload</groupId>
    	<artifactId>commons-fileupload</artifactId>
    	<version>1.3.1</version>
    </dependency>
    ```
    
- Bean 등록: xml 방식
    
    ```xml
    <!-- servlet-context.xml에 파일 업로드에 필요한 Bean 생성 -->
    <bean class="org.springframework.web.multipart.commons.CommonsMultipartResolver" id="multipartResolver"/>
    ```
    
- Bean 등록: Annotation 방식
    
    ```java
    /**
     * Config.java 파일
     * */
    
    @Configuration // Bean 등록 전용 클래스를 선언하기 위한 어노테이션
    public class Config {
    
    	/**
    	 * 업로드 컴포넌트 생성
    	 * : 메소드 이름을 반드시 multipartResolver로 생성
    	 * */
    	@Bean // Bean 등록을 위한 어노테이션
    	public CommonsMultipartResolver multipartResolver() {
    		CommonsMultipartResolver commonsMultipartResolver = new CommonsMultipartResolver();
    		return commonsMultipartResolver;
    	}
    }
    ```
    

### JSP(HTML) 마크업

```html
<form action="이동 경로" method="post" enctype="multipart/form-data">
<!-- 업로드 폼은 반드시 post 방식, enctype="multipart/form-data" 설정해야 함 -->
	<input type="file" name="file">
	<input type="submit" value="전송">
</form>
```

### Java 예제 코드

```java
/**
 * 폼 정보를 각 객체로 나누어 받을 경우
 * */

@RequestMapping("요청 경로")
// 인수의 MultipartFile 변수명은 input type="file" name과 맞춰야 함
// java 프로젝트 실제 경로를 가져오기 위해 인수로 HttpSession을 받음
public void upload(MultipartFile file, HttpSession session) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 저장할 경로 설정
	
	try {
		file.transferTo(new File(path + "/" + file.getOriginalFilename())); // 저장 경로 아래에 파일 저장
	} catch (Exception e) {
		e.printStackTrace();
	}

	// Model 객체로 넘길 수 있는 정보: file.get~()으로 받을 수 있는 정보
}
```

```java
/**
 * DTO로 파일을 받을 경우 
 * */

@RequestMapping("요청 경로")
// 인수로 받는 DTO의 객체 필드 이름은 input name과 맞춰야 함
// java 프로젝트 실제 경로를 가져오기 위해 인수로 HttpSession을 받음
public void upload(UploadDTO dto, HttpSession session) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 저장할 경로 설정
	
	try {
		dto.getFile().transferTo(new File(path + "/" + dto.getFile().getOriginalFilename()));
		// 저장 경로 아래에 파일 저장
	} catch (Exception e) {
		e.printStackTrace();
	}

	// Model이나 ModelAndView로 넘겨주지 않아도 자동으로 DTO에 저장된 정보가 view로 넘어감
}
```

## Download

### 준비 작업

- Bean 등록: xml 방식
    
    ```xml
    <!-- servlet-context.xml에 파일 업로드에 필요한 Bean 생성 -->
    <bean class="org.springframework.web.servlet.view.BeanNameViewResolver">
    	<property name="order" value="0"/> <!-- 우선순위를 높여 가장 먼저 시도하게 함 -->
    </bean>
    ```
    
- Bean 등록: Annotation 방식
    
    ```java
    /**
     * Config.java 파일
     * */
    @Configuration // Bean 등록 전용 클래스를 선언하기 위한 어노테이션
    public class Config {
    	
    	@Bean // Bean 등록을 위한 어노테이션
    	public BeanNameViewResolver getBeanNameViewResolver() {
    		BeanNameViewResolver beanNameViewResolver = new BeanNameViewResolver();
    		
    		beanNameViewResolver.setOrder(0); // 우선순위를 높여 가장 먼저 시도하게 함
    		
    		return beanNameViewResolver;
    	}
    }
    ```

### JSP(HTML) 마크업

```html
<!-- 다운로드 기능 구현 마크업 -->

<a href="${pageContext.request.contextPath}/이동할 경로?fileName=${fileName}">${fileName}</a>
```

### Java 예제 코드

```java
/**
 * 다운로드 목록 가져오기
 * */
@RequestMapping("/downList.do")
// java 프로젝트 실제 경로를 가져오기 위해 인수로 HttpSession을 받음
public void download(HttpSession session, Model model) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 파일을 저장한 경로 설정
	File file = new File(path); // 저장 경로를 파일 객체로 저장
	String[] fileNames = file.list(); // file 안에 있는 파일 리스트 이름을 배열로 저장
	
	model.addAttribute("fileNames", fileNames);
	// Model이나 ModelAndView로 리스트 넘겨주기
}
```

```java
/**
 * 다운로드 기능 구현용 view
 * : 페이지 이동 없이 현재 화면에서 다운로드 할 수 있도록 제작
 * */
@Component
public class DownLoadCustomView extends AbstractView{
// AbstractView를 상속받아 오버라이딩한 클래스 자체가 view 역할을 함

	@Override
	protected void renderMergedOutputModel(Map<String, Object> map,
		HttpServletRequest request, HttpServletResponse response) throws Exception {
		
		File file = (File) map.get("fname"); // 다운로드 할 파일을 맵에서 꺼냄
		
		response.setContentType("application/download;charset-UTF-8"); // 인코딩 설정
		response.setContentLength((int) file.length()); // 파일 길이 설정

		// 브라우저 종류에 맞춰 인코딩
		String userAgent = request.getHeader("User-Agent");

		boolean isInternetExplorer = userAgent.indexOf("MSIE") > -1;
		String fileName = null;
		
		if (isInternetExplorer)
			fileName = URLEncoder.encode(file.getName(), "UTF-8");
		else
			fileName = new String(file.getName().getBytes("UTF-8"), "iso-8859-1");
		// 인코딩 종료

		response.setHeader("Content-Disposition", "attachment;filename=\"" + fileName.replace("+", "%20") + "\";");
		// response.setHeader("Content-Transfer-Encoding", "binary");

		OutputStream out = response.getOutputStream();
		FileInputStream fis = null;
		try {
			fis = new FileInputStream(file);
			FileCopyUtils.copy(fis, out); // 파일 복사

		} catch (Exception e) {
			// map.put("error", e.toString());
			e.printStackTrace();
		} finally {
			if (fis != null) {
				try {
					fis.close();
				} catch (IOException ex) {
					ex.printStackTrace();
				}
			}
		}
		out.flush();
	}
}
```

```java
/**
 * 실제 다운로드 기능 구현
 * */
@RequestMapping("/down.do")
public ModelAndView down(String fileName, HttpSession session) {
	String path = session.getServletContext().getRealPath("루트 기준 하위 경로"); // 파일을 저장한 경로 설정
	File file = new File(path + "/" + fileName); // 요청된 파일 이름으로 해당 파일 경로 설정
	
	return new ModelAndView("DownLoadCustomView", "fname", file);
	// 다운로드 기능 구현용 뷰에서 경로를 사용할 수 있도록 넘겨줌
	// 여기서 modelName은 구현 view에서 객체를 꺼낼 때 사용하는 이름과 맞춰줌
}
```
