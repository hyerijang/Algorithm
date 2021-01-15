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

class Myqueue
{
private:
    Node *front;
    Node *end;

public:
    Myqueue()
    {
        end = NULL;
    }
    void insert(int data)
    {
        Node *temp = new Node(data);
        if (empty())
        {
            end = temp;
            front = temp;
        }

        else
        {
            front->next = temp;
            front = temp;
        }
    }

    int remove()
    {
        if (empty())
        {
            return -1;
        }
        else
        {

            int result = end->data;
            Node *dNode = end;
            end = end->next;
            delete dNode;
        }
    }

    bool empty()
    {
        if (end == NULL)
            return true;
        else
            return false;
    }
};

int main()
{
    Myqueue st;
    st.insert(3);
    st.insert(4);
    st.insert(5);
    st.remove();
    st.remove();
    st.remove();
    st.remove();
}
