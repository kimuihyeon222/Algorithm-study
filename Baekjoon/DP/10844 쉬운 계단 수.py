check = 1000000000
n = int(input())

#2차원 배열 n의 경우 마다 구하기위해
arr = [[0]*10 for _ in range(n)]

# 처음의 경우
for i in range(1,10):
    arr[0][i] = 1

if n > 1:
    for i in range(1, n):
        # n의 길이 마다 이전 값을 이용해 구해줌
        for j in range(10):
            if j == 0: # i 가 0 이면 이전 값의 j+1만 사용
                arr[i][j] = arr[i-1][j+1] % check
            elif j == 9: # i 가 9 이면 이전값의 j-1 값만 사용
                arr[i][j] = arr[i-1][j-1] % check
            else : # i 가 처음과 끝이 아니라면 j-1, j+1값을 합친 것을 저장
                arr[i][j] = (arr[i-1][j-1] + arr[i-1][j+1]) % check

print(sum(arr[n-1]) % check)

### 방법
       0 1 2 3 4 5 6 7 8 9
n==1 : 0 1 1 1 1 1 1 1 1 1
n==2 : 1 1 2 2 2 2 2 2 2 1
n==3 : 1 3 3 4 4 4 4 4 3 2
  이런식으로 진행됨
###
