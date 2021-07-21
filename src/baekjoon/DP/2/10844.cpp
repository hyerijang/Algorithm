#include <iostream>
#include <stdio.h>
using namespace std;
int main(int argc, char const *argv[]) {
  int n;
  cin >> n;

  int dp[101][10] = {};

  for (int j = 1; j < 10; j++) {
    dp[1][j] = 1;
  }

  for (int i = 2; i <= n; i++) {
    dp[i][0] = dp[i - 1][1];
    dp[i][9] = dp[i - 1][8];

    for (int j = 1; j <= 8; j++) {
      dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1];
      dp[i][j] %= 1000000000;
    }
  }

  int sum = 0;
  for (int j = 0; j < 10; j++) {
    sum += dp[n][j];
    sum %= 1000000000;
  }
  cout << sum;
}
