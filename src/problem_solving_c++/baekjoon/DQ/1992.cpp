
#include <cstdio>
#include <vector>

using namespace std;

char arr[64][64];

char press(int n, int y, int x) {

  if (n == 1)
    return arr[y][x];

  int size = n / 2;

  char str[5];
  int a = 0;
  bool ok = true;

  char check = arr[y][x];

  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      char result = press(size, y + i * size, x + j * size);
      if (result != '2')
        str[a] = result;
      if (ok == true)
        printf("(");
      ok = false;
      a++;
      str[a] = NULL;
    }
  }
}

if (ok == false)
  printf("%s)", str);
}

int main() {
  int num;
  scanf("%d", &num);

  for (int i = 0; i < num; i++) {
    getchar();
    for (int j = 0; j < num; j++)
      arr[i][j] = getchar();
  }

  press(num, 0, 0);
}