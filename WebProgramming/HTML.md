# HTML

## 용어

### DOM & BOM

- DOM(Document Object Model)
: 우리가 적은 HTML 문서를 해석해 나타난 웹페이지의 내용
  트리의 형태로 나타냄
- BOM(Browser Object Model)
: 웹페이지 내용을 제외한 브라우저 창에 포함된 모든 객체 요소

## HTML 기본 구조

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

## heading, br, p

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

## 특수문자

```html
&nbsp; <!-- 띄어쓰기 -->
&it; <!-- < 기호 -->
&gt; <!-- > 기호 -->
&amp; <!-- & 기호 -->
```

## pre, xmp

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

## u, i, b, strong

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

## a

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
				창이름
-->
<a href="이동할 경로 | id">content</a>

```

## img, 경로

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

## table

```html
<table> <!-- 테이블 선언 -->

	<caption>title</caption> <!-- 테이블 이름 선언 -->

	<td> <!-- 행 선언 -->
		<th></th> <!-- 열 선언 -->
	</td>

	<th> <!-- 헤더행 선언: 디폴트값이 중앙 정렬/굵은 글씨 -->
	</th>

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

## form

```html
<!-- form 선언: 선언하지 않으면 form 내부 정보 전달 불가 -->
<form action="submit되었을 때 이동할 페이지" method="get | post | ..." name="" | id="">
<!-- method = "get" - 입력된 값이 url 주소에 보여지면서 전송됨
					  보안상 주로 select 전용으로 사용
			  "post" - 전송되는 정보들이 request의 body 영역에 숨겨져 전송됨
						 update, delete, select일 때 많이 사용--> 
<!-- name="" | id="": JS나 jQuery에서 form에 접근할 때 사용 -->
	<input...>
</form>
```

```html
<!-- name="속성": 정보를 전송하기 위해서는 필수적으로 입력해야 함 -->
<input type="text" name="속성" size="필수X" value="초기값(필수X)" disabled="disabled(submit 시 전송X)" readonly="readonly(submit 시 전송O)"> <!-- 텍스트 박스 -->

<input type="password" name="속성" maxlength="필수X" placeholder="안내 메세지"> <!-- 비밀번호 박스 -->

<fieldset>
	<legend>박스 이름</legend> <!-- 필드셋에 이름을 설정 -->
	<input type="check" name="속성" value="안내 메세지"> <!-- 체크 버튼 -->
	<input type="radio" name="속성" value="안내 메세지"> <!-- 라디오 버튼: named이 같은 라디오 버튼끼리는 하나만 선택 가능 -->
</fieldset>

<select name="속성" size="한 번에 보여지는 옵션 갯수" multiple="multible(size를 설정했을 때 여러 개 선택 가능 옵션)"> <!-- 셀렉트 박스 생성 -->
	<option value=""></option> <!-- 셀렉트 박스의 옵션 추가 -->
</select>

<textarea name="속성" col="열 길이" rows="행 길이"></textarea>

<input type="button" value="버튼에 표시되는 텍스트"> <!-- 버튼 -->
<input type="submit" value="버튼에 표시되는 텍스트"> <!-- submit 버튼 -->
```