//솔
#include <bits/stdc++.h>

using namespace std;

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

int timeToint(string str) { //분 단위로 변환
  istringstream iss(str);
  string hours;
  getline(iss, hours, ':');
  string minutes;
  getline(iss, minutes, ':');

  int time = stoi(hours) * 60 + stoi(minutes);
  return time;
}

vector<int> solution(vector<int> fees, vector<string> records) {
  vector<vector<string>> recs;
  map<string, int> carList;
  //문자열 자름
  for (auto &r : records) {
    vector<string> v = strCutting(r);
    recs.push_back(v);
    carList[v[1]]++;
  }

  map<string, int> carInOutTime; //출입출차 시간 기록
  map<string, int> carTotalTime; //총 주차 시간 기록

  for (auto &r : recs) {
    int time = timeToint(r[0]);
    int tmp = 0;
    auto iter = carInOutTime.find(r[1]);
    if (iter != carInOutTime.end()) { //입차 기록 있음
      tmp = time - carInOutTime[r[1]];
      carTotalTime[r[1]] += tmp;
      cout << r[1] << " : " << time << " - " << carInOutTime[r[1]] << " = "
           << tmp << endl;
      carInOutTime.erase(iter);
    } else
      carInOutTime[r[1]] = time;
  }

  int maxTime = 23 * 60 + 59;
  for (auto &i : carInOutTime) {
    int tmp = maxTime - i.second;
    carTotalTime[i.first] += tmp;
    carInOutTime[i.first] = 0; //기록 삭제
  }

  //자동차별 주차 요금
  vector<int> answer;

  for (auto &t : carTotalTime) {
    int totalfee = fees[1]; // 기본 요금
    if (t.second > fees[0]) //기본 시간 초과인 경우
    {
      int addTime = ((t.second - fees[0]) / fees[2]);
      if ((t.second - fees[0]) % fees[2]) //올림
        addTime++;
      totalfee += addTime * fees[3];
    }
    answer.push_back(totalfee);
  }

  return answer;
}

int main() {

  vector<int> fees = {1, 461, 1, 10};

  vector<string> records = {"00:00 1234 IN"};

  solution(fees, records);
  return 0;
}