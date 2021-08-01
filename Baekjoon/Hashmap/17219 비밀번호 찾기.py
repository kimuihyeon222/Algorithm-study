import sys


data = dict()
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    a,b = map(str, sys.stdin.readline().split())
    data[a] = b

for _ in range(m):
    site = sys.stdin.readline().strip()
    print(data[site])
