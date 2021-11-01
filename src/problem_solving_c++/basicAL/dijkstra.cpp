//1. a를 선형탐색으로 구현한 경우, O(N)
#include <cstdio>

using namespace std;
int number = 6;
int INF = 1000000;

int a[6][6] = {
    {0, 2, 5, 1, INF, INF},
    {2, 0, 3, 2, INF, INF},
    {5, 3, 0, 3, 1, 5},
    {1, 2, 3, 0, 1, INF},
    {INF, INF, 1, 1, 0, 2},
    {INF, INF, 5, INF, 2, 0},
};

bool v[6]; //방문한 노드 정보

int d[6]; //거리

int getSmallIndex()
{
    int min = INF;
    int index = 0;

    for (int i = 0; i < number; i++)
    {
        if (d[i] < min && !v[i])
        {
            min = d[i];
            index = i;
        }
    }
    return index;
}
void dijkstra(int start)
{
    for (int i = 0; i < number; i++)
    {
        d[i] = a[start][i];
    }
    v[start] = true;

    for (int i = 0; i < number - 2; i++)
    {
        //3. 방문하지 않은 노드 중 가장 비용이 적게 드는 노드 선택
        int select = getSmallIndex();
        v[select] = true;
        //4. 선택한 노드를 거쳐가는 경우를 고려하여 d[] 갱신
        for (int j = 0; j < number; j++)
        {
            if (!v[j])
            {
                if (d[select] + a[select][j] < d[j])
                {
                    d[j] = d[select] + a[select][j];
                }
            }
        }
    }
}

int main()
{
    dijkstra(0);
    for (int i = 0; i < number; i++)
    {
        printf("%d", d[i]);
    }

    return 0;
}