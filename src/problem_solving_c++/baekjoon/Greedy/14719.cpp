#include <iostream>
#include <string>
#include <vector>

using namespace std;
int main() {

  int H, W;
  cin >> H >> W;

  vector<int> blocks(W, 0);

  for (auto &b : blocks)
    cin >> b;

  int answer = 0;
  for (int h = 0; h < H; h++) {
    vector<int> w;
    int wall = 0;
    for (int i = 0; i < W; i++) {
      if (blocks[i] > 0) {
        w.push_back(i);
        wall++; //벽의 수 저장
      }
      blocks[i]--;
    }

    if (wall < 2) //양쪽에 벽 없으면 그대로 종료
      break;

    int sum = 0;
    for (int i = 1; i < w.size(); i++) {
      sum += (w[i] - w[i - 1]) - 1;
    }

    answer += sum;
    // cout << sum << endl;
  }
  cout << answer << endl;
  return 0;
}