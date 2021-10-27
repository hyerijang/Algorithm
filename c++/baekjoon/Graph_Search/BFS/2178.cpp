// 2178 미로찾기. (틀림)
// 최단 경로 구하는 건데 DFS로 풀면 시간초과로 틀린다. ^^...

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
int N, M;

int numOfV = 0;
int answer = 987654321;

int dx[] = {0, 1, 0, -1}; // 12시부터 시계방향
int dy[] = {-1, 0, 1, 0};

vector<bool> visited;

void DFS(int y, int x, int length, vector<vector<int>> &maze) {

  //갈 수 없는 경로
  if (maze[y][x] == 0)
    return;

  if (length > answer)
    return;

  if (maze[y][x] == numOfV) {
    answer = min(answer, length);
    return;
  }

  //상하좌우 검사
  for (int i = 0; i < 4; i++) {
    int next = maze[y + dy[i]][x + dx[i]];
    if (next > 0)
      if (!visited[next]) {
        visited[next] = true;
        DFS(y + dy[i], x + dx[i], length + 1, maze);
        visited[next] = false;
      }
  }
}

int main() {

  cin >> N >> M;

  //미로 초기화
  vector<vector<int>> maze;
  for (int i = 0; i <= N + 1; i++) {
    vector<int> v(M + 2, 0);
    maze.push_back(v);
  }

  //   for (int y = 1; y <= N; y++) {
  //     string str;
  //     cin >> str;
  //     for (int x = 0; x < str.size(); x++) {
  //       if (str[x] == '1') {
  //         maze[y][x + 1] = ++numOfV; //색칠되어있는 칸에 번호 부여
  //       }
  //     }
  //   }

  //입력
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= M; j++) {
      int tmp = 0;
      scanf("%1d", &tmp);
      if (tmp == 1)
        maze[i][j] = ++numOfV; //색칠되어있는 칸에 번호 부여
    }
  }

  visited.resize(numOfV + 1);
  visited[1] = true;

  // allDFS
  // 1번 정점을 시작으로 numOfV번 노드를 끝으로 하는 경로 중 가장 짧은 경로 찾기

  //항상 도착 위치로 이동할 수 있는 경우만 입력으로 주어짐
  DFS(1, 1, 1, maze);

  cout << answer << endl;
  return 0;
}
