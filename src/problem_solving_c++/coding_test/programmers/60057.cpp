#include <iostream>
#include <string>
#include <vector>

using namespace std;

int compress(int unit, string str) {
  vector<string> tmp;

  for (auto it = str.begin(); it != str.end(); it += unit)
    str.substr(unit);

  return tmp.size();
  //문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
};

int solution(string s) {

  int answer = 0;
  vector<int> v;
  for (int i = 0; i < s.size(); i++) {
    v.push_back(compress(i, s));
    if (v[i - 1] < v[i])
      break;
  }
  return answer;
}

int main(int argc, char const *argv[]) {

  string s;

  while (1) {
    s.clear();
    cin >> s;
    if (s.size() < 1)
      break;
    cout << s << " : " << solution(s) << endl;
  }

  return 0;
}
