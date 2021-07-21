// 조건
// 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
// 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
// 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    string str;
    cin >> str;
    int total = 0;
    int count = 0;
    int end = 0;
    for (int i = 0; i < str.size(); i++)
    {
        if (str[i] == '(')
        {
            if (str[i + 1] == ')')
            {
                total += count;
                count -= end;
                end = 0;
                i++;
            }
            else
                count++;
        }
        else
            end++;
    }

    total += count;
    cout << total;
}