import sys
from collections import deque

t = int(sys.stdin.readline())

arr = [ sys.stdin.readline().strip() for _ in range(t) ]

# 일반인
def check_color(t, tmp_arr, arr):
    check = deque([])
    x = [0, 0, -1, 1]
    y = [-1, 1, 0, 0]
    result = 0
    for i in range(t):
        for j in range(t):
            # 가능한 경우가 있으면 queue에 넣음
            if tmp_arr[i][j] == 0:
                result += 1
                # 위치와 색상을 저장
                check.append([i, j, arr[i][j]])
                tmp_arr[i][j] = -1

                # 가능한 범위를 전부 검사
                while check:
                    color = check.popleft()
                    # 4방향 검사
                    for go in range(4):
                        if 0 <= color[0]+x[go] < t and 0<= color[1]+y[go] < t:
                            # 같은 색일 경우
                            if tmp_arr[color[0]+x[go]][color[1]+y[go]] == 0 and color[2] == arr[color[0]+x[go]][color[1]+y[go]]:
                                check.append([color[0]+x[go], color[1]+y[go], arr[color[0]+x[go]][color[1]+y[go]]])
                                tmp_arr[color[0]+x[go]][color[1]+y[go]] = -1
    return result

# 일반인
ans1 = check_color(t, [[0]*t for _ in range(t)], arr)

# 적록색약
# 적록 색은 r==g이므로 arr 배열을 바꿔줌
for i in range(t):
    arr[i] = arr[i].replace('G', 'R')
ans2 = check_color(t, [[0]*t for _ in range(t)], arr)

print(ans1, ans2)
