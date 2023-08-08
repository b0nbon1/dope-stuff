class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            # Move the node to the front of the list
            node = self.cache[key]
            self.__remove(node)
            self.__add(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            # Update the value and move the node to the front of the list
            node = self.cache[key]
            node.value = value
            self.__remove(node)
            self.__add(node)
        else:
            # Create a new node and addtail it to the front of the list
            node = Node(key, value)
            self.__add(node)
            self.cache[key] = node
            # If the cache is at capacity, remove the least recently used item
            if len(self.cache) > self.capacity:
                del self.cache[self.tail.prev.key]
                self.__remove(self.tail.prev)

    def __add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def __remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value
    