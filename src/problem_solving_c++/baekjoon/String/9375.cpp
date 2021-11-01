#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>

using namespace std;

int main() {

  int cases;
  scanf("%d", &cases);

  while (cases--) {
    int n; //의상 수
    scanf("%d", &n);

    map<string, int> m;

    for (int i = 0; i < n; i++) {
      string name, type;
      cin >> name;
      cin >> type;
      m[type]++;
    }

    auto it = m.begin();

    int answer = 1;
    while (it != m.end()) {
      answer *= (it->second + 1); //안입는 경우를 포함하여 곱함
      it++;
    }

    //모두 안입는 경우 제외
    answer--;

    cout << answer << endl;
  }
}