# 해당 위치의 값을 선택했을때 이전의 선택 할수 있는 누적값을
# 활용해서 점화식을 세우면됨
# https://pacific-ocean.tistory.com/197
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
        
    # 이것도 규칙을 찾으면 됨
    dp = [[0]*(n+2) for _ in range(2)]
    
    for i in range(2, n+2):
        # 위에를 선택 할 경우
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i-2]
        # 아래를 선택 할 경우
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i-2]
    
    print(max(dp[0][-1], dp[1][-1]))
