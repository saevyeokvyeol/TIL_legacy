# HTML

## 용어

### DOM & BOM

- DOM(Document Object Model)
: 우리가 적은 HTML 문서를 해석해 나타난 웹페이지의 내용
  트리의 형태로 나타냄
- BOM(Browser Object Model)
: 웹페이지 내용을 제외한 브라우저 창에 포함된 모든 객체 요소

## 태그

### HTML 기본 구조

```html
<!DOCTYPE html> <!-- 문서의 첫 줄에 작성해 문서의 형태를 나타냄 -->
<html>
	<head>
		<!-- 브라우저에서 보이지 않는 문서의 정보 등을 작성 -->
		<meta charset="EUC-KR">
		<title>Title</title> <!-- 탭에 나타나는 페이지 제목을 작성 -->
	</head>
	<body>
		<!-- 실제로 웹 브라우저에 나타나는 부분을 작성 -->
		<태그이름 속성="값" 속성="값"...>
			content
		</태그이름>
	</body>
</html>
```

### heading, br, p

```html
<!-- 문서 내부에서 제목이나 타이틀을 표시할 때 사용 -->
<h1>제일 큰 글씨</h1>
<h2>숫자가</h2>
<h3>커질수록</h3>
<h4>글자가</h4>
<h5>작아짐</h5>
<h6>제일 작은 글씨</h6>
```

```html
<!-- 개행 -->
줄을 바꿀 때에는<br>br태그를 사용
<br><br><br><br>여러 번 사용하면 줄이 여러 번 바뀜(반복 가능)
```

```html
<!-- 단락 구분 -->
단락을 구분할 때에는<p>p태그를 사용
<p><p><p><p>여러 번 사용해도 단락이 여러 번 바뀌지는 않음(반복 불가능)
```

### 특수문자

```html
&nbsp; <!-- 띄어쓰기 -->
&it; <!-- < 기호 -->
&gt; <!-- > 기호 -->
&amp; <!-- & 기호 -->
```

### pre, xmp

```html
<!-- pre -->
<pre>
	pre 태그 안에 작은 텍스트는
	   작성한 그대로 브라우저에
	      출력됨
	         (띄어쓰기, 개행 등 자동 적용)
</pre>
```

```html
<!-- xmp -->
<xmp>
	xmp 태그 안에 작은 텍스트는
	   <b>태그</b>까지 문자로 인식해
	      작성한 그대로 브라우저에 출력됨
</xmp>
```

### u, i, b, strong

```html
<!-- u 태그 -->
<u>밑줄을 표현하고 싶을 때에 사용</u>
```

```html
<!-- i 태그 -->
<i>기울임꼴(이탤릭체)를 표현하고 싶을 때 사용</i>
```

```html
<!-- b, strong 태그 -->
<b>글씨를 굵게 표현하고 싶을 때 사용</b>
<strong>글씨를 굵게 표현+브라우저에 중요한 내용임을 알리고 싶을 때 사용</strong>
```

### a

```html
<!--
	a 태그
	1. 다른 페이지로 이동
	2. 현재 페이지 내에서 특정 영역으로 이동
	3. mailto 기능 -> 요즘에는 거의 사용X
	
	대표적인 인라인 요소

	속성: target="_self | _blank | _top | _parent | 창이름"
	target으로 이동할 페이지가 열릴 창을 지정할 수 있음
	_self: 현재 탭에서 열림(기본값)
	_blank: 새 탭(설정에 따라 새 창)에서 열림
	_top: 부모가 존재할 경우 최상단 브라우징에서, 없을 경우 현재 탭에서 열림
	_parent: 부모가 존재할 경우 부모에, 없을 경우 현재 탭에서 열림
	창이름: 지정된 타겟(= name="속성")에서 열림
-->
<a href="이동할 경로 | id">content</a>

```

### img, 경로

```html
<!-- img 태그 -->
<img alt="대체 텍스트" src="이미지 경로" title="(필수X)툴팁 텍스트">

<a href="이미지 경로">
	<img alt="대체 텍스트" src="이미지 경로">
</a>
<!-- 태그를 겹쳐 이미지를 클릭할 경우 이미지 파일이 열리게 수 있음 -->
```

```html
../ <!-- 상위 폴더 -->
./ <!-- 현재 폴더 -->
/ <!-- 최상위 root -->
```

### table

```html
<table> <!-- 테이블 생성 -->

	<caption>title</caption> <!-- 테이블 이름 생성 -->

	<tr> <!-- 행 생성 -->
		<th></th> <!-- 헤더열 생성: 디폴트값이 중앙 정렬/굵은 글씨 -->
		<td></td> <!-- 열 생성 -->
	</tr>

	

	<thead> <!-- 테이블의 헤더 영역 선언: 어디에 선언되도 테이블의 맨 위로 올라감 -->
	</thead>

	<tbody> <!-- 테이블의 바디 영역 선언 -->
	</tbody>

	<tfoot> <!-- 테이블의 푸터 영역 선언: 어디에 선언되도 테이블의 맨 아래로 내려감 -->
	</tfoot>

</table>
```

```html
<th colspan="n"> <!-- n열 병합 -->
<th rowspan="n"> <!-- n행 병합 -->
```

### form

```html
<!-- form 선언: 선언하지 않으면 form 내부 정보 전달 불가 -->
<form action="submit되었을 때 이동할 페이지" method="get | post | ..." name="" | id="">
<!-- method = "get" - 입력된 값이 url 주소에 보여지면서 전송됨(생략 시 기본값)
					보안상 주로 select 전용으로 사용
	"post" - 전송되는 정보들이 request의 body 영역에 숨겨져 전송됨
						update, delete, select일 때 많이 사용--> 
<!-- name="" | id="": JS나 jQuery에서 form에 접근할 때 사용 -->
	<input...>
</form>
```

```html
<!-- name="속성": 정보를 전송하기 위해서는 필수적으로 입력해야 함 -->
<input type="text" name="속성" size="필수X" value="초기값(필수X)" disabled="disabled(submit 시 전송X)" readonly="readonly(submit 시 전송O)"> <!-- 텍스트 박스: type을 생략해도 텍스트 박스가 생성됨 -->

<input type="password" name="속성" maxlength="필수X" placeholder="안내 메세지"> <!-- 비밀번호 박스 -->
<!-- placeholder="안내 메세지": 모바일 환경에서 작은 화면에 필요한 정보를 주기 위해 사용함 -->

<fieldset>
	<legend>박스 이름</legend> <!-- 필드셋에 이름을 설정 -->
	<input type="checkbox" name="속성" value="안내 메세지"> <!-- 체크 버튼: 같은 속성끼리는 name을 같게 쓰는 것을 권장(필수X) -->
	<input type="radio" name="속성" value="안내 메세지"> <!-- 라디오 버튼: name이 같은 라디오 버튼끼리는 하나만 선택 가능 -->
</fieldset>

<select name="속성" size="한 번에 보여지는 옵션 갯수" multiple="multible(size를 설정했을 때 여러 개 선택 가능 옵션)"> <!-- 셀렉트 박스 생성 -->
	<option value=""></option> <!-- 셀렉트 박스의 옵션 추가 -->
</select>

<textarea name="속성" col="열 길이" rows="행 길이">content</textarea>
<!-- value 없음, 태그 사이에 적은 content가 텍스트에리어에 작성한 그대로 들어감 -->

<input type="hidden" name="속성" value="안내 메세지"> <!-- hidden: 클라이언트에게 보이지 않으면서 서버로 보내야 하는 정보를 입력할 때 사용 -->

<input type="button" value="버튼에 표시되는 텍스트"> <!-- 버튼 -->
<input type="file" name="file">
<!-- file 버튼: file을 첨부할 때 사용, 다른 버튼과 달리 name 필수
	file 버튼을 사용할 때는 반드시 method는 post, form 요소 속성으로 enctype="multipart/form-data"를 설정해야 함 -->
<input type="submit" value="버튼에 표시되는 텍스트"> <!-- submit 버튼: form에 입력된 내용을 전송함 -->
<input type="reset" value="버튼에 표시되는 텍스트"> <!-- reset 버튼: form에 입력된 내용이 웹페이지가 로딩되었을 때 초기 상태로 돌아감 -->
```

```html
<button type="button">
<button type="submit">
<button type="reset">
<!--
	input의 button, submit, reset과 동일
	type 생략 시 form 안에 있을 때는 기본값 submit, form 밖에 있을 때는 기본값 button
	때문에 bootstrap을 이용해 비동기화 통신을 할 때 form 안에서는 type 필수
-->

```

```html
<!-- HTML5부터 추가된 attribute -->
<input type="date" name="속성" min="최소 날짜" max="최대 날짜"> <!-- 날짜를 입력받을 때 사용 -->

<input type="number" name="속성" min="최소 숫자" max="최대 숫자"> <!-- 숫자를 입력받을 때 사용 -->

<input type="color" name="속성"> <!-- 색을 입력받을 때 사용 -->

<input type="email" name="속성"> <!-- 메일을 입력받을 때 사용 -->

<input type="range" name="속성"> <!-- 범위를 입력받을 때 사용 -->

<input type="text" name="속성" required="required"> <!-- required="required": 입력하지 않으면 submit불가(모든 input에 사용 가능) -->

<form novalidate="novalidate"> <!-- novalidate="novalidate": form 내부에 required input이 있어도 입력하지 않을 수 있음 -->

<label for="속성">content</label> <!-- content 클릭 시 속성 값이 같은 input에 커서가 놓임 -->
```

### ul, ol

```html
<!-- unordered list: 순서없는 리스트 작성 시 사용 -->
<ul type="disc | circle | square">
	<li>첫번째</li>
	<li>두번째</li>
	<li>세번째</li>
</ul>
```

```html
<!-- ordered list: 순서가 있는 리스트 작성 시 사용 -->
<ol type="1 | a | A | i | I" start="순서 시작 번호 입력">
	<li>첫번째</li>
	<li>두번째</li>
	<li>세번째</li>
</ol>
```

### iframe

```html
<iframe src="경로" name="속성">
```

### div, span

```html
<div>content</div>
<!-- 특별한 기능없이 block 공간을 만드는 태그 -->

<span>content</span>
<!-- 특별한 기능없이 inline 공간을 만드는 태그 -->
```

### 구조 태그

```html
<!-- unordered list: 순서없는 리스트 작성 시 사용 -->

<header></header>
<!--
	헤더 영역 요소
	내부에 section, header, footer, nav가 들어올 수 없음
	section 안에 생성할 수 있음
-->

<nav></nav>
<!--
	네비게이션 영역 요소
	메뉴 등 페이지 안의 주요 네비게이션 링크를 묶을 때 사용
-->

<aside></aside>
<!--
	어사이드 영역 요소
	본문과 직접적인 관계가 없는 좌우 영역 정보를 묶을 때 사용
-->

<section></section>
<!--
	섹션 영역 요소
	페이지 내에서 섹션을 나눌 때 사용
	내부에 header, footer를 생성할 수 있음
-->

<article></article>
<!--
	아티클 영역 요소
	페이지 내에서 독립적인 글을 묶을 때 사용
-->

<footer></footer>
<!--
	푸터 영역 요소
-->
```