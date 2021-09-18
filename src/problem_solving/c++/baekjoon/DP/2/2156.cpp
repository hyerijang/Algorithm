//포도주 시식
//연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
#include <stdio.h>
#define max(a, b) a > b ? a : b;
int main(int argc, const char **argv) {

  int n; // 포도주 잔의 개수
  scanf("%d", &n);

  int cup[10001] = {};
  for (int i = 1; i <= n; i++) {
    //첫번째 잔 ~ n번째 잔에 포도주를 채운다.
    //포도주의 양은 1000이하의 음이 아닌 정수
    scanf("%d", &cup[i]);
  }

  int dp[10001] = {};
  dp[1] = cup[1];
  dp[2] = cup[1] + cup[2];
  for (int i = 3; i <= n; i++) {
    dp[i] = max(dp[i - 1], dp[i - 2] + cup[i]);
    dp[i] = max(dp[i], dp[i - 3] + cup[i - 1] + cup[i]);
  }

  printf("%d", dp[n]);

  return 0;
}