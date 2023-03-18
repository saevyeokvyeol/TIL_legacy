# CSS

## 개념 및 특징

- Cascading Style Sheets
- HTML에 디자인(화면 레이아웃)을 추가함
- 과거에는 플래시와 포토샵을 이용해 화면 구성을 시각적으로 풍부하게 만들었지만 현재는 CSS로 대부분 가능함
- 현재는 CSS3 사용
: 대소문자를 가림
  오타가 있어도 오류가 발생하지 않음(적용되지 않은 채로 실행)

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