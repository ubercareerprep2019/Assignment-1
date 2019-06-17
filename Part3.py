import unittest


#Part 3A
class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
    def is_empty(self):
        return self.num_items == 0
    
    def is_full(self):
        return self.num_items == self.capacity
    
    def push(self, item):
        if self.num_items != self.capacity:
            self.items[self.num_items] = item
            self.num_items += 1
        else:
            raise IndexError()

    def pop(self):
        if self.num_items != 0:
            value = self.items[self.num_items - 1]
            self.num_items -= 1
            return value
        else:
            raise IndexError()
    
    def peek(self):
        if self.num_items != 0:
            return self.items[self.num_items - 1]
        else:
            raise IndexError()

    #returns minimum item in the stack in O(1) time        
    def min_item(self):
        return min(self.items[:self.num_items])
    
    def size(self):
        return self.num_items

    
class TestStack(unittest.TestCase):

    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
   
    def test_pop(self):
        stack = Stack(3)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertEqual(stack.size(), 0)
        s = Stack(2)
        s.push(1)
        self.assertEqual(1, s.pop())

    def test_push(self):
        stack = Stack(2)
        stack.push(1)
        self.assertEqual(stack.size(), 1)
        stack.push(0)
        self.assertEqual(stack.size(), 2)
        self.assertRaises(IndexError, lambda: stack.push(3))

    def test_pop_error(self):
        stack = Stack(3)
        stack.push(3)
        item = stack.pop()
        self.assertRaises(IndexError, lambda: stack.pop())

    def test_peek(self):
        s = Stack(3)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        stack = Stack(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        self.assertRaises(IndexError, lambda: stack.peek())
    
    def test_full_push(self):
        stack = Stack(2)
        stack.push(2)
        stack.push(2)
        self.assertRaises(IndexError, lambda: stack.push(2))

    def test_empty(self):
        stack = Stack(1)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
    

    
#Part 3B, could use extra guidance
class Queue:
    
    def __init__(self, capacity):
        self.instack = Stack(capacity)
        self.outstack = Stack(capacity)
    
    def enqueue(self, data):
        self.instack.push(data)
        
    def dequeue(self, data):
        while instack.size != 0:
            value = instack.pop()
            self.outstack.push(value)
        return self.outstack.pop()
    
