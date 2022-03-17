# CSS

## 기본 구성

```css
/* 
	여러 선택자에 동일한 속성을 적용하고 싶을 때에는 콤마로,
	하나의 속성에 여러 값을 줄 때는 공백으로 구
*/
element, element {속성: 값; 속성: 값 값; 속성: 값 값 값; ...}
```

## 적용 방법

### 인라인Inline

- CSS가 짧게 들어갈 때 주로 사용

```html
<element style="속성: 값; 속성: 값; 속성: 값;"></element>
<!-- HTML 파일 내부에서 element의 속성으로 style을 사용 -->
```

### 내부 스타일 시트Internal

- CSS 길이가 길 때 주로 사용

```html
<style type="text/css">
	selector {속성: 값; 속성: 값; 속성: 값; ...}
</style>
<!-- HTML 파일 head 태그 안(관례)에서 style 태그를 만들어 적용 -->
```

### 외부 스타일 시트External

- 여러 웹페이지에서 동일한 형식의 CSS를 적용해야 할 때 주로 사용

```html
<!-- HTML -->
<link rel="stylesheet" href="CSS 경로">
```

```css
/* CSS */
selector {속성: 값; 속성: 값; 속성: 값; ...}
```

## 선택자Selector

```css
* {} /* html 내의 모든 요소에 적용 */

element {} /* 해당하는 요소에 적용 */
.class {} /* 해당 클래스에 적용 */
#id {} /* 해당 아이디에 적용 */

element.class {} /* 해당하는 요소 중에서 클래스값이 같은 것에만 적용 */
element .class {} /* 해당하는 요소의 자식 중에서 클래스 값이 같은 것에만 적용 */

element1 element2 {} /* 요소 1의 자식 중에서 요소 2인 것에만 적용 */
element1 > element2 {} /* 요소 1을 직접적인 부모로 두고 있는 요소 2에만 적용 */

[attripute] {} /* target 속성을 가진 요소에만 적용 */
[attripute=value] {} /* 속성값이 value인 요소에만 적용 */
[attripute~=value] {} /* 속성값에 value가 포함된(여러 속성값 중 하나) 요소에만 적용 */
[attribute|=value] {} /* 속성값이 value거나 value로 시작하는 요소에만 적용 */
[attribute^=value] {} /* 속성값이 value로 시작하는 요소에만 적용 */
[attribute$=value] {} /* 속성값이 value로 끝나는 요소에만 적용 */
[attribute*=value] {} /* 속성값이 value가 포함된(문자열에 포함) 요소에만 적용 */

element:first-child {} /* 해당하는 요소들 중 첫번째 요소에만 적용 */
element:last-child {} /* 해당하는 요소들 중 마지막 요소에만 적용 */
element:nth-child(n) {} /* 해당하는 요소들 중 n번째 요소에만 적용 */

a:link {} /* 방문하지 않은 a 태그에 적용 */
a:visit {} /* 방문한 a 태그에 적용 */
a:hover {} /* 마우스를 올린 a 태그에 적용 */
a:active {} /* 현재 클릭하고 있는 a 태그에 적용 */
```

## 속성의 종류

### font

```css
{font: font-style; font-weight; font-size; line-height; font-family;} /* 아래의 모든 속성 사용 가능 */

{font-family: 글꼴이름 | 기본 글꼴 이름;}
/*
	브라우저에서 사용할 font 종류 결정
	글꼴을 두 개 이상 사용할 때는 쉼표로 구분
	글꼴 이름이 두 단어 이상이면 큰 따옴표로 묶음
*/

{font-size: 절대값 | 상대값 | 길이 | 퍼센트;}
/*
	길이의 경우 em, ex, px, pt 등의 단위 사용
	절대값 범위: xx-small ~ xx-large
	상대값 종류: smaller | larger 사용
*/

{font-weight: 절대값 | 상대값;}
/*
	절대값 범위: 100 ~ 900
	상대값 종류: lighter, normal, bold, bolder
*/

{font-style: normal | italic | oblique;} /* 폰트 기울임 */

{color: 색상;} /* 폰트 색상 */
```

### text

```css
{text-indent: 길이 | 퍼센트;} /* 문단 들여쓰기 */

{text-align: left | right | center | justify(양쪽 정렬);} /* 텍스트 수평 정렬 */

{vertical-align: 위치 | 길이 | 퍼센트 | 글로벌값;}
/*
	텍스트 수직 정렬
	위치 종류: baseline(디폴트), sub, super, top, text-top, middle, bottom, text-bottom
	글로벌값 종류: inherit, initial, unset 
*/

{text-decoration: none | [underline(밑줄) overline(윗줄) line-throgh(가운데줄);]} /* 텍스트에 선 추가 */ 

{text-transform: none | capitalize | uppercase | lowercase;} /* 영문 대소문자 변경 */

{letter-spacing: normal | 길이} /* 글자 사이 간격 조절 */

{word-spacing: normal | 길이} /* 단어 사이 간격 조절 */

{line-height: normal | 길이} /* 줄 사이 간격 조절 */
```

### list

```css
{list-style: list-style-type; list-style-position; list-style-image;}

{list-style-type: 모양;}
/*
	list 마커 모양을 바꿈
	list-style-image와 동시에 사용하면 이미지 로딩이 불가능할 때 적용됨
	모양 종류: dist, circle, square, decimal, lower-roman, upper-roman, lower-alpha, upper-alpha, none
*/

{list-style-position: inside | outside(기본값);}
/*
	list 위치를 바꿈
	inside는 outside보다 들여쓰기가 더 들어감
*/

{list-style-image: none(기본값) | url(경로);}
/*
	list 마커 모양을 이미지로 바꿈
	list-style-type과 동시에 사용하면 이미지 로딩이 불가능할 때 적용됨
*/
```

### background

```css
{background: background-color; background-image; background-repeat; background-attachment; background-position;}
/* 배경 속성을 한 번에 줄 때 사용 */

{background-color: 색상;}
/* 배경 색상을 설정할 때 사용 */

{background-image: none(기본값) | url(경로);}
/* 배경 이미지를 설정할 때 사용 */

{background-repeat: no-repeat | repeat | repeat-x | repeat-y;}
/*
	배경 이미지를 설정할 때 이미지 연속 출력 여부 설정
	no-repeat: 연속X
	repeat: 가로 세로 연속
	repeat-x: 가로로 연속
	repeat-y: 세로로 연속
*/

{background-attachment: fixed(고정) | scroll(스크롤 시 이동) | local(컨텐츠와 함께 이동);}
/* 배경 이미지를 설정할 때 이미지 고정 여부 설정 */

{background-position: 길이 | 퍼센트 | 위치;}
/*
	배경 이미지를 설정할 때 시작점 설정
	위치값: top, bottom, left, right, center
*/
```

### box 크기 조정

```css
{margin: 길이 | 퍼센트 (n | n, n | n, n, n | n, n, n, n) | auto;}
/*
	box 마진값 지정
	margin-top, margin-right, margin-bottom, margin-left를 따로 설정 가능
	길이/퍼센트 설정 규칙: n = 상하좌우; n, n = 상하, 좌우; n, n, n = 상, 좌우, 하; n, n, n, n = 상, 우, 하, 좌
*/

{padding: 길이 | 퍼센트 (n | n, n | n, n, n | n, n, n, n) | auto;}
/*
	box 패딩값 지정
	padding-top, padding-right, padding-bottom, padding-left를 따로 설정 가능
	길이/퍼센트 설정 규칙: n = 상하좌우; n, n = 상하, 좌우; n, n, n = 상, 좌우, 하; n, n, n, n = 상, 우, 하, 좌
*/
```

```css
{border: border-width; border-style; border-color;} /* 보더 속성 한 번에 지정 */

{border-width: 길이(n | n, n | n, n, n | n, n, n, n) | thin | medium | thick;}
/*
	box 테두리 굵기 지정
	border-top-width, border-right-width, border-bottom-width, border-left-width를 따로 설정 가능
	길이 설정 규칙: n = 상하좌우; n, n = 상하, 좌우; n, n, n = 상, 좌우, 하; n, n, n, n = 상, 우, 하, 좌
*/

{border-color: 색상(c | c, c | c, c, c | c, c, c, c);}
/*
	box 테두리 색상 지정
	border-top-color, border-right-color, border-bottom-color, border-left-color를 따로 설정 가능
	색상 설정 규칙: c = 상하좌우; c, c = 상하, 좌우; c, c, c = 상, 좌우, 하; c, c, c, c = 상, 우, 하, 좌
*/

{border-radius: 길이 | 퍼센트 (n | n, n | n, n, n | n, n, n, n) | auto;}
/*
	box 테두리 둥글림 지정
	border-top-radius, border-right-radius, border-bottom-radius, border-left-radius를 따로 설정 가능
	길이/퍼센트 설정 규칙: n = 상하좌우; n, n = 오른위/왼아래, 왼위/오른아래; n, n, n = 오른위, 왼위/오른아래, 왼아래; n, n, n, n = 오른위, 오른아래, 왼아래, 왼위
*/

{border-style: none | datted | dashed | solid | double | groove | ridge | inset | outset;}
/*
	box 테두리 모양 지정
	border-top-style, border-right-style, border-bottom-style, border-left-style를 따로 설정 가능
	모양 설정 규칙: s = 상하좌우; s, s = 상하, 좌우; s, s, s = 상, 좌우, 하; s, s, s, s = 상, 우, 하, 좌
*/
```

```css
{box-sizing: content-box(기본값) | border-box;}
/*
	box의 패딩값과 테두리 굵기에 상관없이 박스를 정해진 크기 내로 고정시킬 때 사용
	border-box: 설정된 width, height 길이 안에서 패딩값과 테두리 굵기를 적용시킨 뒤 비율에 맞춰 축소
*/
```

### box 위치 조정

```css
{display: 키워드;}
/*
	박스 배치 방식을 정할 때 사용
	none: 렌더링X(공간 차지X), 비가시화
	inline: 요소의 크기만큼 공간을 차지함(width, height 설정X), 한 줄에 여러 박스 배치 가능, 상하 margin 적용X
	block: 설정한 width, height만큼 공간을 차지함, 한 줄에 한 박스만 배치 가능
	inline-block: 설정한 width, height만큼 공간을 차지함, 한 줄에 여러 박스 배치 가능
*/
```

```css
{position: 키워드;}
/*
	박스 위치 방식을 정할 때 사용
	static을 제외하고는 top, left, bottom, right, z-index(요소가 겹칠 경우 우선 순위 설정) 속성으로 위치를 지정함

	static: 기본값, html에서 생성된 순서대로 위치시킴
	relative: 생성된 위치의 상대 위치에 배치, 다른 요소는 해당 요소의 생성된 위치를 비워둠
	absolute: 페이지의 절대 위치에 배치
	sticky: 화면의 절대 위치에 고정(스크롤 이동해도 위치를 벗어나지 않고 따라붙음)
*/
```

```css
{float: none | left | right;}
/*
	요소들의 어울림 배치 지정
	none: 어울리지 않음
	left: 생성된 순서에 따라 왼쪽으로 어울림
	right: 생성된 순서에 따라 오른쪽으로 어울림
*/

{clear: none | left | right | both;}
/*
	어울림 배치 지우기
	none: 아무 것도 지우지 않음
	left: 왼쪽 어울림 지우기
	right: 오른쪽 어울림 지우기
	both: 양쪽 어울림 지우기
*/
```

```css
{overflow: visible | hidden | scroll | auto;}
/*
	박스 안의 요소가 박스 범위를 넘어섰을 때 처리 방법 설정
	visible: 기본값, 박스의 범위를 넘기며 출력
	hidden: 박스 범위를 넘기면 표시X
	scroll: 수직, 수평 스크롤바를 생성함
	auto: 필요한 부분만 스크롤바를 생성함
*/
```

```css
{visibility: visible | hidden;}
/*
	가시화 설정
	visible: 기본값, 가시화
	hidden: 비가시화, but 공간은 차지함
*/
```

## 반응형 웹

### 내부 스타일 시트Internal

```html
<style type="text/css" media="screen and (min-width: 길이) and (max-width: 길이)">
	selector {속성: 값; 속성: 값; 속성: 값; ...}
</style>
<!-- style 태그 전체에 특정 값을 줘 해당 값을 만족할 때 스타일을 적용시킴 -->
```

```html
<style type="text/css">
	@import url(css 파일 경로) screen and (min-width: 길이) and (max-width: 길이);
</style>
<!-- 태그 안에서 @import를 사용해 값을 만족할 때 해당 CSS파일을 적용시킴 -->
```

### 외부 스타일 시트External

- 여러 웹페이지에서 동일한 형식의 CSS를 적용해야 할 때 주로 사용

```html
<!-- HTML -->
<link rel="stylesheet" href="CSS 경로">
```

```css
/* CSS */
@import screen and (min-width: 길이) and (max-width: 길이);
selector {속성: 값; 속성: 값; 속성: 값; ...}

/* CSS 파일 내부에 직접 media 속성을 줘 값을 만족할 때 스타일을 적용시킴 */
```