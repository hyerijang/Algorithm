#include <stdio.h>
#include <limits.h>
#include <algorithm>
using namespace std;

int n, all;
int cost[16][16];
int dp[16][1 << 16];

int func(int cur, int stat)
{
    //1. 종료조건 : 모든 도시 방문한 경우
    if (stat == all)
    {
        //도시 cur에서 도시 0으로 갈 수 없는 경우
        if (cost[cur][0] == 0)
            return 987654321;
        else
            return cost[cur][0];
    }

    //2. 아직 종료할 때가 아닌 경우 이어서 계산
    int &ref = dp[cur][stat];
    //2.1 이전에 저장된 기록 있으면 그거 사용
    if (ref != 0)
        return ref;

    //2.2 저장된 기록 없으면 계산
    int m = INT_MAX - 16000001;
    //1번 도시부터 n-1번 도시까지 순회, 그 중 최소 비용을 m에 저장
    for (int i = 1; i < n; ++i)
    {
        //방문한 도시가 아니고 cur에서 i까지 가는 길이 있으면 m을 구한다.
        if (((stat & (1 << i)) == 0) && (cost[cur][i] != 0))
            m = min(m, cost[cur][i] + func(i, (stat | (1 << i))));
        //1 << i : i번 비트에 1을 표시
        //cost[cur][i] : cur에서 i까지 가는 최소 비용
        //func(i, (stat | (1 << i))) : i에서 stat-{0,i}를 거쳐 0까지 가는데 드는 최소 비용
        //cur에서 i까지 + i에서 0까지
    }

    //최소비용을 ref에 저장
    return ref = m;
}

int main()
{
    scanf("%d", &n);
    all = (1 << n) - 1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            scanf("%d", &cost[i][j]);

    printf("%d", func(0, 1));
    return 0;
}