n = int(input())

arr = list(map(int, input().split()))

d = [1 for _ in range(n)]

for i in range(1, n):
    cnt = 0
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))

###
방법은 끝 부분에 있음
https://www.youtube.com/watch?v=5Lu34WIx2Us
###
