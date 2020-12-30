#include <stdio.h>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int N;
int *list;

void partition(int start, int end, int &pivotpoint)
{

	int i, j;
	j = start;

	const int pivotitem = list[start];

	for (i = start + 1; i <= end; i++)
	{
		if (pivotitem >= list[i])
		{
			j++;
			swap(list[i], list[j]);
		}
	}
	pivotpoint = j;
	swap(list[pivotpoint], list[start]);
}
void quicksort(int start, int end)
{

	if (start >= end)
		return;

	//1.분할
	int pivotpoint = start;
	partition(start, end, pivotpoint);
	//2.정복
	quicksort(start, pivotpoint - 1);
	quicksort(pivotpoint + 1, end);
}

int main()
{
	scanf("%d", &N);
	int index = N;
	int k = 0;
	list = new int[N];
	while (index--)
	{
		scanf("%d", &list[k++]);
	}

	quicksort(0, N - 1);

	for (index = 0; index < N; index++)
		printf("%d\n", list[index]);

	return 0;
}