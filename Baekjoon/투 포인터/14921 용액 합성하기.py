import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))

if n == 2:
    print(sum(arr))
else:
    head, tail = 0, n-1
    result = arr[head] + arr[tail]
    while head != tail:
        tmp = arr[head] + arr[tail]
        if abs(tmp) < abs(result):
            result = tmp
        if tmp < 0:
            head += 1
        else:
            tail -=1

    print(result)
    
   
# 투포인터 성질과
# 음수 양수 성질로 0에 가깝게 하려는 것을 파악하면 풀이가  
