import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

arr = [ [0]*n for _ in range(n)]

for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = 1
    arr[y-1][x-1] = 1


result = [-1,-1]
# 1번부터 5번까지 최솟값 구하기
for num in range(n):
    tmp = deque([[num, 0]])
    tmp_min = 0
    tmp_dict = {}
    for set_dict in range(n):
        tmp_dict[set_dict] = 1
    tmp_dict[num] = 0
    stop = 0
    while len(tmp) != 0:
        check = tmp.popleft()
        # 검사를 안한 check 가 있다면 count 를 tmp_min에 저장
        if tmp_dict[check[0]] != 0:
            tmp_min += check[1]
            tmp_dict[check[0]] = 0
            stop += 1
            if stop == n-1:
                break
        for go in range(n):
            # 연결 관계가 있다면 tmp 큐에 넣어줌
            if arr[check[0]][go] != 0 and tmp_dict[go] != 0:
                # 해당 연결관계 번호와, 몇번째의 정보를 같이 넣어줌
                tmp.append([go, check[1]+1])

    if result[0] == -1:
        result = [num+1, tmp_min]
    else:
        if result[1] > tmp_min:
            result = [num+1, tmp_min]

print(result[0])
