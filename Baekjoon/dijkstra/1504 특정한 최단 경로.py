import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    # a -> b로 가는데 c라는 값
    graph[a].append((b,c))
    graph[b].append((a,c))

# 서로 다른 정점 2개는 지나가야함
visit_1, visit_2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)
dijkstra(visit_1)
dijkstra(visit_2)


result = min(distance[1][visit_1] + distance[visit_1][visit_2] + distance[visit_2][n], distance[1][visit_2] + distance[visit_2][visit_1] + distance[visit_1][n])
if result < INF:
    print(result)
else:
    print(-1)
