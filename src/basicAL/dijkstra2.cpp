//2. a를 선형탐색으로 구현한 경우, O(N)
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
int number = 6;
int INF = 1000000;

vector<pair<int, int>> a[7];

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

    d[start] = 0;
    priority_queue<pair<int, int>> pq; //힙
    pq.push(make_pair(start, 0));

    while (!pq.empty())
    {
        int current = pq.top().first;
        //짧은 것이 넘저 오도로 음수화(-)
        int distance = -pq.top().second;
        pq.pop();

        //최단거리가 아닌경우 스킵
        if (d[current] < distance)
            continue;

        //4. 선택한 노드를 거쳐가는 경우를 고려하여 d[] 갱신
        for (int i = 0; i < a[current].size(); i++)
        {
            int next = a[current][i].first;
            int nextDistance = distance + a[current][i].second;

            if (nextDistance < d[next])
            {
                d[next] = nextDistance;
                pq.push(make_pair(next, -nextDistance));
            }
        }
    }
}

int main()
{

    for (int i = 1; i < number; i++)
    {
        d[i] = INF;
    }

    a[1].push_back(make_pair(2, 2));
    a[1].push_back(make_pair(3, 5));
    a[1].push_back(make_pair(4, 1));

    a[2].push_back(make_pair(1, 2));
    a[2].push_back(make_pair(3, 3));
    a[2].push_back(make_pair(4, 2));

    a[3].push_back(make_pair(1, 5));
    a[3].push_back(make_pair(2, 3));
    a[3].push_back(make_pair(4, 3));
    a[3].push_back(make_pair(5, 1));
    a[3].push_back(make_pair(6, 5));

    a[4].push_back(make_pair(1, 1));
    a[4].push_back(make_pair(2, 2));
    a[4].push_back(make_pair(3, 3));
    a[4].push_back(make_pair(5, 1));

    a[5].push_back(make_pair(3, 1));
    a[5].push_back(make_pair(4, 1));
    a[5].push_back(make_pair(6, 2));

    a[6].push_back(make_pair(3, 5));
    a[6].push_back(make_pair(5, 2));

    dijkstra(1);

    for (int i = 1; i < number; i++)
    {
        printf("%d", d[i]);
    }

    return 0;
}