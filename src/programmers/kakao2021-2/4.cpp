#include <bits/stdc++.h>

using namespace std;

map<int, int> rion_score;

//초기화 : n번 다 10번 쐈다
vector<int> rionInfo(11, 0);

vector<vector<int>> tmp;

void solve() {
  int rionScore = 0;
  int apeachScore = 0;
  for (int i = 0; i < 11; i++) {
    if (rionInfo[i] > info[i])
      rionScore += (10 - i); //라이언에게 점수 추가
    else
      apeachScore += (10 - i);
  }

  if (rionScore > apeachScore)
    tmp.push_back(rionInfo);

  solve()
}
vector<int> solution(int n, vector<int> info) {

  int count = 0;
  for (int i = 0; i < 11; i++) {
    if (info[i] > 0) {
      rionInfo[i] = min(count, info[i] + 1);
      count -= min(count, info[i] + 1);
    } else {
      rionInfo[i] = 1;
      count--;
    }
    if (count == 0)
      break;
  }

  vector<int> answer;
  return answer;
}

int main() {

  int n = 5;
  vector<int> info = {2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
  solution(n, info);
  return 0;
}