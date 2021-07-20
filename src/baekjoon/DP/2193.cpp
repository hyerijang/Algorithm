#include <stdio.h>
#include <vector>

using namespace std;
int main(int argc, char const *argv[]) {

  int n;
  scanf("%d", &n);

  long long dp[91] = {};
  dp[1] = 1;
  dp[2] = 1;
  dp[3] = 2;

  for (int i = 4; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  printf("%lld", dp[n]);
  return 0;
}
