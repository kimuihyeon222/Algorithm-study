# 입력 예제
# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

# 출력
# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun

import sys
n = int(input())

people = [ sys.stdin.readline().strip().split() for _ in range(n) ]
people.sort(key = lambda x : int(x[0]))
for i in range(n):
    print(people[i][0], people[i][1])
    
    
# 15, 16라인 잘 알고있기
