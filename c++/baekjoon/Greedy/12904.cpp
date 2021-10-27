#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[]) {
  ios_base ::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  string S, T;
  cin >> S >> T;

  while (1) {

    if (S.length() == T.length()) {
      if (S == T)
        cout << 1;
      else
        cout << 0;
      return 0;
    }

    //문자열 T에서 한글자씩 뺀다
    char tmp = T.back();
    T.pop_back();

    if (tmp == 'B')
      reverse(T.begin(), T.end());
  }

  return 0;
}