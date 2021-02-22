#include <iostream>
#include <vector>
using namespace std;

#define YES "YES"
#define NO "NO"

int N;
bool OK = true;
int sum, sum_2;
vector<int> h;

bool water()
{
    //조건1) 합이 3의 배수가 아니면 불가
    if (sum % 3)
        return false;
    //h중에서 max에서 -2, min에서 -1

    if (sum_2 < sum / 3)
        return false;
    return true;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    h.resize(N);

    sum = sum_2 = 0;
    int i = 0;
    while (i < N)
    {
        cin >> h[i];
        sum += h[i];
        sum_2 += h[i] / 2;
        i++;
    }

    OK = water();

    if (!OK)
        cout << NO;
    else
        cout << YES;
}