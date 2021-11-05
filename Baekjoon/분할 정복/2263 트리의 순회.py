import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# preorder 저장
preorder = []

tmp = [0]*(n+1)
for i in range(n):
    tmp[inorder[i]] = i

# inorder에서 root기준 왼쪽 left자식들, 오른쪽 right자식
# left자식들의 수는 postorder에서도 수는 똑같음
# 예를들어 inorder 6 4 1 5 2 7 3 8
# postorder 6 4 5 1 7 8 3 2 일때, root2기준
# 좌측은 4개로 1 4 5 6으로 inorder postorder의 구성은 같다
# 이러한 성질로 인오더에서 자식수를 파악해 postorder에서 root를 구한다.

def move(in_start, in_end, p_start, p_end):
    
    if in_start > in_end or p_start > p_end:
        return
    # postorder에서 부모노드 찾기
    parent = postorder[p_end]
    preorder.append(parent)
    
    # 왼쪽 갯수
    left_cnt = tmp[parent] - in_start
    right_cnt = in_end - tmp[parent]

    # 왼쪽 노드
    move(in_start, in_start+left_cnt-1, p_start, p_start+left_cnt-1)
    # 오른쪽 노드
    move(in_end-right_cnt+1, in_end, p_end-right_cnt, p_end-1)

move(0, n-1, 0, n-1)

for data in preorder:
    print(data, end=" ")
    
    
# https://ca.ramel.be/114 참고  
