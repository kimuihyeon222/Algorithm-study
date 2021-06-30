import sys

n = int(sys.stdin.readline().strip())

result = 0
data = []
for _ in range(n):
    a,b = map(int ,sys.stdin.readline().split())
    data.append([a,b])
    
data.sort()
data = sorted(data, key = lambda x : x[1])
if len(data) > 0 :
    end = data[0][1]
    result += 1

for i in range(1, len(data)):
    # 저장된 것의 끝보다 시작하는 것의 값이 클경우
    if data[i][0] >= end:
        end = data[i][1]
        result += 1

print(result)

# 핵심 -> 종료 시간을 토대로 
