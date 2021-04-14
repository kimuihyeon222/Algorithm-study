n = int(input())

data = [ [-1],[-1], [1], [7], [4], [2,3,5,9], [0,6], [8] ]

for i in range(n):
    minnum = [0,0,1,7,4,2,6,8,10,18,22]
    maxnum = [ ]
    test = int(input())
    #min값 구하기
    tmp_test = test
    if test <= 10:
        print(minnum[test], end = ' ')
    else:
        tmp_min=''
        while tmp_test - 7 >= 0:
            # 7로 계속 빼줌 (제일 갯수 많은 것)
            tmp_min += '8'
            tmp_test -= 7
        if tmp_test == 0:
            print(tmp_min, end =' ')
        elif tmp_test == 1:
            print('10'+tmp_min[1:], end=' ')
        elif tmp_test == 2:
            print('1'+tmp_min, end = ' ')
        elif tmp_test == 3:
            print('200'+tmp_min[2:], end = ' ')
        elif tmp_test == 4:
            print('20'+ tmp_min[1:], end=' ')
        elif tmp_test == 5:
            print('2'+tmp_min, end=' ')
        else:
            print('6'+tmp_min, end = ' ')


    #max값 구하기
    tmp_test = test
    while True:
        if tmp_test - 2 >= 2:
            maxnum.append(1)
            tmp_test -= 2
        else:
            maxnum.append(max(data[tmp_test]))
            break
    maxnum.sort(reverse=True)
    for i in maxnum:
        print(i, end='')
    print()
