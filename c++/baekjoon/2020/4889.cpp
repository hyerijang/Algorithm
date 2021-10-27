#include <iostream>

using namespace std;

int main()
{

    int cases = 0;
    while (++cases)
    {
        string str;
        cin >> str;

        //문장의 첫 시작이 '-'이면 종료
        if (str[0] != '{' && str[0] != '}')
            break;

        //연산: 여는 괄호를 닫는 괄호로 바꾸거나, 닫는 괄호를 여는 괄호로 바꾸는 것
        int changeCount = 0;
        int openBracket = 0;
        for (int i = 0; i < str.size(); i++)
        {
            if (str[i] == '{')
                openBracket++;

            else if (str[i] == '}') //닫는 괄호 만남
            {
                //정상적인 경우 : 이전에 여는 괄호 있었음
                if (openBracket > 0)
                    openBracket--;
                //여는 괄호로 변경해야 하는 경우
                else
                {
                    str[i] = '{';
                    openBracket++;
                    changeCount++;
                }
            }
        }
        cout << cases << ". " << changeCount + (openBracket) / 2 << '\n';
    }
}
