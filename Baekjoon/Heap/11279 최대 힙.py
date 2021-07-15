import sys
import heapq

t = int(sys.stdin.readline())

arr = []

for i in range(t):
    num = int(sys.stdin.readline())
    if num == 0:
        # heap 에 넣고, 최대 힙을 만들기위해 0를 붙여줌
        heapq.heappush(arr, -num)
        # heap 에서 최대값뺌
        
        print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -num)
