import sys
from collections import deque

n, m= map(int, sys.stdin.readline().split())

arr = [[0]*n for _ in range(n)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    arr[x-1][y-1]=1
    arr[y-1][x-1]=1

go = deque([])
cnt = 0
visit = [0]*n

for i in range(len(visit)):
    # 아직 방문 하지 않은 노드가 있을 경우 탐색
    if visit[i] == 0:
        # i번째 줄을 불러와서 검사
        visit[i] = 1
        go.append(i)
        cnt += 1
        while go:
            now = go.popleft()
            for j in range(n):
                if arr[now][j] == 1:
                    if visit[j] == 0:
                        visit[j] = 1
                        go.append(j)

print(cnt)

# 일반적으로 탐색하면안되고
# visit라는 배열을 하나 더 두어서 방문했는지를 검사해야
# 시간초과를 안걸림
