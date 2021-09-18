#include <stdio.h>
#include <vector>

using namespace std;
int main(int argc, char const *argv[]) {
  /* code */
  vector<int> dp;
  dp.push_back(0);
  dp.push_back(1); // 1
  dp.push_back(2); // 1+1, 2
  dp.push_back(4); // 1+1+1, 2+1, 1+2, 3

  int t;
  scanf("%d", &t);

  while (t--) {

    int n;
    scanf("%d", &n);

    for (int i = dp.size(); i <= n; i++) {
      dp.push_back((dp[i - 1] + dp[i - 2] + dp[i - 3]));
    }

    printf("%d\n", dp[n]);
  }
  return 0;
}
