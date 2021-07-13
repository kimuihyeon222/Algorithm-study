import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())

arr = [ list(map(int,sys.stdin.readline().split())) for _ in range(n) ]

zero = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero = 1
            break

# 이미 모든 토마토가 익었을 경우
if zero == 0:
    print(0)
# 검사할 토마토가 있을 경우
else:
    tomato = deque([])
    day = -1
    # 검사가능한 토마토를 찾음
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                # 처음은 day가 0 이니 0도 같이 저장
                tomato.append([i, j, 0])
    
    x = [0, 0, -1, 1]
    y = [-1, 1, 0, 0]

    # 검사 시작
    while len(tomato) != 0:
        tmp = tomato.popleft()
        if day < tmp[2]:
            day = tmp[2]

        # 4방향 검사
        for i in range(4):
            if 0 <= tmp[0]+x[i] < n and 0 <= tmp[1]+y[i] < m:
                
                if arr[tmp[0]+x[i]][tmp[1]+y[i]] == 0:
                    arr[tmp[0]+x[i]][tmp[1]+y[i]] = 1
                    tomato.append([ tmp[0]+x[i], tmp[1]+y[i], tmp[2]+1])
    
    zero = 0
    # 안익은 토마토가있는지 검사
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                zero = 1
                break

    if zero == 1:
        print(-1)
    else:
        print(day)
