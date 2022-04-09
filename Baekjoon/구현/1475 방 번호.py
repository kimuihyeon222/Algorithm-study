import sys
input = sys.stdin.readline

n = input()

# 1세트에 0~9숫자 6은 9를 뒤집어서 사용 가능
# 각 자리수 갯 수 체크
tmp = [0] * 10
for i in range(len(n)-1):
    tmp[int(n[i])] += 1
    
result = -1
# 반복문 돌면서 최소 필요한 세트 갯수 파악
# 6,9를 제외한 나머지 수 중에서 최대 값 파악
# 6,9를 더한 뒤 나눈 값과 비교
for i in range(len(n)-1):
    if i==6 or i==9:
        continue
    if result < tmp[i]:
        result = tmp[i]
        
# 6,9를 더한 뒤 2로 나눈 값보다 작을 경우
# 6,9를 반올림 한 세트 수 만큼 필요
if result < ((tmp[6] + tmp[9])/2):
    print(round((tmp[6] + tmp[9])/2)+0.1 )
else:
    print(result)
