import sys
input = sys.stdin.readline

n = int(input().strip())

data = [[] for _ in range(26)]

for _ in range(n):
    a,b,c = map(str, input().split())
    data[ord(a) - ord('A')].append(ord(b))
    data[ord(a) - ord('A')].append(ord(c))

def search(start, cnt):
    if cnt == 1 : 
        print(chr(start), end = "")
    if data[start-ord('A')][0] != ord('.'):
        search(data[start-ord('A')][0], cnt)
    if cnt == 2:
        print(chr(start), end = "")
    if data[start-ord('A')][1] != ord('.'):
        search(data[start-ord('A')][1], cnt)
    if cnt == 3:
        print(chr(start), end= "")

#전위 순회
search(ord('A'), 1)
print()
#중위 순회
search(ord('A'), 2)
print()
#후위 순회
search(ord('A'), 3)
