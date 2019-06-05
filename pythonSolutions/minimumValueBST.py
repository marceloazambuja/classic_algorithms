# Find the minimum value in Binary Search Tree (BST)
# Considering that in BST each value from left to each root is always less than the root value, to find the very minimum value it's needed to read each left node until reach the NULL value, i.e., the most left node is always the minimum value in BST.
# Created by Marcelo Cunha de Azambuja on 6/4/19, based on https://www.geeksforgeeks.org/find-the-minimum-element-in-a-binary-search-tree/

# our node
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# to insert new node, first test if the current node is None. If so, insert, if not, test if the new node will be to the left or to the right of the current node.
def insertNode (node, newValue):
    if (node is None):
        return (Node(newValue))
    else:
        if (newValue < node.data):
            node.left = insertNode(node.left, newValue)
        else:
            node.right = insertNode(node.right, newValue)
        
        # return the (unchanged) node pointer
        return (node)

# the minimum value of a BST is always the most left value, so it's needed to read all left pointer until reach the some None value. Only the very last node have None in the left field of the node
def minValue(node):
    currentNode = node

    while (currentNode.left is not None):
        currentNode = currentNode.left # walking downward the tree until reach the very last node

    return(currentNode.data)

#main program

root = None
root = insertNode(root,50)
insertNode(root, 90)
insertNode(root, 140)
insertNode(root, 30)
insertNode(root, 10)
insertNode(root, 45)

print ("Minimum value of Tree: %d" % minValue(root))
