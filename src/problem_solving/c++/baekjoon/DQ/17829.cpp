#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int second(vector<int> &tmp) {
  sort(tmp.begin(), tmp.end());
  tmp.pop_back();
  return tmp.back();
}
int solve(int n, int y, int x, int arr[][1024]) {

  vector<int> tmp;

  if (n == 2) {
    tmp.push_back(arr[y][x]);
    tmp.push_back(arr[y][x + 1]);
    tmp.push_back(arr[y + 1][x]);
    tmp.push_back(arr[y + 1][x + 1]);
    return second(tmp);
  }

  int next = n / 2;
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++)
      tmp.push_back(solve(next, y + i * next, x + j * next, arr));
  }
  return second(tmp);
}
int main() {
  int arr[1024][1024] = {};

  //입력
  int num;
  scanf("%d", &num);

  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++)
      scanf("%d", &arr[i][j]);
  }

  // 2번째로 큰 수만 남긴다.
  int result = solve(num, 0, 0, arr);
  printf("%d", result);
}