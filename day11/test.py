import unittest

from day11.part1 import blink, update_node
from utils.Node import Node

class TestHikeTrailFinder(unittest.TestCase):
    def test_split_string(self):
        """Test split string"""
        
        stone = "1234"
        
        left = stone[0:len(stone)//2]
        right = stone[len(stone)//2:]
        
        self.assertEqual(left, "12")
        self.assertEqual(right, "34")
        
    def test_split_string_zeros(self):
        """Test split string"""
        
        stone = "253000"
        
        left = stone[0:len(stone)//2]
        right = str(int(stone[len(stone)//2:]))
        
        self.assertEqual(left, "253")
        self.assertEqual(right, "0")
    
    def test_update_node(self):
        """Test update node"""
        a = Node("A")
        b = Node("B")
        c = Node("C")
        
        a.next = b
        b.prev = a
        b.next = c
        c.prev = b
        
        #A -> B -> C
        
        b1 = Node("B1")
        b2 = Node("B2")
        update_node(a, b, b1, b2)
        
        #A -> B1 -> B2 -> C
        
        self.assertIsNone(a.prev)
        self.assertEqual(a.next, b1)
        self.assertEqual(b1.prev, a)
        self.assertEqual(b1.next, b2)
        self.assertEqual(b2.prev, b1)
        self.assertEqual(b2.next, c)
        self.assertEqual(c.prev, b2)
        self.assertIsNone(c.next)
        
    def test_update_node_head(self):
        """Test update node head"""
        
        a = None
        b = Node("B")
        c = Node("C")
        
        b.prev = a
        b.next = c
        c.prev = b
        
        #B -> C
        
        b1 = Node("B1")
        b2 = Node("B2")
        update_node(b, b, b1, b2)
        
        #B1 -> B2 -> C
        
        self.assertIsNone(b1.prev)
        self.assertEqual(b1.next, b2)
        self.assertEqual(b2.prev, b1)
        self.assertEqual(b2.next, c)
        self.assertEqual(c.prev, b2)
        self.assertIsNone(c.next)
        
    def test_update_node_tail(self):
        """Test update node head"""
        
        a = Node("A")
        b = Node("B")
        c = None
        
        a.next = b
        b.prev = a
        b.next = c
        
        #A -> B
        
        b1 = Node("B1")
        b2 = Node("B2")
        update_node(a, b, b1, b2)
        
        #A -> B1 -> B2
        
        self.assertIsNone(a.prev)
        self.assertEqual(a.next, b1)
        self.assertEqual(b1.prev, a)
        self.assertEqual(b1.next, b2)
        self.assertEqual(b2.prev, b1)
        self.assertIsNone(b2.next)
        
        
if __name__ == '__main__':
    unittest.main()