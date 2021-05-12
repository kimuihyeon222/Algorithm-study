from typing import final


n, m = map(int, input().split())

arr = [ input() for _ in range(n)]

# 8*8 크기 체스판중 고쳐야 할 부분이 가장 적은 갯수

start_W = ['WBWBWBWB', 'BWBWBWBW']
start_B = ['BWBWBWBW', 'WBWBWBWB']

final_min = 99999999

for i in range(n):
    if i+8 > n:
        break
    for j in range(m):
        tmp_min1 = 0
        tmp_min2 = 0
        if j+8>m:
            break
        for z in range(8):
            # 시작이 하얀색일 경우
            if start_W[0][z] != arr[i][j+z]:
                tmp_min1 += 1
            if start_W[0][z] != arr[i+2][j+z]:
                tmp_min1 += 1
            if start_W[0][z] != arr[i+4][j+z]:
                tmp_min1 += 1
            if start_W[0][z] != arr[i+6][j+z]:
                tmp_min1 += 1
            if start_W[1][z] != arr[i+1][j+z]:
                tmp_min1 += 1
            if start_W[1][z] != arr[i+3][j+z]:
                tmp_min1 += 1
            if start_W[1][z] != arr[i+5][j+z]:
                tmp_min1 += 1
            if start_W[1][z] != arr[i+7][j+z]:
                tmp_min1 += 1

            if start_B[0][z] != arr[i][j+z]:
                tmp_min2 += 1
            if start_B[0][z] != arr[i+2][j+z]:
                tmp_min2 += 1
            if start_B[0][z] != arr[i+4][j+z]:
                tmp_min2 += 1
            if start_B[0][z] != arr[i+6][j+z]:
                tmp_min2 += 1
            if start_B[1][z] != arr[i+1][j+z]:
                tmp_min2 += 1
            if start_B[1][z] != arr[i+3][j+z]:
                tmp_min2 += 1
            if start_B[1][z] != arr[i+5][j+z]:
                tmp_min2 += 1
            if start_B[1][z] != arr[i+7][j+z]:
                tmp_min2 += 1
        final_min = min(final_min, tmp_min1, tmp_min2)
print(final_min)
