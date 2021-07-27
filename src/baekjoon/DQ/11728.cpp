#include <stdio.h>

//정렬되어있는 두 배열 A와 B가 주어진다.
//두 배열을 합친다음 정렬하는 프로그램을 작성

int A[1000001] = {};
int B[1000001] = {};
void devide(int N, int M) {

  int a, b;
  a = b = 0;

  for (int i = 0; i < N + M; i++) {
    if (a < N && b < M) {
      if (A[a] < B[b])
        printf("%d ", A[a++]);
      else
        printf("%d ", B[b++]);
    } else if (a < N)
      printf("%d ", A[a++]);
    else
      printf("%d ", B[b++]);
  }
}
int main(int argc, char const *argv[]) {

  int N, M;
  scanf("%d %d", &N, &M);

  for (int i = 0; i < N; i++)
    scanf("%d", &A[i]);

  for (int i = 0; i < M; i++)
    scanf("%d", &B[i]);

  devide(N, M);

  return 0;
}
