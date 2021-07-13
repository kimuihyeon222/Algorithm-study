import sys

t = int(sys.stdin.readline())

def search(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return search(n-1) + search(n-2) + search(n-3)
for _ in range(t):
    n = int(sys.stdin.readline())
    print(search(n))
