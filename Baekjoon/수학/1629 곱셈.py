import sys

a,b,c = map(int, sys.stdin.readline().split())

def DaC(a,b):
    if b == 1:
        return a%c
    
    tmp = DaC(a, b//2)
    
    #짝수라면 tmp*tmp
    if b % 2 == 0:
        return tmp*tmp%c
    #홀수라면 tmp*tmp*a
    else:
        return tmp*tmp*a%c
    
print(DaC(a,b))
