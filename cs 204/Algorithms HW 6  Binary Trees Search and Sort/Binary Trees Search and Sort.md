Below is the Pseudocode  implementation of a Binary Search Tree (BST) with pre-order, in-order, and post-order traversal, along with an AVL tree for maintaining balance:

```pascal
// Node structure for Binary Search Tree
Node:
    value
    left_child
    right_child

// Binary Search Tree class
BST:
    root
    
    // Constructor to initialize an empty BST
    Constructor():
        root = null

    // Function to insert a value into the BST
    Insert(value):
        root = InsertRecursive(root, value)

    // Recursive function to insert a value into the BST
    InsertRecursive(node, value):
        if node == null:
            node = CreateNode(value)
        else if value < node.value:
            node.left_child = InsertRecursive(node.left_child, value)
        else:
            node.right_child = InsertRecursive(node.right_child, value)
        return node
    
    // Function to create a new node with given value
    CreateNode(value):
        newNode = Node()
        newNode.value = value
        newNode.left_child = null
        newNode.right_child = null
        return newNode

    // Function for pre-order traversal of the BST
    PreOrderTraversal():
        PreOrderRecursive(root)

    // Recursive function for pre-order traversal
    PreOrderRecursive(node):
        if node != null:
            print(node.value)
            PreOrderRecursive(node.left_child)
            PreOrderRecursive(node.right_child)

    // Function for in-order traversal of the BST
    InOrderTraversal():
        InOrderRecursive(root)

    // Recursive function for in-order traversal
    InOrderRecursive(node):
        if node != null:
            InOrderRecursive(node.left_child)
            print(node.value)
            InOrderRecursive(node.right_child)

    // Function for post-order traversal of the BST
    PostOrderTraversal():
        PostOrderRecursive(root)

    // Recursive function for post-order traversal
    PostOrderRecursive(node):
        if node != null:
            PostOrderRecursive(node.left_child)
            PostOrderRecursive(node.right_child)
            print(node.value)

// AVL Tree class for balancing BST
AVLTree:
    // Function to get height of a node
    Height(node):
        if node == null:
            return 0
        return max(Height(node.left_child), Height(node.right_child)) + 1

    // Function to get balance factor of a node
    BalanceFactor(node):
        return Height(node.left_child) - Height(node.right_child)

    // Function to rotate subtree rooted with 'node' to the right
    RotateRight(node):
        newRoot = node.left_child
        node.left_child = newRoot.right_child
        newRoot.right_child = node
        return newRoot

    // Function to rotate subtree rooted with 'node' to the left
    RotateLeft(node):
        newRoot = node.right_child
        node.right_child = newRoot.left_child
        newRoot.left_child = node
        return newRoot

    // Function to balance the BST
    Balance(node):
        if node == null:
            return null
        balance = BalanceFactor(node)
        
        // Left heavy
        if balance > 1:
            if BalanceFactor(node.left_child) < 0:
                node.left_child = RotateLeft(node.left_child)
            return RotateRight(node)
        
        // Right heavy
        else if balance < -1:
            if BalanceFactor(node.right_child) > 0:
                node.right_child = RotateRight(node.right_child)
            return RotateLeft(node)
        
        return node
```

Explanation:
- The `Node` structure represents a single node in the Binary Search Tree.
- The `BST` class contains methods to perform operations like insertion and traversals (pre-order, in-order, post-order).
- AVL Tree operations like `Height`, `BalanceFactor`, `RotateRight`, `RotateLeft`, and `Balance` are implemented to maintain balance in the BST.
- During insertion, the `Balance` function is called to ensure the balance property of the AVL tree.
- Traversal methods (`PreOrderTraversal`, `InOrderTraversal`, `PostOrderTraversal`) are implemented recursively.
- The `CreateNode` function is a helper function to create a new node with a given value.
