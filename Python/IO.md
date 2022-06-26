# input

## input()

- 문자열을 입력받을 때 쓰는 함수

```python
text = input()
```

## sys.stdin.readline()

- 문자열을 입력받을 때 쓰는 함수
- input()보다 빠르게 입력받을 수 있어 알고리즘을 풀 때는 이걸 사용하는 게 더 좋다

```python
text = sys.stdin.readline()
```

# output

## print()

- 문자열을 출력할 때 쓰는 함수

```python
print() # 인수를 출력함

print(*자료구조) # 인수로 입력한 자료구조의 요소를 공백으로 구분해 순서대로 출력함
```