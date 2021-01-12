#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;
int main()
{
    int cases;
    scanf("%d", &cases);
    cin.clear();

    string str;
    for (int i = 1; i <= cases; ++i)
    {
        vector<string> list;
        do
        {

            cin >> str;
            list.push_back(str);
        } while (getchar() != '\n');

        cout << "Case #" << i << ": ";
        for (int i = list.size() - 1; i >= 0; i--)
        {
            cout << list[i];

            if (i != 0)
                cout << ' ';
            else
                cout << '\n';
        }
    }

    cin.clear();
}