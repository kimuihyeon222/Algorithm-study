import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    minheap = []
    maxheap = []
    check = [0] * 1000001
    for key in range(k):
        oper, num = sys.stdin.readline().split()
        if oper == 'I':
            heapq.heappush(maxheap, [-int(num), key])
            heapq.heappush(minheap, [int(num), key])
            check[key] = 1
        else:
            if int(num) == 1:
                # 다른 곳에서 삭제되었을 경우를 파악해야함
                while len(maxheap) != 0:
                    if check[maxheap[0][1]] != 1:
                        heapq.heappop(maxheap)
                    else:
                        break
                if len(maxheap) != 0:
                    check[maxheap[0][1]] = 0
                    heapq.heappop(maxheap)
            else:
                # 다른 곳에서 삭제되었을 경우를 파악해야함
                while len(minheap) != 0:
                    if check[minheap[0][1]] != 1:
                        heapq.heappop(minheap)
                    else:
                        break
                if len(minheap) != 0:
                    check[minheap[0][1]] = 0
                    heapq.heappop(minheap)
                    
    # 최종적으로 배열을 최신화 시켜줌
    while True:
        if len(maxheap) != 0 and check[maxheap[0][1]] != 1:
            heapq.heappop(maxheap)
        else:
            break
    while True:
        if len(minheap) != 0 and check[minheap[0][1]] != 1:
            heapq.heappop(minheap)
        else:
            break

    # 정답
    if len(maxheap) != 0 and len(minheap) != 0:
        print(maxheap[0][0]*-1, minheap[0][0])
    else:
        print("EMPTY")
