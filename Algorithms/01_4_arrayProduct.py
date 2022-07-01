# 행렬의 곱셈
# n * n 행렬의 곱 구하기
# C = A * B일 때, C[i][j] = A[i][1] * B[1][j] + A[i][2] * B[2][j]

def matrixMultiple(n, A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

print(matrixMultiple(2, [[2, 3], [4, 1]], [[5, 7], [6, 8]]))