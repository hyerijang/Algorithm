//어려워서 중간에 포기
#include <bits/stdc++.h>

using namespace std;
#define REQUEST_TIME 0
#define TIME_REQUIRED 1
#define CATEGORY 2
#define IMPORTANT 3

bool isOK[10001] = {};

int priority[10001] = {};
vector<int> solution(vector<vector<int>> jobs) {

  // jobs는 요청 시각을 기준으로 오름차순 정렬되어 있습니다.

  vector<vector<int>> category;
  for (int i = 0; i <= 10000; i++) {
    vector<int> v;
    category.push_back(v);
  }

  //분류별로 작업 인덱스 저장
  for (int i = jobs.size() - 1; i >= 0; i--) {
    category[jobs[i][CATEGORY]].push_back(i);
  }

  int rest = jobs.size();
  int targetIdx = 0;
  long long currentTime = jobs[targetIdx][REQUEST_TIME];

  vector<int> answer;
  while (rest > 0) {
    currentTime += jobs[targetIdx][TIME_REQUIRED];
    rest--;
    category[jobs[targetIdx][CATEGORY]].pop_back();

    //다음 작업 지정
    int nextIdx = category[jobs[targetIdx][CATEGORY]].back();
    if (jobs[nextIdx][REQUEST_TIME] <= currentTime) {
      //현재 작업과 분류 같은 작업이 요청되어 있음
      targetIdx = nextIdx;
    } else {
      //다른 분류의 작업 탐색
      int tmpIdx = 0;
      memset(priority, 0, sizeof(priority));
      int mostImp_category = 0;
      while (jobs[tmpIdx][REQUEST_TIME] <= currentTime &&) {
        priority[jobs[tmpIdx][CATEGORY]] += jobs[tmpIdx][IMPORTANT];
        if (priority[jobs[tmpIdx][CATEGORY]] > priority[mostImp_category])
          mostImp_category = jobs[tmpIdx][CATEGORY];

        tmpIdx++;
      }
    }
  }
  return answer;
}

int main() {

  vector<vector<int>> jobs = {{1, 5, 2, 3}, {2, 2, 3, 2}, {3, 1, 3, 3},
                              {5, 2, 1, 5}, {7, 1, 1, 1}, {9, 1, 1, 1},
                              {10, 2, 2, 9}};

  solution(jobs);
}