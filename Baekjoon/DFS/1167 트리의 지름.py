# import sys
# from collections import deque

# t = int(sys.stdin.readline())

# connect = [[] for _ in range(t)]

# for _ in range(t):
#     tmp = list(map(int, sys.stdin.readline().split()))[:-1]
#     for i in range(1, len(tmp), 2):
#         connect[tmp[0]-1].append([tmp[i]-1, tmp[i+1]])

# result = -1

# #1부터 돌면서 bfs로 최장 지름을 찾음
# for i in range(t):
#     check = set()
#     check.add(i)
#     start = deque([])
#     #i에서 갈수 있는 것들을 전부 start큐에 넣어줌
#     for j in range(len(connect[i])):
#         start.append([connect[i][j]])
#         #해당 정점이 방문되었으므로 체크를해줌
#         check.add(connect[i][j][0])
    
#     while start:
#         #tmp[0] -> 간선 정보, tmp[1] -> 간선 길이
#         tmp = start.popleft()[0]
        
#         if result < tmp[1]:
#             result = tmp[1]
#         for k in connect[tmp[0]]:
#             if k[0] not in check:
#                 check.add(k[0])
#                 start.append([[k[0], tmp[1]+k[1]]])
# print(result)

# 위의 방식은 일반적으로 생각했을 경우 bfs로 하였고 시간 초과발생

#트리의 지름 풀이 방법
#1. 임의의 정점에서 가장 먼 노드를 구함
#2. 가장먼 노드에서 또 가장먼 노드를 구함
#3. 그중에서 가장 긴 거리를 가진 노드 존재

import sys

t = int(sys.stdin.readline())

tree = [[] for _ in range(t+1)]

for _ in range(t):
    tmp = list(map(int, sys.stdin.readline().split()))[:-1]
    for i in range(1, len(tmp), 2):
        tree[tmp[0]].append([tmp[i], tmp[i+1]])

def dfs(start, result):
    for go, num in tree[start]:
        #아직 방문을 하지않았다면
        if result[go] == 0:
            result[go] = result[start] + num
            dfs(go, result)

result_1 = [0 for _ in range(t+1)]
dfs(1, result_1)

#시작위치는 다시 돌아올수 없으니 0값으로 초기화해줌
result_1[1] = 0
#임의의 정점 1에서 구해진 가장 거리가먼 정점 구함
tmp_max = result_1.index(max(result_1))

result_2 = [0 for _ in range(t+1)]
dfs(tmp_max, result_2)
#시작위치는 다시 돌아올수 없으니 0값으로 초기화해줌
result_2[tmp_max] = 0
print(max(result_2))
