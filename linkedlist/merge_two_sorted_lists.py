class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = next
    
class LinkedList:
    def merge_two_lists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        ## edge cases:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if not list1 and list2:
            return None
        
        ## main algorithm

        head = ListNode()
        curr_node = head

        while list1 and list2:
            if list1.data <= list2.data:
                curr_node.next = list1 
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        
        if list1 is not None:
            curr_node.next = list1
        else:
            curr_node.next = list2
        return head.next
        ##pass

### TC: O(n) <-- n is the size of list1 and list 2 (n + m)
### SPC: O(1) <-- we're doing this in place


