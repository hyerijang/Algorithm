#include <stdio.h>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {

  int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  string day[7] = {"SUN", "MON", "TUE", "WED",
                   "THU", "FRI", "SAT"}; //일: 0, 월: 1

  int x, y;
  scanf("%d, %d", &x, &y); // x월 y일

  int result = 0;
  if (x > 0) {
    result += month[x--];
  }
  result += y;

  printf("%s", day[result % 7].c_str());
}
