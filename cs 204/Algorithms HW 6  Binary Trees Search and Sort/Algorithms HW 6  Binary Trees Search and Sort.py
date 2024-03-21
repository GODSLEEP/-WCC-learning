# Node structure for Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None

    # Function to insert a value into the BST
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    # Recursive function to insert a value into the BST
    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left_child = self._insert_recursive(node.left_child, value)
        else:
            node.right_child = self._insert_recursive(node.right_child, value)
        return node

    # Function for pre-order traversal of the BST
    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)

    # Recursive function for pre-order traversal
    def _pre_order_recursive(self, node):
        if node is not None:
            print(node.value)
            self._pre_order_recursive(node.left_child)
            self._pre_order_recursive(node.right_child)

    # Function for in-order traversal of the BST
    def in_order_traversal(self):
        self._in_order_recursive(self.root)

    # Recursive function for in-order traversal
    def _in_order_recursive(self, node):
        if node is not None:
            self._in_order_recursive(node.left_child)
            print(node.value)
            self._in_order_recursive(node.right_child)

    # Function for post-order traversal of the BST
    def post_order_traversal(self):
        self._post_order_recursive(self.root)

    # Recursive function for post-order traversal
    def _post_order_recursive(self, node):
        if node is not None:
            self._post_order_recursive(node.left_child)
            self._post_order_recursive(node.right_child)
            print(node.value)

# AVL Tree class for balancing BST
class AVLTree:
    # Function to get height of a node
    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left_child), self.height(node.right_child)) + 1

    # Function to get balance factor of a node
    def balance_factor(self, node):
        return self.height(node.left_child) - self.height(node.right_child)

    # Function to rotate subtree rooted with 'node' to the right
    def rotate_right(self, node):
        new_root = node.left_child
        node.left_child = new_root.right_child
        new_root.right_child = node
        return new_root

    # Function to rotate subtree rooted with 'node' to the left
    def rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        new_root.left_child = node
        return new_root

    # Function to balance the BST
    def balance(self, node):
        if node is None:
            return None
        balance = self.balance_factor(node)
        
        # Left heavy
        if balance > 1:
            if self.balance_factor(node.left_child) < 0:
                node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        
        # Right heavy
        elif balance < -1:
            if self.balance_factor(node.right_child) > 0:
                node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)
        
        return node

# Example usage:
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("In-order traversal:")
bst.in_order_traversal()

print("\nPre-order traversal:")
bst.pre_order_traversal()

print("\nPost-order traversal:")
bst.post_order_traversal()
