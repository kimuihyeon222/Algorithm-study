import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n*h) ]

zero = -1

# 안익은 토마토가 있는지 검사
for i in range(n*h):
    if 0 in arr[i]:
        zero = 1
        break

# 있다면 0리턴
if zero == -1:
    print(0)
# 없다면 최소 몇일이 걸리는지 검사
else:
    result = -1
    day = deque([])
    # 익은 토마토의 위치를 저장
    for i in range(n*h):
        for j in range(m):
            if arr[i][j] == 1:
                # 저장 방식은
                # 현재 위치, 몇층인지, 첫날 이므로 0 을 저장
                day.append([i, j, i//n, 0])
    
    x_spot = [-1, 1, 0, 0]
    y_spot = [0, 0, -1, 1]

    while len(day) != 0:
        data = day.popleft()
        if result < data[3]:
            result = data[3]
        # 첫날의 위치에서 하루가 지났을 경우 익을수 있는 토마토들 선택
        # 4방향 먼저 검사 ( 동 서 남 북)
        for go in range(4):
            if data[2]*n <= data[0]+x_spot[go] < n*(data[2]+1) and 0 <= data[1]+y_spot[go] < m:
                if arr[data[0]+x_spot[go]][data[1]+y_spot[go]] == 0:
                    arr[data[0]+x_spot[go]][data[1]+y_spot[go]] = 1
                    day.append([data[0]+x_spot[go], data[1]+y_spot[go], data[2], data[3]+1])
        
        # 한층 아래 검사
        if 0<=data[2]-1:
            if arr[data[0]-n][data[1]] == 0:
                arr[data[0]-n][data[1]] = 1
                day.append([data[0]-n, data[1], data[2]-1, data[3]+1])

        # 한층 위 검사
        if data[2]+1 < h:
            if arr[data[0]+n][data[1]] == 0:
                arr[data[0]+n][data[1]] = 1
                day.append([data[0]+n, data[1], data[2]+1, data[3]+1])
    
    # 최종 저장된 토마토 검사
    error = -1
    for data in arr:
        # 검사를 한뒤 안익은 토마토가 존재 할 경우
        if 0 in data:
            print(-1)
            error = 1
            break

    # 모두 익은 토마토일 경우
    if error == -1:
        print(result)
