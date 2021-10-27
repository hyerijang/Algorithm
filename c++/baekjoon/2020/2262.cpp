#include <iostream>
#include <vector>

using namespace std;

#define RANK 0
#define LENGTH 1

//player[x][RANK]은 해당 플래이어의 랭킹
//player[x][LENGTH]은 오른쪽 멤버와의 랭킹 차이
vector<vector<int>> player;
int main()
{

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        vector<int> temp;
        temp.resize(2);
        player.push_back(temp);
    }

    int rank;
    int min = 987654321;
    int minIndex;
    for (int i = 0; i < N; i++)
    {
        cin >> rank;
        player[i][RANK] = player[i][LENGTH] = rank;
        if (i != 0)
        {
            int *prevDiff = &player[i - 1][LENGTH];
            *prevDiff -= rank;
            *prevDiff = abs(*prevDiff);
            if (*prevDiff < min)
            {
                min = *prevDiff;
                minIndex = i - 1;
            }
        }
    }
    player[N - 1][LENGTH] = 987654321;

    int result = 0;
    while (N > 1)
    {

        int loseIndex; //탈락자
        //인접한 두 플레이어의 랭킹 비교
        if (player[minIndex][RANK] > player[minIndex + 1][RANK])
            loseIndex = minIndex;
        else
            loseIndex = minIndex + 1;

        player.erase(player.begin() + loseIndex);

        //탈락 후 양 옆 플레이어의 변동사항 반영
        //오른쪽 끝이 탈락한 경우
        if (loseIndex == N - 1)
            player[loseIndex - 1][LENGTH] = 987654321;

        //중간에서 빠진 경우
        else if (loseIndex != 0)
            player[loseIndex - 1][LENGTH] = abs(player[loseIndex - 1][RANK] - player[loseIndex][RANK]);

        result += min;
        min = 987654321;
        for (int i = 0; i < N - 1; i++)
            if (player[i][LENGTH] < min)
            {
                min = player[i][LENGTH];
                minIndex = i;
            }
        N--;
    }
    cout << result;
}