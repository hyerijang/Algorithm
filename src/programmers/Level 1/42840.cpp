#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> first = {1, 2, 3, 4, 5};
vector<int> second = {2, 1, 2, 3, 2, 4, 2, 5};
vector<int> third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> selectPattern(int who) {

  switch (who) {
  case 1:
    return first;

  case 2:
    return second;

  case 3:
    return third;
  }
}

//채점
int grade(vector<int> pattern, vector<int> &answer) {

  int score = 0;
  int p_size = pattern.size();

  for (int i = 0; i < answer.size(); i++) {
    if (answer[i] == pattern[i % p_size])
      score++;
  }

  return score;
}

bool compare(pair<int, int> &a, pair<int, int> &b) {
  return a.second > b.second;
}

vector<int> solution(vector<int> answers) {

  vector<pair<int, int>> rank;
  int max_score = 0;
  for (int who = 1; who <= 3; who++) {
    int score = grade(selectPattern(who), answers);
    rank.push_back(make_pair(who, score));
    max_score = max(max_score, score);
  }

  //내림차순으로 정렬
  sort(rank.begin(), rank.end(), compare);

  vector<int> answer;
  int max = 0;
  for (int i = 0; i < 3; i++) {
    if (rank[i].second == max_score)
      answer.push_back(rank[i].first);
    else
      break;
  }

  sort(answer.begin(), answer.end(), less<>());

  return answer;
}

int main() {

  // vector<int> numbers = {1, 2, 3, 4, 5};
  vector<int> numbers = {1, 3, 2, 4, 2};

  for (auto i : solution(numbers))
    cout << i << endl;
}