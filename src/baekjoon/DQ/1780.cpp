// 종이의 개수
#include <cstdio>
#include <math.h>
#include <stdio.h>

int output[3];            // -1 0 1
int arr[2187][2187] = {}; // 18683 KB

void divide(int x, int y, int size) {
  int first = arr[x][y];
  bool flag = true;

  for (int i = x; i < x + size; i++) {
    for (int j = y; j < y + size; j++) {
      if (arr[i][j] != first) {
        flag = false;
        break;
      }
    }
  }
  if (flag) {
    output[first + 1]++;

  } else {
    for (int a = x; a < x + size; a += size / 3) {
      for (int b = y; b < y + size; b += size / 3) {
        divide(a, b, size / 3);
      }
    }
  }
}

int main(int argc, char const *argv[]) {
  //첫째 줄에 N(1 ≤ N ≤ 3^7, N은 3k 꼴)이 주어진다.
  // 3^7 = 2187
  int N;
  scanf("%d", &N);

  //   printf("%ld KB\n", sizeof(arr) / 1024);

  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++) {
      scanf("%d", &arr[i][j]);
    }

  divide(0, 0, N);
  for (int i = 0; i < 3; i++) {
    printf("%d\n", output[i]);
  }

  return 0;
}
