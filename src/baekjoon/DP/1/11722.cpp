//가장 긴 감소하는 부분 수열의 길이 출력
#include <stdio.h>
#define max(a, b) a > b ? a : b;
int main(int argc, const char **argv) {

  int N; // 수열 A의 크기
  scanf("%d", &N);

  int A[1001] = {};
  for (int i = 1; i <= N; i++) {
    scanf("%d", &A[i]);
  }

  int dp[1001] = {}; // i번째 원소를 반드시 포함하는, 감소하는 부분 수열의 길이
  int max = 0;
  for (int cur = 1; cur <= N; cur++) {
    dp[cur] = 1;                    //부분수열 : 최소 1개
    for (int j = 1; j < cur; j++) { // A[cur]보다 이전 값들 검사
      if (A[j] > A[cur]) //이전 값이 현재 값보다 더 크면 감소하는 부분 수열
        //현재 부분 수열의 크기와 A[j]+1 비교해서 더 긴 것 저장
        dp[cur] = max(dp[cur], dp[j] + 1);
    }
    //현재 계산된 값중 가장 큰 것 저장
    max = max(dp[cur], max);
  }

  printf("%d", max);
  return 0;
}