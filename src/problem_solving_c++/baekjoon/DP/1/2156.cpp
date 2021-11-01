#include <stdio.h>
#include <vector>
#define max(a, b) a > b ? a : b

using namespace std;
int main() {
  //포도주 잔의 개수 n
  int n;
  scanf("%d", &n);

  //포도주의 양
  vector<int> wine(1, 0);
  for (int i = 0; i < n; i++) {
    int tmp;
    scanf("%d", &tmp);
    wine.push_back(tmp);
  }

  vector<int> dp(n + 1, 0);
  int ans = 0;

  dp[0] = 0;
  dp[1] = wine[1];
  dp[2] = wine[1] + wine[2];
  // 3잔 연속 마실 수 없다.
  // 1. 마지막 잔을 기준으로 3번째 앞에 잔을 마시고, 2번째 앞에 잔을 건너뛰고
  // 1번째 앞에 잔 + 마지막잔
  // 2. 마지막 잔을 기준으로 2번째 앞에 잔을 마시고 + 마지막 잔
  // 3. 마지막 잔을 마시지 않고, 1번째 앞에 잔의 최댓값

  for (int i = 3; i <= n; i++) {
    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i]);
    dp[i] = max(dp[i], dp[i - 1]);
  }

  printf("%d", dp[n]);
}
