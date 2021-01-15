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

void insert(char parentData, char leftData, char rightData)
{

    node *p = &tree[parentData - 'A'];
    if (leftData != '.')
        p->leftchild = &tree[leftData - 'A'];
    if (rightData != '.')
        p->rightchild = &tree[rightData - 'A'];
    // cout << parentData << endl;
}

void initTree()
{

    tree = new node[N];
    for (int i = 0; i < N; i++)
        tree[i].data = 'A' + i;

    string parentData;
    string leftData;
    string rightData;

    for (int i = 0; i < N; i++)
    {
        cin >> parentData;
        cin >> leftData;
        cin >> rightData;
        insert(parentData[0], leftData[0], rightData[0]);
    }
}

void preorder(node *tree)
{
    //부모 -> 왼쪽 자식 - > 오른쪽 자식

    cout << tree->data;
    if (tree->leftchild != NULL)
        preorder(tree->leftchild);
    if (tree->rightchild != NULL)
        preorder(tree->rightchild);
}

void inorder(node *tree)
{
    //왼쪽 자식 - >  부모 -> 오른쪽 자식

    if (tree->leftchild != NULL)
        inorder(tree->leftchild);
    cout << tree->data;
    if (tree->rightchild != NULL)
        inorder(tree->rightchild);
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
    initTree();
    preorder(tree);
    cout << '\n';
    inorder(tree);
    cout << '\n';
    postorder(tree);

    cout << '\n';

    return 0;
}
