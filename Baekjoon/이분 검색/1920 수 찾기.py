n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for i in range(m):
    left = 0
    right = len(arr1)-1
    result = -1
    while(left <= right):
        mid = int((left+right)/2)
        # python에서 몫 구하는 방법 // 쓰면됨 -> mid = (left+right) // 2 
        if arr1[mid] > arr2[i]:
            right = mid - 1
        elif arr1[mid] < arr2[i]:
            left = mid + 1
        else:
            result = mid;
            break
    
    if result != -1:
        print(1)
    else:
        print(0)
