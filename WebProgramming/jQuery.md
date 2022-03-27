# jQuery

## 세팅 방법

```jsx
<script type="text/javascript" src="jQuery 파일 경로"></script>
<script>
	JS 실행문;
</script>
```

## 기본 구조

```jsx
<script type="text/javascript">
	$(document).ready(function(){ // $ = jQuery
		$("선택자").속성 | 함수();
	});
</script>
```

```jsx
// 축약형
<script type="text/javascript">
	$(function(){
		$("선택자").속성 | 함수();
	});
</script>
```

## 선택자Selectors

```jsx
// n은 0부터 시작됨

요소:(n) // 요소 중 n번째 요소
요소:gt(n) // n번째 요소보다 큰 요소
요소:lt(n) // n번째 요소보다 작은 요소

요소:not(seletor) // 특정 선택자가 아닌 요소

요소:even // 짝수 번째 요소
요소:odd // 홀수 번째 요소

[attripute] // 속성을 가진 요소에만 적용
[attripute=value] // 속성값이 value인 요소에만 적용
[attripute~=value] // 속성값에 value가 포함된(여러 속성값 중 하나) 요소에만 적용
[attribute|=value] // 속성값이 value거나 value로 시작하는 요소에만 적용
[attribute^=value] // 속성값이 value로 시작하는 요소에만 적용
[attribute$=value] // 속성값이 value로 끝나는 요소에만 적용
[attribute*=value] // 속성값이 value가 포함된(문자열에 포함) 요소에만 적용
```

## 반복문

```jsx
$.each(반복 대상, function(index, item){
	실행문;
});
/*
	배열 등 선택자가 아닌 것을 반복함
	index, item는 각각 번지수와 값을 나타냄
*/

$(selector).each(function(index, item){
	실행문;
});
/*
	선택자를 반복함 
	index, item는 각각 번지수와 값을 나타냄
*/

/* 
	※ 참고: item.value == $(this).val()
*/
```

## CSS 적용 방법

```jsx
$("선택자[, 선택자, 선택자...]").css("속성", "값[ 값 값...]")[.css("속성", "값").css("속성", "값")];
/*
	메소드 체인 기법으로 속성을 작성할 때는 카멜 표기법과 케밥 표기법 어느 쪽을 사용해도 적용됨
*/

$("선택자[, 선택자, 선택자...]").css({속성: "값", 속성: "값", 속성: "값"...});
/*
	이 방법으로 속성을 작성할 때는
	속성을 따옴표로 묶으면 케밥 표기법을, 속성을 묶지 않으면 카멜 표기법을 사용해야 함
*/
```

## DOM 접근&조작

### div, span 내부 텍스트 읽어오기

```jsx
$("선택자").text() // = innerText
$("선택자").html() // = innerHTML
```

### 텍스트 박스에서 값 읽어오기

```jsx
$("선택자").val(); // = value
```

### 이벤트 적용

```jsx
$("선택자").이벤트종류(); // onxxx 이벤트에서 on 생략
```