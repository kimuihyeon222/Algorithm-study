import sys

n, m = map(int, sys.stdin.readline().split())

arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max = -1

for x in range(n):
    for y in range(m):
        # 파란색
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x][y+3]:
                max = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x][y+3]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y]:
                max = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y]
        except IndexError:
            pass
        # 노란색
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x+1][y] + arr[x+1][y+1]:
                max = arr[x][y] + arr[x][y+1] + arr[x+1][y] + arr[x+1][y+1]
        except IndexError:
            pass
        # 주황색
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+2][y+1]:
                max = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+2][y+1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+2][y-1]:
                max = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+2][y-1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y-1] + arr[x][y-2] + arr[x+1][y-2]:
                max = arr[x][y] + arr[x][y-1] + arr[x][y-2] + arr[x+1][y-2]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y-1] + arr[x][y-2] + arr[x-1][y-2]:
                max = arr[x][y] + arr[x][y-1] + arr[x][y-2] + arr[x-1][y-2]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x-1][y] + arr[x-2][y] + arr[x-2][y+1]:
                max = arr[x][y] + arr[x-1][y] + arr[x-2][y] + arr[x-2][y+1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x-1][y] + arr[x-2][y] + arr[x-2][y-1]:
                max = arr[x][y] + arr[x-1][y] + arr[x-2][y] + arr[x-2][y-1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+2]:
                max = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+2]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x-1][y+2]:
                max = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x-1][y+2]
        except IndexError:
            pass
        # 녹색
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+2][y+1]:
                max = arr[x][y] + arr[x+1][y] + arr[x+1][y+1] + arr[x+2][y+1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+1][y-1] + arr[x+2][y-1]:
                max = arr[x][y] + arr[x+1][y] + arr[x+1][y-1] + arr[x+2][y-1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y-1] + arr[x+1][y-1] + arr[x+1][y-2]:
                max = arr[x][y] + arr[x][y-1] + arr[x+1][y-1] + arr[x+1][y-2]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y-1] + arr[x-1][y-1] + arr[x-1][y-2]:
                max = arr[x][y] + arr[x][y-1] + arr[x-1][y-1] + arr[x-1][y-2]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x-1][y] + arr[x-1][y-1] + arr[x-2][y-1]:
                max = arr[x][y] + arr[x-1][y] + arr[x-1][y-1] + arr[x-2][y-1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x-1][y] + arr[x-1][y+1] + arr[x-2][y+1]:
                max = arr[x][y] + arr[x-1][y] + arr[x-1][y+1] + arr[x-2][y+1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x-1][y+1] + arr[x-1][y+2]:
                max = arr[x][y] + arr[x][y+1] + arr[x-1][y+1] + arr[x-1][y+2]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y+2]:
                max = arr[x][y] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y+2]
        except IndexError:
            pass
        # 보라색
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1]:
                max = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y-1]:
                max = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y-1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x-1][y+1]:
                max = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x-1][y+1]
        except IndexError:
            pass
        try:
            if max < arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1]:
                max = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1]
        except IndexError:
            pass
print(max)


# 안에 try except한 부분 가능한 경우의수를 배열로 만들어놓고 for문 돌리면서 가능한 범위 일 때
# 검사 하게 하면 코드 수를 줄일 수 있음
# 너무 간단하게 생각해서 코드가 너무 
