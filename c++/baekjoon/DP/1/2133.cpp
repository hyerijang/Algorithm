// 타일 채우기
// 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
// 틀려서 https://yabmoons.tistory.com/536 참고
#include <stdio.h>
#include <vector>

using namespace std;

bool isOdd(int n) {
  if (n % 2)
    return true;
  return false;
}

int solve(int n) {

  // n이 홀수면 벽에 빈공간 생김
  if (isOdd(n))
    return 0;

  vector<int> W(n + 1, 0);
  W[0] = 1;
  W[2] = 3;
  // **N이 2씩 커질 때 마다 특별한 모양도 2개씩 추가된다.

  for (int cur = 4; cur <= n; cur = cur + 2) {
    //(1) : [ N-2 ][2]
    W[cur] = W[cur - 2] * W[2];

    //(2) : [2][ N- 2 ] 중 (1)과 중복되지 않는 경우
    //중복되지 않게 하는 법?
    // => [ N-2 ]를 채울 때 특별한 모양(2개)을 넣는다.

    /*
    예시: N = 8인 경우
    Case1 : 3x8크기의 벽을 3x6 + 3x2 크기로 채우는 경우
        (F[6] * F[2])
    Case2 : 3x8크기의 벽을 3x4 + 3x4 크기로 채우는 경우
        (F[4] * 2) -> 특별한 모양 2개
    Case3 : 3x8크기의 벽을 3x2 + 3x6 크기로 채우는 경우
        (F[2] * 2) ->    특별한모양 2개
    */

    for (int j = cur - 4; j >= 0; j = j - 2) {
      W[cur] = W[cur] + (W[j] * 2);
    }

    // printf("%d\n", W[cur]);
  }

  return W[n];
}

int main(int argc, const char **argv) {

  int N; // 3×N 크기의 벽
         // N(1 ≤ N ≤ 30)
  scanf("%d", &N);

  //결과 출력
  printf("%d", solve(N));
  return 0;
}
