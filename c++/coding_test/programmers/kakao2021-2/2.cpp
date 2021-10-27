//솔
#include <bits/stdc++.h>

using namespace std;

vector<long long> s;
string str = "";

//가능한 모든 P 찾기
void find_all_numbers(int n, int k) {

  while (n > 0) {
    int left = n % k;
    n /= k;

    if (left == 0) {
      if (!str.empty()) {
        reverse(str.begin(), str.end());
        s.push_back(stoll(str));
      }
      str.clear();
    } else
      str += to_string(left);
  }
  if (!str.empty()) {
    reverse(str.begin(), str.end());
    s.push_back(stoll(str));
  }
}

bool isPrime(long long n) {
  if (n <= 1) {
    return false;
  }

  for (long long i = 2; i <= sqrt(n); i++) {
    if ((n % i) == 0) {
      return false;
    }
  }

  return true;
}

int solution(int n, int k) {
  find_all_numbers(n, k);

  int answer = 0;
  if (s.begin() == s.end())
    return answer;

  for (auto &it : s) {
    if (isPrime(it))
      answer++;
  }

  return answer;
}

int main() {

  int n = 1024 * 1024 - 1;
  int k = 3;

  cout << solution(n, k);
  return 0;
}