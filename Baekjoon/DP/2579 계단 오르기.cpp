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
