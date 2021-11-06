//모범답안

#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

// set과 달리 원소들이 정렬되어 있지 않음
// insert, erase, find 모두가 O(1)이다!
unordered_set<int> s;
string str = "";
bool check[7];

//종이 조각으로 만들 수 있는 모든 조합을 찾는다.
void find_all_numbers(int depth, int limit, string &numbers) {
  if (depth == limit)
    return;

  for (int i = 0; i < limit; i++) {
    if (!check[i]) {   //사용하지 않은 종이조각이면
      check[i] = true; //사용했다고 표시하고

      str.push_back(numbers[i]); // str의 뒤쪽에 추가
      s.insert(stoi(str));       // string을 int로 변형해서 set에 추가
      find_all_numbers(depth + 1, limit, numbers); //재귀호출

      //사용 완료 후 표시 해제!!
      str.pop_back();
      check[i] = false;
    }
  }
}

int solution(string numbers) {
  int size = numbers.size();

  find_all_numbers(0, size, numbers);

  int answer = 0;

  int max_value = *max_element(s.begin(), s.end());

  //에라토스테네스의 체
  vector<bool> array(max_value, 0);
  int rootSqrt = sqrt(max_value);

  for (int i = 2; i <= rootSqrt; i++) {
    if (array[i])
      continue;

    for (int j = i + i; j <= max_value; j += i) {
      array[j] = true;
    }
  }

  for (auto &it : s) {
    if (it == 1 || it == 0)
      continue;

    if (!array[it])
      answer++;
  }

  return answer;
}

int main() {

  // numbers는 길이 1 이상 7 이하인 문자열입니다.
  //"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
  string numbers = "17";

  // 예제 #2
  // [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
  // 11과 011은 같은 숫자로 취급합니다.

  cout << solution(numbers) << endl;
}