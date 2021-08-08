#include <stdio.h>

using namespace std;

int first(int rank) {
  //진출 못함
  if (rank == 0)
    return 0;

  int money[7] = {0, 500, 300, 200, 50, 30, 10};
  int num[7] = {0, 1, 2, 3, 4, 5, 6};

  int prizeMoney = 0;

  // i등의 상금을 받으려면 left < rank <= right 범위에 속해야함
  int left = 0;
  int right = 0;

  for (int i = 1; i <= 6; i++) {
    left = right;
    right += num[i];
    if (left < rank && rank <= right) {
      //   printf("a: %d만원   ", money[i]);
      return money[i];
    }
  }

  return 0;
}

int second(int rank) {
  //진출 못함
  if (rank == 0)
    return 0;

  int money[6] = {0, 512, 256, 128, 64, 32};
  int num[6] = {0, 1, 2, 4, 8, 16};

  // i등의 상금을 받으려면 left < rank <= right 범위에 속해야함
  int left = 0;
  int right = 0;

  for (int i = 1; i <= 5; i++) {
    left = right;
    right += num[i];
    if (left < rank && rank <= right) {
      //   printf("b : %d만원\n", money[i]);
      return money[i];
    }
  }

  return 0;
}
int main() {
  int t, a, b;

  scanf("%d", &t);

  while (t--) {
    scanf("%d %d", &a, &b);
    printf("%d\n", (first(a) + second(b)) * 10000);
  }
}
