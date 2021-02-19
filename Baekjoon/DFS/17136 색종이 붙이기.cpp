#include <iostream>
#include <algorithm>
#include <vector>
//#include <queue>
using namespace std;

int paper[6]; //1x1~5x5갯수 파악하기 위한 배열
int map[10][10]; //검사해야 하는 10x10배열 

void result(){
	//만약에 함수가 끝나고map에 1이 남았을 경우 -1리턴
	for(int i=0; i<10; i++){
		for(int j=0; j<10; j++){
			if(map[i][j] == 1){
				cout << "-1";
				exit(0);
			}
		}
	} 
	int min=0;
	for(int i=1; i<=5; i++) min += paper[i];
	cout << min;
	exit(0);
}


//해당 x,y좌표와 cnt갯수-> 즉 paper배열의 해당 색종이가 쓰일수있는지 검사하기위한 변수 
void check(int x, int y){
	if(x < 10 && y < 10){
		if(map[x][y] == 0){ //해당 자리가 0이라면 가장 가까운 1로 좌표를 옮김
			while(1){
				if(y < 9){
					y++;
					if(map[x][y] == 1) break;
				}
				else{
					y=0;
					x++;
					if(map[x][y] == 1) break;
				}
			}
			check(x,y);
		}
		else{ //검사
			for(int i=1; i<=5; i++){ //1x1배열부터~ 5x5배열까지 검사 
				if(paper[i]+1 <= 5){ //현재 색종이(ixi크기)를 다쓰지 않았을 경우
					//해당 색종이를 사용 할수 있는지 범위 검사
					if(x + i <= 10 && y + i <= 10){
						int no = -1;
						for(int x_tmp=x; x_tmp < x+i; x_tmp++){
							for(int y_tmp=y; y_tmp < y+i; y_tmp++){
								if(map[x_tmp][y_tmp] != 1){
									no = 1;
									break;
								}
							}
						}
						if(no == -1){
							//위에서 걸리지 않았다면 해당 색종이를 붙일 수 있다는 것 map배열 최신화
							for(int x_tmp=x; x_tmp < x+i; x_tmp++){
								for(int y_tmp=y; y_tmp < y+i; y_tmp++){
									map[x_tmp][y_tmp] = 0;
								}
							}
							paper[i]++; //해당 크기의 색종이 사용했으니 1증가시켜줌
							//다음으로
							if(y < 9){
								check(x, y+1);
							}
							else{
								check(x+1, 0);
							}
							cout <<"two " <<  x << " " << y << "sex\n";
							//위에 과정에서 실패 했을 경우 다시 map, paper배열을 복구 
							for(int x_tmp=x; x_tmp < x_tmp+i; x_tmp++){
								for(int y_tmp=y; y_tmp < y_tmp+i; y_tmp++){
									map[x_tmp][y_tmp] = 1;
								}
							}
							paper[i]--;
						}
					}
				}
				cout << "three " << x << " " << y << "\n";
			}
		}
	}
	else{ //print하러감 
		result();
	}
}

int main(){
	for(int i=0; i<10; i++){
		for(int j=0; j<10; j++) cin >> map[i][j];
	}
	for(int i=1; i<=5; i++) paper[i] = 0;
	check(0, 0); //시작은 0,0
	return 0;
}
