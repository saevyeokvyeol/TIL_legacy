# form

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