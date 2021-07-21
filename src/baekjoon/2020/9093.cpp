#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    cin.clear();
    cin.ignore();
    while (N > 0)
    {

        char c;
        do
        {
            string substr;
            cin >> substr;
            for (int i = substr.size() - 1; i >= 0; i--)
                cout << substr[i];
            if ((c = cin.get()) != EOF)
                cout << c;
        } while (c != EOF && c != '\n');

        N--;
    }
}
