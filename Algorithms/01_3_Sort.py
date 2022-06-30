# n개의 수로 구성된 리스트 S를 올림차 순으로 정렬

# 교환 정렬
# : 정렬할 원소와 그 다음 원소들을 비교해 작은 원소와 교환하며 선행 원소부터 차례대로 정렬하는 방법
def exchange(S):
    n = len(S)
    for i in range(n - 1): # 첫 번째 원소부터 마지막에서 두 번째 원소까지 반복
        for j in range(i + 1, n): # i번째 원소 이후부터 마지막 원소까지 반복
            if(S[i] > S[j]): # 만일 i번째 원소가 j번째 원소보다 크다면
                S[i], S[j] = S[j], S[i] # i번째 원소와 j번째 원소를 바꾼다
    return S

# 선택 정렬
# : 아직 정렬되지 않은 원소들 중 가장 작은 원소를 선택해 앞으로 내보내며 정렬하는 방법
def selection(S):
    n = len(S)
    for i in range(n - 1): # 첫 번째 원소부터 마지막에서 두 번째 원소까지 반복
        min = i # min을 i로 초기화
        for j in range(i + 1, n): # i번째 원소 이후부터 마지막 원소까지 반복
            if(S[min] > S[j]): # 만일 현재 반복에서 가장 작은 원소가 j번째 원소보다 크다면
                min = j # min에 j를 저장
        S[i], S[min] = S[min], S[i] # 두번째 for문이 종료된 후 i번째 원소와 가장 작은 원소를 바꾼다
    return S

# 삽입 정렬
# : 아직 정렬되지 않은 원소를 이미 정렬된 원소들과 비교해 알맞은 자리에 삽입하며 정렬하는 방법
def insertion(S):
    n = len(S)
    for i in range(n): # 배열의 크기만큼 반복
        for j in range(i, 0, -1): # i에서 0까지 반복
            if S[j - 1] > S[j]: # 만일 j번째 원소보다 j - 1번째 원소가 크다면
                S[j - 1], S[j] = S[j], S[j - 1] # j번째 원소와 j - 1번째 원소를 바꾼다
    return S

# 버블 정렬
# : 아직 정렬되지 않은 원소들 중에서 가장 큰 숫자를 뒤로 밀어내며 정렬하는 방법
def bubble(S):
    n = len(S)
    for i in range(n): # 배열의 크기만큼 반복
        for j in range(n - i - 1): # 아직 정렬되지 않은 원소의 갯수 - 1만큼 반복
            if S[j] > S[j + 1]:  # 만일 j번째 원소보다 j + 1번째 원소가 크다면
                S[j], S[j + 1] = S[j + 1], S[j] # j번째 원소와 j + 1번째 원소를 바꾼다
    return S

S = [14, 10, 2, 11, 5, 13, 8]
print(exchange(S))
print(selection(S))
print(insertion(S))
print(bubble(S))