"""
LINKED LIST REVERSAL:

write a function to reverse a linked list in place, the function will take in the head of the listas
input and return new head of the list

SOLUTION:

Since we want to this in place we want to make the funciton operate in 0(1) space,meaning we dont want
to create a new list, we simply use the current nodes! Timewise , we can perform the reversal in O(n) time.

we can reverse the list by changing the next pointer of each node.each node's next pointer should point to the 
previous mode.

in one pass from head to tail of our input list, we will point each node's next pointer to the previous element

make sure to copy current.next_node into next_node before setting current.next_node to previous.

"""

class Node:
    
    # constructor to initialize the node object
    def __init__(self, value):
        self.value = value
        self.next_node = None
        

class LinkedList:
    
    # function to instialize the head
    def __init__(self):
        self.head = None
    
    # function to insert a new node
    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node
    
    # function to reverse the linked list
    def reverse_linked_list(self):
        prev = None
        current = self.head
        
        
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
            
        self.head = prev 
            
        
    # utility function to print the linked linkedlist
    def print_list(self):
        temp = self.head
        final_result = []
        while temp:
            final_result.append(temp.value)
            temp = temp.next_node
        
        print(final_result)



if __name__ == '__main__':
    
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4) 
    print('Given Linked list')
    llist.print_list()
    print('Reverse Linked list')
    llist.reverse_linked_list()
    llist.print_list()
    # a = Node(1)
    # b = Node(2)
    # c = Node(3)
    
    # a.next_node = b
    # b.next_node = c
    # c.next_node = a
    
    # print(a.next_node.value, b.next_node.value, c.next_node.value)
    
    # result = reverese_linkedlist(a)
    # print(c.next_node.value, b.next_node.value, a.next_node.value)

    
        
    








