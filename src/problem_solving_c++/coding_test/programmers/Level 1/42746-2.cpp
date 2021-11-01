#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solution(vector<int> numbers) {

  vector<pair<string, string>> strNums;
  bool isAllZero = true;

  for (auto &num : numbers) {
    string tmp = to_string(num);
    // 세번 더하는 이유?
    // 문자열을 *세자리 이상의 수*로 만들기 위함.
    // 입력이 {3, 330}이라 하면
    // 두 번 반복할 경우 만들어지는 문자열 : "33", "330330"
    // 비교 시 "33" <  "33~" (330의 마지막 숫자인 0을 고려하지 않고 비교)
    // 세 번 반복할 경우 만들어지는 문자열 : "33", "330330"
    // 비교 시 "333" > "330~"  (330의 마지막 숫자인 0을 고려하여 비교)

    string strForcmp = tmp + tmp + tmp;
    strNums.push_back(make_pair(strForcmp, tmp));

    // 0,0,0,0,0 인 경우 "00000"으로 출력되는 것 예방 위함
    if (num != 0)
      isAllZero = false;
  }

  //모든 숫자가 0인경우 "0"리턴
  if (isAllZero)
    return "0";

  //내림차순 정렬
  sort(strNums.begin(), strNums.end(), greater<pair<string, string>>());

  string answer = "";
  for (auto &str : strNums) {
    answer += str.second;
  }

  return answer;
}

int main(int argc, char const *argv[]) {
  vector<int> numbers = {3, 330};
  string result = solution(numbers);
  string answer = "3330";

  if (result != answer)
    cout << "오답 : " << result << " != " << answer << endl;
  return 0;
}
