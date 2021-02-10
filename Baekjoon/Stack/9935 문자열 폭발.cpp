#include <iostream>
#include <algorithm>
//#include <vector>
#include <stack>
#include <queue>
//#include <cmath>
using namespace std;
--------------------------------------------------------------------------------------------------
//방법 1. 실패
//해당 문제는 시간 제한 2초
// find, substr이런 함수들의 시간복잡도도 생각해야함
int main() {
	string input, boom, tmp;
	cin >> input >> boom;
	 
	for(int i=0; input[i] != '\0'; i++){ //문자열을 하나씩 검사 
		tmp += input[i]; //string에 연결시켜주고
		//폭발 문자열이 있는지 확인
		if(tmp.find(boom) != string::npos){ //해당 문자열이 존재할 경우 
			tmp = tmp.substr(0, tmp.length()-boom.length()); //boom을 제외한 나머지로 substring을 만들어줌 
		} 
	}
	if(tmp.empty()){
		cout << "FRULA";
	}
	else cout << tmp;
	return 0;
 }
 --------------------------------------------------------------------------------------------------
 
--------------------------------------------------------------------------------------------------
//방법2. 성공
//rope 자료구조 사용 -> 긴문자열 처리에 대해 longN의 시간복잡도로 해결할수 있게하는 자료구조
// c_str()은 string을 char *으로 변화해주어 strcmp() substr이런것들을 가능하게 해줌
#include <ext/rope>
using namespace __gnu_cxx; //rope사용 하기위해 선언 
int main(){
	string input, boom;
	crope tmp;
	cin >> input >> boom; 
	tmp.append(input.c_str()); //tmp에 input을 저장
	int n = input.size();
	
	for(int i=0; i<n; i++){ //문자열을 해당 위치부터 boom이 있는지 검사 
		if(tmp.substr(i, boom.length()).c_str() == boom){
			tmp.erase(i, boom.length());
			i -= boom.length(); 
		}
	}
	if(tmp.empty()){
		cout << "FRULA";
	}
	else cout << tmp;
	return 0;
}
--------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------
/방법3. 성공
//검사를 뒤에서부터함
//stack, queue이용 
int main(){
	string input, boom;
	cin >> input >> boom;
	stack<char> result; //최종 결과
	
	for(int i=input.size()-1; i>=0; i--){ //문자열을 하나씩 검사 뒤에서 -> 앞으로 
		result.push(input[i]);
		//result스택의 윗부분이 boom의 첫시작과 같으면서 사이즈가 클 경우 폭발 문자열인지 검사 
		if(result.top() == boom[0] && result.size() >= boom.size()){
			int check; //해당 문자열이 전부 맞는지 검사
			for(check=0; check<boom.size(); check++){
				if(result.top() == boom[check]){
					result.pop();
				}
				else { //폭발 문자열이 아니였다면 다시 stack에 쌓음
					for(int j=check-1; j>=0; j--) result.push(boom[j]);
					break;
				}
			} 
		}
	}
	if(result.empty()){
		cout << "FRULA";
	}
	else {
		while(!result.empty()){
			cout << result.top();
			result.pop();
		}
	}
	return 0;
}
--------------------------------------------------------------------------------------------------
