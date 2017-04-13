"""
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 
5 elements, the 3rd element from the end is the 3rd element. The function definition should look like 
"question5(ll, m)", where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. Return 
the value of the node at that position.
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

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
            
#calculate the  size of linked  list    
    def linked_list_size(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count

# Assume the first position is 1.
# Return "None" if position is not in the list.
    def question5(self,ll,m):    
        counter = 1
        ll = self.head
        l_size = self.linked_list_size()
#         print "linked list size:", l_size
        if m < 1:   # None for the first position less than  0
            return None
        # m is the "mth number from the end, which is  equal element with (linked_list size+1)-m from start.
        while ll :  #while current exit(not None)
            if counter == (l_size+1)-m:                    
                return ll.data
            ll = ll.next
            counter += 1
        return None

print "test set 1"
#create Node with 1,2,3,4,5    
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

#Find value for each element of position from end: 1,2,3,4,5
print ll.question5(ll, 1)
print ll.question5(ll, 2)
print ll.question5(ll, 3)
print ll.question5(ll, 4)
print ll.question5(ll, 5)

    
print "test set 2"
#create Node with 1,2,3,4,5    
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

#Find value for each element of position from end: 1,2,3,4,5
print ll.question5(ll, 1)
print ll.question5(ll, 2)
print ll.question5(ll, 3)
print ll.question5(ll, 4)
print ll.question5(ll, 5)
print ll.question5(ll, 6)

print "test set 3"
#create Node with 1,2,3,4,5    
e1 = Node(6)
e2 = Node(5)
e3 = Node(4)
e4 = Node(0)
e5 = Node('')
e6 = Node(3)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

#Find value for each element of position from end: 1,2,3,4,5
print ll.question5(ll, 1)
print ll.question5(ll, 2)
print ll.question5(ll, 3)
print ll.question5(ll, 4)
print ll.question5(ll, 5)
print ll.question5(ll, 6)
    