arr_list = []

# -1 -1 -1 입력시까지 계속 arr_list에 저장
tmp = []
while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == -1 and tmp[1] == -1 and tmp[2] == -1:
        break
    else:
        arr_list.append(tmp)

d = dict()

def w(data):
    # 먼저 해당 값으로 된 리스트의 값이 있는지 검사
    if d.get(str(data)) :
        return d[str(data)]
    else :
        # 해당 값이 존재 하지 않다면 중간 중간 값을 저장하면서 진행함
        if data[0] <= 0 or data[1] <= 0 or data[2] <= 0:
            d[str(data)] = 1
            return d[str(data)]

        elif data[0] > 20 or data[1] > 20 or data[2] > 20:
            d[str(data)] = w([20, 20, 20])
            return d[str(data)]
    
        elif data[0] < data[1] and data[1] < data[2]:
            d[str(data)] = w( [data[0], data[1], data[2]-1] ) + w( [data[0], data[1]-1, data[2]-1] ) - w( [ data[0], data[1]-1, data[2] ])
            return d[str(data)]
        else:
            d[str(data)] = w( [ data[0]-1, data[1], data[2] ] ) + w( [ data[0]-1, data[1]-1, data[2] ] ) + w( [ data[0]-1, data[1], data[2]-1 ] ) - w( [ data[0]-1, data[1]-1, data[2]-1 ] )
            return d[str(data)]

for data in arr_list:
    result = w(data)
    print('w(' + str(data[0]) + ', ' + str(data[1]) + ', ' + str(data[2]) +') = ' + str(result))
