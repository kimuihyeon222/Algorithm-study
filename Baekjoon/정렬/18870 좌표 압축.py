import sys

t = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

# 최종 검사를 위해 변형 전 arr를 복사해둠
tmp = arr.copy()

# 중복 제거를 위해 set사용
set_arr = set(arr)
arr = list(set_arr)

# 작은 순으로 정렬
arr.sort()

# 정렬 된것을 dict 형태로 저장
result = dict()
for i in range(len(arr)):
    result[arr[i]] = i

for data in tmp:
    print(result[data], end = ' ')
