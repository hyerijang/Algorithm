#include <stdio.h>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int N;
short *list;

int partition(int start, int end)
{

    int pivot = start;
    int pivotitem = list[pivot];

    for (int i = start + 1; i <= end; i++)
    {
        if (pivotitem > list[i])
        {
            pivot++;
            swap(list[pivot], list[i]);
        }
    }
    swap(list[pivot], list[start]);
    return pivot;
}

void quicksort(int start, int end)
{
    if (start == end)
        return;
    int pivot = partition(start, end);
    quicksort(start, pivot);
    quicksort(pivot + 1, end);
}

int main()
{
    scanf("%d", &N);
    int index = N;
    int k = 0;
    list = new short[N];
    while (index--)
    {
        scanf("%hd", &list[k++]);
    }

    quicksort(0, N - 1);

    for (index = 0; index < N; index++)
        printf("%hd\n", list[index]);

    delete list;
    return 0;
}