
// 2251 물통 (틀림)
// https://www.acmicpc.net/problem/2251
// BFS문제인데 DFS로 하고 있었음...
//(정확히는 DFS로 풀수 있다는데 비효율적이래,시간초과 나려나?)
//나중에 BFS 공부할때 다시 풀겠음

#include <cassert>
#include <cstring>
#include <iostream>
using namespace std;

// 물병의 용량
int size[3];
//물의 양
int water[3];
bool amountOfC[201] = {};
int visited[3][3] = {};

int waterlog[3];

void init() {
  //물병 C만 꽉 차있다.
  water[0] = water[1] = 0;
  water[2] = size[2];

  memset(visited, 0, sizeof(visited));
}

void rollback() {
  water[0] = waterlog[0];
  water[1] = waterlog[1];
  water[2] = waterlog[2];
}

void pourWater(int from, int to) {
  waterlog[0] = water[0];
  waterlog[1] = water[1];
  waterlog[2] = water[2];

  int availableSpace = size[to] - water[to];

  if (water[from] > availableSpace) //물이 남은 공간보다 더 많으면
  {
    water[from] -= availableSpace;
    water[to] += availableSpace; //병을 가득 채움
  } else {                       //병의 물이 더 적으면
    water[to] += water[from];
    water[from] = 0; //다 따름
  }
}

void DFS() {
  if (water[0] == 0) { //첫 번째 물통(용량이 A인)이 비어 있을 때,
    amountOfC[water[2]] = true;
    return;
  }

  for (int from = 0; from <= 2; from++)
    for (int to = 0; to <= 2; to++) {
      if (visited[from][to])
        continue;

      int availableSpace = size[to] - water[to];

      if (water[from] > 0 && availableSpace > 0) {
        visited[from][to] = true;
        pourWater(from, to);
        DFS();
        visited[from][to] = false;
        rollback();
      }
    }
}

int main() {
  cin >> size[0] >> size[1] >> size[2];

  int from = 2;
  for (int to = 0; to <= 1; to++) {
    init();
    visited[from][to] = true;
    pourWater(from, to);
    DFS(); // 2의 물을 i에 따르면서 시작
  }

  for (int i = 1; i < 201; i++)
    if (amountOfC[i] == true)
      cout << i << " ";

  return 0;
}