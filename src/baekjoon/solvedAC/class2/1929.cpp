// 소수 구하기
// M이상 N이하의 소수를 모두 출력
// (1 ≤ M ≤ N ≤ 1,000,000)
#include <math.h>
#include <stdio.h>
#include <vector>

using namespace std;
int main() {
  int m, n;
  scanf("%d %d", &m, &n);

  bool isPrimeNum = true;

  vector<int> arr;

  for (int i = 0; i <= n; i++) {
    arr.push_back(i);
  }

  arr[0] = 1;
  arr[1] = 1; //소수 아님
  int maxPrime = 1;
  for (int i = 2; i <= n; i++) {
    if (arr[i] != 1)
      maxPrime = i;

    if ((unsigned int)pow(maxPrime, 2) > n)
      break;

    for (int j = pow(maxPrime, 2); j <= n; j++) {
      if (arr[j] != 1)
        if (arr[j] % maxPrime == 0) {
          arr[j] = 1; // 소수 아님
        }
    }
  }

  for (int i = m; i <= n; i++) {
    if (arr[i] != 1)
      printf("%d\n", i);
  }
}