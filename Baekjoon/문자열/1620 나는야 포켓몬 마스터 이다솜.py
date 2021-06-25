import sys
n, c = map(int, sys.stdin.readline().split())

data = {}
for i in range(n):
    a = sys.stdin.readline().strip()
    data[a] = i+1
reverse_dict = dict(map(reversed, data.items())) # key, value를 바꾸는 방법

for i in range(c):
    a = sys.stdin.readline().strip()
    if a[0] == '0' or a[0] == '1' or a[0] == '2' or a[0] == '3' or a[0] == '4' or a[0] == '5' or a[0] == '6' or a[0] == '7' or a[0] == '8' or a[0] == '9':
        print(reverse_dict[int(a)])
    else:
        print(data[a])
