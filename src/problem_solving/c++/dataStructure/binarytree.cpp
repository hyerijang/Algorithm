#include <iostream>

using namespace std;

int number = 15;
//struct node * 를 treePointer로 지정
typedef struct node *treePointer;
//struct node 를 node로 지정
typedef struct node
{
    int data;
    treePointer left, right;
} node;

void preorder(treePointer ptr)
{
    if (ptr)
    {
        cout << ptr->data << ' ';
        preorder(ptr->left);
        preorder(ptr->right);
    }
}
void inorder(treePointer ptr)
{
    if (ptr)
    {
        preorder(ptr->left);
        cout << ptr->data << ' ';
        preorder(ptr->right);
    }
}
void postorder(treePointer ptr)
{
    if (ptr)
    {
        preorder(ptr->left);
        preorder(ptr->right);
        cout << ptr->data << ' ';
    }
}

int main(int argc, const char **argv)
{
    node nodes[number + 1];
    for (int i = 1; i <= number; i++)
    {
        nodes[i].data = i;
        nodes[i].left = NULL;
        nodes[i].right = NULL;
    }

    for (int i = 1; i <= number; i++)
    {
        if (i % 2 == 0)
            nodes[i / 2].left = &nodes[i];
        else
            nodes[i / 2].right = &nodes[i];
    }

    preorder(&nodes[1]);
    return 0;
}