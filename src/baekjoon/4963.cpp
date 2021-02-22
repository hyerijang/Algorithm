#include <iostream>
#include <vector>

using namespace std;

int w, h;
vector<vector<int>> map;
vector<vector<int>> visited;

void initMapAndVisited()
{
    map.clear();
    visited.clear();
    for (int i = 0; i < h; i++)
    {
        vector<int> tmp_map(w, 0);
        for (int j = 0; j < w; j++)
            cin >> tmp_map[j];
        map.push_back(tmp_map);

        vector<int> tmp_visited(w, 0);
        visited.push_back(tmp_visited);
    }
}

int land = 0;
int check(int y, int x)
{

    //map을 벗어난 경우
    if (y < 0 || x < 0 || y >= h || x >= w)
        return 0;

    // 방문하지 않은 섬을 찾았으면
    if (visited[y][x] == 0 && map[y][x] == 1)
    {
        land++;
        visited[y][x] = 1; //방문했다고 표시

        //주변 노드 8개  검사
        land -= check(y - 1, x - 1);
        land -= check(y - 1, x);
        land -= check(y - 1, x + 1);
        land -= check(y, x - 1);
        land -= check(y, x + 1);
        land -= check(y + 1, x - 1);
        land -= check(y + 1, x);
        land -= check(y + 1, x + 1);

        return 1;
    }

    //바다인 경우
    visited[y][x] = 1; //방문했다고 표시
    return 0;
}

void getland()
{

    land = 0;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            check(i, j);
        }
    }
}

int main()
{

    while (true)
    {

        cin >> w >> h;

        //입력 종료
        if (w == 0 || h == 0)
            break;

        //map, visited 초기화
        initMapAndVisited();

        getland();
        cout << land << '\n';
    }
}