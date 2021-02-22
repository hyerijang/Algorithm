#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main()
{

    int N, K;
    cin >> N >> K;

    set<int> sensorList;
    for (int i = 0; i < N; i++)
    {
        int tmp;
        cin >> tmp;
        sensorList.insert(tmp);
    }

    auto iter = sensorList.begin();
    int prvData = *iter++;

    vector<int> area;
    while (iter != sensorList.end())
    {
        area.push_back(*iter - prvData);
        prvData = *iter++;
    }

    sort(area.begin(), area.end());

    int count = K - 1;
    while (count-- && area.size())
        area.pop_back();

    int sum = 0;
    for (int i = 0; i < area.size(); i++)
    {
        sum += area[i];
    }
    cout << sum;
}
