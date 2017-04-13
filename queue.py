# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
''' Queue : FIFO , so head(First Input) is oldest , and go out first(First Out) 
    Queue :  Dequeue(operatoin : remove element in head) <- head(oldest).... tail(newest) <- Enqueue(operation : add element in tail)'''
''' operation Peek(just look the head element) '''
''' head(value:1, next) -> value:2 next -> tail(value:3, next) '''

'''From a library called collections, you can import a package called deque. 
a deque is a double-ended queue. You can enqueue on either end, 
but in the example you only enqueue one way and treat it as a normal queue.'''

"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):  #add element in tail(newest)
        self.storage.append(new_element)   #As for the list(self.storage),append new_element

    def peek(self):
        return self.storage[0]  #just return first(head) of list(self.storage)

    def dequeue(self):   #remove element in head(oldes)
        return self.storage.pop(0)   #list.pop(0)
    
# Setup (head:oldest)1,2,3(tail:newest)
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()