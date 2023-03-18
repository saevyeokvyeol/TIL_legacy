
# DOM 접근

## 네임값으로 접근

```jsx
document.name값[.name값 ...]; // name값으로 접근
```

## 속성값으로 접근

```jsx
document.getElementByClass("class값"); // class 값으로 접근
document.getElementById("id값"); // id 값으로 접근
document.getElementsByName("name값"); // name 값으로 접근
document.getElementsByTagName("tagName값"); // tagName 값으로 접근
```

## 특정 노드 기준으로 접근

```jsx
기준 노드.parentNode; // 부모 노드 접근
기준 노드.childNodes; // 자식 노드 리스트 접근
기준 노드.firstChild; // 첫 번째 자식 노드 접근
기준 노드.lastChild; // 마지막 자식 노드 접근
기준 노드.previousSibling; // 이전 형제 노드 접근
기준 노드.nextSibling; // 다음 형제 노드 접근
```

## img 접근

```jsx
document.images[index]; // html 파일 내의 모든 이미지를 선언순대로 배열로 만들어 접근
document.name값; // img name 속성의 값으로 접근 
/* 매개변수로 name값을 받을 때 "name값"으로 따옴표를 사용해 넘기면 new Function을 사용해 변환해야 하므로 주의 */
```

# DOM 생성

## 일반 태그 생성

1. 태그 생성
    
    ```jsx
    let x = document.createElement("tag명");
    // 추가하고 싶은 태그를 생성함
    ```
    
2. text 생성
    
    ```jsx
    let txt = document.createTextNode("문자열");
    // 태그 사이에 입력할 문자열을 생성함
    ```
    
3. 자식 노드 추가
    
    ```jsx
    x.appendChild(txt);
    // 문자열을 태그 안에 추가함
    
    부모 노드.appendChild(x);
    // 태그를 원하는 위치에 추가함
    ```
    
4. 결과
    
    ```html
    <태그명>문자열</태그명>
    <!-- HTML에 나타나는 결과 -->
    ```
    

## 테이블 생성

```jsx
// id값이 있는 테이블에 tr, td 추가

let row = 테이블id값.insertRow(0); // tr행 생성

let td1 = row.insertCell(0); // td열 생성
let td2 = row.insertCell(1); // td열 생성
let td3 = row.insertCell(2); // td열 생성

td2.innerHTML = "두 번째 td";
```

```html
<!-- 결과 -->
<table id="ta">
  <tr>
    <td></td>
    <td>두 번째 td</td>
    <td></td>
  </tr>
</table>
```

# DOM 삭제

```jsx
부모 노드.removeChild(삭제할 노드);
```

# DOM 메소드

```jsx
부모 노드.hasChildNodes() // 자식 노드 존재 여부를 가져옴

부모 노드.removeChild() // 자식 노드 삭제

부모 노드.replaceChild() // 자식 노드를 다른 노드로 교체

노드.settAttribute(속성명, 속성값) // 노드의 속성 추가

노드.getAttribute(속성명) // 노드의 속성 값 조회
```


# 주요 BOM

## window 객체

```jsx
```

## location 객체

```jsx
location.href;
/*
	현재 페이지의 url을 가져옴
*/

location.replace("경로");
/*
	현재 페이지의 url을 입력한 경로로 변경함
*/

location.reload();
/*
	현재 페이지를 새로고침함
*/
```

## history 객체

```jsx
history.go(n);
/*
	현재 페이지를 기준으로 현재 탭이 기억하고 있는 앞 n단계 페이지로 이동함
	-n을 입력할 경우 뒷 n단계 페이지로 이동함
*/

history.forward();
/*
	현재 탭이 기억하고 있는 앞 페이지로 이동함
*/

history.back();
/*
	현재 탭이 기억하고 있는 뒷 페이지로 이동함
*/
```

## navigator 객체

```jsx
navigator.userAgent;
/*
	현재 브라우저의 정보를 가져옴
*/
```

## screen 객체

```jsx
screen.width;
/*
	현재 스크린(=화면)의 너비를 가져옴
*/

screen.height;
/*
	현재 스크린(=화면)의 높이를 가져옴
*/
```