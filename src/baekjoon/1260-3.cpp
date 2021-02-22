#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, V;
vector<vector<int>> list;
vector<bool> visited;

void DFS(int v)
{
    if (visited[v])
        return;
    else
    {
        cout << v << ' ';
        visited[v] = true; // 방문 체크

        for (int i = 0; i < list[v].size(); i++)
        {
            int next = list[v][i];
            DFS(next);
        }
        return;
    }
}

vector<int> q;

void BFS(int v)
{
    vector<int> queue;
    queue.push_back(v);
    visited[v] = true;

    while (!queue.empty())
    {
        v = queue[0];
        queue.erase(queue.begin());
        cout << v << ' ';

        int next;
        for (int i = 0; i < list[v].size(); i++)
        {
            next = list[v][i];
            if (visited[next] == false)
            {
                queue.push_back(next);
                visited[next] = true;
            }
        }
    }
}

void initList()
{ // 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
    // 간선의 개수 M(1 ≤ M ≤ 10,000),
    // 탐색을 시작할 정점의 번호 V가 주어진다.
    cin >> N >> M >> V;
    for (int i = 0; i <= N; i++)
    {
        vector<int> sublist;
        list.push_back(sublist);
    }

    // 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
    // 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
    for (int i = 0; i < M; i++)
    {
        int A, B;
        cin >> A >> B;
        // 입력으로 주어지는 간선은 양방향이다.
        list[A].push_back(B);
        list[B].push_back(A);
    }

    //방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
    for (int i = 0; i <= N; i++)
    {
        sort(list[i].begin(), list[i].end());
    }
}
void initVisited()
{
    visited.resize(N + 1);
    visited.assign(N + 1, false);
}

int main()
{

    initList();
    initVisited();
    DFS(V);
    cout << '\n';

    initVisited();
    BFS(V);
    cout << '\n';

    return 0;
}