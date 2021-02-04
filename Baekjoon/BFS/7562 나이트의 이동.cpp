#include <iostream>
#include <algorithm>
//#include <cstring> //strlen사용
//#include <math.h> //pow함수사용, round
//#include <vector>
//#include <cmath>
#include <queue>
using namespace std;

vector<int> answer;

//해당 지역이 사용되었는지 확인하는 배열 300x300 최대 범위인 0으로 초기화된 배열 선언 
vector< vector<int> > map(300, vector<int>(300, -1));  
int change_x[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
int change_y[8] = {-1, 1, -2, 2, -2, 2, -1, 1};
int l;
int start_x, start_y;
int end_x, end_y; 
int cnt;
queue< pair<int,int> > q;
pair<int, int> tmp;
//bfs를 이용하여 최단경로 체크 
int check(){
	cnt=-3;
	while(!q.empty()){
		tmp = q.front(); //queue의 처음 위치의 값을 뺌 
		q.pop();
		if(cnt == -3){
			map[tmp.first][tmp.second] = 0;
			cnt=0;
		}
		else{
			cnt = map[tmp.first][tmp.second];
		}
		//현재 위치에서 가능한 좌표를 전부 map에 체크
		for(int i=0; i<8; i++){
			if((tmp.first + change_x[i]>=0 && tmp.first + change_x[i]<l) && (tmp.second + change_y[i]>=0 && tmp.second + change_y[i] < l)){ //뺀 값이 범위 안에 들어갈 경우 
				//현재 사용되지 않았을 경우 새롭게 초기화 후 queue에 push 
				if(map[tmp.first+change_x[i]][tmp.second+change_y[i]] == -1){
					map[tmp.first+change_x[i]][tmp.second+change_y[i]] = cnt+1; //해당 위치는 사용
					q.push(make_pair(tmp.first+change_x[i], tmp.second+change_y[i]));
					if(end_x == tmp.first+change_x[i] && end_y == tmp.second+change_y[i]){
						answer.push_back(cnt+1);
						return 0;
					}
				}
			}
		}
	}
	return 0;
}

void init(){ //queue초기화 하는 함수 
	//queue초기화 
	while(!q.empty()) q.pop();
	//map초기화
	for(int i=0; i<300; i++){
		for(int j=0;j <300; j++) map[i][j] = -1;
	}
} 

int main() {
	int n;
	cin >> n;
	for(int i=0; i<n; i++){ //총 n번 진행 
		cin >> l;
		cin >> start_x >> start_y;
		cin >> end_x >> end_y;
		init(); //모든설정 초기화 
		//처음 위치를 넣어줌
		if(start_x == end_x && start_y == end_y){
				answer.push_back(0);
		}
		else{
			q.push(make_pair(start_x, start_y)); //처음 위치를 queue에 넣어줌 
			check(); //입력을 받고 최단 거리 구하는 함수 실행
		}
	}
	for(int i=0; i<answer.size(); i++){
		cout << answer[i] << "\n";
	}
	return 0;
 }
