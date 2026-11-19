
# Derived Binary Search Tree
# Name: Christian Gonzalez
# Date: November 15, 2026
# Description: This class inherits from BST and adds helper methods
# for checking leaf nodes, counting nodes, finding minimum and
# maximum values, and performing breadth-first traversal.

from collections import deque
from bst import BST


class Derived_BST(BST):

    def __init__(self):
        # Call the parent class constructor
        super().__init__()

    # Check if a node is a leaf node
    def is_leaf(self, key):
        node = self.search(key)

        if node is None:
            return False

        return node.left is None and node.right is None

    # Check if a node is a branch (has at least one child)
    def is_branch(self, key):
        node = self.search(key)

        if node is None:
            return False

        return node.left is not None or node.right is not None

    # Find the parent of a node
    def parent_node(self, key):
        current = self.root
        parent = None

        while current is not None:
            if current.key == key:
                return parent

            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # Count the total number of leaf nodes
    def total_leaf_nodes(self, node):

        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return (self.total_leaf_nodes(node.left) +
                self.total_leaf_nodes(node.right))

    # Count the total number of non-leaf nodes
    def total_nonleaf_nodes(self):
        return self._count_nonleaf_nodes(self.root)

    # Helper method for counting non-leaf nodes
    def _count_nonleaf_nodes(self, node):

        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 0

        return (1 + self._count_nonleaf_nodes(node.left) +
                self._count_nonleaf_nodes(node.right))

    # Find the maximum value in the tree
    def get_max(self):

        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.key

    # Find the minimum value in the tree
    def get_min(self):

        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.key

    # Perform breadth-first traversal
    def breadth_first(self):

        if self.root is None:
            return

        queue = deque([self.root])

        while queue:

            level_size = len(queue)
            level_nodes = []

            for i in range(level_size):

                current = queue.popleft()
                level_nodes.append(str(current.key))

                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

            print(" ".join(level_nodes))
