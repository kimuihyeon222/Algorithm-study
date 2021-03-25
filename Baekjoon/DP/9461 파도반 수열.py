n = int(input())

test = []
for _ in range(0, n):
    test.append(int(input()))

d = [1, 1, 1]

for i in test:
    if len(d) < i:
        for j in range(len(d), i):
            d.append(d[j-2] + d[j-3])
    print(d[i-1])
