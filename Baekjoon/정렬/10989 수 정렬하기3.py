# counting 정
import sys

n = int(sys.stdin.readline())
data = [0]*10001
for i in range(n):
    tmp = int(sys.stdin.readline())
    data[tmp] += 1

for i in range(1, 10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)
