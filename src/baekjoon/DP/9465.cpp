#include <cstring>
#include <stdio.h>

int max(int a, int b) { return a > b ? a : b; }

int main(int argc, char const *argv[]) {

  int T;
  scanf("%d", &T);

  while (T--) {

    int dp[2][100001], score[2][100001];

    //입력
    int n;
    scanf("%d", &n);
    for (int i = 0; i < 2; i++) {
      for (int j = 1; j <= n; j++) {
        scanf("%d", &score[i][j]);
      }
    }

    //초기화
    dp[0][0] = dp[1][0] = 0;
    dp[0][1] = score[0][1];
    dp[1][1] = score[1][1];

    //계산
    int ret = 0;
    for (int j = 1; j <= n; j++) {
      dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + score[0][j];
      dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + score[1][j];
    }
    printf("%d\n", max(dp[0][n], dp[1][n]));
    return 0;
  }
}
