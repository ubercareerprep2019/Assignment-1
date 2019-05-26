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

    def size(self):
        return self.num_items
