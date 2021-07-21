#include <stdio.h>
#include <vector>
#define max(a, b) a > b ? a : b

using namespace std;
int main() {
  //계단의 개수
  int n;
  scanf("%d", &n);

  //계단의 점수
  vector<int> step(n + 1, 0);

  for (int i = 1; i <= n; i++) {
    scanf("%d", &step[i]);
  }

  // i번째 계단을 밟는다고 가정햇을 때의 최대 점수
  vector<int> dp(n + 1, 0);
  dp[1] = step[1];
  dp[2] = step[1] + step[2];

  for (int i = 3; i <= n; i++) {
    dp[i] = max(dp[i - 2], dp[i - 3] + step[i - 1]);
    dp[i] = max(dp[i], dp[i - 4] + step[i - 2]);
    dp[i] += step[i];
  }

  printf("%d", dp[n]);
}
