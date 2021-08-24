#include <iostream>
#include <string>

int main() {
  // 검색 대상 문자열
  std::string str = std::string("abcdefg!");

  // 어떤 문자들을 찾아볼 것인가?
  std::string search_str = std::string("bc");
  std::cout << str.find_first_of(search_str) << '\n';
  std::cout << str.find_first_of(search_str, 5) << '\n';

  const char *search_cstr = "Good Bye!";
  std::cout << str.find_first_of(search_cstr) << '\n';
  std::cout << str.find_first_of(search_cstr, 0, 4) << '\n';
  // 'x' 는 Hello World 에 없으므로 npos 가 리턴된다
  std::cout << str.find_first_of('x') << '\n';
}