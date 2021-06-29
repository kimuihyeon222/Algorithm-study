import sys
data = sys.stdin.readline().strip()

val = data.split('-')

result = 0
for i in range(len(val)):
    if i == 0:
        if '+' in val[i]:
            tmp = val[i].split('+')
            for j in tmp:
                result += int(j)
        else:
            result += int(val[i])
    else:
        if '+' in val[i]:
            tmp = val[i].split('+')
            for j in tmp:
                result -= int(j)
        else:
            result -= int(val[i])
print(result)
