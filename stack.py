# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
'''Remember that wonderful Python list we talked about eariler? 
It turns out that stack functionality is already built into it! '''

# def delete_first(self):   #like pop , which delete first element.
#     deleted = self.head
#     if self.head:  #if first(most upper) element exit,
#         self.head = self.head.next  #second upper element become most upper(self.head) element.
#         deleted.next = None  #deleted(which is self.head=most upper)'s link become None , so no link for "deleted"
#     return deleted

'''You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"? '''

'''Here's the code for an Element, which will be a single unit in a linked list:'''
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
# This code is very similar—we're just establishing that a LinkedList is something 
# that has a head Element, which is the first element in the list. If we establish 
# a new LinkedList without a head, it will default to None.  
      
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head  #put new_element on self.head, so new_element's next link indicate self.head
        self.head = new_element       #So new_element become upper most self.head  
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:    #if not empty stack(list)
            deleted_element = self.head  #sef.head(uppper most) one became deleted_element
            temp = deleted_element.next  #assign deleted_element's below(next) in temporary place 
            self.head = temp             # deleted_element's below element became self.head(upper most)one, since deleted_element will be removed(pop)
            return deleted_element       #deleted_item pop up.
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)  #class LinkedList(Object): ; def _init_ (self, head=None): ; self.head=head

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value