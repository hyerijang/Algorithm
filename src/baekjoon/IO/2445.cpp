#include <math.h>
#include <stdio.h>

int main(int argc, const char **argv) {
  int N;
  scanf("%d", &N);
  for (int y = -N + 1; y < N; y++) {
    for (int x = -N; x <= N; x++) {
      if (x == 0)
        continue;
      if (abs(x) > abs(y))
        printf("*");
      else
        printf(" ");
    }
    printf("\n");
  }
}
