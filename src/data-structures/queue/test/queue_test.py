import unittest
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
from queue import Queue



class TestQueue(unittest.TestCase):
    def test_enqueue(self):
      q = Queue()
      print(q.isEmpty())
      q.enqueue(5)
      q.enqueue(6)
      self.assertEqual(q.traverse(), '6 5', "Should be `6 5`")
    
    def test_dequeue(self):
      q = Queue()
      q.enqueue(5)
      q.enqueue(6)
      q.enqueue(7)
      q.enqueue(8)
      q.dequeue()
      self.assertEqual(q.traverse(), '8 7 6', "Should be `8 7 6`")
    
    def test_isEmpty(self):
      q = Queue()
      self.assertEqual(q.isEmpty(), True, "Should True")

    def test_peek(self):
      q = Queue()
      q.enqueue(5)
      q.enqueue(6)
      q.enqueue(7)
      q.enqueue(8)
      self.assertEqual(q.peek(), 8, "Should be 8")
    
    def test_traverse(self):
      q = Queue()
      q.enqueue(5)
      q.enqueue(6)
      q.enqueue(7)
      q.enqueue(8)
      self.assertEqual(q.traverse(), '8 7 6 5', "Should be '5 6 7 8'")

if __name__ == '__main__':
  unittest.main()