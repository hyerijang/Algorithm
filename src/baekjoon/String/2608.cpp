#include <algorithm>
#include <functional> // greater<int>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

using namespace std;

void init_map(map<char, int> &m) {
  m['I'] = 1;
  m['V'] = 5;
  m['X'] = 10;
  m['L'] = 50;
  m['C'] = 100;
  m['D'] = 500;
  m['M'] = 1000;
}

void init_map_reverse(map<int, string, greater<int>> &m) {
  m[1000] = 'M';
  m[500] = 'D';
  m[100] = 'C';
  m[50] = 'L';
  m[10] = 'X';
  m[5] = 'V';
  m[1] = 'I';
}

int romeToArabic(string &str, map<char, int> &m) {
  int ans = 0;

  char last = 'Z';
  for (auto c : str) {

    //작은 숫자가 큰 숫자의 왼쪽에 오는 경우
    if (m[last] < m[c])
      ans += (m[c] - m[last] * 2);

    else
      ans += m[c];

    last = c;
  }
  return ans;
}

string arabicToRome(int num, map<char, int> &m) {
  string ans;
  map<int, string, greater<int>> m_reverse; //내림차순으로 정렬

  init_map_reverse(m_reverse);

  int d = 1;
  while (num > 0) {
    int tmp = num % 10;
    string str;

    if (tmp == 0)
      continue;
    else if (tmp == 4) {
      str += m_reverse[d] + m_reverse[d * 5];
    } else if (tmp == 9) {

      str += m_reverse[d] + m_reverse[d * 10];
    } else {

      if (tmp >= 5) {
        str += m_reverse[d * 5];
        tmp -= 5;
      }
      while (tmp--)
        str += m_reverse[d];
    }
    ans = str + ans;
    num /= 10;
    d *= 10;
  }

  return ans;
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string a, b;
  cin >> a >> b;

  map<char, int> m;
  init_map(m);

  int a_Arabic, b_Arabic;

  a_Arabic = romeToArabic(a, m);
  b_Arabic = romeToArabic(b, m);

  cout << a_Arabic + b_Arabic << endl;
  cout << arabicToRome(a_Arabic + b_Arabic, m) << endl;
}