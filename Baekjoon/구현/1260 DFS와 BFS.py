import sys
sys.setrecursionlimit(10**6)
from collections import deque

# n, m, v입력
n,m,v = map(int, sys.stdin.readline().split())

# 정점 +1 에 대한 배열 생성
arr = [[0]*(n+1) for _ in range(n+1)]
arr2 = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    arr[x][y] = 1
    arr[y][x] = 1
    arr2[x][y] = 1
    arr2[y][x] = 1

# 최종 결과 저장
result = [v] 

def dfs(start):
    for i in range(1, n+1):
        if arr[start][i] == 1:
            # 연결된 선 배열에서 삭제
            for j in result:
                arr[i][j] = 0
                arr[j][i] = 0
            result.append(i)
            dfs(i)

# 최종 결과 저장
result2 = []
tmp = deque([v])
def bfs():
    start = tmp.popleft()
    for j in result2:
        arr2[start][j] = 0
        arr2[j][start] = 0
    result2.append(start)
    for i in range(1, n+1):
        if arr2[start][i] == 1:
            # queue에 넣음
            if i not in tmp:
                tmp.append(i)
    if len(tmp) != 0:
        bfs()

dfs(v)
for i in result:
    print(i, end = ' ')

print()

bfs()
for i in result2:
    print(i, end = ' ')
