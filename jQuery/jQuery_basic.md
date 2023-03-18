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