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


        def __init__(self, data):
        
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):

        if data < node.data:

            if node.left is None:

                node.left = BST.Node(data)
            else:

                self._insert(data, node.left)
        else:
 
            if node.right is None:
                node.right = BST.Node(data)
            else:

                self._insert(data, node.right)

         
    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

```
### Common operations assosciated with the BST...
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

### As you can see, the BST has an O(log(n)) time complexity for it's data within all common operations. This differs from other major Data Structures in that it is faster than O(n) time. (Remember: Fastest to slowest = O(1) --> O(log(n)) --> O(n)). This provides a great data structure for quickly searching, insertion, and deletion.


## An important concept: Recursion

### Recursion is a poetic way of saying 'loop'. It's nearly identical to loops in programming, with the exception of how the loop is created: within a function. Recursion occurs when a function is called within itself. This loop will continue on forever, so most of the time there's a "break point" that's included within the function to prevent crashing your computer. Look at the diagram below for a visual representation:

![Visual Diagram of Recursion](https://github.com/joehawkens/data-structures-final/blob/main/Assets/RecursionDiagram.PNG)

### Recursion is an important concept to understand with BSTs because they are implemented within them. You'll see this in the practice problem below:


## Now that you have an idea of the what and how, let's jump right into a practice problem. Your goal will be to add data to the BST. Reference the example above for hints on how to accomplish this method within the BST class.


# Practice:

``` Python

class BST:


    class Node:


        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
        
            self.root = BST.Node(data)
            
        else:
        
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):

        if data < node.data:
     
            if node.left is None:
 
                node.left = BST.Node(data)
                
            else:
  
                self._insert(data, node.left)
            else:
   
                node.right = BST.Node(data)
            else:
                
                # RECURSION (calling the function on itself)
                self._insert(data, node.right)

```

## [Click here for the solution](https://github.com/joehawkens/data-structures-final/blob/main/Code/tree_solution.py)

## Key Takeaways:

> A Binary Search Tree is extremely efficient in searching within it's Nodes, pulling an impressive O(log(n)) time complexity.

> The Tree is very beneficial if you need real-time data accessed faster than O(n) time.

> Binary Trees are similar to Linked Lists in that they are structured with Nodes.
