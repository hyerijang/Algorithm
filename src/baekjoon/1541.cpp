#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    string a;
    cin >> a;
    bool minus = false;
    string temp = "";
    int result = 0;
    for (int i = 0; i <= a.size(); i++)
    {
        if (a[i] == '+' || a[i] == '-' || a[i] == '\0')
        {
            if (minus == true)
                result += -stoi(temp);
            else
                result += stoi(temp);
            temp = "";
            if (a[i] == '-')
                minus = true;
            continue;
        }
        temp += a[i];
    }
    cout << result;
}