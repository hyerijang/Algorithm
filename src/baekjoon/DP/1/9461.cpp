// 파도반 수열

#include <stdio.h>
#include <vector>
using namespace std;

int main() {

  int T;
  scanf("%d,", &T);

  vector<long long> P;
  P.push_back(0);
  P.push_back(1); // P(1)
  P.push_back(1); // P(2)

  while (T--) {
    int N;
    scanf("%d,", &N);

    for (int i = P.size() - 2; i <= N - 2; i++) {
      P.push_back(P[i - 1] + P[i]);
    }

    printf("%lld\n", P[N]);
  }
}