#include <iostream>

using namespace std;

int main(void)
{
    char s1[15];

    cin >> s1;
    cout << s1 << endl;
    fgets(s1, 1, stdin);
    cout << s1 << endl;
}