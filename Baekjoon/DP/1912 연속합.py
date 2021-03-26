n = int(input())

arr = list(map(int, input().split()))

d = [ 0 for _ in range(n)]
d[0] = arr[0]

if n > 1:
    for i in range(1, n):
        #총 3가지 경우
        # 1. 연속적일 경우 d배열과 현재 arr값 합
        # 2. 연속 2개 일 경우, 즉 d와 상관없음 
        # 3. 그냥 현재 값만 선택 
        d[i] = max((d[i-1] + arr[i]), (arr[i-1]+arr[i]), arr[i])

print(max(d))
