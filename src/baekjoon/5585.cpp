//타로가 지불할 돈(1 이상 1000미만의 정수)
//받을 잔돈에 포함된 잔돈의 개수를 구하기
//500엔, 100엔, 50엔, 10엔, 5엔, 1엔

#include <iostream>
using namespace std;

int coin[6] = {500, 100, 50, 10, 5, 1};

int getTheNumOfCoins(int l)
{
    int result = 0;
    for (int i = 0; i < 6; i++)
    {
        result += l / coin[i];
        l %= coin[i];
    }
    return result;
}

int main()
{

    int price = 0;
    cin >> price;
    cout << getTheNumOfCoins(1000 - price);

    return 0;
}