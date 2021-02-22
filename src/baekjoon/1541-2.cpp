#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    string fomula;
    // cin >> fomula;

    int a;
    cin >> a;

    bool minus = false;
    int m = 0;
    int result = a;

    char tmp;
    while (true)
    {
        if ((tmp = cin.get()) == '-')
            minus = true;
        else if (tmp != '+')
            break;

        cin >> a;
        if (minus)
            result -= a;

        else
            result += a;
    }

    cout << result;
}