#include <stdio.h>

int main(int argc, char const *argv[]) {
  int N;
  scanf("%d", &N);

  char tmp[101];
  scanf("%s", tmp);

  int sum = 0;
  for (int i = 0; i < N; i++) {
    sum += (tmp[i] - '0');
  }

  printf("%d", sum);

  return 0;
}
