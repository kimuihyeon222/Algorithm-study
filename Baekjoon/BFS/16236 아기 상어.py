import sys
from collections import deque

t = int(sys.stdin.readline())


arr = [[0] * t for _ in range(t)]

# 물고기가 총 몇 마리인지 검사
fish_cnt = 0
# 상어위치
shark = deque([])

for i in range(t):
    tmp = list(map(int, sys.stdin.readline().split()))   
    for j in range(t):
        if tmp[j] != 0 and tmp[j] != 9:
            fish_cnt += 1
        elif tmp[j] == 9:
            # 0은 이동횟수
            shark.append([i, j, 0, -1])
            tmp[j] = 0
        arr[i][j] = tmp[j]

if fish_cnt == 0:
    print(0)
else:
    # 물고기를 잡아먹어야될 경우
    # 한 마리 일 경우
    if fish_cnt == 1:
        # 크기가 1일 경우에만 잡아먹을 수 있음
        for i in range(t):
            for j in range(t):
                if arr[i][j] == 1:
                    tmp = shark.pop()
                    print(abs(i - tmp[0]) + abs(j - tmp[1]))
                    break
    # 여러 마리 일 경우
    else:
        # 갈 수 있는 방향 기준은 위 -> 왼 -> 오 -> 아래 순서로 검사
        x = [-1, 0, 0, 1]
        y = [0, -1, 1, 0]
        # 먹이를 발견하기전 움직이는 범위를 저장하는 변수
        load_use = [[0]*t for _ in range(t)]
        size_shark = 2
        eat_shark = 0
        result = 0
        while len(shark):
            # 상어의 위치를 꺼내고
            move_shark = shark.popleft()
            load_use[move_shark[0]][move_shark[1]] = -1
            # 만약 먹을 수 있는 상어를 꺼냈다면 검사를 해야함
            # 가장 조건에 적합한 상어 찾기
            if move_shark[3] == 1:
                for k in range(len(shark)):
                    if move_shark[2] >= shark[k][2]:
                        if shark[k][3] == 1:
                            if move_shark[0] > shark[k][0]:
                                move_shark = shark[k]
                            elif move_shark[0] == shark[k][0] and move_shark[1] > shark[k][1]:
                                move_shark = shark[k]
                # 선택된 상어 제거
                result += move_shark[2]
                arr[move_shark[0]][move_shark[1]] = 0
                # 초기화
                load_use = [[0]*t for _ in range(t)]
                eat_shark += 1
                if eat_shark == size_shark:
                    size_shark += 1
                    eat_shark = 0
                while len(shark):
                    shark.popleft()

                shark.append([move_shark[0], move_shark[1], 0, -1])
            else:   
                for i in range(4):
                    if 0 <= move_shark[0] + x[i] < t and 0 <= move_shark[1] + y[i] < t:
                        # 방문을 하지 않았고
                        if load_use[move_shark[0] + x[i]][move_shark[1] + y[i]] == 0:
                            # 현재 상어보다 작거나 같다면
                            if arr[move_shark[0] + x[i]][move_shark[1] + y[i]] <= size_shark:
                                if arr[move_shark[0] + x[i]][move_shark[1] + y[i]] < size_shark and arr[move_shark[0] + x[i]][move_shark[1] + y[i]] != 0:
                                    # 처음 2개 좌표, 이동거리, 먹을 수 있는지 
                                    shark.append([move_shark[0] + x[i], move_shark[1] + y[i], move_shark[2] + 1, 1])
                                    load_use[move_shark[0] + x[i]][ move_shark[1] + y[i]] = -1
                                else:
                                    shark.append([move_shark[0] + x[i], move_shark[1] + y[i], move_shark[2] + 1, -1])
                                    load_use[move_shark[0] + x[i]][ move_shark[1] + y[i]] = -1
                            
        print(result)
