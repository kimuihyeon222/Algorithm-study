import sys

n = int(sys.stdin.readline())

arr = [ list(map(int, sys.stdin.readline().strip())) for _ in range(n) ]

result = []

def search(s, x, y):
    # 압축이 가능한지 본다
    check = arr[x][y] # 값을 하나 설정하여 다른게 있으면 나누기 시작
    for i in range(x, x+s):
        for j in range(y, y+s):
            if check != arr[i][j]:
                result.append('(')
                search(s//2, x, y)
                search(s//2, x, y+s//2)
                search(s//2, x+s//2, y)
                search(s//2, x+s//2, y+s//2)
                result.append(')')
                return
    result.append(check)
search(n, 0, 0)
for i in result:
    print(i, end='')
