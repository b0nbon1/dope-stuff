#ifndef __linkedlists_h__
#define __linkedlists_h__

#include "linked-list-node.hpp"
#include <iostream>

template <class T>
class Linkedlist
{
private:
  Node<T> *head, *tail;
public:
  Linkedlist()
  {
    head=NULL;
    tail=NULL;
  }
  Linkedlist prepend(T value)
  {
    Node<T> *temp = new Node<T>;
    temp->data=value;
    temp->next=head;
    if(tail==NULL)
    {
      this->head=temp;
      this->tail=temp;
      temp=NULL;

    }
    
    return this;
  }
  Linkedlist append(T value)
  {
    Node<T> *temp = new Node<T>;
    temp->data=value;
    temp->next=NULL;
    if(head==NULL)
    {
      this->head=temp;
      this->tail=temp;
      temp=NULL;
      return this;
    }

      this->tail->next = temp;
      this->tail=temp;
      return this;
  }
  
};


#endif
