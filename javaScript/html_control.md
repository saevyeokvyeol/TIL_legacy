# HTML 적용

## div, span에 텍스트 입력

```jsx
적용할 대상.innerText = "텍스트"; // 대상에 텍스트를 입력하되, 태그 적용X
적용할 대상.innerHTML = "텍스트"; // 태그를 적용해 텍스트 입력, DOM 생성법 대신 사용 가능
```

## form 조작

- input text
    
    ```jsx
    적용할 대상.value; // input text에 입력된 텍스트 가져오기
    적용할 대상.value = "텍스트"; // input text에 값 입력
    ```
    
- input radio/check
    
    ```jsx
    radioCheckName값; // name값이 같은 라디오/체크 버튼을 리스트로 가져옴
    radioCheckName값[n]; // name값이 같은 라디오/체크 버튼 중 n번째 체크 버튼을 가져옴
    
    radioCheckName값[n].check; // n번째 라디오/체크 버튼의 선택 여부를 가져옴
    radioCheckName값[n].value; // n번째 라디오/체크 버튼의 밸류값을 가져옴
    ```
    
- select
    
    ```jsx
    select.length; // select의 옵션의 갯수를 가져옴
    
    select.value; // select에서 선택한 옵션의 value값을 가져옴
    select[n].value; // select에서 n번째 옵션의 value값을 가져옴
    
    select.selectedIndex; // select에서 선택한 옵션의 index값을 가져옴
    
    select.options[n] = new Option("값", "value값"); // select의 n번째 옵션을 추가/덮어쓰기함
    
    select.options[n] = null; // select의 n번째 옵션을 삭제함
    ```

- submit, reset
    
    ```html
    <form onsubmit="return false" onreset="return false">
    	<input type="submit">
    	<input type="reset">
    	<!--
    		submit과 reset은 input이 아니라 form에 함수를 적용함
    		onsubmit과 onreset에서 false가 리턴되면 submit과 reset을 실행하지 않음
    		(함수에서만 리턴하면 적용X onsubmit, onreset에서 다시 처리해야 적용)
    	-->
    </form>
    ```
    
    ```html
    <!-- button을 submit 버튼, reset 버튼으로 만들기	-->
    <form>
    	<input type="button" onclick="submitBtn(form)">
    	<input type="button" onclick="resetBtn(form)">
    </form>
    	
    <script type="text/javascript">
    	function submitBtn(fr) {
    		fr.action="경로"; // 폼 액션 변경
    		fr.submit(); // 폼 전송
    	}
    	function resetBtn(fr) {
    		fr.reset(); // 폼 초기화
    	}
    </script>
    ```

## image

- img 변경
    
    ```jsx
    적용할 대상.src = "경로"; // 대상 이미지를 경로 이미지로 변경함
    
    적용할 대상.width = "너비"; // 대상 이미지의 html 너비를 변경함
    적용할 대상.height = "높이"; // 대상 이미지를 html 높이를 변경함
    ```

## event 등록

```jsx
onload = function() { // HTML이 로드되었을 때 실행
	document.getElementById("id값").on이벤트종류 = 함수명; // 함수 호출 시 반드시 () 생략

	document.getElementById("id값").on이벤트종류 = function() {
		실행문;
	} // 익명 함수 선언도 가능
}
```