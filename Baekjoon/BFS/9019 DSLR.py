# pypy로 체점했음
import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        print('')
        continue
    # 검사
    arr = deque([])
    check = dict()
    arr.append([a, ''])
    while len(arr) != 0:
        data = arr.popleft()
        # D 변환
        if 2*data[0] < 10000:
            # 정답인지
            if 2*data[0] == b:
                print(data[1]+'D')
                break
            # 이미 사용되었는지
            if 2*data[0] in check:
                pass
            else:
                check[2*data[0]] = 1
                arr.append([2*data[0], data[1]+'D'])
        else:
            if (2*data[0])%10000 == b:
                print(data[1]+'D')
                break
            # 이미 사용되었는지
            if (2*data[0])%10000 in check:
                pass
            else:
                check[(2*data[0])%10000] = 1
                arr.append([(2*data[0])%10000, data[1]+'D'])

        # S 변환
        if data[0] == 0:
            if 9999 == b:
                print(data[1]+'S')
                break
            if 9999 in check:
                pass
            else:
                check[9999] = 1
                arr.append([9999, data[1]+'S'])
        else:
            if data[0]-1 == b:
                print(data[1]+'S')
                break
            if data[0]-1 in check:
                pass
            else:
                check[data[0]-1] = 1
                arr.append([data[0]-1, data[1]+'S'])
        # L 변환
        
        # 3자리일 경우 앞을 0으로 채워줌
        if len(str(data[0])) < 4:
            data[0] = '0'*(4-len(str(data[0]))) + str(data[0])
        if int(str(data[0])[1:] + str(data[0])[0]) == b:
            print(data[1]+'L')
            break
        if int(str(data[0])[1:] + str(data[0])[0]) in check:
            pass
        else:
            check[int(str(data[0])[1:] + str(data[0])[0])] = 1
            arr.append([ int(str(data[0])[1:] + str(data[0])[0]), data[1]+'L'])
        # R 변환
        if int(str(data[0])[-1] + str(data[0])[:-1]) == b:
            print(data[1]+'R')
            break
        if int(str(data[0])[-1] + str(data[0])[:-1]) in check:
            pass
        else:
            check[int(str(data[0])[-1] + str(data[0])[:-1])] = 1
            arr.append([ int(str(data[0])[-1] + str(data[0])[:-1]), data[1]+'R'])
