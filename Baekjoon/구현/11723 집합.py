import sys

t = int(sys.stdin.readline())

arr = [-1]*20
ans = []
for i in range(t):
    tmp = sys.stdin.readline().split()

    if tmp[0] == 'add':
        if arr[int(tmp[1])-1] == -1:
            arr[int(tmp[1])-1] = int(tmp[1])
    elif tmp[0] == 'remove':
        if arr[int(tmp[1])-1] != -1:
            arr[int(tmp[1])-1] = -1
    elif tmp[0] == 'check':
        if arr[int(tmp[1])-1] != -1:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'toggle':
        if arr[int(tmp[1])-1] == -1:
            arr[int(tmp[1])-1] = int(tmp[1])
        else:
            arr[int(tmp[1])-1] = -1
    elif tmp[0] == 'all':
        arr = [1]*20
    elif tmp[0] == 'empty':
        arr = [-1]*20
