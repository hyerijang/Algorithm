#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{

    int K;
    cin >> K;

    vector<int> stack;
    int n, sum = 0;
    for (int i = 0; i < K; i++)
    {
        cin >> n;

        if (n)
        {
            stack.push_back(n);
            sum += n;
        }
        else
        {
            n = stack[stack.size() - 1];
            stack.pop_back();
            sum -= n;
        }
    }

    cout << sum;
    return 0;
}
