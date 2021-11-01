#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> answer;
void hanoi(int n, int from, int to, int tmp) {
  vector<int> temp = {from, to};
  if (n == 1)
    answer.push_back(temp);
  else {
    hanoi(n - 1, from, tmp, to);
    answer.push_back(temp);
    hanoi(n - 1, tmp, to, from);
  }
}

vector<vector<int>> solution(int n) {
  hanoi(n, 1, 3, 2);
  return answer;
}

int main() {

  int n = 3;
  vector<vector<int>> answer = solution(n);

  for (auto v : answer) {
    cout << v[0] << " " << v[1] << endl;
  }
}