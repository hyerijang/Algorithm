//다시 풀기
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(int argc, const char **argv)
{
    int N = 7;
    vector<int> a = {3, 1, 6, 2, 7, 30, 1};

    sort(a.begin(), a.end());

    int sum = 1;

    for (int i = 0; i < N; i++)
    {
        if (sum < a[i])
            break;
        sum += a[i];
    }

    return 0;
}