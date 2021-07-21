#include <iostream>

using namespace std;

int anwser(int n)
{

    if (n < 100)
        return n;

    int count = 99;

    int o, t, h;

    for (int i = 100; i <= n; i++)
    {
        o = i % 10;
        t = (i % 100) / 10;
        h = i / 100;

        if (h - t == t - o)
            count++;
    }

    return count;
}
int main()
{
    int n;
    cin >> n;
    cout << anwser(n);
}