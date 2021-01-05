// #2751  heapsort

#include <stdio.h>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int number = 9;
int heap[9] = {1, 2, 6, 8, 3, 5, 4, 7, 9};

class Heap
{
    int heapsize;
    int maxsize;
    int *list;

public:
    Heap(int maxsize)
    {
        heapsize = 0;
        this->maxsize = maxsize;
        list = new int[maxsize];
        /*
        조사식 쓰는법 
            *(int(*)[5])(h).list
        OR
            *h.list@5
        */
    }

    void push(int item)
    {
        list[heapsize] = item;
        heapsize++;
    }
};

int main()
{
    int *hl = new int[9];
    hl[0] = 9;
    hl[1] = 6;
    hl[2] = 7;

    Heap h = Heap(50);
    h.push(3);
    h.push(5);
    h.push(9);
    h.push(7);
    return 0;
}