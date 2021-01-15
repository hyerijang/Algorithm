//실패한 코드
//heap에서 노드가 짝수 개 일때 right node가 없다는 걸 놓침.

#include <cstdio>
#include <iostream>
using namespace std;

int n = 9;
int heap[9] = {1, 5, 2, 9, 3, 4, 7, 8, 6};

//힙? 부모 노드가 자식노드 보다 큰 것

void heapify()
{
    // 봐야하는 노드의 개수 = n / 2
    for (int parent = n / 2; parent >= 0; parent--)
    {
        int leftC = parent * 2 + 1;
        int rightC = leftC + 1;

        if (heap[rightC] > heap[parent] && rightC < n)
            swap(heap[rightC], heap[parent]);
        if (heap[leftC] > heap[parent])
            swap(heap[leftC], heap[parent]);
    }
}

void heapsort()
{
    if (n == 1)
        return;
    heapify();
    //root를 맨 뒤로 보냄
    int end = n - 1;
    swap(heap[0], heap[end]);
    n--;
    heapsort();
}

int main(int argc, const char **argv)
{
    heapsort();
    return 0;
}
