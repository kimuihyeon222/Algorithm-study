import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
road = deque([])

# 벽을 뚫고 안뚫고 갔을 경우를 저장해야 되기 때문에 배열을 하나 더 생성
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]

xs = [1, -1, 0, 0]
ys = [0, 0, -1, 1]

def bfs():
    road.append([0, 0, 0])
    visited[0][0][0] = 1
    while road:
        # check는 벽돌을 부셧는지 판단하는 변수
        x, y, check = road.popleft()
        for i in range(4):
            next_x = x + xs[i]
            next_y = y + ys[i]

            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 0 and visited[next_x][next_y][check] == -1:
                    visited[next_x][next_y][check] = visited[x][y][check] + 1
                    road.append([next_x, next_y, check])
                elif graph[next_x][next_y] == 1 and visited[next_x][next_y][check] == -1 and check == 0:
                    visited[next_x][next_y][check+1] = visited[x][y][check] + 1
                    road.append([next_x, next_y, check+1])
bfs()
ans1, ans2 = visited[n-1][m-1][0], visited[n-1][m-1][1]
if ans1 == -1 and ans2 == -1:
    print(-1)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(ans2)
    
    
# 문제의 핵심!
# 벽을 뚫고 갔을 경우 해당 칸을 -1로 접근을 못하게 하면 나중에
# 벽을 안 뚫고 갈 수 있는 경우가 생길경우 처리를 하지 않음
# 따라서 배열을 하나 더 만들어 벽을 뚫고 간 최단거리, 벽을 안 뚫고 간 최단거리를
# 가지는 배열을 사용!
