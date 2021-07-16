#include <math.h>
#include <stdio.h>

int main(int argc, const char **argv) {
  int N;
  scanf("%d", &N);

  int count = 0;

  for (int y = 1; y <= N; y++) {
    for (int x = y; x < N; x++) {
      printf(" ");
    }
    for (int x = 1; x <= y * 2 - 1; x++) {
      if (x % 2 == 1)
        printf("*");
      else
        printf(" ");
    }
    printf("\n");
  }
}
