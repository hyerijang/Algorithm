#include <stdio.h>

int main(int argc, const char **argv) {
  int N;
  scanf("%d", &N);

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (j < N - (i + 1))
        printf(" ");

      else
        printf("*");
    }
    printf("\n");
  }
}
