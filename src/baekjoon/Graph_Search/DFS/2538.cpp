#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define NO 0
#define CANGO 1

int M, N, K;

int numOfV = 0;
int count = 0;

int dx[] = {0, 1, 0, -1}; // 12시부터 시계방향
int dy[] = {-1, 0, 1, 0};

int maze[101][101] = {};

int DFS(int y, int x) {

  bool isEND = true;
  int area = 1;

  //상하좌우 검사
  for (int i = 0; i < 4; i++) {
    int nextY = y + dy[i];
    int nextX = x + dx[i];
    if (0 <= nextY && 0 <= nextX)
      if (maze[nextY][nextX] == CANGO) {
        isEND = false; //더 볼 곳 남아있음
        maze[nextY][nextX] = NO;
        area += DFS(nextY, nextX);
      }
  }

  //상하좌우 모두 갈 곳 없으면
  if (isEND)
    return 1;

  return area;
}

int main() {

  // M: 세로길이
  cin >> M >> N >> K;

  for (int y = 0; y < M; y++) {
    for (int x = 0; x < N; x++) {
      maze[y][x] = CANGO;
    }
  }

  //입력
  for (int i = 0; i < K; i++) {
    int ax, ay, bx, by;
    cin >> ax >> ay >> bx >> by;

    for (int y = ay; y < by; y++) {
      for (int x = ax; x < bx; x++) {
        maze[y][x] = NO;
      }
    }
  }

  // allDFS
  // 1번 정점을 시작으로 numOfV번 노드를 끝으로 하는 경로 중 가장 짧은 경로
  // 찾기

  vector<int> areas;
  //항상 도착 위치로 이동할 수 있는 경우만 입력으로 주어짐
  for (int y = 0; y < M; y++) {
    for (int x = 0; x < N; x++) {
      if (maze[y][x] == CANGO) {
        maze[y][x] = NO;
        areas.push_back(DFS(y, x));
      }
    }
  }

  sort(areas.begin(), areas.end());
  cout << areas.size() << endl;
  for (auto v : areas)
    cout << v << " ";

  return 0;
}
