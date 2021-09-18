#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int data = -1)
    {
        this->data = data;
        this->next = NULL;
    }
};

class Mystack
{
public:
    Node *top;
    Mystack()
    {
        top = NULL;
    }
    void push(int data)
    {
        Node *temp = new Node(data);
        if (empty())
            top = temp;

        else
        {
            temp->next = top;
            top = temp;
        }
    }

    int pop()
    {
        if (empty())
        {
            return -1;
        }
        else
        {

            int result = top->data;
            Node *dNode = top;
            top = top->next;
            delete dNode;
        }
    }

    bool empty()
    {
        if (top == NULL)
            return true;
        else
            return false;
    }
};

int main()
{
    Mystack st;
    st.push(3);
    st.push(4);
    st.push(5);
    st.pop();
    st.pop();
    st.pop();
    st.pop();
}
