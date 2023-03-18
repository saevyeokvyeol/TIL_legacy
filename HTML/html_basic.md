# HTML

## 개념 및 특징

- Hyper Text Markup Language
- 화면 구성=구조=GUI를 담당: 주로 사용자 입력값을 받는 폼이나 사용자가 요청한 결과를 화면에 출력
- 현재는 HTML5 사용
: 다양한 API 제공(WabStorage, Drag&Drop, Audio, Video, WebSocket) → API이기 때문에 HTML, CSS, JS를 모두 알아야 함
- 대소문자를 구분하지 않고 오타가 있어도 오류가 발생하지 않음(적용되지 않은 채로 실행)

## HTML 기본 구조

```html
<!DOCTYPE html> <!-- 문서의 첫 줄에 작성해 문서의 형태를 나타냄 -->
<html>
	<head>
		<!-- 브라우저에서 보이지 않는 문서의 정보 등을 작성 -->
		<meta charset="EUC-KR">
		<title>Title</title> <!-- 탭에 나타나는 페이지 제목을 작성 -->
	</head>
	<body>
		<!-- 실제로 웹 브라우저에 나타나는 부분을 작성 -->
		<태그이름 속성="값" 속성="값"...>
			content
		</태그이름>
	</body>
</html>
```