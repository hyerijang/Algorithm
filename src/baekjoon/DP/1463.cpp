#include <cstring>
#include <stdio.h>

#define min(x, y) x <= y ? x : y
#define INF 987654321

char dp[1000001];
void cal(int n) {
  dp[1] = 0;

  for (int i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + 1;
    if (i % 3 == 0)
      dp[i] = min(dp[i], dp[i / 3] + 1);
    if (i % 2 == 0)
      dp[i] = min(dp[i], dp[i / 2] + 1);
  }
}

int main(int argc, const char **argv) {
  int x;
  scanf("%d", &x);
  memset(dp, -1, sizeof(dp));
  cal(x);
  printf("%d", dp[x]);
  return 0;
}