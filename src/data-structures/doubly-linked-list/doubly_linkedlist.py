from linked_list_node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
      n = Node(data)
      if self.head is None:
        self.head = n
        return
      
      n.next = self.head
      self.head.prev = n
      self.head = n

    def append(self, data):
      if self.head is None:
        new_node = Node(data)
        self.head = new_node
        return
      n = self.head
      while n.next is not None:
        n = n.next
      new_node = Node(data, None, n)
      n.next = new_node
      return
    
    def insert_at(self, index, data):
      if index < 0 or index >= self.length():
            raise Exception('Index out of range')
      count = 0
      itr = self.head
      while itr:
          if count == index - 1:
              newNode = Node(data, itr.next, itr)
              itr.next = newNode
              break
          itr = itr.next
          count += 1

    def insert_list(self, data_list):
        for data in data_list:
          self.append(data)
    
    def deleting_start(self):
      if self.head is None:
        print("The list has no element to delete")
        return False
      if self.head.next is None:
        self.head = None
        return True
      self.head = self.head.next
      self.head.prev = None
      return True

    def deleting_end(self):
      if self.head is None:
        print("The list has no element to delete")
        return False
      if self.head.next is None:
        self.head = None
        return True
      n = self.head
      while n.next is not None:
        n = n.next
      n.prev.next = None
      return True

    def delete_by_value(self, value):
      if self.head is None:
        print("The list has no element to delete")
        return False
      if self.head.next is None:
        if self.head.data == value:
          self.head = None
          return True
        else:
          return False
      if self.head.data == value:
        self.head = self.head.next
        self.head.prev = None
        return True
      
      n = self.head
      while n.next is not None:
        if n.data == value:
          break
        n = n.next
      if n.next is not None:
        n.prev.next = n.next
        n.next = n.prev
        return True
      else:
        if n.data == value:
          n.prev.next = None
          return True
        else:
          print("Element not found")
          return False
    
    def reverse(self):
      if self.head is None:
        print("The list has no element to delete")
        return
      p = self.head
      q = p.next
      p.next = None
      p.prev = q
      while q is not None:
        q.prev = q.next
        q.next = p
        p = q
        q = q.prev
      self.head = p
    
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def traverse(self):
        if self.head is None:
            print("Doubly LinkedList is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '<-->'
            itr = itr.next
        return llstr
      
if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.prepend(5)
    ll.prepend(90)
    ll.append(50)
    ll.insert_list([1,2,3,4,5])
    print(ll.traverse())
    ll.delete_by_value(5)
    print(ll.traverse())
    ll.reverse()
    print(ll.traverse())
    print(ll.length())