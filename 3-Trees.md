# Trees [What is it?]

### The Tree data structure gets it's name from a tree in real life. You can imagine a tree flipped upside down. The Tree DS comes in many different flavors (Binary, Search, Red-Black, AVL, etc.) But to keep things grounded we will focus on only one type: The Binary Search Tree (BST). The Tree at it's core is very similar to the Linked List in that it shares a structure of Nodes. However, unlike a linked list, a Node in a Tree is able to reference two other Nodes instead of one. Look at the diagram below for a visual representation:

![A Tree Data Structure](https://github.com/joehawkens/data-structures-final/blob/main/Assets/TreeDiagram.PNG)

### The Root Node represents the Node at the top, it's also a "parent" Node of the Nodes below it. These Nodes are known as it's children Node. And those Children Nodes are parents to the Nodes below them, this pattern repeats the bigger the Tree gets. The Nodes located at the bottom of the tree are known as it's leaves. It's also important to notice that there can be "Subtrees" inside of trees, which simply represent the recurring pattern mentioned earlier.

### The above diagram shows what a tree consists of, but now let's make meaning out of it by adding data into the nodes. The diagram below is a representation of a Binary Search Tree (BST).

![A Binary Search Tree](https://github.com/joehawkens/data-structures-final/blob/main/Assets/BinarySearchTreeDiagram.PNG)

### A Binary Search Tree behaves as follows: Starting at the Root Node we have 12. You will notice that every time you go to the right of a Node, the number will be bigger than the previous, and if you go to the left of a Node, the number gets smaller. A BST is set up this way in order to provide fast access and searchig capabilities, which we will reference later in "Implementation".

# Documentation [How to use it?]

### In the Python programming language, like a Linked List, A Tree is created using Classes. We create the Nodes and add functionality through methods (functions) within the classes. A simple BST structure is show below...
```

```
### Common operations assosciated with the Queue...
```
Adding (Enqueue):  
Removing (Dequeue):    
Find size (Size):      
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
