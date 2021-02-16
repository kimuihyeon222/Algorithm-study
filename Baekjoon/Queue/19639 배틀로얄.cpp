#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

priority_queue<pair<int,int>, vector<pair<int, int> >, greater<pair<int, int> > > x_pq; //적
priority_queue<pair<int,int>, vector<pair<int, int> >, greater<pair<int, int> > > y_pq; //물약
vector<int> result; //게임 진행 순서

int main(){
	int x, y, m;
	cin >> x >> y >> m;
	int before=m; //싸움이 시작되기전에 이길 가능성이 있는지 판단하는 변수 
	int tmp;
	for(int i=1; i<=x; i++){
		cin >> tmp;
		x_pq.push(make_pair(tmp, i));
		before -= tmp; //적이니까 현재 체력에서 -를 해줌 
	}	
	for(int i=1; i<=y; i++){
		cin >> tmp;
		y_pq.push(make_pair(tmp, i));
		before += tmp; //회복 아이템이니까 체력에 +를 해줌 
	}
	
	if(before <= 0){ //체력이 0이하면 검사를 할 필요가 없이 0출력후 종료 
		cout << 0;
	}
	else{ //싸워서 이길 가능성이 있다면 검사 시작
		int m_tmp = m;
		while(!x_pq.empty()){
			if(m_tmp > x_pq.top().first){ //m_tmp보다 작다면 상대 가능 단 0이 안되니 같은 것은 빼야함 
				result.push_back(-x_pq.top().second); //적을 쓰려트렷으니 해당 번호 result에 삽입
				m_tmp -= x_pq.top().first; //m을 적의 공격만큼 감소시켜줌 
				x_pq.pop(); //해당 적을 처리했으니 pop해줌
			}
			else{ //더이상 적을 죽일 수 없을 경우 회복을 시켜줌 
				//최대 회복치까지 회복시켜줌
				while(!y_pq.empty()){
					if(m_tmp + y_pq.top().first <= m){ //만약 더한 값이 m을 초과하지 않는다면 더해줌 
						m_tmp += y_pq.top().first;
						result.push_back(y_pq.top().second); //적을 쓰려트렷으니 해당 번호 result에 삽입
						y_pq.pop();
					}
					else break;
				} 
			}
		}
		while(!y_pq.empty()){ //남은 물약이 있다면 다 먹어줌
			result.push_back(y_pq.top().second);
			y_pq.pop();
		}
		for(int i=0; i<x+y; i++) cout << result[i] << "\n";
	}
	return 0;
}
