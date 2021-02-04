#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;

int n;
int check_x[16]={0,};
int check_y[16]={0,};

//DFS, back tracking 
int start(int x, int y){
	int tmp=0; 
	//해당 x, y자리에 놓을수 있는지 검사 
	for(int i=0; i<x; i++){
		//x,y줄에 넣을 수 있는지, 대각선에 넣을 수 있는지 
		if((check_x[i] == x)|| (check_y[i] == y) || (abs(check_x[i] - x) == abs(check_y[i] - y))){
			return 0;
		}
	}
	
	if(x == n-1) return 1;
	
	check_x[x] = x;
	check_y[x] = y;
	
	for(int j=0; j<n; j++){
		tmp += start(x+1, j); //다음 줄의 가능한 것 확인 
	}
	return tmp;
}

int main() {
	cin >> n;
	int total = 0; 
	for(int i=0; i<n; i++){
		total += start(0, i); // 첫 번째 줄에 대한 검사 
	}
	cout << total;
	return 0;
 }
