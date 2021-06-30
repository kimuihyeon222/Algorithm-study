import sys

n = int(sys.stdin.readline())

data = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

result = {-1:0, 0:0, 1:0}

def search(s, x, y):
    # 검사할 값 하나 설정
    check = data[x][y]
    for i in range(x, x+s):
        for j in range(y, y+s):
            if check != data[i][j]:
                # 다른 것을 발견 했을 경우
                search(s//3, x, y)
                search(s//3, x, y+s//3)
                search(s//3, x, y+s//3*2)
                search(s//3, x+s//3, y)
                search(s//3, x+s//3, y+s//3)
                search(s//3, x+s//3, y+s//3*2)
                search(s//3, x+s//3*2, y)
                search(s//3, x+s//3*2, y+s//3)
                search(s//3, x+s//3*2, y+s//3*2)
                return
    result[check] += 1

search(n, 0, 0)
for i in result.values():
    print(i)
