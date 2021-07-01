import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    func = sys.stdin.readline().strip()
    cnt = int(sys.stdin.readline().strip())
    if cnt != 0:
        data = deque(map(int, sys.stdin.readline().strip()[1:-1].split(',')))
    else:
        sys.stdin.readline().strip()
        data = deque([])
        
    cur = 'front'
    error = 0
    for i in range(len(func)):
        # 삭제
        if func[i] == 'D':
            if len(data) == 0:
                print("error")
                error = 1
                break
            else:
                # 현재 기준이 맨 앞부터 일 경우
                if cur == 'front':
                    data.popleft()
                # cur == 'back'일 경우
                else:
                    data.pop()
        # fucn[i] == R일 경우
        else:
            if cur == 'front':
                cur = 'back'
            else:
                cur = 'front'
                
    if error == 1:
        continue
    if len(data) == 0:
        print('[]')
    else:
        if cur == "front":
            data = str(list(data))
            print(str(data).replace(' ',''))
        else:
            print(str(list(reversed(data))).replace(' ',''))
