#include <stdio.h>

int main(int argc, char const *argv[]) {
  char c = fgetc(stdin);

  while (c != EOF) {
    printf("%c", c);
    c = fgetc(stdin);
  }

  return 0;
}
