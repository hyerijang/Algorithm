//솔
#include <bits/stdc++.h>

using namespace std;

#define REPORTER 0
#define REPORTED 1
vector<string> strCutting(string &str) {
  stringstream ss(str);
  vector<string> log;
  string tmp;
  while ((ss >> tmp)) {
    log.push_back(tmp);
    // cout << tmp << endl;
  }
  return log;
}
vector<int> solution(vector<string> id_list, vector<string> report, int k) {
  vector<vector<string>> reportList;

  for (auto &r : report) {
    vector<string> v = strCutting(r); // v[0] 신고자 v[1] 신고당한 사람
    reportList.push_back(v);
  }

  //메일 발송용 결과 테이블 초기화
  vector<map<string, int>> result;
  for (int i = 0; i < id_list.size(); i++) {
    map<string, int> v;
    result.push_back(v);
  }

  //유저가 신고당한 횟수
  map<string, int> reportedcount;

  for (auto &rl : reportList) {
    for (int i = 0; i < id_list.size(); i++) {
      if (rl[REPORTER] == id_list[i]) {
        if (result[i].find(rl[REPORTED]) ==
            result[i].end()) { //중복 신고 아닌 경우
          reportedcount[rl[REPORTED]]++;
        }
        result[i][rl[REPORTED]]++;
        break;
      }
    }
  }

  vector<int> answer(id_list.size(), 0);
  int idx = 0;
  for (auto &rl : result) {
    for (auto it = rl.begin(); it != rl.end(); it++) {
      if (reportedcount[it->first] >= k)
        answer[idx]++;
    }
    idx++;
  }
  return answer;
}
int main() {
  vector<string> id_list = {"muzi", "frodo", "apeach", "neo"};
  vector<string> report = {"muzi frodo", "apeach frodo", "frodo neo",
                           "muzi neo", "apeach muzi"};
  int k = 2;
  solution(id_list, report, k);
  return 0;
}