#include <cstdio>
#include <iostream>

#define ERASE 1
using namespace std;

int main() {

  int n, k;
  scanf("%d %d", &n, &k);

  int count = 0;

  bool arr[1001] = {};
  arr[0] = arr[1] = ERASE; //지워진 수
  int minI = 1;

  while (true) {
    if (!arr[minI]) { //아직 지워지지 않은 수면
      int p = minI;   // p는 소수

      // p의 배수를 모두 지운다.
      for (int i = 1; i * p <= n; i++) {
        if (!arr[i * p]) {
          count++;
          arr[i * p] = ERASE;

          if (count == k) {
            cout << i * p << endl;
            return 0;
          }
        }
      }
    }
    minI++;
  }
}