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

class Hash
{
private:
    Node *hashTable;
    int size;

public:
    Hash(int size)
    {
        hashTable = new Node[size];
        this->size = size;
    }
    void insert(int data)
    {
        Node *temp = new Node(data);
        int key = data % 10;

        temp->next = hashTable[key].next;
        hashTable[key].next = temp;
    }

    int remove(int data)
    {
        int key = data % 10;
        Node *s = &hashTable[key];
        Node *sfront;
        bool find = false;
        while (s->next != NULL)
        {
            sfront = s;
            s = s->next;
            if (data == s->data)
            {
                find = true;
                break;
            }
        }

        if (find)
        {
            sfront->next = s->next;
            delete s;
        }

        else
            cout << "cannot search\n";
    }
    Node *search(int data)
    {
        int key = data % 10;
        Node *s = &hashTable[key];

        while (s->next != NULL)
        {
            s = s->next;
            if (data == s->data)
                return s;
        }
        return NULL;
    }
    bool empty()
    {
    }
};

int main()
{
    Hash h = Hash(10);
    h.insert(3);
    h.insert(13);
    h.insert(23);
    h.insert(33);
    h.insert(43);
    h.remove(23);
    h.remove(23);
}
