#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<pair<int, int>> tag;
    string str;
    getline(cin, str);

    int i = 0;
    int opentag = str.size(), endtag = 0;

    while (i < str.size())
    {
        if (str[i] == '<')
            opentag = i;
        i++;
    }

    for (i = opentag - 1; i > 0; i--)
        cout << str[i];

    i = opentag;
    while (i < str.size())
    {

        if (str[i] == '<')
        {
            opentag = i;
            do
            {
                cout << str[i++];
            } while (str[i] != '>');
            endtag = i;
            cout << str[i];
        }

        i++;
    }

    return 0;
}
