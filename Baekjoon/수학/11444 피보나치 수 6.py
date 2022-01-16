# https://my-coding-notes.tistory.com/97
import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 피보나치 분할정복 풀이법
# 밑의 행렬을 제곱해주면됨
fibo = [[1,1], [1,0]]
mod = 1000000007

# 행렬 곱
def mul(mat1, mat2):
    a = ( mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0] ) % mod
    b = ( mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1] ) % mod
    c = ( mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0] ) % mod
    d = ( mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1] ) % mod
    return [[a,b],[c,d]]

# 거듭 제곱 함수 분할
def divid(mat, p):
    if p == 1:
        return mat
    else:
        tmp = divid(mat, p//2)
        if p % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), mat)
        
result = divid(fibo, n)
print(result[0][1])
