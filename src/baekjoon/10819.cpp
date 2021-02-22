#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    int A[8] = {0};

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &A[i]);

    sort(A, A + n);

    int max = -987654321;
    do
    {

        int result = 0;
        for (int i = 0; i < n - 1; i++)
        {
            result += abs(A[i] - A[i + 1]);
        }

        if (result > max)
            max = result;
    } while (next_permutation(A, A + n));
    cout << max;
}