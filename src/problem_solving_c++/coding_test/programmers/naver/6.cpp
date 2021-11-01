//시간초과로 풀다 말았음
#include <bits/stdc++.h>

using namespace std;

#define UID 0
#define PID 1

vector<string> dates;

string dayBefor10;

string makeDayBefor10(const string &str) {

  istringstream iss(str);
  string tmp;

  int year, month, day;

  getline(iss, tmp, '-');
  year = stoi(tmp);
  getline(iss, tmp, '-');
  month = stoi(tmp);
  getline(iss, tmp, '-');
  day = stoi(tmp);

  day = day - 9;
  if (day <= 0) {
    month--;
    day += 30;
  }
  if (month <= 0) {
    year--;
    month += 12;
  }

  return to_string(year) + '-' + to_string(month) + '-' + to_string(day);
};

vector<int> cut(const string &str) {
  //문자열 자르기
  vector<int> log;

  string tmp;

  stringstream ss(str);
  while ((ss >> tmp)) {
    if (tmp.front() == 'u' || tmp.front() == 'p') {
      tmp = tmp.substr(3); // uid, pid는 생략하고 저장
      log.push_back(stoi(tmp));
      // cout << tmp << endl;
    } else
      dates.push_back(tmp);
  }

  return log;
}

bool isOK(int idx, string date) {
  //지정 일자 초과
  if (dates[idx] > date || dates[idx] < dayBefor10)
    return false;

  return true;
}
//기준 날짜를 포함한 10일간
//따라서 2월 26일부터 3월 5일까지의 기록을 바탕으로 계산
vector<string> solution(vector<string> records, int k, string date) {

  vector<vector<int>> recs;
  for (auto &str : records) {
    recs.push_back(cut(str));
  }

  dayBefor10 = makeDayBefor10(date);

  vector<bool> available(recs.size(), false);
  for (int idx = 0; idx < recs.size(); idx++) {
    available[idx] = isOK(idx, date);
  }

  for (int idx = 0; idx < recs.size(); idx++) {
    if (available[idx])
      if (recs[UID])
  }

  vector<string> answer;
  cout << date;
  return answer;
}

int main() {

  vector<string> records = {
      "2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1",
      "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3",
      "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1",
      "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3",
      "2020-03-06 uid1 pid4"};
  int k = 10;
  string date = "2020-03-05";
  solution(records, k, date);
}