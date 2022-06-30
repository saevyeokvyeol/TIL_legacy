"""
순차 탐색
: 리스트(or 배열)을 처음부터 끝까지 차례대로 탐색하는 것
"""

# 어떤 수 x가 n개의 수로 구성된 리스트 S에 존재하면 해당하는 순번을, 없으면 0을 출력

# 강의 예제
def sequentialSearch(n, S, x):
    location = 1
    while location <= n and S[location] != x:
        location += 1
    if location > n:
        location = 0
    return location

# for문을 이용한 응용
def sequentialSearchFor(n, S, x):
    result = 0
    for i in range(n):
        if S[i] == x:
            result = i
            break
    return result

# for문을 이용한 응용2: 파라미터 n을 사용하지 않고 리스트의 index() 함수 사용
def sequentialSearchFor2(n, S, x):
    result = 0
    for i in S:
        if i == x:
            result = S.index(i)
            break
    return result

S = [0, 10, 7, 11, 5, 13, 8]
x = 5
print(sequentialSearch(len(S) - 1, S, x))
print(sequentialSearchFor(len(S) - 1, S, x))
print(sequentialSearchFor2(len(S) - 1, S, x))