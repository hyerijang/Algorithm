#include <iostream>
#include <string>
#include <vector>

using namespace std;

void DFS(int cur, vector<vector<int>> &computers, vector<int> &visited) {
  for (int i = 0; i < computers.size(); i++) {
    if (visited[i] == 0)          // 미방문이고
      if (computers[cur][i] == 1) //연결되어 있으면
      {
        visited[i] = 1;
        DFS(i, computers, visited);
      }
  }
}

int solution(int n, vector<vector<int>> computers) {
  int answer = 0;

  vector<int> visited(n, 0);

  for (int i = 0; i < n; i++) {
    if (visited[i] != 1) {
      DFS(i, computers, visited);
      answer++;
    }
  }

  return answer;
}

int main() {

  // int arr[3][3] = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
  int arr[3][3] = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};
  vector<vector<int>> computers;

  // for (int i = 0; i < 3; i++) {
  //   vector<int> v;
  //   for (int j = 0; j < 3; j++) {
  //     v.push_back(arr[i][j]);
  //   }
  //   computers.push_back(v);
  // }

  for (int i = 0; i < 3; i++) {
    vector<int> v(begin(arr[i]), end(arr[i]));
    computers.push_back(v);
  }

  int n = 3;
  cout << solution(n, computers) << endl;
}