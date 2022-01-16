# 이분그래프란 ?
# 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로 칠할 수 있는 그래프
# https://www.youtube.com/watch?v=5UxWEw6CTxQ
import sys
from collections import deque
input = sys.stdin.readline

# test 케이스 입력
k = int(input().rstrip())

def bfs(start):
    tmp[start] = 1
    q = deque()
    q.append(start)
    while q:
        go = q.popleft()
        # 이웃한 정점에 해당 정점의 반대되는 색갈을 칠함
        for i in arr[go]:
            if tmp[i] == 0:
                tmp[i] = -tmp[go]
                q.append(i)
            else:
                # 색이 이미 칠해져있고 같은 색갈일 경우
                # 이분 그래프가 될수 없음
                if tmp[i] == tmp[go]:
                    return False
    # 해당 정점으로부터 색을 다 칠하면
    # 이분 그래프가 가능
    return True

for _ in range(k):
    # 간선, 정점
    v,e = map(int, input().split())
    possible = True
    arr = [[] for _ in range(v+1)]
    tmp = [0 for _ in range(v+1)]
    
    for _ in range(e):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
        
    for i in range(1, v+1):
        # 현재 정점이 색칠이 안되어있다면
        if tmp[i] == 0:
            # 현재 정점으로 부터 이웃된 노드들을 색칠하러(검사하러)들어감
            result = bfs(i)
            if result == False:
                possible = False
                break
    
    if possible == True:
        print("YES")
    else:
        print("NO")
