# 창 제어

## 새 창 열기

```jsx
window.open("경로", "이름", "속성", replace);
// a 태그와 달리 새 창에 다양한 속성을 부여할 수 있음
```

## 새 창에서 부모창 접근

```jsx
opener.부모창 요소;
// open() 함수를 통해 열린 새 창에서는 opener를 이용해 부모창에 있는 요소에 접근할 수 있음
```

## iframe 창 제어

```html
<a target="name값"></a>
<!-- HTML만 사용할 경우: a 태그의 target값으로 iframe 영역의 name값을 입력하면 해당 iframe에서 경로가 열림 -->

<a onclick="top.name값.location.href='경로'"></a>
<!-- JS에서 location.href를 사용할 경우: 상위 부모 페이지로 올라간 후 name값을 입력해야 해당 iframe에서 경로가 열림 -->
```