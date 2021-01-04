#ifndef __array_h__
#define __array_h__

#include <assert.h>
#include <iostream>

const int INITIAL_CAPACITY = 2;
const int GROWTH_FACTOR = 2;

template <class T>
class Array
{
private:
  int capacity = INITIAL_CAPACITY;
  int _size;
  T *array;
  void resize()
  {
    capacity *= GROWTH_FACTOR;
    T *temp = new T[capacity];
    std::copy(array, array + _size, temp);
    delete[] array;
    array = temp;
  }

public:
  Array()
  {
    this->array = new T[capacity];
    this->_size = 0;
  }

  ~Array()
  {
    delete[] this->array;
  }

  void insertAt(int element, int pos)
  {
    assert(0 <= pos && pos <= _size);
    if (_size == capacity)
    {
      resize();
    }
    for (int i = _size; i > pos; i--)
    {
      array[i] = array[i - 1];
    }
    _size++;
    array[pos] = element;
  }

  void append(T element)
  {
    insertAt(element, _size);
  }

  void prepend(T element)
  {
    insertAt(element, 0);
  }

  void deleteAt(int pos)
  {
    assert(0 <= pos && pos < _size);
    _size--;
    for (int i = pos; i < _size; i++)
    {
      array[i] = array[i + 1];
    }
  }

  T &operator[](int pos)
  {
    return this->array[pos];
  }

  void pretty_print()
  {
    std::cout << "[";
    for (int i = 0; i < _size - 1; i++)
    {
      std::cout << array[i] << " ";
    }
    if (_size)
    {
      std::cout << array[_size - 1];
    }
    std::cout << "]\n";
  }

  int length()
  {
    return _size;
  }
};

#endif
