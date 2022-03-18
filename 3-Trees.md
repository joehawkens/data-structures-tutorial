# Trees [What is it?]

### The Tree data structure gets it's name from a tree in real life. You can imagine a tree flipped upside down. The Tree DS comes in many different flavors (Binary, Search, Red-Black, AVL, etc.) But to keep things grounded we will focus on only one type: The Binary Search Tree (BST). The Tree at it's core is very similar to the Linked List in that it shares a structure of Nodes. However, unlike a linked list, a Node in a Tree is able to reference two other Nodes instead of one. Look at the diagram below for a visual representation:

![A Tree Data Structure](https://github.com/joehawkens/data-structures-final/blob/main/Assets/TreeDiagram.PNG)

### The Root Node represents the Node at the top, it's also a "parent" Node of the Nodes below it. These Nodes are known as it's children Node. And those Children Nodes are parents to the Nodes below them, this pattern repeats the bigger the Tree gets. The Nodes located at the bottom of the tree are known as it's leaves. It's also important to notice that there can be "Subtrees" inside of trees, which simply represent the recurring pattern mentioned earlier.

### The above diagram shows what a tree consists of, but now let's make meaning out of it by adding data into the nodes. The diagram below is a representation of a Binary Search Tree (BST).

![A Binary Search Tree](https://github.com/joehawkens/data-structures-final/blob/main/Assets/BinarySearchTreeDiagram.PNG)

### A Binary Search Tree behaves as follows: Starting at the Root Node we have 12. You will notice that every time you go to the right of a Node, the number will be bigger than the previous, and if you go to the left of a Node, the number gets smaller. A BST is set up this way in order to provide fast access and searchig capabilities, which we will reference later in "Implementation".

# Documentation [How to use it?]

### In the Python programming language, like a Linked List, A Tree is created using Classes. We create the Nodes and add functionality through methods (functions) within the classes. A simple BST structure is show below...
``` Python
"""
A Simple, bare-bones, binary search tree.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

         
    def __iter__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a loop
        is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
        use.  When the 'for' loop wants to get the next value, the code in
        this function will start back up where the last 'yield' returned a 
        value.  The keyword 'yield from' is used when we want to 'yield' a
        value that is returned from a function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(1)
for x in tree:
    print(x)  # 1, 3, 5, 7, 10

```
### Common operations assosciated with the Queue...
```
Insert(value)
Remove(value)
Traverse Forward
Traverse Reverse
Contains(value)
``` 


# Implementation [When to use it?]:

### Big-O Notation

Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(log(n))  |  O(log(n))  |   O(log(n))    |    O(log(n))  |

# Example:
### Let's see what this looks like with an example problem.

### Scenario: 
```
```
### Additional Example Notes

# Practice:

### Try this practice by implementing a linked list yourself...

### Scenario: .....

```
CODE
```

## [Click here for the solution](https://github.com/joehawkens/data-structures-final/blob/main/Code/tree_solution.py)

## Key Takeaways:

> A Binary Search Tree is extremely efficient in searching and accessing data within it's Nodes, pulling an impressive O(log(n)) time complexity.

> Takeaway 2

> Takeaway 3
