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

    #returns true if remove is successful, false otherwise.
    def remove(self, data):
        node = self.front
        self.remove_helper(data, node)
        
    def remove_helper(self, data, node):
        if self.is_empty():
            return False
        elif data == node.data:
            temp = Node("temp", node.next)
            #need help here, incomplete
        elif node.next == None:
            return False
        else:
            self.remove_helper(data, node.next)

    def search(self, data):
        node = self.front
        index = 0
        self.search_helper(data, node, index)

    def search_helper(self, data, node, index):
        if self.is_empty():
            return False
        elif node.data == data:
            return index
        elif node.next == None:
            return False
        else:
            count += 1
            self.search_helper(data, node.next, count)

    
    def size(self):
        return self.num_in_queue
    
class testLinked(unittest.TestCase):
    
    def testPushBackAddsOneNode(self):
        testqueue = Queue(10)
        testqueue.enqueue("something")
        self.assertEqual(testqueue.front.get_data(), "something")

    def PopBackRemovesCorrectNode(self):
        testqueue = Queue(10)
        testqueue.enqueue("test")
        self.assertEqual(testqueue.dequeue(), "test") 
    
    def ElementatReturnNode(self):
        testqueue = Queue(5)
        testqueue.enqueue("1")
        testqueue.enqueue("2")
        testqueue.enqueue("3")
        testqueue.enqueue("4")
        testqueue.enqueue("5")
        self.assertEqual(testqueue.search("4"), 3)


    def testElementAtReturnsNoNodeIfIndexDoesNotExist(self):
        testqueue = Queue(9)
        testqueue.enqueue("test1")
        testqueue.enqueue("test2")
        testqueue.enqueue("test3")
        testqueue.enqueue("test4")
        self.assertEqual(testqueue.search("doesnotexist"), False)


    def testSizeReturnsCorrectSize(self):
        testqueue = Queue(4)
        testqueue.enqueue("a")
        testqueue.enqueue("b")
        testqueue.enqueue("c")
        self.assertEqual(testqueue.size(), 3)
