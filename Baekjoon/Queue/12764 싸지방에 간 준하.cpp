#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main(){
	int n;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > where; //컴퓨터의 자리를 나타내는 큐 
	priority_queue<int, vector<int>, greater<int> > useful; //사용가능한 컴퓨터 확인(가장 작은 컴퓨터부터 쓸수있게 오름차순으로 정렬하게함)
	vector<int> computer(500005, 0); //컴퓨터 1~x번까지 각 컴퓨터 사용횟수 저장 배열
	
	cin >> n;
	for(int i=0; i<n; i++){
		int start, end;
		cin >> start >> end;
		pq.push(make_pair(start, end));
		useful.push(i);
	}
	
	//맨 
	where.push(make_pair(pq.top().second, useful.top())); //끝나는 시간과 컴퓨터 위치를 queue에 삽입
	computer[useful.top()]++;
	pq.pop();
	useful.pop();
	int seat=0; //컴퓨터 최대 몇개인지 나타내는 변수
	 
	while(!pq.empty()){
		//컴퓨터의 끝나는 시간이 시작시간보다 클 경우 queue에 삽입
		if(pq.top().first < where.top().first){
			computer[useful.top()]++;
			if(useful.top() > seat){
				seat = useful.top();
			}
			where.push(make_pair(pq.top().second, useful.top())); //컴퓨터를 한대 더 사용한 것이므로 해당위치와 끝위치를 저장, size만큼 저장하면 컴퓨터의 갯수를 알수있음 
			pq.pop();
			useful.pop();
		}
		//시작시간이 끝나는 시간보다 클 경우 더 작은 것들을 queue에서 전부 뺌 -> 사용자가 컴퓨터 사용을 끝낸거임
		else{
			while(!where.empty()){
				if(where.top().first < pq.top().first){
					useful.push(where.top().second);
					where.pop();
				}
				else break;
			}
			computer[useful.top()]++;
			where.push(make_pair(pq.top().second, useful.top())); //컴퓨터를 한대 더 사용한 것이므로 해당위치와 끝위치를 저장, size만큼 저장하면 컴퓨터의 갯수를 알수있음 
			pq.pop();
			useful.pop();
		}
	}
	cout << seat+1 << "\n";
	for(int i=0; i<seat+1; i++){
		cout << computer[i] << " ";
	}
	return 0;
}
