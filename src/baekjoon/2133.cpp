#include <iostream>

#define MAXSIZE 31
#define EMPTY 0
using namespace std;

int N;
int W[MAXSIZE][3];
int count = 0;

void attacheTile(int y)
{
    bool isAttachAll = true;
    int i, j;

    for (i = y; i < N; i++)
    {
        for (j = 0; j < 3; j++)
            if (W[i][j] == EMPTY)
            {
                isAttachAll = false;
                break;
            }
        if (isAttachAll == false)
            break;
    }

    if (isAttachAll)
    {
        count++;
        return;
    }

    //세로로 공간 있음
    if (j < 2)
        if (W[i][j + 1] == false)
        {
            W[i][j] = W[i][j + 1] = 2;
            attacheTile(i);
            W[i][j] = W[i][j + 1] = EMPTY;
        }
    //가로로 공간 있음
    if (i < N - 1)
        if (W[i + 1][j] == EMPTY)
        {
            W[i][j] = W[i + 1][j] = 1;
            attacheTile(i);
            W[i][j] = W[i + 1][j] = EMPTY;
        }

    return;
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;

    if (N % 2)
        cout << 0;

    attacheTile(0);
    cout << count;
}