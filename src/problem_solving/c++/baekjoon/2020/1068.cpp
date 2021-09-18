#include <iostream>
using namespace std;

typedef struct node *nodelink;
typedef struct node
{
    int data = -1;
    nodelink leftchild = NULL;
    nodelink rightchild = NULL;
} node;

int N;
int liveN;
node *tree;

void insert(int parentData, int Data)
{

    node *p = &tree[parentData];
    if (p->leftchild == NULL)
        p->leftchild = &tree[Data];
    else
        p->rightchild = &tree[Data];
    // cout << parentData << endl;
}

void initTree()
{

    tree = new node[N];
    for (int i = 0; i < N; i++)
        tree[i].data = i;

    //둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다.
    //만약 부모가 없다면 -1 (루트의 경우)

    int parentData;

    for (int i = 0; i < N; i++)
    {
        cin >> parentData;
        insert(parentData, i);
    }

    liveN = N;
}

void deleteNode(const int d, bool root)
{

    //부모로부터 해당 노드의 링크 삭제
    if (root)
        for (int p = d - 1; p >= 0; p--)
        {
            if (tree[p].leftchild == &tree[d])
            {
                tree[p].leftchild = NULL;
                break;
            }
            else if (tree[p].rightchild == &tree[d])
            {
                tree[p].rightchild = NULL;
                break;
            }
        }

    //자식들 삭제
    if (tree[d].leftchild != NULL)
    {
        node *leftC = tree[d].leftchild;
        deleteNode(leftC->data, false);
        leftC = NULL;
    }
    if (tree[d].rightchild != NULL)
    {
        node *rightC = tree[d].rightchild;
        deleteNode(rightC->data, false);
        rightC = NULL;
    }

    tree[d].data = -1;
    liveN--;
}

int numOfleaf()
{
    node *n;
    int notLeaf = 0;
    for (int i = 0; i < N; i++)
    {
        n = &tree[i];

        if (n->data != -1)
            if (n->leftchild != NULL || n->rightchild != NULL)
                notLeaf++;
    }

    return (liveN - notLeaf);
}

int main()
{

    // 트리의 노드의 개수 N
    cin >> N;

    initTree();

    int d;
    cin >> d;
    deleteNode(d, true);
    cout << numOfleaf();
    //셋째줄: 지울 노드의 번호
}