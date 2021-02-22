#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(pair<int, int> a, pair<int, int> b)
{
    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<pair<int, int>> request;

    for (int i = 0; i < N; ++i)
    {
        int start, end;
        cin >> start >> end;
        request.push_back(make_pair(start, end));
    }

    //빨리 끝나는 순으로 정렬
    sort(request.begin(), request.end(), comp);

    int count = 1;
    int iLast = N - 1; //가장 늦게 끝나는 회의의 인덱스
    int endedTime = request[0].second;
    for (int i = 1; i < request.size(); i++)
    {
        if (endedTime <= request[i].first)
        {
            endedTime = request[i].second;
            count++;
        }
    }
    cout << count;
}