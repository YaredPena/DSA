## Define the listnode class
## Define the linkedlist class

## then build your functions

class ListNode:
    def __init__(self, x): ## instantiating a class... -> 
        self.val = x
        self.next = None
        ##pass

class LinkedList: 
    def __init___(self):
        self.head = None 

    def add_element_at_head(self, x):
        new_node = ListNode(x) ## we store the reference to our element in a new variable
        new_node.next = self.head ## we set the next reference to the old head
        self.head = new_node ## referring to the node
        ##L.size = L.size + 1 <-- incrementing node count but we're not keeping track of the count
        ##pass
    
    def add_element_at_tail(self, x):
        new_node = ListNode(x)
        new_node.next = None
        self.tail.next = new_node
        self.tail = new_node

## to call a class 
## store in a variable

node = ListNode()
linked_list = LinkedList()