import sys
from collections import deque

my, target = map(int, sys.stdin.readline().split())

if my == target:
    print(0)
elif my > target:
    # 내가 더 앞에 있으면 x-1이동밖에 안되므로 그냥 뺌
    print(my-target)
else:
    arr = [999999 for _ in range(100001)]
    tmp = deque([my])
    max_time = 100001
    arr[my] = 0
    # x-1, x+1, 2*x의 가능한 길과 초를 전부 구함
    while len(tmp) != 0:
        check = tmp.popleft()
        # x-1
        if check-1 >= 0 and max_time > arr[check]+1 and arr[check-1] > arr[check]+1:
            tmp.append(check-1)
            arr[check-1] = arr[check]+1
            # 정답일 경우
            if check-1 == target:
                max_time = arr[check-1]
        
        # x+1
        if check+1 <= 100000 and max_time > arr[check]+1 and arr[check+1] > arr[check]+1:
            tmp.append(check+1)
            arr[check+1] = arr[check]+1
            # 정답일 경우
            if check+1 == target:
                max_time = arr[check+1]
        # 2*x
        if check*2 <= 100000 and max_time > arr[check]+1 and arr[check*2] > arr[check]+1:
            tmp.append(2*check)
            arr[2*check] = arr[check]+1
            # 정답일 경우
            if 2*check == target:
                max_time = arr[2*check]

    print(max_time)
