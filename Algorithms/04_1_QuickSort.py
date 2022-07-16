"""
퀵 정렬
: pivotpoint를 기준으로 파티션을 분할해 정렬하는 방법
  정렬 해야 하는 대상이 정렬 되어 있을수록 파티션의 크기가 커져 비효율적인 정렬 방법
"""

# 퀵 정렬 풀이 1

def quickSort(S, low, high):
    if low < high: # low가 high보다 작을 경우
        pivotpoint = partition(S, low, high) # partition 함수를 사용해 pivotpoint 초기화
        quickSort(S, low, pivotpoint - 1) # low부터 pivotpoint까지 재정렬
        quickSort(S, pivotpoint + 1, high) # pivotpoint부터 high까지 재정렬

def partition(S, low, high):
    pivotitem = S[low] # 리스트 S의 low번째 원소(=현재 정렬해야 하는 원소 중 첫 번째 원소) 저장
    j = low # j에 low 저장
    for i in range(low + 1, high + 1): # low + 1번째 원소부터 마지막 원소까지 반복
        if S[i] < pivotitem: # i번째 원소가 low번째 원소보다 작다면
            j += 1 # j++
            S[i], S[j] = S[j], S[i] # i번째 원소와 j번째 원소의 자리를 바꿈
    pivotpoint = j # pivotpoint에 j를 저장
    S[low], S[pivotpoint] = S[pivotpoint], S[low] # pivotpoint와 low의 자리를 바꿈
    return pivotpoint # pivotpoint 리턴

S = [16, 10, 12, 20, 25, 13, 15, 22]
quickSort(S, 0, len(S) - 1)
print(S)

# 퀵 정렬 풀이 2: 보편적으로 사용하는 방법

def quickSort2(S, low, high):
    if low < high: # low가 high보다 작을 경우
        pivotpoint = partition(S, low, high) # partition 함수를 사용해 pivotpoint 초기화
        quickSort(S, low, pivotpoint - 1) # low부터 pivotpoint까지 재정렬
        quickSort(S, pivotpoint + 1, high) # pivotpoint부터 high까지 재정렬

def partition2(S, low, high):
    pivotitem = S[low] # 리스트 S의 low번째 원소(=현재 정렬해야 하는 원소 중 첫 번째 원소) 저장
    i = low + 1 # i에 low + 1 저장
    j = high # j에 high 저장
    while i <= j: # i가 j보다 작거나 같은 동안 반복(=i가 j를 역전할 때까지 반복)
        while S[i] < pivotitem:
            i += 1 # pivotitem보다 큰 원소를 찾을 때까지 반복(=큰 원소의 번지를 저장)
        while S[j] > pivotitem:
            j -= 1 # pivotitem보다 작은 원소를 찾을 때까지 반복(=작은 원소의 번지를 저장)
        if i < j: # 만일 i가 j보다 작으면
            S[i], S[j] = S[j], S[i] # i와 j의 자리를 바꿈
    pivotpoint = j # pivotpoint에 j를 저장
    S[low], S[pivotpoint] = S[pivotpoint], S[low] # pivotpoint와 low의 자리를 바꿈
    return pivotpoint # pivotpoint 리턴

S = [16, 10, 12, 20, 25, 13, 15, 22]
quickSort2(S, 0, len(S) - 1)
print(S)