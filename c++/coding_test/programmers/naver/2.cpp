#include <bits/stdc++.h>

using namespace std;

//이슈 검색어
//어떤 검색어가 연속된 n일 동안 매일 최소 k 번 이상 검색되고,
//같은 연속된 n일 동안 총 2 x n x k번 이상 검색되었을 경우
map<char, int> m;

//최고의 이슈 검색어
//이슈 검색어 중에서 가장 여러 번 이슈 검색어가 된 검색어
string solution(vector<string> research, int n, int k) {

  // 하루의 검색기록을 알파벳 순으로 정렬
  for (auto &r : research) {
    sort(r.begin(), r.end());
  }

  //검색결과 분석
  int analysis[31][26] = {}; // 26 = 알파벳 문자 개수

  for (int day = 0; day < research.size(); day++) {
    //해당 날짜의 검색어 분석
    for (int c = 0; c < research[day].size(); c++) {
      int cIdx = research[day][c] - 'a';
      analysis[day][cIdx]++;
    }
  }

  int isOK[26] = {};                      // 26 = 알파벳 문자 개수
  for (int cIdx = 0; cIdx < 26; cIdx++) { //각 문자에 대하여 분석

    for (int day = 0; day < research.size(); day++) {
      if (analysis[day][cIdx] >= k) // 오늘 k번이상 검색된 경우
      {
        isOK[cIdx]++;

        // n일이상 k번 검색된 경우
        if (isOK[cIdx] >= n) {
          int count = 0;
          for (int i = 0; i < n; i++) {
            count += analysis[day - i][cIdx];
          }
          if (count >= 2 * n * k) {
            char c = cIdx + 'a';
            m[c]++;
          }
        }
      } else {
        isOK[cIdx] = 0;
      }
    }
  }

  string answer = "None";
  //최고의 검색어 찾기
  int max = 0;
  for (int cIdx = 0; cIdx < 26; cIdx++) {
    char c = cIdx + 'a';
    if (m[c] > max) {
      answer = c;
      max = m[c];
    }
  }

  return answer;
}

int main() {

  vector<string> research = {"yxxy", "xxyyy"};
  int n = 1;
  int k = 1;
  solution(research, n, k);
}