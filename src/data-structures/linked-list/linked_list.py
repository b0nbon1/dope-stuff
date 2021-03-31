from linked_list_node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception('Index out of range')
        
        if index == 0:
            self.prepend(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                newNode = Node(data, itr.next)
                itr.next = newNode
                break

            itr = itr.next
            count += 1

    def insert_list(self, data_list):
        for data in data_list:
            self.append(data)
    
    def delete_at(self, index):
        if index < 0 or index >= self.length():
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        return True
    
    def delete_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return False
        if self.head.next is None:
            self.head = None
            return True
        n = self.head
        while n.next is not None:
            if n.next.next is None:
                n.next = None
                break
            n = n.next
        return True
    
    def delete_by(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        
        itr = self.head
        check = False
        while itr.next is not None:
            if itr.next.data == value:
                itr.next = itr.next.next
                check = True
                break
            itr = itr.next
        
        return check
    
    def contains(self, value):
        if self.head is None:
            return False

        itr = self.head
        check = False
        while itr is not None:
            if itr.data == value:
                check = True
                break
            itr = itr.next
        return check

    def reverse(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        currNode = self.head
        prevNode = None
        nextNode = None

        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode
    
    def toList(self):
        nodes = []

        itr = self.head
        while itr is not None:
            nodes.append(itr.data)
            itr = itr.next
        
        return nodes

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def traverse(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '->'
            itr = itr.next
        return llstr

if __name__ == '__main__':
    ll = LinkedList()
    ll.prepend(5)
    ll.prepend(90)
    ll.append(50)
    ll.insert_list([1,2,3,4,5])
    ll.delete_at(7)
    ll.delete_by(50)
    print(ll.contains(50))
    print(ll.traverse())
    ll.reverse()
    ll.delete_end()
    print(ll.traverse())
    print(ll.length())
