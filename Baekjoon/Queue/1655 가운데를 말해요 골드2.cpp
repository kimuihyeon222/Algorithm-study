#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main(){
	int n;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > where; //컴퓨터의 자리를 나타내는 큐 
	vector<int> computer(500000, 0); //컴퓨터 1~x번까지 사용횟수 저장 배열
	int com=0; //현재 컴퓨터 위치를 나타내기 위한 변수
	 
	cin >> n;
	for(int i=0; i<n; i++){
		int start, end;
		cin >> start >> end;
		pq.push(make_pair(start, end));
	}  
	
	if(pq.top().second == 0){ //끝나는 시간이 0이면 빼버림 
		pq.pop();
	}
	int start=pq.top().first; //컴퓨터 시작 시간
	where.push(make_pair(pq.top().second, com)); //끝나는 시간과 컴퓨터 위치를 queue에 삽입
	computer[com]++; 
	pq.pop();
	
	while(!pq.empty()){
		com++;
		//구간안에 시작 값이 포함될 경우
		if(start < pq.top().first && pq.top().first < where.top().first){
			//시작위치를 바꿔줌
			start = pq.top().first;
		}
		else{ //컴퓨터 하나가 끝나고 새로운 사람이 그 자리로 들어갈 경우 
			start = pq.top().first;
			computer[where.top().second]++; //끝난 자리에 +1를 해줌
			where.push(make_pair(pq.top().second, where.top().second)); //끝나는 시간과 컴퓨터 위치를 queue에 삽입
			where.pop();
			pq.pop();
			com--; //원래 사용하던 자리에 들어갔으니 com을 하나 줄여줌 
			continue;
		}
		where.push(make_pair(pq.top().second, com)); //끝나는 시간과 컴퓨터 위치를 queue에 삽입
		computer[com]++; //해당위치를 하나 증가 
		pq.pop(); //구간을 사용했으니 빼줌 
	}
	
	cout << com+1 <<"\n";
	for(int i=0; i<=com; i++){
		cout << computer[i] << " ";
	} 
	return 0;
}
