import sys
sys.setrecursionlimit(10 ** 6)

one = sys.stdin.readline().strip()
two = sys.stdin.readline().strip()

d = [ [-1] * 1000 for _ in range(1000)]

def check(a, b):
    #기저 사례
    if a >= len(one) or b >= len(two):
        return 0
    
    if d[a][b] != -1:
        return d[a][b]
    
    # 현재 a위치의 값이 two배열에 있을 경우를 찾음
    target = one[a]
    # one 배열의 값이 존재하여 선택 할 경우
    for i in range(b, len(two)):
        if two[i] == target:
            d[a][b] = max(d[a][b], check(a+1, i+1)+1)
            # break 걸어주는 이유는 발견을 했고 다음 것을 발견했는데 굳이 그 뒤에 있는걸 갈 필요가 없다(오히려 길이가 짧아짐)
            # 여기서 break를 안 걸어줘도 어차피 max값을 비교해서 정답은 나오지만 시간초과발생!
            break
    # one 배열의 값이 존재하지 않아 선택하지 않을 경우
    d[a][b] = max(d[a][b], check(a+1, b))
    return d[a][b]

print(check(0,0))
