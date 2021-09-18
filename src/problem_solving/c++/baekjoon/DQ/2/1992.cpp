//틀림 ... 어떤 테스트케이스에서 틀리는진 모르겠네
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

char video[65][65];

bool isAllTheSame(string str) {
  for (int i = 1; i < 4; i++)
    if (str[0] != str[i])
      return false;
  return true;
}

string solve(int n, int y, int x) {
  if (n == 1) {
    string str2 = "";
    str2 += video[y][x];
    return str2;
  }

  //   vector<char> str(5, NULL);
  string str = "";

  int size = n / 2;
  str += solve(size, y, x);
  str += solve(size, y, x + size);
  str += solve(size, y + size, x);
  str += solve(size, y + size, x + size);

  if (isAllTheSame(str)) {
    //한글자만 리턴
    return str.substr(0, 1);
  } else {
    return "(" + str + ")";
    // return str;
  }
}

int main() {
  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf("%s", &video[i]);
  }

  string str = solve(n, 0, 0).c_str();

  printf("%s", str.c_str());

  return 0;
}