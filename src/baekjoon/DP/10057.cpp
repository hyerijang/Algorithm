#include <stdio.h>
#include <vector>

using namespace std;
int main(int argc, char const *argv[]) {
  /* code */

  int n;
  scanf("%d", &n);

  int dp[1001][10] = {};
  for (int j = 0; j < 10; j++)
    dp[1][j] = 1;

  for (int i = 2; i <= n; i++) {
    for (int j = 0; j < 10; j++) {
      if (j == 9)
        dp[i][9] = dp[i - 1][9];
      else {
        for (int k = j; k < 10; k++) {
          dp[i][j] += dp[i - 1][k];
        }
        dp[i][j] %= 10007;
      }
    }
  }

  int sum = 0;
  for (int i = 0; i < 10; i++)
    sum = (sum + dp[n][i]);
  printf("%d", sum % 10007);
  return 0;
}
