#include <cstdio>

int n = 9;
int heap[9] = {1, 5, 2, 9, 3, 4, 7, 8, 6};

void makeheap()
{

    for (int i = 1; i < n; i++)
    {
        int child = i;
        do
        {
            //root : 자기 자신의 부모
            int root = (child - 1) / 2;
            if (heap[root] < heap[child])
            {
                int temp = heap[root];
                heap[root] = heap[child];
                heap[child] = temp;
            }

            child = root;

        } while (child != 0);
    }
}

void sortheap()
{
    for (int i = n - 1; i >= 0; i--)
    {
        int temp = heap[0];
        heap[0] = heap[i];
        heap[i] = temp;
        int root = 0;
        int c = 1;
        do
        {
            c = 2 * root + 1; //c는 왼쪽 자식
            //자식들 중 큰값 찾기
            if (heap[c] < heap[c + 1] && c < i - 1)
            {
                c++;
            }
            //루트보다 자식이 더 크다면 교환
            if (heap[root] < heap[c] && c < i)
            {
                int temp = heap[root];
                heap[root] = heap[c];
                heap[c] = temp;
            }
            root = c;

        } while (c < i);
    }
}

void printheap()
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", heap[i]);
    }
    printf("\n");
}
int main()
{

    makeheap();
    sortheap();
    printheap();

    return 0;
}
