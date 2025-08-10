class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = next
    
class LinkedList:
    def insertion_sort_linked_list(self, head):
        ## can i initialize the dummy like this instead??? Nope
        dummy = ListNode(0, head)
        ##head = dummy

        prev_node = head ## start prev at dummy
        curr_node = head.next ## start curr at real node
        ##curr_node = head.next

        while curr_node:
            ## what if the linked list is already sorted?
            if curr_node.data >= prev_node.data:
                prev_node = curr_node
                curr_node = curr_node.next
                continue

            ## what if the current value is less than the next value
            ## that temp is referencing
            temp = dummy
            while curr_node.data > temp.next.data:
                temp = temp.next
            
            prev_node.next = curr_node.next
            curr_node.next = temp.next
            temp.next = curr_node
            curr_node = prev_node.next
        return dummy.next


