import sys
input = sys.stdin.readline

n = int(input())

result = 0
count = 1 # 더할 값
tmp = 10 # 기준

# 기준보다 n 값이 크면 계속 진행
while tmp <= n:
    result += count * (9 * (10**(count-1)))
    count += 1
    tmp *= 10

# 남은 수 계산
result += count * (n - (10**(count-1)) + 1)
print(result)
