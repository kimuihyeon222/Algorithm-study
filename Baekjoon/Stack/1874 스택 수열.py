import sys
n = int(sys.stdin.readline())

test = []
num = []

for i in range(n):
    test.append(int(sys.stdin.readline().strip()))
    num.append(i+1)

stack = []
num_cnt = 0
test_cnt = 0

answer = []
while True:
    if len(stack) == 0:
        stack.append(num[num_cnt])
        num_cnt +=1
        answer.append('+')
    else:
        if stack[-1] == test[test_cnt]:
            answer.append('-')
            stack.pop()
            test_cnt += 1
            if test_cnt > n-1:
                break
        elif stack[-1] > test[test_cnt]:
            answer = []
            break
        else:
            while stack[-1] != test[test_cnt]:
                stack.append(num[num_cnt])
                num_cnt+=1
                answer.append('+')

if len(answer) != 0:
    for i in answer:
        print(i)
else:
    print('NO')
