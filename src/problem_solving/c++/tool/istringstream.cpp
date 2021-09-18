#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string str = "java c c++ python";
  istringstream ss(str);
  istringstream ss2(str);
  string stringBuffer;
  string str_copy;
  string str_copy2;
  vector<string> x;
  x.clear();
  int ss_count = 0;
  // ss.str()을 하면 알아서 문자열이 추출된다.
  cout << "1결과-> " << ss.str() << endl;
  // ss의 사이즈는 문자열의 길이가 출력된다.
  cout << "ss의 size: " << ss.str().size() << endl;

  //잘린 ss를 이런식으로 다른 문자열에 copy할 수 있다.
  cout << "다른 문자열에 복사(옮기기)-> ";
  while (ss >> str_copy) {
    cout << str_copy << ",";
  }
  cout << endl;

  // vector에 넣으려했는데 ss가 몇개로 나뉜건지 size를 알수가 없다..그래서
  // ss2>>str_copy2를 조건으로 걸었다. ss2를 사용한 이유는 위에서 이미 ss를
  // 사용해서 str_copy에 넣었기 때문에 사용이 안되더라..그래서 ss2와 str_copy2를
  // 만들었다
  cout << "vector에 넣고 확인해봅시다" << endl;
  while (ss2 >> str_copy2) {
    x.push_back(str_copy2);
    ss_count++;
  }

  for (int i = 0; i < x.size(); i++) {
    cout << x[i] << endl;
  }
  cout << "몇개가 잘렸는지 확인해봅시다: " << ss_count << endl;

  return 0;
}