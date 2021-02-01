#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int k, n;
	cin >> k >> n;
	if(k <= n){
		int len[10001]={0,};
		long long total=0; //랜선의 전체 길이 저장 변수 
		for(int i=1; i<=k; i++){
			cin >> len[i];
			total += len[i];
		}
		total /= n; //전체 길이에 필요한 랜선 갯수를 나눠줌 -> 1~total사이의 값이 정답이됨
		long long lt=1, rt=total, mid, cnt, len_len=-1;
		//검사 시작 
		while(lt <= rt){
			cnt = 0;
			mid = (lt + rt) / 2;
			for(int i=1; i<=k; i++){	
				cnt += (len[i] / mid);
			}
			if(cnt >= n){ //현재 값으로 len을 잘라냈을때 필요한 갯수보다 많이 나오게된다면 
				//len길이 보다 현재 구한 len길이 가 더 클경우 바꿔줌
				if(len_len <= mid) len_len = mid; 
				//최소인 부분을 늘려줌 -> 더 큰 값이 존재하는지 다시 검사 
				lt = mid+1;
			}
			else{
				rt = mid-1;
			}
		}
		cout << len_len;
	}
	return 0;
 }
