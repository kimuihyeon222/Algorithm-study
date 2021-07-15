import sys
from collections import deque

t = int(sys.stdin.readline())

arr = [ list(map(int,sys.stdin.readline().split())) for _ in range(t) ]

tmp = deque([])
for i in range(t):
    for j in range(t):
        # 가는 길이 있다면 다른 가능한 것들 확인
        if arr[i][j] == 1:
            tmp.append(j)
            while tmp:
                check = tmp.popleft()
                # check에서 갈수 있는 노드들을 전부 검사
                for go in range(t):
                    if arr[check][go] == 1:
                        if arr[i][go] == 0:
                            arr[i][go] = 1
                            tmp.append(go)

for i in range(t):
    for j in range(t):
        print(arr[i][j], end = ' ')
    print()
