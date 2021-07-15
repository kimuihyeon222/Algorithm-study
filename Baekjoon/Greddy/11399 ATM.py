import sys

t = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

tmp = 0
time = 0

for i in range(t):
    time += tmp + arr[i]
    tmp += arr[i]

print(time)
