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