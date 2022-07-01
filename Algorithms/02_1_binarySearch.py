"""
이분 탐색
: 정렬된 리스트(or 배열)의 중앙에 위치한 원소와 찾을 원소를 비교해 전체 리스트를 반으로 나누며 탐색하는 방식
  크기가 n인 리스트에서 logn + 1번의 비교를 수행
"""

# n개의 원소로 이루어진 오름차순 정렬 S에서 x의 위치 검색
# 만일 x가 없을 경우 -1 출력

def binarySearch(n, S, x):
    low = 0
    high = n
    location = -1
    while low <= high and location == -1:
        mid = (low + high) // 2
        print(low, high, mid)
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return location

S = [1, 5, 7, 8, 10, 11, 13, 16]
x = 8
print(binarySearch(len(S) - 1, S, x))