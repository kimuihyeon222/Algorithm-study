#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int m, n;
	cin >> m >> n;
	
	vector<int> arr(2*m-1, 1); //맨 왼쪽, 맨 윗줄의 칸만큼 배열하나 생성
	
	int zero, one, two;
	for(int i=0; i<n; i++){
		cin >> zero >> one >> two;
		//0은 재끼고 1부터 넣음
		for(int j=0; j<one; j++){
			arr[zero+j] += 1;
		}
		//2넣음
		for(int j=0; j<two; j++){
			arr[zero+one+j] += 2;
		} 
	}
	
	//맨 윗줄 출력
	int k;
	for(k=m-1; k<2*m-1; k++){
		cout << arr[k] << " ";
	}
	cout << "\n";  
	int tmp_max;
	k = m-2; //두번째의 첫번째 값을 가르킴 
	int tmp_k = m-2; //위치를 따로 저장해둠 k는 검사할때 바뀌기 때문에

	for(int i=1; i<m; i++){
		cout << arr[tmp_k--] << " ";
		for(int j=1; j<m; j++){ //2번째 줄 나머지 값 구하기 m-1번 돌아야함 
			tmp_max = max(arr[k], max(arr[k+1], arr[k+2])); //왼, 왼위, 위 큰 값을 구해서
			cout << tmp_max << " "; //출력해주고
			arr[k+1] = tmp_max; //다음 값 검사를위해 초기화 시켜줌
			k++; 
		}
		k = tmp_k; // 한줄의 검사가 끝나면 그 밑의 줄을 가르키는 tmp_k로 k를 바꿔줌 
		cout << "\n";
	}
	return 0;
 }
