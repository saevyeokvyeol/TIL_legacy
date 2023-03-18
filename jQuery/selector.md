# 선택자Selectors

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

"요소", this // this를 기준으로 요소를 찾음
```