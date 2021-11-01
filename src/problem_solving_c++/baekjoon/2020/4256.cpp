//1991 트리 순회

#include <iostream>
#include <string>

using namespace std;

typedef struct node *nodelink;
typedef struct node
{
    char data;
    nodelink leftchild = NULL;
    nodelink rightchild = NULL;
} node;

int N;
node *tree;
int *inorder, preorder;

void insert(int parentData, int leftData, int rightData)
{

    node *p = &tree[parentData];
    if (leftData != '.')
        p->leftchild = &tree[leftData];
    if (rightData != '.')
        p->rightchild = &tree[rightData];
    // cout << parentData << endl;
}

void initTree(start, end)
{

    int rootData = preorder[start];
    int leftCount;
    for (int i = start; i <= end; i++)
    {
        if (inorder[i] != rootData)
            leftCount++;
        else
            break;
    }
}

void postorder(node *tree)
{
    //왼쪽 자식 - >  오른쪽 자식 -> 부모

    if (tree->leftchild != NULL)
        postorder(tree->leftchild);
    if (tree->rightchild != NULL)
        postorder(tree->rightchild);
    cout << tree->data;
}
int main()
{

    cin >> N;

    tree = new node[N + 1];
    for (int i = 1; i < N; i++)
        tree[i].data = i;

    preorder = new int[N + 1];
    for (int i = 1; i <= N; i++)
        cin >> preorder[i];
    inorder = new int[N + 1];
    for (int i = 1; i <= N; i++)
        cin >> inorder[i];
    initTree(1, N);
    // postorder(tree[1]);

    cout << '\n';

    return 0;
}
