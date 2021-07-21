#include <iostream>
#include <queue>
using namespace std;

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    priority_queue<int, vector<int>, greater<int>> pq; //최소힙
    int N;
    cin >> N;
    int tmp;

    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        if (tmp == 0)
        {
            if (pq.empty())
                cout << tmp;
            else
            {
                cout << pq.top();
                pq.pop();
            }
            cout << '\n';
        }

        else
            pq.push(tmp);
    }
    return 0;
}
