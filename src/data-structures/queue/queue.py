import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../linked-list')))

from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.linkedList = LinkedList()
  
  def isEmpty(self):
    return not self.linkedList.head
  
  def peek(self):
    if self.isEmpty():
      return None
    
    return self.linkedList.head.data
  
  def enqueue(self, value):
    self.linkedList.prepend(value)
    return
  
  def dequeue(self):
    self.linkedList.delete_end()
    return

  def traverse(self):
    q = self.linkedList.toList()
    return " ".join(str(e) for e in q).strip()

if __name__ == '__main__':
  q = Queue()
  print(q.isEmpty())
  q.enqueue(1)
  q.enqueue(5)
  q.enqueue(11)
  q.enqueue(2)
  q.enqueue(3)
  print(q.traverse())
  print(q.peek())
  q.enqueue(4)
  q.dequeue()
  print(q.traverse())
  