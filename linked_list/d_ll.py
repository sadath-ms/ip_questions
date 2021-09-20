"""
Doubly linked list:-

we defines a linked list in which each node keeps an explict reference to the node before it and a reference
to the node after it

these lists allow a greater variety of 0(1)-time update operations, including insertion and deletions

we continue to use the term next for the reference to the node that follows another

we have a new term "prev" for the reference to the node that precedes it

we add special nodes at both ends of the list

a header node at the beginning of the list, a trailer node at the end of the list

these dummy nodes are known as sentinels(or guards)


"""

class DoubleLinkedList(object):
    
    def __init__(self,value ):
        self.value = value
        self.next_node = None
        self.prev_node = None
        