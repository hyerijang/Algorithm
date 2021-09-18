#include <stdio.h>

int main(int argc, char const *argv[]) {

  int N; // 숫자의 개수
  scanf("%d", &N);

  char c;
  int sum = 0;
  while ((c = fgetc(stdin)) != EOF) {
    if (c < '0')
      continue;
    sum += (c - '0');
  }

  printf("%d", sum);
  return 0;
}
