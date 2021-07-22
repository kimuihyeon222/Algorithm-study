# 내가 짠 코드
import sys

n = int(sys.stdin.readline())

d = [0, 1, 3]

if n > 2:
    for i in range(3, n+1):
        if i % 2 == 0:
            d.append((d[i-1]*2 + 1) % 10007)
        else:
            d.append((d[i-1]*2 - 1) % 10007)
    print(d[n])
else:
    print(d[n])
    


# 아래는 다른 코드
s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i - 2] * 2) + s[i - 1])
n = int(input())
print(s[n] % 10007)
