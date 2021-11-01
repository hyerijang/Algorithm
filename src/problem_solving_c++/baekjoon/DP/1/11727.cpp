#include <stdio.h>
#include <vector>

using namespace std;
int main(int argc, char const *argv[]) {
  /* code */

  int n;
  scanf("%d", &n);

  vector<int> dp;
  dp.push_back(1);
  dp.push_back(3);
  for (int i = 2; i < n; i++) {
    dp.push_back((dp[i - 1] + dp[i - 2] + dp[i - 2]) % 10007);
  }

  printf("%d", dp[n - 1]);
  return 0;
}
