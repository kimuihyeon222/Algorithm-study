import sys

from collections import deque

check = [0]*101

check[1] = 1
dice = deque([])
dice.append([1, 0])

# 주사위
data = [1, 2, 3, 4, 5, 6]

n, m = map(int, sys.stdin.readline().split())

ladder = dict()
snake = dict()
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    ladder[a] = b

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    snake[a] = b

while dice:
    # 현재 위치에서 갈수있는 곳을 확인하여 dice에 추가
    spot, num = dice.popleft()

    for i in range(len(data)):
        # 100을 넘어가면 안함
        if spot+data[i] == 100:
            print(num+1)
            dice = 0
            break
        elif spot+data[i] < 100:
            # 사다리 확인
            if spot+data[i] in ladder:
                if check[ladder[spot+data[i]]] == 0:
                    dice.append([ladder[spot+data[i]], num+1])
                    check[ladder[spot+data[i]]] = 1
            # 뱀 확인
            elif spot+data[i] in snake:
                if check[snake[spot+data[i]]] == 0:
                    dice.append([snake[spot+data[i]], num+1])
                    check[snake[spot+data[i]]] = 1
            # 둘다 아닐 경우
            else:
                if check[spot+data[i]] == 0:
                    dice.append([spot+data[i], num+1])
                    check[spot+data[i]] = 1
