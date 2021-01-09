//다시 풀어 볼것

#include <iostream>
#include <vector>

using namespace std;

int d[11];
int main()
{
    int n;

    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        //i번째 사람의 왼쪽에 그보다 큰 사람이 x명 있었다.
        int x;
        cin >> x;

        int count = 0;
        //j는 순서
        for (int j = 1; j <= n; j++)
        {
            if (count == x && d[j] == 0)
            {
                d[j] = i;
                break;
            }
            if (d[j] == 0)
                count++;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        printf("%d ", d[i]);
    }
    return 0;
}