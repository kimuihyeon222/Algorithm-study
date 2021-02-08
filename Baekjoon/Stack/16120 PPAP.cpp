#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void) {
    string ppap;
    cin >> ppap;
    stack<char> check;
    int p_cnt=0; //p의 갯수를 세는 변수
    int a_cnt=0;
    char t1,t2;
    for(int i=0; i<ppap.length(); i++){
        check.push(ppap[i]);
        if(ppap[i] == 'P'){
            if(a_cnt == 1){
                if(p_cnt >= 2){ //현재 p가 2개 이상일 경우 ppap가 될수도있으니 검사
                    //ppap를 만족하는지 검사
                    t1 = check.top(); //P 
                    check.pop(); 
                    t2 = check.top(); //A
                    if(t2 != 'A'){ // P이전에 A가 존재하지 않으면 PPAP가 성립하지 않는다 (ex. papp이럴 경우 무시하고 p를 스택에 그대로 쌓음)
                        p_cnt++;
                        check.push(t1);
                    }
                    else{
                        check.pop(); //A
                        check.pop(); //P
                        //3개만 pop하면됨 왜냐 ppap -> pap 만 스택에서 빼면 되기때문에
                        p_cnt--;
                        a_cnt--;   
                    }
                }
                else p_cnt++;
            }
            else p_cnt++;
        }
        else a_cnt++;
    }

    if(check.top() == 'P' && check.size() == 1){
        cout << "PPAP";
    }
    else cout << "NP";
    return 0;
}
