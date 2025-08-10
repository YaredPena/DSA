## tree basics

## binary tree:
## has a root 
## a left  --> root.left
## and a right --> root.right

## to build a tree:
## we have the node class
## this usually holds a root.val (value of the root node)
## the left node (root.left)
## and the (root.right) 
## these values can be null.
## leaf node - nodes that have no branches (basically the end of a tree)
## parent nodes connect to other nodes futher down the tree.
## child nodes are connected to their respective part node
## we usually NEVER make a root.parent

## depth first search on a tree:
## starts at root
## priotizes depth, how deep the tree nodes go 
## goes down first left path fully before returning to root
## EXAMPLE:
##  1 go down
## 2 go down
## 4 stop
## array = [ 1, 2, 4]

## DFS: preorder
## process order
## (current Node)  --> root
## left 
## right
## we go left fully first then we go right
##              1
##        2               3
##     4     5      10
## array = [1, 2, 4, 5, 3, 10] <-- preorder traversal

## DFS: Inorder
## just because we visit a node doesn't mean we process it
## process left first
## then Node --> root
## right
## we start at root but we don't print it
## we have to keep going left before we process
##              1
##        2               3
##     4     5      10
## array = [4, 2, 5, 1, 10, 3]

## DFS: postorder
## we process left first
## then we process right
## then we process Node (root) last
##              1
##        2               3
##     4     5      10
## array = [4, 5, 2, 10, 3, 1]


## do preorder than inorder traversal DFS on this tree bonus do postorder
## DFS preorder:
## Node 
## left 
## right
## array = [1, 2, 4, 5, 3, 6, 7]

## DFS Inorder:
## left
## Node
## right
## array = [4, 2, 5, 1, 6, 3, 7]

## DFS postorder:
## left 
## right
## Node
## array = [4, 5, 2, 6, 7, 3, 1]

## BFS / level order traversal:
## we're focusing on visiting from the top down...
## BFS prioritizes scanning all nodes at every level from the top down
##              1                   (2^0)
##        2               3         (2^1)
##     4     5      10              (2^2)
## array = [1, 2, 3, 4, 5, 10]

## DFS uses stack --> usually with recursion
## BFS uses queue

## iterative DFS:
## build an empty stack with just the root node
## stack = [1]
## build a while loop (while we have a stack)
## pop an element from the stack onto our result
##  stack = []
## we would keep doing this until the loop concludes.
##  result = [1, 2, 4, 5, 3, 10] <-- processed nodes

## BFS: Level order traversal:
## build an empty queue
## queue = []
## while we have a queue--> (build while loop for queue)
## we'll deque instead of pop
## result = [1, 2, 3, 4, 5, 10] <-- processed nodes 

## check if a value exists in the tree:
## BFS && DFS:
## time = O(n)
## lookup for a value O(n) because we have to look at all nodes for the value
## Space is also O(n) based on the number of nodes in our tree

## Binary Search Trees:
## at the root
## everything on the left of the root is smaller than the root
## everything on the right of the root is bigger than the root

## with a regular binary tree, this doesn't happen, we could have a root
## point to a node with a value greater than itself.

## Lookup w/ BST --> using DFS
## when looking up values we are able to wipe out halves of areas
## within the binary search tree that are not in our general search area
## Time complexity O(log n) <-- we'll keep cutting the input size by 2
## ^^ assuming the tree is height balanced (has left and right nodes)

## how to code these
## Binary tree ##

## initialize the treenodes

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    
    ## this will let just print the string of nodes inside of our tree ##
    def __str__(self):
        return str(self.val) ## this is printing our the nodes value

## in leetcode we  wouldn't have to build a tree like this
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

## our root is 1
A.left = B
A.right = C

##  1
## 2  3

B.left = D
B.right = E
C.left = F

##print(A)

## recursive pre order traversal ( DFS )
## TC: O(n)
## SPC: O(n)

## pre order (node @ 1)
'''
def pre_order(node):
    if not node: ## if we have 0 nodes
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

## calling the function
pre_order(A)
'''

## in_order (node @ 2)

'''
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)
'''


'''
## pre_order (node @ 3)
def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)
'''

## ^ this was all recursive how to do this without recursion
## Pre order iterative Traversal DFS
'''
def pre_order_iterative(node):
    stack = [node]

    while stack:
        node  = stack.pop() ## popping from topn of stavk

        print(node)

        ## we're doing right BEFORE left to make the left end up on top
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
'''

##pre_order_iterative(A)

'''
def in_order_iterative(node):
    stack = [node]

    while stack:

        if not node:
            return
        
        if node.left:
            stack.append(node.left)
        
        print(node)

        if node.right:
            stack.append(node.right)

in_order_iterative(A)
'''

## Level Order Traversal (BFS) 
## TC: O(n)
## SPC: O(n)
'''
from collections import deque

def bfs_level_order(node):

    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node)
        
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

bfs_level_order(A)
'''

## checking if a value exist (DFS)

def search(node, target):
    if not node:
        return False ## we couldn't find anything 
    
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

search(A, 11)

## BINARY SEARCH TREE
## TC: O(log n)
## SPC: O(log n)

def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None


class all_orders:
    def __init__(self, root):
        self.root = root

    ## do pre order dfs:
    def dfs_preorder(self, node):
        if not node:
            return 
        
        print(node)
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)

    def dfs_inorder(self, node):
        if not node:
            return
        self.dfs_inorder(node.left)
        print(node)
        self.dfs_inorder(node.right)

    def dfs_postorder(self, node):
        if not node:
            return
        
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print(node)

        