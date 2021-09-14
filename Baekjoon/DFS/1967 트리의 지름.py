import sys
sys.setrecursionlimit(10**9)

t = int(sys.stdin.readline())

tree = [[] for _ in range(t+1)]

for _ in range(t-1):
    tmp = list(map(int, sys.stdin.readline().split()))
    tree[tmp[0]].append([tmp[1], tmp[2]])
    tree[tmp[1]].append([tmp[0], tmp[2]])


def dfs(start, result):
    for go, num in tree[start]:
        #아직 방문을 하지않았다면
        if result[go] == 0:
            result[go] = result[start] + num
            dfs(go, result)

#트리의 지름 풀이 방법
#1. 임의의 정점에서 가장 먼 노드를 구함
#2. 가장먼 노드에서 또 가장먼 노드를 구함
#3. 그중에서 가장 긴 거리를 가진 노드 존재

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
