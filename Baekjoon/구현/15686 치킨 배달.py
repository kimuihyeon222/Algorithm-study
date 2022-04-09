import sys
input = sys.stdin.readline
from itertools import combinations

# nxn배열, m은 치킨집 선택
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 집 위치
home = []
# 각 치킨 집 별로 모든 집의 값을 구함
tmp_store = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            tmp_store.append((i,j))
            
# 선택 된 치킨 집 기준으로 모든 집과 거리를 구함
store = [[]*(len(tmp_store)) for _ in range(len(tmp_store)) ]
sum_store = []
for i in range(len(tmp_store)):
    for j in range(len(home)):
        store[i].append(abs( tmp_store[i][0] - home[j][0] ) + abs( tmp_store[i][1] - home[j][1] ))
    sum_store.append(sum(store[i]))

store_list = []
for i in range(1, len(sum_store)+1):
    store_list.append(i)

# m개의 치킨집 선정했을 경우의 수
store_comb = list(combinations(store_list, m))

result = 1e9
for i in range(len(store_comb)):
    tmp_result = 0
    for j in range(len(store[0])): # 0~5
        tmp_min = store[store_comb[i][0]-1][j]
        for k in range(1, m):
            if tmp_min > store[store_comb[i][k]-1][j]:
                tmp_min = store[store_comb[i][k]-1][j]
        tmp_result += tmp_min
        if tmp_result > result:
            break
    if result > tmp_result:
        result = tmp_result

print(result)
        
