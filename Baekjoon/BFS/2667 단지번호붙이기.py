import sys
from collections import deque

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
result = []

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

tmp = deque([])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 1
            tmp.append([i, j])
            # 연관 된것들 검사
            while len(tmp) != 0:
                check = tmp.popleft()
                arr[check[0]][check[1]] = 0
                for k in range(4):
                    if 0 <= check[0] + x[k] < n and 0 <= check[1] + y[k] < n:
                        if arr[check[0]+x[k]][check[1]+y[k]] == 1:
                            cnt +=1
                            tmp.append([check[0]+x[k], check[1]+y[k]])
                            arr[check[0]+x[k]][check[1]+y[k]] = 0
            result.append(cnt)
print(len(result))
result.sort()
for data in result:
    print(data)
