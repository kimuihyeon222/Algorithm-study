n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

# (a, b)일 때 a값을 기준으로 정렬
re_data = sorted(data, key = lambda x : x[0])

d = [1] * n

for i in range(1, n):
    for j in range(i):
        if re_data[j][1] < re_data[i][1]:
            d[i] = max(d[j]+1, d[i])

print(n-max(d))

"""
Longest Increasing Subsequence - LIS알고리즘을 사용하여
방법 :
A기둥 B기둥에서 A기중의 값들로 오름차순 정렬을 함
이후에 B기둥의 값들로 LIS알고리즘을 적용하여 안겹치게 최대로 만들수 있는 전깃줄 갯수를 구함
마지막으로 전체(n)에서 안겹치는 전깃줄 최대 갯수를 빼주면 끝
"""
