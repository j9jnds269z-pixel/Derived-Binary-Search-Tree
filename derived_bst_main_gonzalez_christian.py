
# Derived Binary Search Tree - Main Program
# Name: Christian Gonzalez
# Date: November 15, 2026
# Description: This program tests the Derived_BST class by
# inserting nodes, finding maximum and minimum values,
# checking leaf and branch nodes, counting nodes, and
# displaying a breadth-first traversal.

from derived_bst import Derived_BST


def main():

    # Create a new binary search tree
    tree = Derived_BST()

    # Insert the original nodes
    values = [12, 5, 46, 80, 30, 2, 56, 25, 10]

    for value in values:
        tree.insert_node(value)
        print(f"Node {value} has been added to the tree")

    # Display maximum and minimum values
    print(f"Node with max value: {tree.get_max()}")
    print(f"Node with min value: {tree.get_min()}")

    # Add a new node
    tree.insert_node(37)
    print("New node 37 has been added to the tree")

    # Check whether node 37 is a leaf or branch
    print(f"Node 37 is a leaf node? {tree.is_leaf(37)}")
    print(f"Node 37 is a branch? {tree.is_branch(37)}")

    # Find the parent of node 37
    parent = tree.parent_node(37)

    if parent is not None:
        print(f"Node {parent.key} is the parent node of node 37")

    # Count leaf and non-leaf nodes
    print(f"Total leaf nodes: {tree.total_leaf_nodes(tree.root)}")
    print(f"Total non-leaf nodes: {tree.total_nonleaf_nodes()}")

    # Display breadth-first traversal
    print("Breadth-First Traversal:")
    tree.breadth_first()


# Run the main program
if __name__ == "__main__":
    main()
