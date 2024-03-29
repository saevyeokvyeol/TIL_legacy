# DOM 접근&조작

## div, span 내부 텍스트 읽어오기

```jsx
$("선택자").text() // = innerText
$("선택자").html() // = innerHTML
```

## 텍스트 박스에서 값 읽어오기

```jsx
$("선택자").val(); // = value
```

## 이벤트 적용

```jsx
// 정적 요소에 이벤트 적용
$("선택자").이벤트종류()[.이벤트종류().이벤트종류()...]; // onxxx 이벤트에서 on 생략

// 정적 | 동적 요소에 이벤트 적용
$("선택자").on("이벤트종류", function(){실행문;})[.on().on()...];
$("선택자").on({"이벤트종류", function(){실행문;}, "이벤트종류", function(){실행문;}, "이벤트종류", function(){실행문;}...};

$(부모 노드).on("이벤트 종류", "선택자", function(){실행문;}); // 동적 요소에 이벤트를 적용할 때

// 특정 선택자가 가지고 있는 이벤트 강제로 호출
$("선택자").trigger("이벤트종류");
```

## 요소 추가

```jsx
$("선택자").prepend("요소");
// 입력한 선택자의 자식 노드 중 맨 앞에 추가됨

$("선택자").append("요소");
// 입력한 선택자의 자식 노드 중 맨 뒤에 추가됨

$("선택자").before("요소");
// 입력한 선택자의 앞 형제 노드로 추가됨

$("선택자").after("요소");
// 입력한 선택자의 뒷 형제 노드로 추가됨
```

## 요소 삭제

```jsx
$("선택자").remove();
// 입력한 선택자를 삭제함

$("선택자").empty();
// 입력한 선택자 내부의 컨텐츠를 삭제함
```

## 요소 수정

```jsx
$("선택자").attr("속성", "값")[.attr("속성", "값").attr("속성", "값").attr("속성", "값")...];
$("선택자").attr({속성: 값, 속성: 값, 속성: 값...};
/*
	선택자의 속성값을 변경함
	값을 입력하지 않을 경우 선택자의 속성값을 가져옴
	값으로 익명 함수를 사용할 수 있음
	(단, 값을 바꾸기 위해서는 리턴값을 바꿀 값으로 지정해줘야 함)
*/
```

## 클래스 추가&삭제

```jsx
$("선택자").addClass("클래스명");
$("선택자").removeClass("클래스명");
/*
	선택자에 클래스를 추가 혹은 삭제함
*/

$("선택자").toggleClass("클래스명");
/*
	선택자에 클래스를 번갈아 추가 혹은 삭제함
*/
```

## 요소 가시화&비가시화

- show, hide
    
    ```jsx
    $("선택자").show([speed, function(){}]);
    /*
    	파라미터가 없을 경우 선택자의 display 속성값을 기본값(block)으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").hide([speed, function(){}]);
    /*
    	파라미터가 없을 경우 선택자의 display 속성값을 none으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").toggle([speed, function(){}]);
    /*
    	파라미터가 없을 경우 선택자의 display 속성값을 기본값(block) 혹은 none으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    ```
    
- fadeIn, fadeOut
    
    ```jsx
    $("선택자").fadeIn([speed, function(){}]);
    /*
    	파라미터가 없을 경우 요소가 페이드인되며 display 속성값을 기본값(block)으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").fadeOut([speed, function(){}]);
    /*
    	파라미터가 없을 경우 요소가 페이드아웃되며 display 속성값을 none으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").fadeToggle([speed, function(){}]);
    /*
    	파라미터가 없을 경우 요소가 페이드인 혹은 페이드아웃 display 속성값을 기본값(block) 혹은 none으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").fadeTo([speed, opacity, function(){}]);
    /*
    	파라미터가 없을 경우 작동X
    	speed 파라미터를 넣을 경우 display 속성값을 기본값(block)으로 바꿈
    	(opacity 0이므로 보이지 않고 자리만 차지함)
    	opacity 파라미터가 나올 경우 요소에 입력한 투명도가 적용됨
    
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    ```
    
- slideDown, slideUp
    
    ```jsx
    $("선택자").slideDown([speed, function(){}]);
    /*
    	파라미터가 없을 경우 요소가 슬라이드다운되며 display 속성값을 기본값(block)으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").slideUp([speed, function(){}]);
    /*
    	파라미터가 없을 경우 요소가 슬라이드업되며 display 속성값을 none으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    */
    
    $("선택자").slideToggle([speed, function(){}]);
    /*
    	파라미터가 없을 경우 요소가 슬라이드다운 혹은 슬라이드업되며 display 속성값을 기본값(block) 혹은 none으로 바꿈
    
    	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
    	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
    ```
    

## 애니메이트 효과

```jsx
$("선택자").animate({속성: "값", 속성: "값", 속성: "값"...}, speed, function(){}]);
/*
	파라미터가 없을 경우 css 속성값을 기본값에서 입력한 속성값으로 변화시킴
	속성값에 +=와 -= 등의 대입 연산자 사용 가능

	speed 파라미터를 넣을 경우 ms 속도로 애니메이터 효과가 들어감
	콜백 함수를 넣을 경우 완료된 후 진행할 기능을 입력할 수 있음
*/
```