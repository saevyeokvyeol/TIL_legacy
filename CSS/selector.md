# 선택자Selector

```css
* {} /* html 내의 모든 요소에 적용 */

element {} /* 해당하는 요소에 적용 */
.class {} /* 해당 클래스에 적용 */
#id {} /* 해당 아이디에 적용 */

element.class {} /* 해당하는 요소 중에서 클래스값이 같은 것에만 적용 */
element .class {} /* 해당하는 요소의 자식 중에서 클래스 값이 같은 것에만 적용 */

element1 element2 {} /* 요소 1의 자식 중에서 요소 2인 것에만 적용 */
element1 > element2 {} /* 요소 1을 직접적인 부모로 두고 있는 요소 2에만 적용 */

[attripute] {} /* 특정 속성을 가진 요소에만 적용 */
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