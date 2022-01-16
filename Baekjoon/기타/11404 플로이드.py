# https://blog.naver.com/ndb796/221234427842
# 플로이드 와샬
# 거쳐갈경우를 고려해주면 됨
import sys
input = sys.stdin.readline

INF = 1e9
n = int(input().rstrip())
m = int(input().rstrip())

city = [[INF]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    city[a-1][b-1] = min(c, city[a-1][b-1])

# 거쳐가는 지점
for i in range(n):
    # 출발 지점
    for j in range(n):
        # 도착 지점
        for k in range(n):
            # 출발지점 -> 거쳐가는 지점 -> 도착 지점
            # vs 출발지점 -> 도착 지점
            if city[j][i] + city[i][k] < city[j][k]:
                city[j][k] = city[j][i] + city[i][k]
                
for i in range(n):
    for j in range(n):
        if i == j or city[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(city[i][j], end=" ")
    print()
