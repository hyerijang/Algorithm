//틀림

#include <algorithm>
#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {

  string s = "";
  getline(cin, s);
  s += '\n';
  stack<char> st;
  bool check = false;

  for (int i = 0; i < s.size(); i++) {

    if (s[i] == '<') {
      //스택에 쌓여있던 문자들 출력 (문자열 reverse)
      while (!st.empty()) {
        printf("%c", st.top());
        st.pop();
      }
      //태그 시작
      printf("<");
      check = true;
    }

    else if (s[i] == '>') {
      printf(">");
      check = false;
    }

    else if (check) {
      //태그 내부의 문자
      printf("%c", s[i]); //그냥 받자마자 출력하자

    }

    else if (s[i] == ' ' || s[i] == '\n') {
      while (!st.empty()) {
        printf("%c", st.top());
        st.pop();
      }
      printf(" ");
    }

    else
      st.push(s[i]);
  }
  return 0;
}