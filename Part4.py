import unittest

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, item):
        self.next = item


class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.num_in_queue = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.num_in_queue == 0

    def is_full(self):
        return self.num_in_queue == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError()
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.num_in_queue += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError()
        item = self.front.data
        if self.size() == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.num_in_queue -= 1
        return item

    def size(self):
        return self.num_in_queue
