'''
              
'''

class MinHeap:
    def __init__(self) -> None:
        self.data = []
        self.length = 0
    
    def insert(self, value):
        self.data.append(value)
        self.__heapifyUp(self.length)
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        out = self.data[0]
        self.length -= 1
        if self.length == 0:
            self.data = []
            return out
        self.data[0] = self.data[self.length]
        self.__heapifyDown(0)
        return out
    
    def __parent(self, idx):
        return (idx - 1) // 2
    
    def __leftChild(self, idx):
        return idx * 2 + 1
    
    def __rightChild(self, idx):
        return idx * 2 + 2
    
    def __heapifyUp(self, idx):
        curr_idx = idx
        while curr_idx > 0:
          p_idx = self.__parent(curr_idx)
          parent_val = self.data[p_idx]
          curr_val = self.data[curr_idx]

          if parent_val > curr_val:
              self.data[curr_idx], self.data[p_idx] = parent_val, curr_val
              curr_idx = p_idx
          else:
              break
    
    def __heapifyDown(self, idx):
        
        while idx < self.length:
            l_idx = self.__leftChild(idx)
            r_idx = self.__rightChild(idx)
            if l_idx >= self.length:
                break
            l_val = self.data[l_idx]
            r_val = self.data[r_idx]
            curr_val = self.data[idx]

            if l_val > r_val and curr_val > r_val:
                self.data[idx], self.data[r_idx] = r_val, curr_val
                idx = r_idx
            elif r_val > l_val and curr_val > l_val:
                self.data[idx], self.data[l_idx] = l_val, curr_val
                idx = l_idx
            else:
                break

heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(69)
heap.insert(420)
heap.insert(4)
heap.insert(1)
heap.insert(8)
heap.insert(7)

print(heap.data)
print(heap.length)
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.data)


    
