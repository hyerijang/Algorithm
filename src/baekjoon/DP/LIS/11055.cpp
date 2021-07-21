#include <stdio.h>
#include <vector>
#define max(a, b) a > b ? a : b

using namespace std;
int main() {
  //수열의 크기
  int n;
  scanf("%d", &n);

  //수열
  vector<int> seq(n + 1, 0);
  vector<int> dp(n + 1, 0);

  for (int i = 1; i <= n; i++) {
    scanf("%d", &seq[i]);
    dp[i] = seq[i];
  }

  int ret = 0;

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      if (seq[j] < seq[i]) {
        dp[i] = max(dp[j] + seq[i], dp[i]);
      }
    }
    ret = max(dp[i], ret);
  }
  printf("%d", ret);
}
