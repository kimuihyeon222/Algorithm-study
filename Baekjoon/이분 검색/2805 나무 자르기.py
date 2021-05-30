import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(data) 
high = 0

# 값 찾는게 아니니까 sort 안해도됨

while left <= right:
    mid = (left + right) // 2
    tmp = 0
    # 검사
    for i in data:
        if i > mid:
            tmp += i - mid
            if tmp >= m: # 지정한 값을 넘었을때 더이상 루프를 진행 안시켜도됨 -> 
                break
    if tmp >= m:
        if high < mid:
            high = mid
        left = mid+1
    else:
        right = mid-1
print(high)
