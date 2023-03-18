# 반복문

```jsx
$.each(반복 대상, function(index, item){
	실행문;
});
/*
	배열 등 선택자가 아닌 것을 반복함
	index, item는 각각 번지수와 값의 변수명을 나타냄
*/

$(selector).each(function([index, item]){
	실행문;
});
/*
	선택자를 반복함 
	index, item는 각각 번지수와 값의 변수명을 나타냄
*/

/* 
	※ 참고: item.value == $(this).val()
*/
```