#include <iostream>
#include <vector>

using namespace std;

int d[11];
int main()
{
    int n;

    cin >> n;
    int left;
    for (int i = 1; i <= n; i++)
    {
        cin >> left;
        for (int j = 1; j <= n; j++)
        {

            if (left == 0 & d[j] == 0)
            {
                d[j] = i;
                break;
            }
            else if (d[j] == 0)
            {
                left--;
            }
        }
    }

    //출력
    for (int i = 1; i <= n; i++)
    {
        printf("%d ", d[i]);
    }
    return 0;
}