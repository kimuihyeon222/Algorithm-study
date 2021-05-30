import sys
import math

n,m,b = map(int, sys.stdin.readline().split())
data =[ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = math.inf
high = 0
for i in range(257):
    min_f = 0
    max_f = 0
    for j in range(n):
        for k in range(m):
            if data[j][k] < i:
                min_f += (i-data[j][k])
            else:
                max_f += (data[j][k] - i)
    # 블록 갯수 파악
    if b + max_f >= min_f:
        if 2 * max_f + min_f <= ans:
            high = i
            ans = 2 * max_f + min_f
print(ans, high)


# pypy로 통과 / python3는 시간초과 ;;
