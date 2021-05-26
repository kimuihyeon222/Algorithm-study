import sys
n = int(input())
cards = list(map(int, sys.stdin.readline().strip().split()))
check = {}
for i in cards:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1
m = int(input())
test = list(map(int, sys.stdin.readline().strip().split()))
for i in test:
    if i in check:
        print(check[i], end = ' ')
    else:
        print(0, end = ' ')
