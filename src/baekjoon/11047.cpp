//타로가 지불할 돈(1 이상 1000미만의 정수)
//받을 잔돈에 포함된 잔돈의 개수를 구하기
//500엔, 100엔, 50엔, 10엔, 5엔, 1엔

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N, K;
vector<int> coin;

int getTheNumOfCoins(int l)
{
    int result = 0;
    for (int i = 0; i < N; i++)
    {
        result += l / coin[i];
        l %= coin[i];
    }
    return result;
}

bool compare(int x, int y)
{
    return x > y;
}

int main()
{
    cin >> N >> K;
    int tmp = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        coin.push_back(tmp);
    }
    sort(coin.begin(), coin.end(), compare);

    cout << getTheNumOfCoins(K);

    return 0;
}