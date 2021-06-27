import sys

n,r,c = map(int, sys.stdin.readline().split())

cnt = 0

def search(s, x, y):
    global cnt
    # 최소 단위인 2로 되었을 경우
    if s < 2:
        for i in range(2):
            for j in range(2):
                if y+i == r and x+j == c:
                    print(cnt)
                    return
                cnt += 1
    else:
        # 왼쪽 위에 포함되는가?
        if c < x + s and r < y+s:
            search(s//2, x, y)
        cnt += s**2
        
        # 오른쪽 위에 포함되는가?
        if x+s <= c < x+(s*2) and r < y+s:
            search(s//2, x+s, y)
        cnt += s**2

        # 왼쪽 아래에 포함되는가?
        if c < x+s and y+s <= r < y+(s*2):
            search(s//2, x, y+s)
        cnt += s**2

        # 오른쪽 아래에 포함되는가?
        if x+s <= c < x+(s*2) and y+s <= r < y+(s*2):
            search(s//2, x+s, y+s)
    
# 전체 크기보다 한단계 작은 크기로 검사 시작
search(2**(n-1), 0, 0)
