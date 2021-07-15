import sys
import heapq

t = int(sys.stdin.readline())

arr = []

for i in range(t):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(num), num))
