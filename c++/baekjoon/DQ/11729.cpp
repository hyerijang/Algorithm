#include <cassert>
#include <stdio.h>
#include <vector>

using namespace std;

void hanoi(int n, int start, int byPass, int to) {
  // 1. 먼저 n-1개의 원판을 to장대를 거쳐  byPass장대로 옮기고,
  // 2. start장대에 있는 가장 큰 크기의 원판을 to 장대로 옮긴 후
  // 3. byPass 장대에 있는 n-1개의 원판을 start 장대를 거쳐 to장대로 옮김
  if (n == 1)
    printf("%d %d\n", start, to);
  else {

    hanoi(n - 1, start, to, byPass); //(1)
    printf("%d %d\n", start, to);    //(2)
    hanoi(n - 1, byPass, start, to); //(3)
  }
}

int main(int argc, const char **argv) {

  int N;
  scanf("%d", &N);
  printf("%d\n", (1 << N) - 1);
  //   두 번째 줄부터 수행 과정을 출력한다.
  hanoi(N, 1, 2, 3);

  return 0;
}