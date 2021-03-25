n = int(input())

data = []

for i in range(0, n):
    data.append(list(map(int, input().split())))

# 3xn배열 생성, 현재 위치까지의 최소 값을 판단하는 배열
check = [ [None] * 3 for _ in range(n+1) ]

rgb = -1 # 현재 어느 위치의 색이 쓰였는지

for i in range(0, n):
    d = [] # 현재 단계까지의 최소 비용을 저장하는 배열
    if i == 0: # 초기 값 설정
        for k in range(3):
            d.append(data[i][k])
    else:
        for check_i in range(3):
            # 이전 집과 안 겹치는 색일 경우 (rgb에 해당하는 수를 더해줌 -> 이건 지금 이전까지의 최소값을 나타냄)
            if rgb != check_i:
                d.append(check[i-1][rgb] + data[i][check_i])
            else:
                # 이전의 칠한 집이 R인데 지금 R에 칠하려고 할경우 이전 단계에서의 G,B 중에 작은 수와 더함
                if check_i == 0:
                    d.append(min(check[i-1][1], check[i-1][2]) + data[i][check_i])
                elif check_i == 1:
                    d.append(min(check[i-1][0], check[i-1][2]) + data[i][check_i])
                else:
                    d.append(min(check[i-1][0], check[i-1][1]) + data[i][check_i])
    check[i] = d
    # 해당 단계에서 각 집에 대한 최소 값들이 구해지면 그 중에서 가장 작은 값은 index를 저장
    rgb = d.index(min(check[i]))

print(check[n-1][rgb])
