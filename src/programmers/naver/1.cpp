#include <bits/stdc++.h>

using namespace std;

int greedy(int target, int k, vector<int> &student) {

  int ans = 0;
  // target의 오른쪽으로  가면서 1 개수가 k개이면 답의 포함
  for (int i = target; i < student.size(); i++) {
    if (student[i] == 1) {
      k--;
    }
    if (k == 0)
      ans++;
  }

  //왼쪽 0 개수 고려
  int left_zero_plus_1 = 1;
  for (int i = target - 1; i >= 0; i--) {
    if (student[i] == 1) {
      break;
    }
    left_zero_plus_1++;
  }

  return ans * left_zero_plus_1;
}

int solution(vector<int> student, int k) {

  int answer = 0;
  int numOf1 = 0;
  for (int i = 0; i < student.size(); i++)
    numOf1++;
  for (int i = 0; i < student.size(); i++)
    if (student[i] == 1 && numOf1 >= k) {
      answer += greedy(i, k, student);
      // right 왼쪽에 남은 k의 개수 --;
      numOf1--;
    }
  return answer;
}

int main() {

  //   vector<int> student = {0, 1, 0, 0};
  vector<int> student = {0, 1, 0, 0, 1, 1, 0};
  int k = 2;
  solution(student, k);
}