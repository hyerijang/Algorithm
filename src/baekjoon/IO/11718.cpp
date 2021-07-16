#include <stdio.h>

int main(int argc, const char **argv) {
  char c;
  while ((c = fgetc(stdin)) > 0) {
    printf("%c", c);
  }
}
