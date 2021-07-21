#include <iostream>

using namespace std;

#define CANTMOVE 1

int N, y = 0; //세로축
int M, x = 0; // 가로축
int visitedTile = 1;

void move(int type)
{

    if (y > N || x > M)
        return;

    switch (type)
    {
    case 1: //x+1 y+2
        x++;
        y++;
        y++;

        break;
    case 2: //x+2 y+1
        x++;
        x++;
        y++;

        break;
    case 3: //x+2 y-1
        x++;
        x++;
        y--;
        break;

    case 4: //x+1 y-2
        x++;
        y--;
        y--;
        break;
    }

    visitedTile++;
}

int getResult(const int N, const int M)
{

    if (min(N, M) < 2 || max(N, M) < 3)
        return CANTMOVE;

    //이동횟수 5회 미만
    if (min(N, M) == 2 && max(N, M) < 9 || min(N, M) != 2 && max(N, M) < 5)
        return max(N, M) / 2 + max(N, M) % 2;

    //4가지 이동 방법 모두 사용해야함
    bool usedAllType = false;
    while (y < N && x < M)
    {
        if (max(N, M) == N) //세로가 더 긴 경우
        {
            if (!usedAllType)
            {
                move(1);
                move(4);
                move(2);
                move(3);
                usedAllType = true;
            }
            move(1);
            move(4);
        }
        if (max(N, M) == M) //가로가 더 긴 경우
        {
            if (!usedAllType)
            {
                move(2);
                move(3);
                move(1);
                move(4);
                usedAllType = true;
            }
            if (N == 2)
            {
                move(2);
                move(3);
            }
            else
            {
                move(1);
                move(4);
            }
        }
    }

    //범위 벗어난 타일 하나 삭제
    visitedTile--;

    return visitedTile;
}
int main()
{

    cin >> N >> M;

    cout << getResult(N, M);
}