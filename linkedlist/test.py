class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    def _insertion_sort_list(self, head):
        dummy = ListNode(0, head)
        prev = head
        curr = head.next

        while curr:
            if curr.val > prev.val:
                prev = prev.next
                curr = curr.next
                continue
        
            temp = dummy
            while curr.val > temp.next.val:
                temp = temp.next
                prev.next = curr.next
                curr.next = temp.next
                temp.next = curr
                curr = prev.next
        return dummy.next

        ##pass