#include <string>
#include <vector>

using namespace std;

#define HOME 1
#define WATER 0

bool isPuddles(int x, int y, vector<vector<int>> &puddles) {

  for (auto p : puddles) {
    if (p[0] == x && p[1] == y)
      return true;
  }

  return false;
}
int solution(int m, int n, vector<vector<int>> puddles) {
  int arr[101][101] = {};
  arr[1][1] = HOME;

  for (int x = 1; x <= m; x++) {
    for (int y = 1; y <= n; y++) {
      if (isPuddles(x, y, puddles)) { // 웅덩이가 있으면 0
        arr[x][y] = WATER;
        continue;
      }
      if (x >= 1) {                 // 접하는 위쪽 구간이 있으면
        arr[x][y] += arr[x - 1][y]; // 위에서 온 수 더하기
        arr[x][y] %= 1000000007;
      }
      if (y >= 1) {                 // 접하는 왼쪽 구간이 있으면
        arr[x][y] += arr[x][y - 1]; // 왼쪽에서 온 수 더하기
        arr[x][y] %= 1000000007;
      }
    }
  }

  int answer = arr[m][n];
  return answer;
}

int main() {
  int m = 4, n = 3;
  vector<vector<int>> puddles = {{2, 2}};
  solution(m, n, puddles);
}