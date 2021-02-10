#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int map[1501][1501]; //선택된 두개의 수 체크 
queue< pair<int, int> > q; //선택된 두개의 수로 갈수 있는 모든 경우의 수 저장
int sum; //세 수의 합
 
void start(int x, int y){
	q.push(make_pair(x,y));
	while(!q.empty()){
		x = q.front().first;
		y = q.front().second;
		q.pop();
		int tmp[3] = {x, y, sum-x-y}; //x, y값을 알면 sum을 통해 나머지 하나의 값도 알 수 있음
		//세 개의 수를 전부 각각 max min으로 비교하면서 그럴 때마다 가능한 경우를 q에 저장함
    for(int i=0; i<3; i++){
			for(int j=0; j<3; j++){
				if(tmp[i] < tmp[j]){
					int t1, t2;
					t1 = tmp[j] - tmp[i];
					t2 = tmp[i] + tmp[i];
					if(map[t1][t2] == 0){ //해당 값이 가능하다면 q에 push하고 map에 check를 해줌
						q.push(make_pair(t1,t2));
						map[t1][t2] = 1;
					}
				}
			}
		}
	}
}

int main(){
	int a,b,c;
	cin >> a >> b >> c;
	sum = a+b+c;
	if(sum%3 != 0) { //3으로 나누어지지 않으면 세 개의 돌이 나눠질수 없음
		cout << 0;
		return 0;
	}
	map[a][b]=1;
	start(a,b);
	if(map[sum/3][sum/3] == 1) cout << 1;
	else cout << 0;
	return 0;
}
