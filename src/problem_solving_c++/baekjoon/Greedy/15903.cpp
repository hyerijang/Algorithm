#include <algorithm>
#include <cstdio>
#include <queue>

using namespace std;

int main() {
  priority_queue<long long, vector<long long>, greater<long long>> pq;

  int n, m;
  scanf("%d %d", &n, &m);

  for (int i = 0; i < n; i++) {

    long long tmp;
    scanf("%lld", &tmp);
    pq.push(tmp);
  }

  for (int i = 0; i < m; i++) {

    long long a = pq.top();
    pq.pop();

    long long b = pq.top();
    pq.pop();

    pq.push(a + b);
    pq.push(a + b);
  }

  long long result = 0;
  while (!pq.empty()) {
    result += pq.top();
    pq.pop();
  }

  printf("%lld", result);
}