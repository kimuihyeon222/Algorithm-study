import sys
input = sys.stdin.readline

t = int(input().rstrip())

data = list(map(int, input().split()))
arr = []
arr.append([int(1e9), -int(1e9)])
for i in range(len(data)):
    arr.append([data[i], data[i]])
arr.append([int(1e9), -int(1e9)])

for i in range(1, t):
    tmp = list(map(int, input().split()))
    tmp_list = []
    for j in range(1, 4):
        tmp_list.append([min(tmp[j-1] + arr[j-1][0], tmp[j-1] + arr[j][0], tmp[j-1] + arr[j+1][0]),
                    max(tmp[j-1] + arr[j-1][1], tmp[j-1] + arr[j][1], tmp[j-1] + arr[j+1][1])])
    
    arr[1:4] = tmp_list

#결과
print(max(arr[1:-1], key = lambda x : x[1])[1], min(arr[1:-1], key = lambda x : x[0])[0])
