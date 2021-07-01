import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
data = sys.stdin.readline().strip()

result = 0
tmp_cnt = 0
i = 1
while i < m-1:
    if data[i-1] == 'I' and data[i] == 'O' and data[i+1] == 'I':
        tmp_cnt +=1
        if tmp_cnt == n:
            result += 1
            tmp_cnt -= 1
        i += 1
    else:
        tmp_cnt = 0
    i += 1
        
print(result)
