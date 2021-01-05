#include <iostream>
// std::swap()
#include <algorithm> // C++11 이전
#include <utility>   // C++11 이후

int main()
{
    int x = 2;
    int y = 4;
    std::cout << "Before swap: x = " << x << ", y = " << y << '\n';
    std::swap(x, y); // swap the values of x and y
    std::cout << "After swap: x = " << x << ", y = " << y << '\n';
}
