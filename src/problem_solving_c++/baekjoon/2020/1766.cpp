#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

struct compare
{
    bool operator()(pair<int, int> &A, pair<int, int> &B)
    {

        //추가 정보 없는 경우
        if (A.second && B.second)
            return A.first > B.first;

        //먼저 풀면 좋은 문제 없는 경우끼리 비교 경우
        else if (!A.second && !B.second)
        {
            return A.second < B.second;
        }
        //먼저 풀면 좋은 문제 있는 겨우
        else if (A.second || B.second)
        {
            if (A.second)
                return A.second >= B.first;
        }
    }
};

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; //문제의 수
    cin >> N;

    int M; //우선순위 정보
    cin >> M;

    // 우선순위 정하기
    int *p_second = new int[N + 1]{};
    int A, B;
    for (int i = 1; i <= M; i++)
    {
        cin >> A;
        cin >> B;

        if (p_second[B] < A)
            p_second[B] = A;
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq; //최소힙

    for (int i = 1; i <= N; i++)
    {
        pq.push(make_pair(i, p_second[i]));
    }
    for (int i = 1; i <= N; i++)
    {

        cout << pq.top().first << ' ';
        pq.pop();
    }
    return 0;
}
