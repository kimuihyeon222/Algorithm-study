import sys

t, price = map(int, sys.stdin.readline().split())

arr = [ int(sys.stdin.readline().strip()) for _ in range(t) ]
this = t-1
coin = 0

while price:
    # 현재 남은 잔액이 선택된 금액보다 클 경우
    if price >= arr[this]:
        coin += price // arr[this]
        price -= arr[this] * (price // arr[this])
    this -= 1
    
print(coin)


# 동전 카운트 할때 index를 유지하면서 반복하기 => 시간초과
# 해결책 : 해당 금액으로 나눌수 있는 최대한을 나눠줌
