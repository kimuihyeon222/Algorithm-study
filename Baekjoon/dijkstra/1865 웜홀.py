# 벨만 포드 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

#벨만 포드 알고리즘
def bf(start):
    dist[start] = 0

    for check in range(1, n+1):
        for cur in range(1, n+1):
            for next, wei in graph[cur]:
                if dist[next] > dist[cur] + wei:
                    dist[next] = dist[cur] + wei

                    # n번째에도 값이 갱신된다면 음수 사이클이 존재한다는것
                    if check == n:
                        return True
    return False


t = int(input().strip())
for _ in range(t):
    n,m,w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)
    #간선은 무방향
    for i in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    #웜홀은 단방향
    for i in range(w):
        a,b,c = map(int, input().split())
        graph[a].append((b,-c))
    
    #음의 사이클이 존재하는지 확인 -> 돌아왔을 때 음수가 될 수 있다는 의미
    negative_cycle = bf(1)

    if negative_cycle == True:
        print("YES")
    else:
        print("NO")
