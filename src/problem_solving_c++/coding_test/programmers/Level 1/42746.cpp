#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool compare(string a, string b) { return a + b > b + a; }

string solution(vector<int> numbers) {
  string answer = "";
  vector<string> tmp;

  for (int i = 0; i < numbers.size(); i++)
    tmp.push_back(to_string(numbers[i]));

  sort(tmp.begin(), tmp.end(), compare);

  if (tmp.at(0) == "0")
    return "0";

  for (int i = 0; i < tmp.size(); i++)
    answer += tmp[i];
  return answer;
}

int main() {

  char tmp;
  // array 입력
  vector<int> numbers;
  int size = 0;

  while (true) {

    scanf("%c", &tmp);
    if (tmp <= '9' && tmp >= '0')
      numbers.push_back(atoi(&tmp));
    if (tmp == ']')
      break;
  }

  solution(numbers);

  return 0;
}