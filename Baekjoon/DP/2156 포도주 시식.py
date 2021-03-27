n = int(input())

arr = [int(input()) for _ in range(n)]

dp = [0]
dp.append(arr[0])
if n >= 2:
    dp.append(arr[0]+arr[1])

if n > 2:
    for i in range(3, n+1):
        # 이전 잔을 마실경우
        dp.append(arr[i-1] + arr[i-2] + dp[i-3])
        # 이전 잔을 안마실 경우
        dp[i] = max(dp[i], dp[i-2]+arr[i-1])
        # 현재 잔을 안마실 경우
        dp[i] = max(dp[i], dp[i-1])

print(max(dp))

###
계단 오르기와 비슷한데 이 문제의 경우는 연속으로 두번을 안먹을수 있음
예를들어
x o o
o x o
o o x -> 이경우에서 만약 다음에서 또 안먹게 되면 연속으로 2번까지 안먹는 것이다.
###
