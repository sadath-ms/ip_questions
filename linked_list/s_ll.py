"""
Singly linked list:-

is a collection if nodes that collectevely form a linear sequence

each node stores a reference to an object that is an element of the sequence, as well as a
reference to the next node of the list

the first node and last node of the linked list are also known as the head and tail of the list

we can identify the tail as the node having None as its next reference

this process is commomly known as traversing the linked list

because the next reference of a node can be viewed as link or pointer to another node, the process of
traversing a list is also known as link hopping or pointer hopping

each node is represented as a unique object , with that instance storing a referece to its element and a 
reference to the next node (or None)


An important property of a linked list is that it does not have a predetermined fixes size

its uses space proportionallu to its current number of elements

to insert a new element at the head of the list
    - we creare a new node
    - set its element to the new element
    - set  its next link to refer to the current head
    - then set the lists head to point to the new node
    

we can also insert an element at the tail of the list,provided we keep a reference to the tail node
    - create a new node
    - assign its next reference to None
    - set the next reference of the tail to point to this new node
    - then update the tail reference itself to this new node
    
    
Removing an element from a singly linked list
    removing element from the head of a singly linked list is essentially the reverse operation of inserting a
    new element at the head
    
    - we cannot easily delete the last node of a singly linked list
    - even if we maintain a tail reference directly to the last node of the list, we must be able to access
        the node before the last node in order to remove the last node
    - but we cannot reach the node before the tail by following next links from the tail
    - if we want to support such an operation effectively , we will need to make our list doubly linked
    
"""

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next_node = None
        

if __name__ == '__main__':
    
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next_node = b
    b.next_node = c
    
    print(c.value, c.next_node.value)
    