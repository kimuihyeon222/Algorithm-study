#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
//스도쿠 문제 배열
vector< vector<int> > arr(9, vector<int>(9, 0));
//x,y축에 해당 숫자가 쓰였는지 확인하는 배열
vector< vector<int> > tmp_x(9, vector<int>(9, 0));
vector< vector<int> > tmp_y(9, vector<int>(9, 0)); 
vector< vector<int> > box(9, vector<int>(9, 0)); //9칸안에 들어가는지 검사하는 배열

void print(){
	for(int i=0; i<9; i++){
		for(int j=0; j<9; j++) cout << arr[i][j]<< " ";
		cout << "\n";
	}
}

//cnt는 1~81로 총 배열의 크기만큼 검사
void start(int cnt){
	int x, y, tmp; 
	if(cnt == 81){ //검사를 다했으면 종료 
		print();
		exit(0);
	}
	x = cnt /9;
	y = cnt % 9;
	if(arr[x][y] != 0){ //이미 채워진 경우 
		start(cnt+1); //다음 숫자 검사 
	}
	else{
		tmp=0; //9칸안에 들어가는지 검사하기 위한 변수
		for(int i=1; i<10; i++){
			//조건을 전부 만족할 경우 
			if(tmp_x[x][i] == 0 && tmp_y[y][i] == 0){
				//9칸(box)안에 들어가는지 검사
				if(box[(x/3)*3 + y/3][i] == 0){
          //조건을 전부 만족하면 일단 가능하다 생각하고 다음으로 진행
					arr[x][y] = i;
					tmp_x[x][i] = 1;
					tmp_y[y][i] = 1;
					box[(x/3)*3 + y/3][i] = 1;
					start(cnt + 1);
					//위의 재귀문에서 끝이 안나게되면 해당 숫자는 잘못된 것이므로
					//위에 값들을 다시 초기화해줌
					arr[x][y] = 0;
					tmp_x[x][i] = 0;
					tmp_y[y][i] = 0;
					box[(x/3)*3 + y/3][i] = 0;
				}
			}
		} 
	}

}

int main() {
	for(int i=0; i<9; i++){
		for(int j=0; j<9; j++) {
			cin >> arr[i][j];
			if(arr[i][j] != 0){ //0 이 아닐 경우 x,y 좌표에 사용했다는 표시 
				tmp_x[i][arr[i][j]] = 1;
				tmp_y[j][arr[i][j]] = 1;
				box[(i/3)*3 + j/3][arr[i][j]] = 1;
			} 
		}
	}
	start(0); //0부터 ~ 81까지 검사시작  
	return 0;
 }
