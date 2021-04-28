r, c, m = map(int, input().split())

data = [ list(map(int, input().split())) for i in range(m) ]
sharkspot = [[0]*c for _ in range(r)]

for i in data:
    sharkspot[i[0]-1][i[1]-1] = i[4]
    

sharktotal = 0 #잡은 상어 총 크기

# 상어의 속력을 바꿔줌
for i in data:
    if i[3] == 3 or i[3] == 4:
        i[2] = i[2] % ((c-1)*2)
    else:
        i[2] = i[2] % ((r-1)*2)

for fishking in range(c):
    # 해당 위치에서 땅에 가장 가까운 상어를 찾아서 없앰
    for catch in range(len(sharkspot)):
        if sharkspot[catch][fishking] != 0: # 만약 상어가 존재한다면
            sharktotal += sharkspot[catch][fishking] # 최종 값에 더해줌
            sharkspot[catch][fishking] = 0 # 해당 상어죽이고
            # 원래 배열에 해당 상어 값 삭제
            for del_data in range(len(data)):
                if data[del_data][0] == catch+1 and data[del_data][1] == fishking+1:
                    data[del_data] = [-1]*5 # 해당 위치의 상어 값 삭제
                    break
            break
    
    # 상어위치를 옮김, shark_tmp배열이 있어야함 겹치는지 안겹치는지 검사하기위해
    tmpsharkspot = [[0]*c for _ in range(r)]
    for set_shark in range(m):
        if data[set_shark][0] == -1: #상어 정보가 없을 경우
            continue
        
        # 오른쪽, 왼쪽으로 진행할 경우
        if data[set_shark][3] == 3 or data[set_shark][3] == 4:
            # 이동후 tmp배열에 위치에 크기저장, 원래 배열 위치,방향 바꿔주기
            gosize = data[set_shark][2] # 이동해야할 크기(속도)저장
                
            while gosize != 0:
                # 상어가 벽에 붙어있다면 방향을 먼저 바꿔줌
                if data[set_shark][1] == c:
                    data[set_shark][3] = 4
                elif data[set_shark][1] == 1:
                    data[set_shark][3] = 3
                
                # 3은 오른쪽 4는 왼쪽
                if data[set_shark][3] == 3:
                    # 최대한 갈수 있는 만큼 가야함
                    if data[set_shark][1] + gosize <= c:
                        data[set_shark][1] += gosize
                        gosize -= gosize
                    else:
                        gosize -= c-data[set_shark][1]
                        data[set_shark][1] += c-data[set_shark][1]
                else:
                    if data[set_shark][1] - gosize >= 1:
                        data[set_shark][1] -= gosize
                        gosize -= gosize
                    else:
                        gosize -= data[set_shark][1]-1
                        data[set_shark][1] -= data[set_shark][1]-1
        # 위, 아래로 진행할 경우
        elif data[set_shark][3] == 1 or data[set_shark][3] == 2:
            # 이동후 tmp배열에 위치에 크기저장, 원래 배열 위치,방향 바꿔주기
            gosize = data[set_shark][2] # 이동해야할 크기(속도)저장
                
            while gosize != 0:
                # 상어가 벽에 붙어있다면 방향을 먼저 바꿔줌
                if data[set_shark][0] == r:
                    data[set_shark][3] = 1
                elif data[set_shark][0] == 1:
                    data[set_shark][3] = 2
                
                # 1은 위, 2는 아래
                if data[set_shark][3] == 2:
                    # 최대한 갈수 있는 만큼 가야함
                    if data[set_shark][0] + gosize <= r:
                        data[set_shark][0] += gosize
                        gosize -= gosize
                    else:
                        gosize -= r-data[set_shark][0]
                        data[set_shark][0] += r-data[set_shark][0]
                else:
                    if data[set_shark][0] - gosize >= 1:
                        data[set_shark][0] -= gosize
                        gosize -= gosize
                    else:
                        gosize -= data[set_shark][0]-1
                        data[set_shark][0] -= data[set_shark][0]-1
        
        # 이동한 상어가 겹치는지 검사
        if tmpsharkspot[data[set_shark][0]-1][data[set_shark][1]-1] == 0:
            # sharkspot이 비어있다면 새로 이동한 상어 위치 저장
            tmpsharkspot[data[set_shark][0]-1][data[set_shark][1]-1] = data[set_shark][4]
        # 새로 들어가야하는 상어크기가 더 크다면
        elif tmpsharkspot[data[set_shark][0]-1][data[set_shark][1]-1] < data[set_shark][4] :
            for del_data in range(len(data)):
                if data[del_data][0] == data[set_shark][0] and data[del_data][1] == data[set_shark][1] and data[del_data][4] == tmpsharkspot[data[set_shark][0]-1][data[set_shark][1]-1]:
                    #print(data[del_data])
                    data[del_data] = [-1]*5 # 해당 위치의 상어 값 삭제
                    break
            tmpsharkspot[data[set_shark][0]-1][data[set_shark][1]-1] = data[set_shark][4]
        elif tmpsharkspot[data[set_shark][0]-1][data[set_shark][1]-1] > data[set_shark][4] :
            # 더 작은 값이 들어올 경우 잡아 먹히므로 삭제해줌
            for del_data in range(len(data)):
                if data[del_data][0] == data[set_shark][0] and data[del_data][1] == data[set_shark][1] and data[del_data][4] == data[set_shark][4]:
                    data[del_data] = [-1]*5 # 해당 위치의 상어 값 삭제
                    break
    sharkspot = tmpsharkspot
    #print(data)
print(sharktotal)
