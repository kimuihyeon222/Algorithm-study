# 해쉬이용하려했는데 61퍼에서 계속에러 해결 못함
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# arr = list(map(int, input().split()))
# dict = {}
# arr.sort()
# for i in arr:
#     if dict.get(i, -1) == -1:
#         dict[i] = 1
#     else:
#         dict[i] += 1

# if dict.get(0, -1) == 2:
#     dict[0] = 0
# result = 0
# if n != 1 or n != 2:
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if dict.get(arr[i]+arr[j], -1) >= 1:
#                 if arr[i] == 0 or arr[j] == 0:
#                     if dict.get(arr[i]+arr[j], -1) >= 2:
#                         result += dict[arr[i]+arr[j]]
#                         dict[arr[i]+arr[j]] = 0
#                 else:
#                     result += dict[arr[i]+arr[j]]
#                     dict[arr[i]+arr[j]] = 0

# print(result)

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n == 1 or n ==2:
    print(0)
else:
    result = 0
    for i in range(n):
        # 해당 값을 찾아야함
        item = arr[i]
        new = arr[0:i] + arr[i+1:]
        head, tail = 0, len(new)-1
        while head < tail:
            if new[head]+new[tail] == item:
                result += 1
                break
            else:
                if new[head]+new[tail] < item:
                    head += 1
                else:
                    tail -= 1
    print(result)
