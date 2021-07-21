#include <cstring>
#include <iostream>
#include <stdio.h>

#define min(x, y) x <= y ? x : y
using namespace std;

int ret = 987654321;
char dp[1000001];

void cal(int x) {

  dp[1] = 0;
  for (int i = 2; i <= x; i++) {

    // 1을 빼는 경우
    dp[i] = dp[i - 1];

    // 3으로 나눠지는는 경우
    if (i % 3 == 0) {
      dp[i] = min(dp[i], dp[i / 3]);
    }

    // 2로 나누는 경우
    if (i % 2 == 0) {
      dp[i] = min(dp[i], dp[i / 2]);
    }

    dp[i]++;
  }
}

int main(int argc, const char **argv) {
  int x;
  cin >> x;
  memset(dp, -1, sizeof(dp));
  cal(x);
  printf("%d", dp[x]);
}