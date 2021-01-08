
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
vector<int> rope;

int getMaxWeight()
{
    int maxW = rope[0];
    int weight;
    //사용할 로프의 개수 (n)
    for (int n = 2; n <= N; n++)
    {

        if (maxW < (weight = rope[n - 1] * n))
            maxW = weight;
    }
    return maxW;
}

bool compare(int x, int y)
{
    return x > y;
}

int main()
{
    cin >> N;
    int tmp = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        rope.push_back(tmp);
    }
    sort(rope.begin(), rope.end(), compare);

    cout << getMaxWeight();

    return 0;
}