n = int(input())

a = list(map(int, input().split()))

# 각 값이 1인 n크기의 1차원 배열 생성
ld = [1] * n # 왼쪽 시작으로 LIS 구하기
rd = [1] * n # 오른쪽 시작으로 LIS 구하기

for i in range(1, n):
    for j in range(i):
        # 왼쪽 시작으로 LIS
        if a[j] < a[i]: # i 위치의 값이 더 클 경우 j에서 1더한 값과 i의 현재 값비교하여 큰 값 사용
            ld[i] = max(ld[j]+1, ld[i])
        # 오른쪽 시작으로 LIS
        if a[n-j-1] < a[n-i-1]:
            rd[n-i-1] = max(rd[n-j-1]+1, rd[n-i-1])

# 각 단계에서 왼LIS, 우LIS를 합하여 최대값을 구함 겹치는 부분이 1개 존재하므로 1빼면 정답
for i in range(n):
    ld[i] += rd[i]

print(max(ld)-1)
