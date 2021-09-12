import sys

#사람 수, 파티 수
n, m = map(int, sys.stdin.readline().split())

#진실을 아는 사람 수
truth = set(list(map(int, sys.stdin.readline().split()))[1:])

party = []
result = []

for _ in range(m):
    party.append(set(list(map(int, sys.stdin.readline().split()))[1:]))
    result.append(1)

for _ in range(m):
    for i, p in enumerate(party):
        # 겹치는게 있다면
        if truth & p:
            result[i] = 0
            truth |= p

print(sum(result))


# union and find를 사용하는 사람도 있음
# 하지만 python의 set 연산을 이용하면 더 쉽게 풀이 가능!!...
