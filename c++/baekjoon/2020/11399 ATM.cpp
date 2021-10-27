#include <cstdio>
#include <algorithm>
int N;
int *P;

using namespace std;

void printP()
{
    for (int i = 0; i < N; i++)
    {
        printf("%d ", P[i]);
    }
    printf("\n");
}

int getTimeofATM()
{
    sort(P, P + N);
    // printP();
    int sum = 0;
    for (int i = 0; i < N; i++)
    {
        int j = 0;
        while (j < N - i)
        {

            sum += P[i];
            j++;
        }
    }
    return sum;
}
int main()
{
    scanf("%d", &N);

    P = new int[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &P[i]);
    }
    printf("%d\n", getTimeofATM());
}
