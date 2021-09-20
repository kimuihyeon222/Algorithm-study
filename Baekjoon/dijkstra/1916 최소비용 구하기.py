import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    dist[start][start] = 0
    while q:
        d, now = heapq.heappop(q)

        if dist[start][now] < d:
            continue

        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[start][i[0]]:
                dist[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [[INF] *(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

s, e = map(int, input().split())

dijkstra(s)

print(dist[s][e])
