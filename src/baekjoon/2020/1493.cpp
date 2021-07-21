#include <iostream>

using namespace std;

int main()
{
    string s;
    cin >> s;

    char prevData = s[0];
    int numOfBundle = 1;

    for (int i = 0; i < s.size(); i++)
        if (prevData != s[i])
        {
            prevData = s[i];
            numOfBundle++;
        }

    cout << numOfBundle / 2;
}