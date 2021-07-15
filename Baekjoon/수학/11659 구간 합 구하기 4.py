import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

data = [ list(map(int, sys.stdin.readline().split())) for _ in range(m) ]

for num in range(1, len(arr)):
    arr[num] = arr[num-1] + arr[num]

for i in range(m):
    if data[i][0] == 1:
        print(arr[data[i][1]-1])
    else:
        print(arr[data[i][1]-1] - arr[data[i][0]-2])
