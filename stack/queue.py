## QUEUES are opposite of a stack
## they can be very similar in many ways though

## concept: FIFO
## first in first out property

## always just use this import for queues 
from collections import deque

## our object is a double ended queue
## just means we can add and remove stuff from the left 
## AND right sides
q = deque()
 ## 5 is the most recent so it's the first that will
 ## be removed 
 ## enqueues are O(1) time 
q.append(5)
q.append(4)
q.append(9)
q.append(2)

## dequeue's are O(1) time left or right
q.pop() ## pops from the right

## we need to specify that we're popping from the left
q.popleft() ## double ended queue

## peeking --> checking from the left time O(1)
print(q[0]) ## check the first element in the queue
## peeking --> checking from the right time O(1)
print(q[-1])

print(q)

'''
def queue(q):
    q = deque(q) 
    q.append(4) <-- this is enqueue
    print(q)

queue([1, 2, 3])
'''

## Enqueue(x) --> puts in a new value onto the queue
## appending --> from the right
## dequeue(x) --> pop from the left, takes off the first thing from the queue
## Dq's are O(n) --> everything has to move over
## generally queue's are not dynamic arrays --> they are static or some linked list
