#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int one[301];
	int two[301];
	int stair[301];
	int n;
	cin >> n;
	for(int i=1; i<=n; i++){
		cin >> stair[i];
	}
	stair[0] = 0;
	one[0]=0;
	one[1]=stair[1];
	two[0]=0;
	two[1]=stair[1];
	
	for(int i=2; i<=n; i++){
		// 이전 계단을 밟지 않았을 경우
		one[i] = one[i-2] + stair[i];
		//이전 계단을 밟았을 경우 
		if(i >= 3) two[i] = two[i-3] + stair[i-1] + stair[i];
		else two[i] = stair[i-1] + stair[i];
		int big = max(one[i], two[i]);
		one[i] = big;
		two[i] = big;
	}
	cout << two[n];
	return 0;
 }


아래코드는 파이썬
n = int(input())

stair = [0]

for _ in range(n):
    stair.append(int(input()))

step1 = [0 for _ in range(n+1)] # 연속 한 번일 경우
step2 = [0 for _ in range(n+1)] # 연속 두 번일 경우

step1[1], step2[1] = stair[1], stair[1]

if n >= 2:
    for i in range(2,n+1):
        step1[i] = step1[i-2] + stair[i]
        if i == 2:
            step2[i] = stair[i] + stair[i-1]
        else:
            step2[i] = stair[i] + stair[i-1] + step2[i-3]
        
        #둘 중에 큰 값으로 둘다 초기화
        step1[i], step2[i] = max(step1[i], step2[i]), max(step1[i], step2[i])

print(step1[n])
