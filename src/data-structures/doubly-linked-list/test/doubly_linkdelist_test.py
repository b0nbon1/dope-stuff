import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doubly_linkedlist import DoublyLinkedList



class TestDoublyLinkedList(unittest.TestCase):

    def test_prepend(self):
        dl = DoublyLinkedList()
        dl.prepend(5)
        dl.prepend(6)
        self.assertEqual(dl.traverse(), '6<-->5<-->', "Should be 6<-->5<-->")
    
    def test_append(self):
        dl = DoublyLinkedList()
        dl.append(5)
        dl.append(6)
        self.assertEqual(dl.traverse(), '5<-->6<-->', "Should be 5<-->6<-->")
    
    def test_insertList(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,6,7,3])
      self.assertEqual(dl.traverse(), '4<-->6<-->7<-->3<-->', "Should be 4<-->6<-->7<-->3<-->")
    
    def test_insertAt(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,6,7,3])
      dl.insert_at(2,9)
      self.assertEqual(dl.traverse(), '4<-->6<-->9<-->7<-->3<-->', "Should be 4<-->6<-->9<-->7<-->3<-->")
    
    def test_deleteBy(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,6,7,3])
      dl.delete_by_value(6)
      self.assertEqual(dl.traverse(), '4<-->7<-->3<-->', "Should be 4<-->7<-->3<-->")

    def test_deleteEnd(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,6,7,3])
      dl.deleting_end()
      self.assertEqual(dl.traverse(), '4<-->6<-->7<-->', "Should be 4<-->7<-->")
    
    def test_deleteStart(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,7,3])
      dl.deleting_start()
      self.assertEqual(dl.traverse(), '7<-->3<-->', "Should be 7<-->3<-->")
    
    def test_reverse(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,6,7,3])
      dl.reverse()
      self.assertEqual(dl.traverse(), '3<-->7<-->6<-->4<-->', "Should be 3<-->7<-->6<-->4<-->")
    
    def test_length(self):
      dl = DoublyLinkedList()
      dl.insert_list([4,6,7,3])
      self.assertEqual(dl.length(), 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()