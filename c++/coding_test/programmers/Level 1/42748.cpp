// K번째 수
// https://programmers.co.kr/learn/courses/30/lessons/42748
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
  vector<int> answer;

  for (int i = 0; i < commands.size(); i++) {

    // i부터 j까지 자른 subarr 생성
    vector<int> subarr;
    for (int j = commands[i][0] - 1; j <= commands[i][1] - 1; j++) {

      subarr.push_back(array[j]);
    }

    //정렬
    sort(subarr.begin(), subarr.end());

    // answer에 k번째 원소 추가
    answer.push_back(subarr[commands[i][2] - 1]);
  }
  return answer;
}

int main() {

  char tmp;
  // array 입력
  vector<int> arr;
  while (true) {

    scanf("%c", &tmp);
    if (tmp <= '9' && tmp >= '0')
      arr.push_back(atoi(&tmp));
    if (tmp == ']')
      break;
  }

  // commands 입력
  vector<vector<int>> commands;
  scanf("%c", &tmp);

  while (true) {
    if (tmp == '[') {
      vector<int> v2;
      while (true) {
        scanf("%c", &tmp);
        if (tmp <= '9' && tmp >= '0')
          v2.push_back(atoi(&tmp));
        else if (tmp == ']') {
          commands.push_back(v2);
          break;
        }
      }
    }

    scanf("%c", &tmp);
    if (tmp == ']')
      break;
  }

  vector<int> answer = solution(arr, commands);

  printf("[");
  for (int i = 0; i < answer.size(); i++) {
    if (i != answer.size() - 1)
      printf("%d, ", answer[i]);
    else
      printf("%d]", answer[i]);
  }

  return 0;
}