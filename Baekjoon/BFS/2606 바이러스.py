import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = 1
    arr[y-1][x-1] = 1

tmp = deque()
tmp.append(0)
cnt = 0
while len(tmp) != 0:
    check = tmp.popleft()
    # check와 연결 관계를 전부 구함
    for i in range(n):
        if arr[check][i] == 1:
            cnt += 1
            arr[check][i] = 0
            arr[i][check]=0
            # 중복 검사를 피하기위해 검사한 것은 지워줌
            for j in tmp:
                arr[j][i] = 0
                arr[i][j] = 0
            tmp.append(i)
print(cnt)
