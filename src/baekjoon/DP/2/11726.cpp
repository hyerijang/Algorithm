#include <stdio.h>

using namespace std;
int main(int argc, char const *argv[]) {

  int n;
  scanf("%d", &n);

  int dp[1001];
  dp[1] = 1;
  dp[2] = 2;
  for (int i = 3; i <= n; i++) {

    dp[i] = dp[i - 2] + dp[i - 1];
    dp[i] %= 10007;
  }

  printf("%d", dp[n]);
  return 0;
}
