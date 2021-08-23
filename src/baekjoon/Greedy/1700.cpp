#include <bits/stdc++.h>
using namespace std;
typedef vector<int>::iterator iter;

vector<int> input, P;
int n, k, ct;

int main() {
  cin >> n >> k;
  for (int i = 0; i < k; ++i) {
    int in;
    cin >> in;
    input.push_back(in);
  }

  for (iter it = input.begin(); it != input.end(); ++it) {
    if (find(P.begin(), P.end(), *it) != P.end())
      continue;

    if (P.size() < n) {
      P.push_back(*it);
      continue;
    }

    iter last = it, idx = P.begin();
    for (iter t = P.begin(); t != P.end(); ++t) {
      iter temp = find(it + 1, input.end(), *t);

      if (temp > last) {
        idx = t;
        last = temp;
      }
    }

    *idx = *it;
    ct++;
  }
  cout << ct;
}