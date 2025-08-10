class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## input: list of chars ['a', 'b' ..]
## output: head of the intialized linkedlist: [] --> a --> b ...

##plan:
def answer(chars):
    if len(chars) == 0:
        return None
    
    head = ListNode(val = chars[0])

    head.next = answer(chars[1:])
    
    return head

    ##pass

## prints list given a head of linked list:
def print_list(l):
    if not l:
        print('None')
    
    arr = []
    curr_val = l.val
    arr.append(curr_val)

    while l.next != None:
        arr.append(l.next.val) ##[]
        l = l.next

    print(arr)

    ##pass

def shuffle_lists(P, Q):
    if not P:
        return reverse(Q)
    if not Q:
        return P

    # Grab last node from Q
    prev = None
    curr = Q
    while curr.next:
        prev = curr
        curr = curr.next

    # Remove that last Q node
    if prev:
        prev.next = None
    else:
        Q = None  ### when q only has one node

    next_p = P.next
    P.next = curr  # P1 -> Qn

    curr.next = shuffle_lists(next_p, Q)  ## use recursion on the rest of the

    return P

def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

print(shuffle_lists())

'''
FUNCTION shuffleLinkedLists(P, Q):

    IF P is NULL:
        RETURN Q (possibly reversed)
    
    IF Q is NULL:
        RETURN P

    lastQ = Q
    prevQ = NULL

    // Traverse to the last node in Q
    WHILE lastQ.next IS NOT NULL:
        prevQ = lastQ
        lastQ = lastQ.next

    // Remove lastQ from Q
    IF prevQ IS NOT NULL:
        prevQ.next = NULL
    ELSE:
        Q = NULL  // Q had only one node

    // Save next pointer of P
    nextP = P.next

    // Stitch P1 → Qn
    P.next = lastQ

    // Recurse on the rest
    lastQ.next = shuffleLinkedLists(nextP, Q)

    RETURN P
'''
