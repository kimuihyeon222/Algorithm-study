from operator import truediv
import sys
input = sys.stdin.readline

sound = input().rstrip()
sound_arr = [0]*len(sound)
quack = ['q', 'u', 'a', 'c', 'k']
idx = 0
result = 0

if len(sound) % 5 != 0 or sound[0] != 'q':
    print(-1)
    exit(0)

while len(sound) != sound_arr.count(-1):
    # 검사
    idx = 0
    check = False
    for i in range(len(sound)):
        if sound_arr[i] == -1:
            continue
        else:
            if sound[i] == quack[idx]:
                idx += 1
                sound_arr[i] = -1
                # quack에서 k까지 검사했을 경우
                if idx == 5:
                    idx = 0
                    if check == False:
                        result += 1
                    check = True
    if idx != 0:
        print(-1)
        exit(0)
        
print(result)
                    
