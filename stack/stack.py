## review  stacks

## putting things on top of a stack

## normally we build things from left to right
## a stack is just a list in programming
## example
## stack = [5, 7, 8, 4]
## right == top 
## left == bottom

## visualizing a stack:
## stack = [5, 7, 8, 4]
## 4
## 8
## 7
## 5

## common operations:
## APPEND adding to the right TC: depends on if dynamic or static stack
## static array --> add space --> TC: O(n)
## dynamic array --> Tc: O(1)

## what if a linked list?
## generally TC: O(1)

## POP always gonna TC: O(1)
## we append and pop from the right so it's fine to make it a dynamic array
## PEEK O(1) always 
## ISEMPTY O(1) --> return true if empty otherwise it will return false

# stack[-1] <-- access last position

## conceptually stacks follow, LIFO
## last in, first out property
## last item in will be the first item to leave

## stacks
def stack(stk):
    stk = []
    stk.append(5)
    stk.append(4)
    stk.append(3)
    print(stk)

    ## pop form the stack O(1)
    x = stk.pop()
    print(x)
    print(stk)

    stk.pop()
    stk.pop()
    print(stk)

    ## print the most recent value in the stack 
    ##print(stk[-1]) ## nothing in the stack --> index is out of range

    ##probably best to have this check in the event your stack is empty
    ## and your not keeping track
    ## check if something is in the stack O(1)
    if stk:
        print('True')
    else:
        print('False')
    
stack([])


## generally you should keep track of the stuff popped from your stack

