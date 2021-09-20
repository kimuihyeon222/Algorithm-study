import sys
input = sys.stdin.readline

data = input().strip()

change_data = ""

stack = []

for i in range(len(data)):
    # 연산자 일 경우
    if data[i] == "(":
        stack.append(data[i])
    elif data[i] == ")":
        #stack에서 ( 까지 모든 값을 다 뺌
        while stack[-1] != "(":
            change_data += stack.pop()
        stack.pop()
    
    elif data[i] == "+" or data[i] == "-":
        while stack and stack[-1] != "(":
            change_data += stack.pop()
        stack.append(data[i])
    
    elif data[i] == "*" or data[i] == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            change_data += stack.pop()
        stack.append(data[i])
    
    #문자일경우
    else:
        change_data += data[i]

while stack:
    change_data += stack.pop()

print(change_data)
