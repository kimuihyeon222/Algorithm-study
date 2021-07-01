import sys
from collections import deque


x, y = map(int, sys.stdin.readline().split())

arr = [ list(map(int,sys.stdin.readline().strip())) for _ in range(x)]
check = [[-1]*y for _ in range(x)]

d_x = [0, 0, -1, 1]
d_y = [-1, 1, 0, 0]

data = deque([])
data.append([0, 0])
check[0][0] = 1
cnt = 1
while len(data) != 0:
    spot = data.popleft()
    # 갈수 있는 곳 검사
    for i in range(4):
        if 0 <= spot[0] + d_x[i] < x and 0<= spot[1] +d_y[i] < y:
            # 해당 부분을 이미 검사 했으면 할 필요 없음
            if check[spot[0]+d_x[i]][spot[1]+d_y[i]] == -1 and arr[spot[0]+d_x[i]][spot[1]+d_y[i]] == 1:
                check[spot[0]+d_x[i]][spot[1]+d_y[i]] = check[spot[0]][spot[1]]+1
                data.append([spot[0]+d_x[i], spot[1]+d_y[i]])
print(check[x-1][y-1])
