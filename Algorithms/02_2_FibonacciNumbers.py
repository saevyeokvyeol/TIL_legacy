# 피보나치 수열의 n번째 값 구하기

# 재귀적 호출
def recursionFibonacci(n):
    num = 0
    if 0 < n < 3:
        num = 1
    elif n > 2:
        num = recursionFibonacci(n - 1) + recursionFibonacci(n - 2)
    return num

# for문을 사용한 방법
def forFibonacci(n):
    f = [0] * (n + 1)
    if n > 0:
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
    return f[n]

# for문을 사용한 방법: list 없이 구하는 방법
def seqFibonacci(n):
    f0, f1 = 0, 1
    result = f0 + f1
    if n == 0:
        result = f0
    elif n == 1:
        result = f1
    else:
        for _ in range(3, n + 1):
            f0, f1, result = f1, result, f1 + result
    return result

n = 4
print(recursionFibonacci(n))
print(forFibonacci(n))
print(seqFibonacci(n))