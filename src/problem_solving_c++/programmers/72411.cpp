// https://programmers.co.kr/learn/courses/30/lessons/72411
//메뉴 리뉴얼
#include <bits/stdc++.h>

using namespace std;

map<string, int> word;
int max_count = 0;

void recursion(int next, const int depth, string str, const string &orders) {

  str += orders[next];

  if (depth == str.size()) {
    // cout << str << endl;
    word[str]++;

    if (max_count < word[str]) {
      max_count = word[str];
    }
  }

  for (int i = next + 1; i < orders.size(); i++)
    recursion(i, depth, str, orders);
}
void make_combination(const int depth, const string &orders) {
  for (int next = 0; next < orders.size(); next++)
    recursion(next, depth, "", orders);
}

vector<string> solution(vector<string> orders, vector<int> course) {

  vector<string> answer;

  //메뉴를 오름차순으로 정렬
  for (int i = 0; i < orders.size(); i++) {
    sort(orders[i].begin(), orders[i].end());
    // cout << orders[i] << endl;
  }

  //가능한 조합 생성
  for (auto &depth : course) {
    word.clear();
    max_count = 0;
    for (int customer = 0; customer < orders.size(); customer++) {
      make_combination(depth, orders[customer]);
    }

    for (auto w : word)
      if (w.second == max_count && max_count >= 2) {
        cout << w.first << endl;
        answer.push_back(w.first);
      }
  }

  sort(answer.begin(), answer.end());
  return answer;
}

int main() {

  vector<string> orders = {"ABFGC", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
  vector<int> course = {2, 3, 4};

  solution(orders, course);

  return 0;
}