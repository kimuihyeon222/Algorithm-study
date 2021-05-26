import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    deq = deque([])
    n, m = map(int, sys.stdin.readline().split())
    tmp = sys.stdin.readline().strip().split()
    for j in range(n):
        deq.append([int(tmp[j]), j])
    cnt = 0
    while True:
        max_tmp = max(deq)[0]
        p_tmp = deq.popleft()
        if max_tmp == p_tmp[0]:
            cnt += 1
            if p_tmp[1] == m:
                print(cnt)
                break
        else:
            deq.append(p_tmp)
