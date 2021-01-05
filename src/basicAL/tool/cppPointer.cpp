#include <cstdio>
#include <iostream>

int main()
{

    int N = 5;
    int* ptr = &N;

    std::cout << &N << '\n';
    std::cout << ptr << '\n';
    std::cout << *ptr << '\n';
}