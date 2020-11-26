
#ifndef __stack_h__
#define __stack_h__

#include "../dynamic-array/array.hpp"

/****
 1. push()
 2. pop()
 3. peek(index)
 5. isEmpty

 a. Array
 b. linkedLists
 ****/

template <typename T>
class StackArray
{
  private:
    Array<T> _array;
  public:
    StackArray()
    {
    };
    void push(T value)
    {
      this->_array.append(value);
    }
    T pop()
    {
      T popped;
      popped = this->_array[this->_array.length() - 1];
      this->_array.deleteAt(this->_array.length() - 1);
      return popped;
    }
    T peek()
    {
      return this->_array[this->_array.length() - 1];
    }
    bool isEmpty()
    {
      return this->_array.length() == 0;
    }
};

#endif