#

import sys

channel = int(sys.stdin.readline())
t = int(sys.stdin.readline())

#set은 dict이랑 비슷하지만 key가 없고 값만 존재함!!
not_btn = set(str(i) for i in range(10))
if t != 0:
    #고장난 버튼이 있다면 제외 시킴
    not_btn -= set(map(str, sys.stdin.readline().split()))

start_channel = 100 #시작채널은 100번 

#최종 결과
min_cnt = abs(start_channel - channel)

#50만 채널까지 존재하기 때문에 0부터 + 했을경우 50만 100만부터 - 했을때 50만 이므로
#범위를 100만까지 잡고 진행
for num in range(10000001):
    for j in range(len(str(num))):
        # 현재 자리의 숫자가 사용 불가능한 버튼인지 검사
        if str(num)[j] not in not_btn:
            break
        # 현재 숫자의 모든 숫자가 가능할 경우 최소 값 비교검사
        elif len(str(num)) -1 == j:
            # 이전의 구한 최저 값보다 작다면 바꿔줌
            min_cnt = min(min_cnt, abs(num-channel) + len(str(num)))

print(min_cnt)
