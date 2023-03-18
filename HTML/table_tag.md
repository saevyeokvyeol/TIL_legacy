# table

```html
<table> <!-- 테이블 생성 -->

	<caption>title</caption> <!-- 테이블 이름 생성 -->

	<tr> <!-- 행 생성 -->
		<th></th> <!-- 헤더열 생성: 디폴트값이 중앙 정렬/굵은 글씨 -->
		<td></td> <!-- 열 생성 -->
	</tr>

	

	<thead> <!-- 테이블의 헤더 영역 선언: 어디에 선언되도 테이블의 맨 위로 올라감 -->
	</thead>

	<tbody> <!-- 테이블의 바디 영역 선언 -->
	</tbody>

	<tfoot> <!-- 테이블의 푸터 영역 선언: 어디에 선언되도 테이블의 맨 아래로 내려감 -->
	</tfoot>

</table>
```

```html
<th colspan="n"> <!-- n열 병합 -->
<th rowspan="n"> <!-- n행 병합 -->
```