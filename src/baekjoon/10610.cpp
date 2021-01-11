//1. 0으로 나눌 수 있는 수인지 확인
//2. 나머지 숫자로 3의 배수를 만들 수 있는지 확인
// 3의 배수  ?  각 자리의 숫자를 전부 더했을 때  그 수가 3의 배수이다.
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{

    string s;
    cin >> s;

    //sort(v.begin(), v.end(), greater<자료형>());    //내림차순 (Descending order)
    //sort(v.begin(), v.end(), less<자료형>());        //오름차순 (default = Ascending order)

    sort(s.begin(), s.end(), greater<char>());

    bool isZero = false;
    int temp = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '0')
        {
            isZero = true;
            continue;
        }

        temp += (s[i] - '0');
    }

    if (temp % 3 == 0 && isZero)
    {
        cout << s;
    }
    else
        cout << -1;

    return 0;
}