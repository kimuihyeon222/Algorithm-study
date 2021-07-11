import sys

t = int(sys.stdin.readline().strip())

def check(m,n,x,y):
    while x <= m*n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1

for _ in range(t):
    m,n,x,y = map(int, sys.stdin.readline().split())
    print(check(m,n,x,y))

    
# https://pacific-ocean.tistory.com/126 참고
