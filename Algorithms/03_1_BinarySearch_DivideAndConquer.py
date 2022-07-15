# 분할 정복을 이용한 이진 탐색

# n개의 원소로 이루어진 오름차순 정렬 S에서 x의 위치 검색
# 만일 x가 없을 경우 0 출력

def location(S, low, high):
    if low > high:
        return 0
    else:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return location(S, low, mid - 1)
        else:
            return location(S, mid + 1, high)

S = [1, 10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]
x = 18
print(location(S, 0, len(S)))