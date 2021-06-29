import sys

n, m = map(int, sys.stdin.readline().split())

data = {}

for _ in range(n+m):
    name = sys.stdin.readline().strip()
    if name in data:
        data[name] += 1
    else:
        data[name] = 1

result = []
for i in data:
    if data[i] == 2:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)
