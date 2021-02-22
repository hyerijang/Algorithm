#include <iostream>
#include <vector>
using namespace std;

#define V 6

int main(int argc, const char **argv)
{

    vector<int> w[V];

    w[1].push_back(2); //1에서 2로 향하는 이음선
    w[1].push_back(4); //1에서 4로 향하는 이음선
    w[2].push_back(3); //2에서 3로 향하는 이음선
    w[3].push_back(4); //3에서 4로 향하는 이음선
    w[4].push_back(2); //4에서 2로 향하는 이음선
    w[4].push_back(5); //4에서 5로 향하는 이음선

    for (int v : w[1])
        cout << v << " ";

    return 0;
}