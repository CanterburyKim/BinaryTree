"""
An example file for a Binary Tree implementation
in Python
"""

class Node:
    """
    Binary Tree implementation.  This binary Tree
    contains left, right, value.  left is a reference
    to another Node (lesser value), right is a reference
    to another Node (of greater value), and value is the
    numerical value associated with this Node
    """
    def __init__(self, root_node_value):
        """
        Init the Node by setting left and right to None
        and by setting the value of the Node.
        """
        self.left = None
        self.right = None
        self.value = root_node_value

    def add(self, new_value):
        """
        add a new node to the tree.
        """
        pass
        # TODO: find the correct insertion place

        # TODO: allocate the new Node and assign the value


    def print(self):
        """
        print the entire tree in ascending order
        """

        # TODO: traverse the binary tree and print from smallest to largest

        pass

    def size(self):
        """
        return the size of the tree, ie., the number of nodes
        """

        # TODO: count all the nodes

        return -1

    def contains(self, other_value):
        """
        Search the tree and see if the other_value is contained
        as a value in any of the nodes
        """

        # TODO: search thru the tree and try to match against other_value

        return False
