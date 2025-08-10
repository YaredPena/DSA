class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:
    def detect_cycle(self, head):
        if head == None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return True
        else:
            return False
        