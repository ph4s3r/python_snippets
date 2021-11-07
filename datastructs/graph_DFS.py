class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"Node({self.value})"


def walk_preorder(tree):
    if tree is not None:
        print(tree)
        walk_preorder(tree.left)
        walk_preorder(tree.right)


def walk_postorder(tree):
    if tree is not None:
        walk_preorder(tree.left)
        walk_preorder(tree.right)
        print(tree)

def mytree() -> Node:
    
    t = Node("A")

    t.left = Node("B")
    t.left.left = Node("D")
    t.left.right = Node("E")
    t.right = Node("C")
    
    return t

"""
Example run in console:

from datastructs.graph_DFS import *

t = mytree()

walk_preorder(t)


"""
