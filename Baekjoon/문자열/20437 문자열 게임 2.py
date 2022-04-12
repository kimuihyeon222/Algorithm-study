import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    data = input()
    k = int(input())
    
    arr = defaultdict(list)
    
    for i in range(len(data)):
        if data.count(data[i]) >= k:
            arr[data[i]].append(i)
         
    if len(arr) == 0:
        print(-1)
    else:
        min = 1e9
        max = -1
        for i in arr.values():
            for j in range(len(i)-k+1):
                if min > i[j+k-1] - i[j] + 1:
                    min = i[j+k-1] - i[j] + 1
                if max < i[j+k-1] - i[j] + 1:
                    max = i[j+k-1] - i[j] + 1
        if min != 1e9 and max != -1:
            print(min, max)
        else:
            print(-1)
            
  # https://hyunse0.tistory.com/288 참고
