# 함수

## 선언&호출 방법

```jsx
// 선언적 함수 선언
function 함수명(매개변수, 매개변수...){
	실행문;
	return 리턴값;
}

// 선언적 함수 호출
함수명; // 함수
함수명(); // 리턴값
// 매개변수의 갯수가 달라도 호출되기 때문에 오버로딩할 필요X
// 오버로딩할 경우 맨 마지막에 생성된 함수만 호출됨
```

```jsx
// 익명 함수 선언
let 변수명 = function(매개변수, 매개변수...){
	실행문;
	return 리턴값;
}

// 익명 함수 호출
result = 변수명; // 함수
result = 변수명(); // 리턴값
```

```jsx
// 람다식 함수 선언
let 변수명 = (매개변수, 매개변수...) => {
	실행문;
	return 리턴값;
}

// 람다식 함수 호출
result = 변수명; // 함수
result = 변수명(); // 리턴값
```

## 대화상자 함수

```jsx
alert("문자열"); // 대화상자로 문자열 출력
prompt("문자열", "초기값") // 프롬프트 창으로 문자열을 출력하고 문자열을 입력받음
confirm("문자열") // 대화상자로 문자열 출력 뒤 확인(true), 취소(false) 입력받음
```

## 문자 → 숫자 변환 함수

```jsx
Number(문자열);
/*
	문자열을 정수형으로 바꾸되, 문자가 섞여있을 경우 NaN(Not a Number)가 도출됨
*/

parseInt(문자열);
/*
	실수를 넣을 경우 소숫점을 머리고 정수형으로 바꿈
	문자열이 숫자일 경우 정수형으로 바꿈
	문자열이 숫자로 시작할 경우 이어지는 숫자만 추출해 정수형으로 바꿈
	문자열이 문자로 시작할 경우 NaN(Not a Number)가 도출됨
*/
```

## 일정 시간마다 특정 함수를 호출해주는 함수

```jsx
window.setTimeout("함수명()", ms);
/*
	입력한 ms가 지나면 입력한 함수를 한 번 호출해주는 함수
	재귀함수로 만들면 일정 시간마다 함수가 반복되도록 설정할 수 있음
*/

window.clearTimeout(대상);
/*
	setTimeout() 함수의 기능을 제거하는 함수
	setTimeout()을 변수에 넣고 그 변수를 clearTimeout()의 매개변수로 넣어야 함
*/

window.setInterval("함수명()", ms)
/*
	입력한 ms마다 입력한 함수를 호출해주는 함수
*/

window.clearInterval(대상);
/*
	setInterval() 함수의 기능을 제거하는 함수
	setInterval()을 변수에 넣고 그 변수를 clearInterval()의 매개변수로 넣어야 함
*/
```

## 날짜 함수

```jsx
let today = new Date(연, 원, 일, 시, 분, 초);
/*
	표준시 방식으로 날짜를 출력하는 함수
	매개변수를 입력하지 않으면 현재 날짜와 시간을 가져옴
*/

today.toLocaleString(); 
/*
	연.월.일 오전|오후 시:분:초 형식으로 날짜와 시간을 출력하는 함수
	today에 연월일 매개변수를 입력했을 경우 시간은 오전 12시 0분 0초로 출력됨
*/

today.getFullYear(); // 연도를 출력하는 함수
today.getMonth(); // 월을 출력하는 함수(0부터 시작)
today.getDay(); // 요일을 출력하는 함수(일=0부터 시작)
today.getDate(); // 일자를 출력하는 함수

today.getHours(); // 시간을 출력하는 함수(24시간제로 출력)
today.getMinutes(); // 분을 출력하는 함수
today.getSecond(); // 초를 출력하는 함수

today.setFullYear(); // 변수에 저장된 연도를 변경하는 함수
today.setMonth(); // 변수에 저장된 월을 변경하는 함수
today.setDay(); // 변수에 저장된 요일을 변경하는 함수
today.setDate(); // 변수에 저장된 일자를 변경하는 함수

today.setHours(); // 변수에 저장된 시간을 변경하는 함수
today.setMinutes(); // 변수에 저장된 분을 변경하는 함수
today.setSecond(); // 변수에 저장된 초를 변경하는 함수
```

## 문자열 → 코드 변환 함수

```jsx
eval("문자열");
/*
	인수로 들어온 문자열을 JS 코드로 만듦
	어떤 코드가 들어가도 JS 코드로 만들기 때문에 보안에 취약해 권장X
*/

new Function("return 문자열")();
/*
	문자열을 JS 코드로 만듦
	eval() 대체용으로 사용
*/
```