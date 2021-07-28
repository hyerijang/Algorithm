
#include <math.h>
#include <stdio.h>

char arr[2188][2188] = {};

void empty(int n, int y, int x) {
  for (int i = y; i < y + n / 3; i++)
    for (int j = x; j < x + n / 3; j++) {
      arr[i][j] = ' ';
    }
};

void fill(int n, int y, int x) {
  for (int i = y; i < y + n / 3; i++)
    for (int j = x; j < x + n / 3; j++) {
      arr[i][j] = '*';
    }
};

void print(int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      printf("%c", arr[i][j]);
    }
    printf("\n");
  }
}

void solve(int n, int y, int x) {

  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++) {
      if (i == 1 && j == 1) // 가운데는 공백
        empty(n, y + (i * n / 3), x + (j * n / 3));
      else {
        fill(n, y + (i * n / 3), x + (j * n / 3));
        if (n / 3 > 0)
          solve(n / 3, y + (i * n / 3), x + (j * n / 3));
      }
    }
}
int main(int argc, const char **argv) {

  //   printf("%ld MB", sizeof(arr) / 1024);

  int n;
  scanf("%d", &n);

  solve(n, 0, 0);

  print(n);
  return 0;
}