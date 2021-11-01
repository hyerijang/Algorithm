// less example
#include <algorithm>  // std::sort, std::includes
#include <functional> // std::less
#include <iostream>   // std::cout

using namespace std;

int main() {
  int foo[] = {10, 20, 5, 15, 25};
  int bar[] = {15, 10, 20};
  std::sort(foo, foo + 5, std::less<int>()); // 5 10 15 20 25
  std::sort(bar, bar + 3, std::less<int>()); //   10 15 20

  cout << foo[0] << endl;
  if (std::includes(foo, foo + 5, bar, bar + 3,
                    std::less<int>())) // less인 경우에는
    std::cout << "foo includes bar.\n";
  return 0;
}