import sys
from collections import deque

t = int(sys.stdin.readline())

x_spot = [-1, 1, 0, 0]
y_spot = [0, 0, -1, 1]


for i in range(t):
    result = 0
    m,n,k = map(int, sys.stdin.readline().split())
    data = [ [0]*(n+2) for _ in range(m+2) ]
    check = deque([])

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        data[x+1][y+1] = 1
    
    # 검사
    for j in range(1, m+1):
        for k in range(1, n+1):
            if data[j][k] != 0:
                data[j][k] = 0
                result += 1
                check.append([j, k])
                # 가능한 모든 경우를 제외 시켜줘야함 -> 주변에 벌레들 다 잡아버림
                while len(check) != 0:
                    where = check.popleft()
                    # 위 앞 옆 아래 검사
                    for p in range(4):
                        if data[where[0]+x_spot[p]][where[1]+y_spot[p]] != 0:
                            check.append([where[0]+x_spot[p] , where[1]+y_spot[p]])
                            data[where[0]+x_spot[p]][where[1]+y_spot[p]] = 0
    print(result)
