#include <iostream>
#include <algorithm>
using namespace std;

int map[201]; //도시들의 연결상태를 나타내는 배열
int city[1001]; //이동할 도시입력 배열

//find
int find(int num){
	if(num == map[num]) return num;
	else return map[num] = find(map[num]); //1-2-3인데 1일 경우 3을 출력하기위해 재귀호출을함 
}
//union
void connect(int a, int b){
	a = find(a);
	b = find(b);
	if(a != b) map[a] = b; //같지 않다면 연결을 해줌 (1, 2이면 1자리에 2를 넣음으로써 1-2연결됐다 의미) 
}

int main() {
	int n, m, c1, c2;
	int tmp;
	cin >> n >> m;
	for(int i=1; i<=n; i++) map[i] = i;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			cin >> tmp;
			if(tmp != 0){ //도시가 연결되있다면 연결함수실행
				connect(i, j);
			}
		}
	}
	
	for(int i=1; i<=m; i++) cin >> city[i];
	//city의 경로를 따라 갈수있는지 검사
	for(int i=1; i<m; i++){
		c1 = find(city[i]);
		c2 = find(city[i+1]);
		if(c1 != c2){ // c1도시에서 c2로 연결이 안되있을 경우 이동 할수 없음 
			cout << "NO";
			return 0;
		}
	}
	cout << "YES";
	return 0;
 }
