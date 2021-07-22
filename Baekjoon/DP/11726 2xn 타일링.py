import sys

n = int(sys.stdin.readline())

# 2xn이어도 만들수 있는 칸을 확인하려면 1xn으로도 충분
# 이건 그림그려보면 알 수 있음 왜 1xn인지

# 라고 생각했지만 이 문제는 피보나치 라는 점...

d = [0, 1, 2]

if n > 2:
    for i in range(3, n+1):
        d.append((d[i-1] + d[i-2]) % 10007)
    
    print(d[n])
else:
    print(d[n])
