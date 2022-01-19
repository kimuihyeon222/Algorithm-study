import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

dict = {}
arr = deque()
result = 0
for cnt in range(n):
    num = int(len(input().rstrip()))
    arr.append(num)
    if dict.get(num, -1) == -1:
        dict[num] = 0
    else:
        dict[num] += 1
    
    if cnt >= k:
        result += dict[arr[0]]
        dict[arr[0]] -= 1
        arr.popleft()

while arr:
    result += dict[arr[0]]
    dict[arr[0]] -= 1
    arr.popleft()
    
print(result)
