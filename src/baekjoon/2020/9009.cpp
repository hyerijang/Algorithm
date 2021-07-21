#include <iostream>
#include <vector>
using namespace std;

int f[46];

void solve(int N)
{

    vector<int> result;
    int fmax = 45;
    while (N > 0 && fmax > 0)
    {
        if (f[fmax] <= N)
        {
            result.push_back(f[fmax]);
            N -= f[fmax];
        }
        fmax--;
    }

    int i = result.size() - 1;
    while (i >= 0)
        cout << result[i--] << ' ';
}
void fibonacci(int N)
{

    if (N > 1000000000)
        return;

    for (int i = 2; i < 46; i++)
    {
        f[i] = f[i - 1] + f[i - 2];
    }
}
int main()
{

    f[0] = 0;
    f[1] = 1;

    int T, N;
    fibonacci(46);

    cin >> T;
    while (T--)
    {
        cin >> N;
        solve(N);
        cout << '\n';
    }

    return 0;
}