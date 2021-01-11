#include <bits/stdc++.h>
using namespace std;
int main()
{

    int T; // 테스트 케이스의 수
    scanf("%d", &T);
    int N; // 지원자의 숫자
    vector<vector<int>> score;
    while (T--)
    {
        score.clear();
        scanf("%d", &N);
        int temp;
        for (int j = 0; j < N; j++)
        {
            vector<int> v;
            scanf("%d", &temp);
            v.push_back(temp);
            scanf("%d", &temp);
            v.push_back(temp);
            score.push_back(v);
        }

        sort(score.begin(), score.end());

        int result = 0;
        int rank = 9999999;

        for (int i = 0; i < N; i++)
        {

            if (score[i][1] < rank)
            {
                rank = score[i][1];
                result++;
            }
        }

        printf("%d\n", result);
    }

    cin.ignore();
}
