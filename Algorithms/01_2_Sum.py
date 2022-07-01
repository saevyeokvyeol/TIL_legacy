# n개의 원소를 가진 리스트 S의 원소의 합 구하기

# 강의 예제
def sequentialSum(n, S):
    sum = 0
    for i in range(n + 1):
        sum += S[i]
    return sum

# for문을 이용한 응용
def sequentialSumFor(n, S):
    sum = 0
    for i in S:
        sum += i
    return sum

S = [1, 10, 7, 11, 5, 13, 8]
print(sequentialSum(len(S) - 1, S))
print(sequentialSumFor(len(S) - 1, S))