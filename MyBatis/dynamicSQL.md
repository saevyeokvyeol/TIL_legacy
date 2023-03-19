# 예제 코드: 동적 SQL

## where

```xml
<!--
	where
	: select, insert, update, delete 태그 안에 사용함
	  where 태그 안에 문장이 있을 경우 태그 안 문장 맨 앞에 where를 추가해주고
		태그 안 문장이 and나 or로 시작한다면 and나 or를 제거함
-->
<where>
	실행문
</where>
```

## trim

```xml
<!--
	trim
	: where의 상위 버전 태그
	  trim 태그 안에 문장이 있을 경우 설정한 값에 따라 태그 안 문장 앞뒤에 문자를 삽입하거나 지워줌
		
		prefix - 태그 안에 문장이 있으면 가장 앞에 해당 문자를 붙여줌
		prefixOverrides - 태그 안 문장 중 가장 앞에 해당 문자가 있으면 자동 삭제
		suffix - 태그 안에 문장이 있으면 가장 뒤에 해당 문자 붙여줌
		suffixOverrides - 태그 안 문장 중 가장 뒤에 해당 문자가 있으면 자동 삭제

		~Overrides 속성의 경우 |(or)로 삭제할 문자 조건을 여러 개 지정하는 것도 가능
-->
<trim prefix="가장 앞에 추가할 문자" prefixOverrides="가장 앞에서 삭제할 문자"
	suffix="가장 뒤에 추가할 문자" suffixOverrides="가장 뒤에서 삭제할 문자">
	실행문
</trim>
```

## set

```xml
<!--
	set
	: update 태그 안에 사용함
	  set 태그 안에 문장이 있을 경우 태그 안 문장 맨 앞에 set를 추가해주고
	  태그 안 문장 앞이나 뒤에 붙은 필요없는 ,(콤마)를 제거함
-->
<set>
	실행문
</set>
```

## if

```xml
<!--
	if
	: select, insert, update, delete 태그 안에 사용하며 조건에 부합할 경우 태그 안에 입력한 문장을 출력함
	  조건문 안에서 파라미터를 사용할 경우 #{}, ${}로 감싸지 않음
-->

<if test="조건문">
	실행문
</if>
```

## choose

```xml
<!--
	choose
	: if의 상위 버전 태그
	  java의 if, else-if, else와 비슷함
		여러 조건 중 처음으로 부합하는 태그 안에 입력한 문장만 출력함
	  조건문 안에서 파라미터를 사용할 경우 #{}, ${}로 감싸지 않음
-->
<choose>
	<when test="조건문1">
		실행문1
	</when>
	<when test="조건문2">
		실행문2
	</when>
	<otherwise>
		실행문3
	</otherwise>
</choose>
```

## foreach

```xml
<!--
	foreach
	: select, insert, update, delete 태그 안에 사용함
	  인수로 받은 자료구조에서 요소를 하나씩 꺼내 문장 안에서 출력함
		separator, open, close 속성을 이용해 반복문 중간이나 가장 앞, 뒤에 추가할 문자를 지정할 수 있음
-->
<foreach collection="변수명(인수로 받은 자료구조)" item="item(자료구조에서 꺼낸 개별 요소)"
	separator="각 반복문 중간에 추가할 문자" open="반복문 가장 앞에 추가할 문자" close="반복문 가장 뒤에 추가할 문자">
	#{item}
</foreach>
```