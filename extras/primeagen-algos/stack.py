class Node:
    def __init__(self, value, prev = None) -> None:
        self.value = value
        self.prev = prev

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, item):
        self.length += 1
        node = Node(item)
        if not self.head:
            self.head = node
            return
        node.prev = self.head
        self.head = node
        

    def pop(self):
        self.length = max(0, self.length-1)
        if self.length == 0:
            head_value = self.head.value if self.head else None
            self.head = None
            return head_value
        head = self.head
        self.head = self.head.prev
        return head.value
        

    def peek(self):
        return self.head.value if self.head else None

