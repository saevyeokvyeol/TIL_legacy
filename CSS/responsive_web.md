# 반응형 웹

## 내부 스타일 시트Internal

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

## 외부 스타일 시트External

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