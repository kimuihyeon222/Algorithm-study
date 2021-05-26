import sys
from collections import deque

n = int(sys.stdin.readline())

data = [ ]
check = {}
for i in range(n):
    tmp = int(sys.stdin.readline())
    data.append(tmp)
    if tmp in check:
        check[tmp] += 1
    else:
        check[tmp] = 1

print(int(round(sum(data)/len(data),0)))
# print(sum(data)//len(data))
data.sort()
print(data[len(data)//2])
tmp = sorted(check.items())
tmp = sorted(tmp, key=lambda x : x[1])
for i in range(n):
    if tmp[i][1] == max(check.values()):
        if i+1 < len(tmp) and tmp[i+1][1] == max(check.values()):
            print(tmp[i+1][0])
            break
        else:
            print(tmp[i][0])
            break
print(max(data)-min(data))

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

10
-3855 
-2693
-3819
-1071
-2994
-1562
-3147
-1008
-446
-2849
# 위의 예제에서 평균 구하는게 round랑 //랑 값이 다름 정답은 -2344
