#include <algorithm>
#include <cstdio>
#include <cstring>
#include <math.h>

using namespace std;

#define ON 1
#define OFF 0

constexpr int MAXSIZE = 100001;

char before[MAXSIZE] = {};
char after[MAXSIZE] = {};
char before2[MAXSIZE] = {};

void changeBulb(int i, char *bulb) {
  //전구 상태 변화
  if (bulb[i] == '0')
    bulb[i] = '1';
  else
    bulb[i] = '0';
}
void push(int i, char *bulb) {
  if (i > 0)
    changeBulb(i - 1, bulb);
  changeBulb(i, bulb);
  if (i < MAXSIZE)
    changeBulb(i + 1, bulb);
};

int solve(int n, char *bulb, bool pushzero) {
  int count = 0;
  if (pushzero) {
    push(0, bulb);
    count++;
  }

  for (int i = 1; i < n; i++) {
    if (bulb[i - 1] != after[i - 1]) {
      push(i, bulb);
      count++;
    }
  }

  if (strncmp(bulb, after, n) == 0)
    return count;
  return -1;
}

int main() {

  int n;
  scanf("%d", &n);
  scanf("%s", before);
  scanf("%s", after);

  strcpy(before2, before);

  int result = 0;
  int pushZero = solve(n, before, true);
  int noPushZero = solve(n, before2, false);

  if (pushZero < 0 || noPushZero < 0)
    result = max(pushZero, noPushZero);
  else
    result = min(pushZero, noPushZero);

  printf("%d", result);
}