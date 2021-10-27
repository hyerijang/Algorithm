#include <stdio.h>
#include <vector>

#define max(x, y) x > y ? x : y
#define MAXH 1000000000

using namespace std;

long long tree[1000001];

long long solve(long long N, long long M, long long start, long long end) {

  while (start <= end) {

    long long mid = (start + end) / 2, total = 0;

    for (long long i = 0; i < N; i++) {
      if (tree[i] > mid)
        total = total + (tree[i] - mid);

      if (total >= M) {  // 나무 수량 초과하면
        start = mid + 1; //커팅 지점 낯추고
        break;           // for문 탈출
      }
    }

    if (total < M)   // 나무 수량이 부족하면
      end = mid - 1; // 커팅 지점을 높여봄
  }
  return end;
}

int main(int argc, const char **argv) {
  // 나무의 수 N
  // 상근이가 집으로 가져가려고 하는 나무의 길이 M
  long long N, M;
  scanf("%lld %lld", &N, &M);

  long long tallest = 0;
  for (long long i = 0; i < N; i++) {
    scanf("%lld", &tree[i]);
    tallest = max(tallest, tree[i]); //이부분이 문제 였던듯.
  }

  //이분 탐색으로 가능 한 값 탐색
  printf("%lld", solve(N, M, 0, tallest * 2));

  return 0;
}