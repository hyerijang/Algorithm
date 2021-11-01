#include <stdio.h>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {

  int x = 1;
  int y = 1;
  scanf("%d %d ", &x, &y);

  int result = 0; //일 : 0 , 월 : 1 , 화 : 2 ... 토: 6

  int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  for (int i = 1; i < x; i++) {
    result += month[i];
  }

  result += y;

  string day[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
  printf("%s", day[result % 7].c_str());

  return 0;
}
