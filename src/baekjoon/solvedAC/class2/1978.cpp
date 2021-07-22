//소수 찾기
#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;
int main() {
  int n;
  scanf("%d", &n);

  int count = n;
  int tmp;

  while (n--) {
    scanf("%d", &tmp);

    if (tmp == 1) // 1은 소수가 아님
    {
      count--;
      continue;
    }

    for (int j = 2; j < tmp / 2 + 1; j++) {
      if (tmp % j == 0) {
        //소수아님
        count--;
        break;
      }
    }
  }

  printf("%d", count);
}