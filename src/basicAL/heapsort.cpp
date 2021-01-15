#include <cstdio>

int n = 9;
int heap[9] = {1, 5, 2, 9, 3, 4, 7, 8, 6};

void makeheap()
{

    //1번 노드부터 탐색
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
        //가장 끝에 있는 노드와 root노드 교환
        int temp = heap[0];
        heap[0] = heap[i];
        heap[i] = temp;

        //새로운 root에서부터 아래로 내려간다.
        int root = 0;
        int c = 1;
        do
        {
            c = 2 * root + 1; //c는 왼쪽 자식
            //자식들 중 큰값 찾기 == c
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
