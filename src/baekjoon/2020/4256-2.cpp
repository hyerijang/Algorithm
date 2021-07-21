#include <iostream>
#include <algorithm>
using namespace std;

int n;
int pre_order[1001], in_order[1001];

void post_order(int start, int end, int root)
{
    for (int i = start; i < end; ++i)
    {
        if (in_order[i] == pre_order[root])
        {
            post_order(start, i, root + 1);                 // 왼쪽 subtree 출력
            post_order(i + 1, end, root + (i - start + 1)); // 오른쪽 subtree 출력
            cout << pre_order[root] << ' ';                 //root 출력
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--)
    {
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> pre_order[i];
        for (int i = 0; i < n; ++i)
            cin >> in_order[i];

        post_order(0, n, 0);
        cout << '\n';
    }
    return 0;
}