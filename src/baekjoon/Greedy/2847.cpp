#include <cstdio>

using namespace std;
int main() {

  int n;
  scanf("%d", &n);

  int arr[100] = {};
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }

  int count = 0;
  for (int i = n - 1; i >= 0; i--) {
    for (int j = i - 1; j >= 0; j--) {
      if (arr[i] <= arr[j]) {
        count += (arr[j] - arr[i]) + 1;
        arr[j] = arr[i] - 1;
      }
    }
  }

  printf("%d\n", count);
}