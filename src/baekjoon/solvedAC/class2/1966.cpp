
// 프린터 큐
// 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때,
// 어떤 한 문서가 몇 번째로 인쇄되는지 알아내기
// 중요도 9 : 가장 우선 순위 높음
// 중요도 1 : 가장 우선 순위 낮음
// 중요도가 같은 문서가 여러개 있을 수 있음.

#include <stdio.h>
#include <vector>

using namespace std;

int cal() {

  int N; // 문서의 개수
  int M; // 궁금한 문서가 큐의 몇번째에 놓여있는지
  scanf("%d %d", &N, &M);
  vector<int> queue(N, 0);
  int p[10] = {}; // 0으로 초기화

  //중요도 입력
  for (int i = 0; i < N; i++) {
    scanf("%d", &queue[i]);
    p[queue[i]]++;
  }

  int result = 0;

  int pointer = 0;
  for (int i = 9; i > 0; i--) {
    //우선순위 9부터 1까지
    if (p[i] == 0) //중요도 i인 문서 없으면 다음 중요도
      continue;

    while (p[i]) {
      if (queue[pointer] == i) {
        //포인터가 가리키는 문서가 중요도 가장 높은 문서이면 출력 (0)
        queue[pointer] = 0;
        result++;
        p[i]--;
        if (pointer == M) { // M번째 문서이면 결과 리턴
          return result;
        }
      }
      //큐의 끝까지 갔으면 포인터 처음으로 변경
      pointer++;
      if (pointer == N)
        pointer = 0;
    }
  }

  return -1;
}

int main() {

  int T;
  scanf("%d", &T);

  while (T--) {
    printf("%d\n", cal());
  }
}