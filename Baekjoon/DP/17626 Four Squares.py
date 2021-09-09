# pypy로했음 -> .py는 시간초과뜸
# Greedy로 했는데 못풀었음
# dp로 푸는법 검색해서 해결...
import sys

n = int(sys.stdin.readline())

d = [0]*(n+1)
d[0], d[1] = 0, 1

# 방법 : n보다 작거나 같은 제곱수를 찾고 (n-제곱수)를 인덱스로 가진 값에 1을 더하면됨

for i in range(2, n+1):
    minValue = 1e9
    j=1
    while (j**2) <= i:
        minValue = min(minValue, d[i - (j**2)])
        j+=1
    d[i] = minValue + 1

print(d[n])
