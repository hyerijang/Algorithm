#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <vector>

#define SET 1;
using namespace std;

int main(int argc, char const *argv[]) {

  int N; // 도현이네 집 개수
  int C; // 공유기의 개수
  scanf("%d %d", &N, &C);

  long long loc[200001] = {};

  for (int i = 0; i < N; i++) {
    scanf("%lld", &loc[i]);
  }

  //오름차순 정렬
  sort(loc, loc + N);

  //목표 : 가장 인접한 두 공유기 사이의 거리를 최대로 하기

  vector<long long> arr;
  // 양 끝에 공유기 설치
  arr.push_back(loc[0]);
  arr.push_back(loc[N - 1]);
  int c = C - 2;

  //인접한 두 공유기의 최소 거리
  long long minimum = 1000000001;

  while (c > 0) {
    for (int i = 1; i < arr.size(); i++) {
      if (arr[i] - arr[i - 1] <
          minimum) { // 두 공유기 사이 거리가 더 짧아졌으면 갱신
        start = arr[i - 1];
        end = arr[i];
        minimum = arr[i] - arr[i - 1];
      }
    }
  }

  return 0;
}
