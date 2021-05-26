import sys
import math

n,m = map(int, sys.stdin.readline().split())

for i in range(n, m+1):
    if i == 1:
        continue
    # 소수 판단
    check = 1
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            check = -1
            break
    if check == 1:
        print(i)
        
# 1 소수 아님 ...
