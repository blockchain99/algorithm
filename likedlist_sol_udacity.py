# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
'''
 There isnt a built-in data structure in Python that looks like a linked list. 
Thankfully, it's easy to make classes that represent data structures in Python! 
 
Here's the code for an Element, which will be a single unit in a linked list:'''
class Element1(object):
    def __init__(self, value):
        self.value = value
        self.next = None
         
'''This code is very similar�we're just establishing that a LinkedList is something 
that has a head Element, which is the first element in the list. If we establish 
a new LinkedList without a head, it will default to None. '''
         
class LinkedList1(object):
    def __init__(self, head=None):
        self.head = head
         
# '''Great! Let's add a method to our LinkedList to make it a little more useful. 
# This method will add a new Element to the end of our LinkedList.'''
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
#LinkedList is something that has a head Element, 
#which is the first element in the list.  
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:  #if head is exist(not None)
            while current.next:   #and if current's next element exist
                current = current.next     #shift to next 
            current.next = new_element   #current's next element become new_element.   
        else:
            self.head = new_element
# Get an element from a particular position.
# Assume the first position is 1.
# Return "None" if position is not in the list.
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:   # useless positon since first point should be 1
            return None
        while current and counter <= position:  #while current exit(not None) & counter is within position 
            if counter == position:  
                return current
            current = current.next
            counter += 1
        return None
# """Insert a new node at the given position.
#         Assume the first position is 1.
#         Inserting at position 3 means between
#         the 2nd and 3rd elements."""
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1: #insert  new_element between current and current.next
                    new_element.next = current.next #new_element's next link is  current's next link 
                    current.next = new_element #current's next linked to new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head  #new_element position before self.head, so new_element's next linked to slfe.head
            self.head = new_element #self.head is substituted by new_element.
    #previous - current(delete) - current.next:deleting current by previous.next = current.next
    def delete(self, value):
        current = self.head  #start with head
        previous = None      #and previous element not exit
        while current.value != value and current.next:  # while current's value is different from "value" and current's next exit
            previous = current  #previous element become current element
            current = current.next  #current shift to right
        if current.value == value:  #if current value is equal "value" 
            if previous:            #and previous exist
                previous.next = current.next  #skip current and move link to the next element and it become previous's next, so delete current.
            else:
                self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print "ll.get_position(3).value:",ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value