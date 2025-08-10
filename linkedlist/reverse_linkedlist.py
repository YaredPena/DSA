# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class LinkedList:
    def reverseList(self, head:[ListNode]) -> [ListNode]:
        if not head:
            return None
        
        prev_node, curr_node = None, head
        
        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node


## <-- how to print a linked list result --> 

## print helper function
def print_result(head):
    while head:
        print(head.val)
        head = head.next
    print("None")

## add values as list nodes
head = ListNode(1, ListNode(2, ListNode(3)))
ll = LinkedList() ## instance of my linkedlist

## variable, storing instance of class + calling function in class with head
result = ll.reverseList(head)

##calling helper function to print result.
print_result(result)


##result_one = reverseList()
##result_one.reverseList()

##print(LinkedList.reverseList(result_one))