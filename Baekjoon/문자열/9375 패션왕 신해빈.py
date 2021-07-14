import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    daily = dict()
    for i in range(n):
        wear = sys.stdin.readline().split()
        if wear[1] in daily:
            daily[wear[1]] += 1
        else:
            daily[wear[1]] = 1
  
    # 이부분 생각 잘안나서 
    result = 1
    for key in daily.keys():
        result *= daily[key] + 1
    
    # 안입는 경우 -1
    print(result - 1)
