import sys
n = int(sys.stdin.readline())

num = 665
while n != 0:
    num += 1
    if str(num).find("666") != -1:
        n -= 1
print(num)

# find()는 못찾을 경우 -1인걸 잘 인지해야함
# 0 번째 찾아서 7번째 처럼 쓰면 if 문이 안돌아가니 확실히 하기!
