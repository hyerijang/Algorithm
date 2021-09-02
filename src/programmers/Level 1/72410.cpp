#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {

  // 1단계 : 모든 대문자를 대응되는 소문자로 치환합니다.
  for (auto &c : new_id) {
    if ('A' <= c && c <= 'Z') //대문자이면
      c = c - 'A' + 'a';      // 소문자로 변경
  }
  cout << "1단계\n" << new_id << endl;

  // 2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든
  // 문자를 제거
  for (auto iter = new_id.begin(); iter != new_id.end(); iter++) {
    // cout << *iter <<endl;
    bool isOk = false;
    if ('a' <= *iter && *iter <= 'z') //소문자
      isOk = true;
    else if ('0' <= *iter && *iter <= '9') //숫자
      isOk = true;
    else if ('-' == *iter || *iter == '_' ||
             *iter == '.') //빼기(-), 밑줄(_), 마침표(.)
      isOk = true;

    if (!isOk) {
      new_id.erase(iter--);
    }
  }
  cout << "2단계\n" << new_id << endl;

  // 3단계 '...'와 '..' 가 '.'로 바뀌었습니다.
  for (auto iter = new_id.begin(); iter != new_id.end(); iter++) {
    if (*iter == *(iter + 1) && *iter == '.')
      new_id.erase(iter--);
  }
  cout << "3단계\n" << new_id << endl;

  // 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
  auto iter = new_id.begin();
  if (*iter == '.')
    new_id.erase(iter);
  iter = new_id.end() - 1;
  if (*iter == '.')
    new_id.erase(iter);
  cout << "4단계\n" << new_id << endl;

  // 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
  if (new_id.empty())
    new_id += 'a';
  cout << "5단계\n" << new_id << endl;

  // 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한
  // 나머지 문자들을 모두 제거합니다.
  if (new_id.size() >= 16)
    new_id.erase(15, new_id.size());
  iter = new_id.end() - 1;
  if (*iter == '.')
    new_id.erase(iter);
  cout << "6단계\n" << new_id << endl;

  // 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가
  // 3이 될 때까지 반복해서 끝에 붙입니다.
  while (new_id.size() <= 2)
    new_id += *(new_id.end() - 1);
  cout << "7단계\n" << new_id << endl;

  string answer = new_id;
  return answer;
}