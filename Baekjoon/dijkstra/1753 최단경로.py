import sys
import heapq

input = sys.stdin.readline

v,e = map(int, input().split())
start = int(input().strip())

INF = int(1e9)
distance = [INF] *(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijksta(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijksta(start)

for i in range(1, v+1):
    if i == start:
        print(0)
    elif distance[i] == int(1e9):
        print('INF')
    else:
        print(distance[i])
