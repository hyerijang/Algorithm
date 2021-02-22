#include <iostream>
#include <queue>
using namespace std;

int main(int argc, const char **argv)
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, x;
    cin >> N;

    struct compare
    {
        bool operator()(int a, int b)
        {
            if (abs(a) == abs(b))
                return a > b;
            else
                return abs(a) > abs(b);
        }
    };

    priority_queue<int, vector<int>, compare> pq;
    queue<int> temp;

    for (int i = 0; i < N; i++)
    {
        cin >> x;
        if (x == 0)
        {
            //배열에서 절댓값이 가장 작은 값을 출력, 그 값을 배열에서 제거
            if (pq.empty())
            {
                cout << '0';
            }
            else
            {
                cout << pq.top();
                pq.pop();
            }
            cout << '\n';
        }
        else
        {
            //배열에 x 추가
            pq.push(x);
        }
    }

    return 0;
}