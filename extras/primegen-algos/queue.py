class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        self.length += 1
        node = Node(item)
        if not self.tail:
            self.tail = self.head = node
            return
        self.tail.next = node
        self.tail = node
        

    def deque(self):
        if not self.head:
            return
        self.length -= 1
        head = self.head
        self.head = self.head.next

        return head.value

    def peek(self):
        return self.head.value if self.head else None

Q = Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.deque()
Q.enqueue(4)
Q.deque()
print(Q.peek())