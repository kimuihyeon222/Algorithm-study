#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
int map[1500][1500]={0, };

int main() {
	int cnt;
	cin >> cnt;
	
	queue< pair<int,int> > q;
	queue<int> time;

	//초기 값 설정
	time.push(1);
	q.push(make_pair(1,1));
	map[1][1] = 1;
	int t, clip, monitor;
	while(!q.empty()){
		t = time.front();
		time.pop();
		clip = q.front().first;
		monitor = q.front().second;
		q.pop();
		// 1번 화면 -> 클립보드에  이모티콘 복사
		if(map[monitor][monitor] == 0){
			if(monitor < 1500){
				map[monitor][monitor] = t+1;
				time.push(t+1);
				q.push(make_pair(monitor, monitor));
			}
		}
		// 2번 클립보드 -> 화면 이모티콘 추가
		if(map[clip][monitor+clip] == 0){
			if(clip<1500 & monitor+clip < 1500){
				map[clip][monitor+clip] = t+1;
				time.push(t+1);
				q.push(make_pair(clip, monitor+clip));
			}
		}
		// 3번 화면 이모티콘 하나 삭제
		if(map[clip][monitor-1] == 0 && monitor-1 >= 0){
			if(monitor-1< 1500 && clip < 1500){
				map[clip][monitor-1] = t+1;
				time.push(t+1);
				q.push(make_pair(clip, monitor-1));
			}
		}
		if(monitor == cnt){
			cout << t;
			break;
		}
	}
	return 0;
 }
