#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

#define PLUS 0
#define MINUS 1
#define MULTIPLY 2
#define DIVIDE 3

using namespace std;

long long max_value = -98765432101;
long long min_value = 98765432101;

long long calculate(long long a, long long b, long sign) {
  switch (sign) {
  case PLUS:
    return a + b;
  case MINUS:
    return a - b;
  case MULTIPLY:
    return a * b;
  case DIVIDE:
    return a / b;
  }
}
void solution(vector<long long> a, vector<long long> sign, long long sum,
              long long count) {

  if (count == a.size() - 1) {
    max_value = max(max_value, sum);
    min_value = min(min_value, sum);
  }

  //부호 별로 한번씩 다 시도
  for (int s = PLUS; s <= DIVIDE; s++) {
    if (0 < sign[s]) {
      sign[s]--;
      solution(a, sign, calculate(sum, a[count + 1], s), count + 1);
      sign[s]++;
    }
  }
}

int main() {

  long long n;
  scanf("%lld", &n);

  vector<long long> a(n, 0);
  for (long long i = 0; i < n; i++)
    scanf("%lld", &a[i]);

  vector<long long> sign(4, 0);
  //차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
  scanf("%lld %lld %lld %lld", &sign[PLUS], &sign[MINUS], &sign[MULTIPLY],
        &sign[DIVIDE]);

  solution(a, sign, a[0], 0);

  printf("%lld\n%lld", max_value, min_value);
}