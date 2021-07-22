// 바이러스
// 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게
// 되는 컴퓨터의 수를 첫째 줄에 출력한다.
#include <algorithm>
#include <stdio.h>
#include <vector>

#define WORM -1
#define CONNECT 1
#define CHECKED 2
using namespace std;
int main(int argc, char const *argv[]) {
  int c; //컴퓨터의 수
  scanf("%d", &c);

  int n; //연결 쌍의 수
  scanf("%d", &n);

  //연결쌍 정보 입력
  int net[101][101] = {};
  while (n--) {
    int a, b;
    scanf("%d %d", &a, &b);

    net[a][b] = CONNECT;
    net[b][a] = CONNECT;
  }

  int computer[101] = {};
  vector<int> wormed;

  // 1은 바이러스에 걸림
  wormed.push_back(1);
  computer[1] = WORM;

  for (int i = 0; i < wormed.size(); i++) {
    int cur = wormed[i];
    for (int j = 1; j <= c; j++) {
      if (net[cur][j] == CONNECT) {
        net[cur][j] = CHECKED;
        net[j][cur] = CHECKED;
        if (computer[j] != WORM) { //이미 확인한 컴퓨터가 아니면
          computer[j] = WORM;
          wormed.push_back(j);
        }
      }
    }
  }

  // 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
  printf("%d", wormed.size() - 1);
  return 0;
}