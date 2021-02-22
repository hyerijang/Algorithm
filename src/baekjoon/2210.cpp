#include <iostream>
#include <vector>
using namespace std;

char board[5][5];
int directon[4][2] = {{+1, +1}, {+1, -1}, {-1, -1}, {-1, +1}};
string tmp = "";
vector<string> list[10];
int count = 0;

int move(int d, int y, int x)
{
    if (tmp.size() == 6)
    {
        bool exist = false;
        int first = tmp[0] - '0';
        for (int i = 0; i < list[first].size(); i++)
            if (tmp == list[first][i])
                exist = true;
        if (!exist)
        {
            list[first].push_back(tmp);
            count++;
        }
        return false;
    }

    int newY = y + directon[d][0];
    int newX = x + directon[d][1];

    if (newY > 4 || newX > 4 || newY < 0 || newX < 0)
        return false;

    //한글자 추가
    tmp += board[newY][newX];
    for (int d = 0; d < 4; d++)
    {
        //한글자 삭제
        if (move(d, newY, newX))
            tmp.pop_back();
    }
    return true;
}

int initStart()
{
    //시작지점 board[i][j]
    for (int y = 0; y < 5; y++)
        for (int x = 0; x < 5; x++)
        {
            for (int d = 0; d < 4; d++)
            {
                move(d, y, x);
                tmp = "";
            }
        }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            cin >> board[i][j];

    initStart();

    cout << count;
}