#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>
int N;

using namespace std;

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    vector<string> word;
    for (int i = 0; i < N; i++)
    {
        string temp;
        cin >> temp;
        reverse(begin(temp), end(temp));
        word.push_back(temp);
    }

    int Alphabet[26];
    memset(Alphabet, 0, sizeof(Alphabet));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 8; j++)
        {

            if (word[i][j] == NULL)
                break;
            Alphabet[word[i][j] - 'A'] += pow(10, j);
        }
    }

    sort(begin(Alphabet), end(Alphabet));

    int result = 0, n = 9;

    for (int i = 25; i >= 0; i--)
    {
        if (Alphabet[i] == 0)
            break;
        result += (n--) * Alphabet[i];
    }
    cout << result;
}