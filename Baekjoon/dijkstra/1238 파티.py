import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

# 다익스트라 알고리즘을 이용해 각 정점에서 최소 거리를 가지는 값을 계산
INF = int(1e9)
distance = [[INF] * (n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는데 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start][start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼냄
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는지 검사
        if distance[start][now] < dist:
            continue
        # 인접한 노드들 확인
        for i in graph[now]:
            # 현재 노드를 거쳐가는데 더 짧은 곳이 있는 경우
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
for i in range(n+1):
    dijkstra(i)
    
# 시작위치 -> x 마을 -> 시작위치의 최소값을 비교하여 가장 큰 값
result = [0] * (n+1)

for i in range(1, n+1):
    if i == x:
        continue
    # 시작위치 -> x 마을 -> 시작위치의 최소값 구해서 result에 저장
    result[i] = distance[i][x] + distance[x][i]

print(max(result))
