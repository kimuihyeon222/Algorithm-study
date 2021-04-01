n = int(input())

arr = [ list(map(int, input().split())) for _ in range(n) ]

dp = [[-1]*500 for _ in range(500)]

def check(a, b):
    if a >= n:
        return 0
        
    if dp[a][b] != -1:
        return dp[a][b]
    #좌, 우측중 하나를 선택하여 더 큰 값을 더해줌
    dp[a][b] = arr[a][b] + max(check(a+1,b), check(a+1,b+1))
    return dp[a][b]

print(check(0, 0))
