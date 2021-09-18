#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <vector>

#define max(x, y) x > y ? x : y

using namespace std;

int main(int argc, char const *argv[]) {

  int N; // 도현이네 집 개수
  int C; // 공유기의 개수
  scanf("%d %d", &N, &C);

  long long loc[200001] = {};

  for (int i = 0; i < N; i++) {
    scanf("%lld", &loc[i]);
  }

  //집을 오름차순 정렬
  sort(loc, loc + N);

  //목표 : 가장 인접한 두 공유기 사이의 거리를 최대로 하기
  // start는 1로 설정 (최소거리 1)
  long long start = 1, end = 2000000002;

  long long result = 0; //가장 인접한 두 공유기 사이의 최대 거리
  while (true) {

    if (start > end)
      break;

    long long dist = (start + end) / 2; // mid는 최소 공유기의 거리

    // loc[0]에는 무조건 공유기가 설치된다고 가정한다.
    long long total = 1;

    int lastIdx = 0; //마지막으로 공유기가 설치된 집의 인덱스
    for (int i = 1; i < N; i++) {
      if (dist <= loc[i] - loc[lastIdx]) {
        total++;
        lastIdx = i;
      }

      if (total == C) //설치된 공유기 숫자가 목표 달성시
      {
        result = max(result, dist); // 최대 간격이면 갱신하고
        start = dist + 1;           // 공유기 간 거리를 늘려본다.
        break;
      }
    }

    if (total < C) {  //설치된 공유기 숫자가 부족하면
      end = dist - 1; //공유기 간 거리를 줄인다.
    }
  }

  printf("%lld", result);

  return 0;
}
