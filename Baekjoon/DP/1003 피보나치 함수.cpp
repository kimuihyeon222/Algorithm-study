t = int(input())

arr = []

for _ in range(t):
    arr.append(int(input()))

d = []
d.append([1,0])
d.append([0,1])

def fibo(num):
    if num == 0:
        print(d[0][0], d[0][1])
    elif num == 1:
        print(d[1][0], d[1][1])
    else:
        start = len(d)-1 # 현재 배열의 끝을 알기위해 전체 크기를 읽어, 4까지 저장되있는데 3을 알고싶으면 검사할 필요가 없기때문에
        if start < num: # 이전 값들을 구해줌
            for i in range(start+1, num+1):
                d.append([d[i-1][0]+d[i-2][0], d[i-1][1] + d[i-2][1]])
        print(d[num][0], d[num][1])

for i in arr:
    fibo(i)
