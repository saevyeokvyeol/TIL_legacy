# 분할 정복을 이용한 합병 정렬

# 풀이 1
def mergesort(S):
    n = len(S)
    if n <= 1: # n이 1보다 작거나 같으면 = n의 원소가 하나 이하면
        return S # S를 그대로 리턴

    else:
        mid = n // 2
        U = mergesort(S[0:mid]) # S의 0번째 원소부터 맨 중간 원소만큼 재귀 함수를 호출해 입력 입력
        V = mergesort(S[mid:n]) # S의 맨 중간 원소부터 마지막 원소만큼 재귀 함수를 호출해 입력
        return merge(U, V) # 위의 정렬 결과를 merge 함수에 입력해 그 리턴값을 리턴

def merge(U, V):
    S = []
    i = j = 0 # i와 j 초기화

    while i < len(U) and j < len(V): # i와 j가 각각 리스트 U와 V의 크기보다 작은 동안 반복
        if U[i] < V[j]: # U의 i번째 원소보다 V의 j번째 원소가 크다면
            S.append(U[i]) # U의 i번째 원소를 리스트 S에 입력
            i += 1
        else: # 아니라면(=U의 i번째 원소보다 V의 j번째 원소가 작거나 같다면)
            S.append(V[j]) # V의 j번째 원소를 리스트 S에 입력
            j += 1

    if i < len(U): # 만약 i가 리스트 U보다 작다면(and로 연결된 while문을 빠져나왔으므로 이 경우 j는 리스트 V보다 크거나 같음)
        S += U[i:len(U)] # 리스트 S에 U의 i번째 원소부터 마지막 원소까지 추가
    else: # 아니라면(=i가 리스트 U보다 크거나 같다면)
        S += V[j:len(V)] # 리스트 S에 V의 j번째 원소부터 마지막 원소까지 추가(만일 j가 V보다 크거나 같다면 아무 것도 추가되지 않음)

    return S # 리스트 S 리턴

# S = [27, 10, 12, 20, 25, 13, 15, 22]
# print(mergesort(S))



"""
풀이 1의 문제점
: 입력 리스트 S 이외에 U와 V를 추가적으로 사용하기 때문에 메모리 사용이 비효율적이다.
  mergesort()를 호출할 때마다 U와 V를 새로 생성하기 때문에 S의 길이의 2배 정도의 리스트를 생성해야 한다.
"""

# 풀이 2: U와 V를 사용하지 않아 메모리 사용을 개선하는 함수
# 리스트 S를 mid를 기준으로 나눠 두 개의 리스트가 있는 것처럼 사용함

def enhancedMergesort(S, low, high):
    if low < high: # low가 high보다 작다면
        mid = (low + high) // 2
        enhancedMergesort(S, low, mid) # low부터 mid까지 재귀 함수에 입력해 다시 정렬
        enhancedMergesort(S, mid + 1, high) # mid부터 high까지 재귀 함수에 입력해 다시 정렬
        enhancedMerge(S, low, mid, high) # 위에서 정렬한 것을 합쳐 다시 정렬

def enhancedMerge(S, low, mid, high):
    U = []
    i = low
    j = mid + 1

    while i <= mid and j <= high: # i와 j가 각각 mid와 high보다 작거나 같은 동안 반복
        if S[i] < S[j]: # 리스트 S의 i번째 함수보다 j번째 함수가 크다면
            U.append(S[i]) # S의 i번째 원소를 리스트 U에 입력
            i += 1
        else: # 아니라면(=S의 i번째 원소보다 S의 j번째 원소가 작거나 같다면)
            U.append(S[j]) # S의 j번째 원소를 리스트 U에 입력
            j += 1

    if i <= mid: # 만약 i가 mid보다 작다면(and로 연결된 while문을 빠져나왔으므로 이 경우 j는 high보다 크거나 같음)
        U += S[i:mid + 1] # 리스트 U에 S의 i번째 원소부터 mid번째 원소까지 추가
    else: # 아니라면(=i가 리스트 U보다 크거나 같다면)
        U += S[j:high + 1] # 리스트 U에 S의 j번째 원소부터 high번째 원소까지 추가(만일 j가 V보다 크거나 같다면 아무 것도 추가되지 않음)

    for k in range(low, high + 1): # low부터 high까지 반복
        S[k] = U[k - low] # 리스트 S의 원소를 정렬한 U의 원소로 덮어씀

S = [27, 10, 12, 20, 25, 13, 15, 22]
enhancedMergesort(S, 0, len(S) - 1)
print(S)