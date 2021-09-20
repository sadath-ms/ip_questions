"""
Single Linked list cycle check

problem:-

given a single linked list , write a function , which takes in the first node in a singly linked list and
return a boolean indicating if the linked list contains a cycle

a cycle is when a node's next point actually points back to a previos node in the list, this is sometimes also know as
circular linked list

solution:-

to solve this problem, we will have two markers traversing through the list. marker 1 and marker 2, we will have
both markers begin at the first node of the list and traverse throught the linked list,
however the second marker marker2 will move two nodes ahead for every one node that marker m1 moves.

by this logic we can imagine that the markers are "racing" through the linked list, with marker2 moving
faster .if the linked list has a cycle and is circular connected we will have the analogy of a track, in this
case the m2 will eventually be "lapping" the marker1 and they will equal each other

if the linked list has no cycle , them marker2 should be able to continue on until the very end, never equalling
the first marker

"""

def cycle_check(node):
    marker1 = node
    marker2 = node
    while marker1 != None and marker2 != None:
        marker1 = marker1.next_node
        if not marker2.next_node:
            marker2 = marker2.next_node.next_node  
        
        if marker1 == marker2:
            return True
    return False
    
    
    
class Node:
    
    def __init__(self, value):
        self.value = value
        self.next_node = None

if __name__ == '__main__':
    # cycle test
    a = Node(1)
    b = Node(2)
    c = Node(3)
    
    a.next_node = b
    b.next_node = c
    c.next_node = a
    
    # non cycle test
    x = Node(1)
    y = Node(2)
    z = Node(3)
    
    x.next_node = y
    y.next_node = z
    
    res = cycle_check(a)
    print(res)
    
    
    
    
