#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

priority_queue<int, vector<int>, less<int> > add; //내림차순 정렬 
priority_queue<int, vector<int>, greater<int> > even; //오름차순 정렬 

//탑의 위치를 바꾸는 함수
void top_change(){
	int t, t1;
	t = even.top();
	t1 = add.top();
	even.pop();
	add.pop();
	add.push(t);
    even.push(t1);
} 

int main(){
	int n;
	int tmp[100001]; //검사해야 되는 값저장 배열 
	cin >> n;
	
	for(int i=0; i<n; i++){
		cin >> tmp[i];
	}
	
	for(int i=1; i<=n; i++){
		if(i % 2 != 0){ //홀수번째 일경우 
			add.push(tmp[i-1]); //add큐에 삽입
			if(!even.empty()){ //만약 even큐가 비어있지 않다면 top을 비교
				if(add.top() > even.top()){ //even이 더 작다면 add와 바꿔줌
					top_change();
				}
			}
		} 
		else{ //짝수번째 일경우 
			even.push(tmp[i-1]);
			if(add.top() > even.top()){ //even의 top이 더 작다면 add와 
				top_change();
			}
		}
		cout << add.top() << "\n";
	}
	return 0;
}
