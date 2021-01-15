#include <iostream>
#include <string>
#include <stack>
using namespace std;
void print(stack<char> &s)
{ // 스택에 있는 값을 모두 출력
    while (!s.empty())
    {
        cout << s.top();
        s.pop();
    }
}
int main()
{
    string str;
    getline(cin, str);
    bool tag = false;
    stack<char> s;
    for (char ch : str)
    { // 문자열에서 한 문자씩 꺼내며 반복
        if (ch == '<')
        {               // 여는 태그가 나오면
            print(s);   // 스택에 값들을 모두 출력하고
            tag = true; // 태그가 열렸다고 표시
            cout << ch; // 태그 출력
        }
        else if (ch == '>')
        {                // 닫는 태그가 나오면
            tag = false; // 태그가 닫혔다고 표시
            cout << ch;  // 태그 출력
        }
        else if (tag)
        {               // 태그가 열린상태라면
            cout << ch; // 문자 '그대로' 출력
        }
        else
        { // 태그가 닫힌상태라면
            if (ch == ' ')
            {               // 공백이 나오면
                print(s);   // 스택을 모두 출력
                cout << ch; // 공백도 출력
            }
            else
            {               // 공백이 나오기 전까지는
                s.push(ch); // 스택에 삽입
            }
        }
    }
    print(s); // 스택에 남은게 있다면 모두 출력
    cout << '\n';
    return 0;
}