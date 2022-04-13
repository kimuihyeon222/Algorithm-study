from operator import truediv
import sys
input = sys.stdin.readline

ip = input().rstrip().split(':')
# 중간에 0이 얼마나 연속되었는지
zero_cnt = 8 - (len(ip)-ip.count(''))
check = True
tmp = 0

for i in range(len(ip)):
    if ip.count('') > 1 and check == False:
        check = True
        continue
    if ip[i] == '':
        for _ in range(zero_cnt):
            print('0000', end='')
            tmp += 1
            if tmp != 8:
                print(':', end='')
        check = False
    else :
        print('0'*(4-len(ip[i])) + ip[i], end ='')
        tmp += 1
        if tmp != 8:
            print(':', end='')
