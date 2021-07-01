import sys

n = int(sys.stdin.readline())

arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

w_cnt = 0
b_cnt = 0
def b_search(s, x, y):
    global b_cnt
    check = 1
    if s == 0:
        return
    for i in range(x, x+s):
        for j in range(y, y+s):
            if check != arr[i][j]:
                # 분할 시작
                b_search(s//2, x, y)
                b_search(s//2, x, y+s//2)
                b_search(s//2, x+s//2, y)
                b_search(s//2, x+s//2, y+s//2)
                return
    b_cnt += 1

def w_search(s, x, y):
    global w_cnt
    check = 0
    if s == 0:
        return
    for i in range(x, x+s):
        for j in range(y, y+s):
            if check != arr[i][j]:
                # 분할 시작
                w_search(s//2, x, y)
                w_search(s//2, x, y+s//2)
                w_search(s//2, x+s//2, y)
                w_search(s//2, x+s//2, y+s//2)
                return
    w_cnt += 1

b_search(n, 0, 0)
w_search(n, 0, 0)
print(w_cnt)
print(b_cnt)
