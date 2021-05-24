n = int(input())
arr = []
for i in range(n):
    arr.append(i+1)

check = 1

while len(arr) != 1:
    tmp = [ ]
    # check 부분부터 남아야 되는 카드들을 다시 tmp배열에 저장
    for i in range(check, len(arr), 2):
        tmp.append(arr[i])
    # 현재 data길이와 저장한 마지막 부분이 같을 경우
    # 다음 저장은 1부터 저장
    if len(arr) == i+1:
        check = 1
    # 마지막 부분을 저장하지 않았을 경우
    # 다음 저장은 0부터 저장
    else:
        check = 0
    arr = tmp

print(arr[0])
