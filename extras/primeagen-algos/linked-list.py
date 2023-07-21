class Node:
    def __init__(self, value, prev = None, next = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None
    
    def prepend(self, item):
        node = Node(item)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        return
        

    def insertAt(self, item, idx):
        if idx > self.length:
            raise Exception("index out of bound")
        elif idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return
        self.length += 1
        curr = self.getAt(idx)

        node = Node(item)
        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        


    def append(self, item):
        self.length += 1
        node = Node(item)
        if not self.tail:
            self.head = self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove(self, item):
        curr = self.head
        while curr:
            if curr.value == item:
                break
            curr = curr.next
        return self.removeNode(curr) 

    def get(self, idx):
        curr = self.getAt(idx)
        if not curr:
            return None
        return curr.value

    def removeAt(self, idx):
        node = self.getAt(idx)

        if not node:
            return None
        return self.removeNode(node)

    def getAt(self, idx):
        curr = self.head
        i = 0
        while curr and i < idx:
            curr = curr.next
            i += 1
        return curr
    
    def removeNode(self, node):
        if not node:
            return None
        self.length -= 1
        if self.length == 0:
            out = self.head.value
            self.head = self.tail = None
            return out
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head == node.next
        if node == self.tail:
            self.tail == node.prev

        node.prev = node.next = None
        return node.value
    
    def debug(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

list = DoublyLinkedList()
list.append(2)
list.prepend(1)
list.append(3)
list.append(4)
list.removeAt(1)
list.insertAt(5,1)
print(list.get(3))
list.debug()


