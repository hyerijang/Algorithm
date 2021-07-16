#include <math.h>
#include <stdio.h>

int main(int argc, const char **argv) {
  int N;
  scanf("%d", &N);
  for (int y = -N + 1; y < N; y++) {
    for (int x = -N + 1; x < N; x++) {

      if (abs(x) <= abs(y))
        printf("*");
      else if (x < 0)
        printf(" ");
      else
        continue;
    }
    printf("\n");
  }
}
