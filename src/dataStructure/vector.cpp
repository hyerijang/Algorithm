#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> v = {1, 2, 3, 4, 5};

  //   vector<int>::iterator iter = v.begin();

  for (auto it = v.begin(); it != v.end(); ++it) {

    printf("%d", *it);
  }
}