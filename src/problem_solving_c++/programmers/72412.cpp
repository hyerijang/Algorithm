// https://programmers.co.kr/learn/courses/30/lessons/72412
//순위 검색
#include <bits/stdc++.h>

using namespace std;

vector<vector<string>> stringConvertor(vector<string> &v) {
  vector<vector<string>> result;
  for (auto it = v.begin(); it != v.end(); ++it) {
    stringstream ss(*it);
    vector<string> log;
    string tmp;
    while ((ss >> tmp)) {
      if (tmp != "and")
        log.push_back(tmp);
    }
    result.push_back(log);
  }

  return result;
}

vector<int> solution(vector<string> info, vector<string> query) {

  vector<vector<string>> infologs = stringConvertor(info);
  vector<vector<string>> querylogs = stringConvertor(query);

  vector<int> answer;
  for (int qurIdx = 0; qurIdx < querylogs.size(); qurIdx++) {
    vector<bool> isOk(infologs.size(), true);
    int ans = infologs.size(); //전체 유저 수로 초기화
    for (int user = 0; user < infologs.size(); user++) {
      if (stoi(querylogs[qurIdx][4]) >
          stoi(infologs[user][4])) { //점수 미달인 경우
        // cout << user << " 탈락" << endl;
        isOk[user] = false; //그 유저는 다음부터 검색에서 제외
        ans--;
      }

      for (int c = 0; c < 4; c++) { //남은 조건은 5개
        if (!isOk[user])
          break;

        if (querylogs[qurIdx][c] != "-") { //조건 c가 고려해야 할 조건일 때
          if (querylogs[qurIdx][c] != infologs[user][c]) // info와 같지 않으면{
          {
            // cout << user << " 탈락" << endl;
            isOk[user] = false; //그 유저는 다음부터 검색에서 제외
            ans--;
          }
        }
      }
    }
    cout << qurIdx << " : " << ans << endl;
    answer.push_back(ans);
  }

  return answer;
}

int main() {

  vector<string> info = {"java backend junior pizza 150",
                         "python frontend senior chicken 210",
                         "python frontend senior chicken 150",
                         "cpp backend senior pizza 260",
                         "java backend junior chicken 80",
                         "python backend senior chicken 50"};
  vector<string> query = {"java and backend and junior and pizza 100",
                          "python and frontend and senior and chicken 200",
                          "cpp and - and senior and pizza 250",
                          "- and backend and senior and - 150",
                          "- and - and - and chicken 100",
                          "- and - and - and - 150"};

  // vector<string> query = {"- and backend and senior and - 150"};

  solution(info, query);

  return 0;
}