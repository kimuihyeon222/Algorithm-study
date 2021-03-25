num = int(input())

if num == 1:
    print(1)
elif num == 2:
    print(2)
else:
    # num-2전 값에 00을 붙인 모든 갯수 + num-1전의 값에 1을 붙여서 만든 모든 갯수
    d = [0]*(num+1)
    d[1] = 1
    d[2] = 2
    for i in range(3, num+1):
        d[i] = (d[i-2] + d[i-1]) % 15746

    print(d[num])
