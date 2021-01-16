#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
    struct Node *front;
    struct Node *rear;
}
void enqueue ()
{
    struct Node *t = new Node;
    if(t==NULL)
    printf("Queue is Full");
    else
    {
        t->data=x;
        t->next=NULL;
        if(front==NULL)
            front=rear=t;
        else{
            rear->next=t;
            rear=t;
        }
    }
}
int main()
{
    
    enqueue();
}