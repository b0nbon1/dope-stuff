import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from linked_list import LinkedList



class TestLinearSearch(unittest.TestCase):

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(5)
        ll.prepend(6)
        self.assertEqual(ll.traverse(), '6->5->', "Should be index 6->5->")
    
    def test_append(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(6)
        self.assertEqual(ll.traverse(), '5->6->', "Should be index 5->6->")
    
    def test_insertList(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      self.assertEqual(ll.traverse(), '4->6->7->3->', "Should be index 4->6->7->3->")
    
    def test_insertAt(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      ll.insert_at(2,9)
      self.assertEqual(ll.traverse(), '4->6->9->7->3->', "Should be index 4->6->9->7->3->")

    def test_deleteAt(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      ll.delete_at(2)
      self.assertEqual(ll.traverse(), '4->6->3->', "Should be index 4->6->3->")
    
    def test_deleteBy(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      ll.delete_by(6)
      self.assertEqual(ll.traverse(), '4->7->3->', "Should be index 4->7->3->")
    
    def test_contains(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      self.assertEqual(ll.contains(6), True, "Should be True")

    def test_not_contains(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      self.assertEqual(ll.contains(9), False, "Should be False")
    
    def test_length(self):
      ll = LinkedList()
      ll.insert_list([4,6,7,3])
      self.assertEqual(ll.length(), 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()