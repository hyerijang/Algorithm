#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> list;
vector<int> templist;

void merge(int start, int end, int mid)
{

    int i = start;
    int j = mid + 1;
    while (i <= mid && j <= end)
    {
        if (list[i] > list[j])
            templist.push_back(list[i++]);
        else
            templist.push_back(list[j++]);
    }

    while (i <= mid)
        templist.push_back(list[i++]);
    while (j <= end)
        templist.push_back(list[j++]);

    for (int a = end; a >= start; a--)
    {
        list[a] = templist.back();
        templist.pop_back();
    }
}

void mergesort(int start, int end)
{
    if (start >= end)
        return;
    int mid = (start + end) / 2;

    mergesort(start, mid);
    mergesort(mid + 1, end);
    merge(start, end, mid);
}
int main()
{
    char temp;
    while (true)
    {
        temp = cin.get();
        if (temp == EOF || temp == '\0' || temp == '\n')
            break;
        if (temp - 48 >= 0 && temp - 48 <= 9)
            list.push_back(temp - 48); // 문자를 int로 변환
    }
    cin.ignore();
    mergesort(0, list.size() - 1);

    for (int i = list.size() - 1; i >= 0; i--)
        printf("%d", list[i]);
}