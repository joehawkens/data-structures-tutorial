# Linked List [What is it?]

### A linked list structures data inside nodes that connect to each other through pointers. If you've ever played with a Barrel of Monkeys, the idea is very similar. A monkey represents a node of data and the arms of the monkey represents the pointers of the node, "pointing" or referencing to the next and previous nodes. Each node can only point to the one behind them and the one in front of them, much like how a monkey can only connect to two others maximum. The head and tail of the linked list is where you're able to access the data within the structure, giving you a starting point that references down the line toward the end or the front. - Also Monkeys have tails too, but that has nothing to do with what we're talking about.

![Photo](https://github.com/joehawkens/data-structures-final/blob/main/Assets/LinkedlistDiagram.PNG)

# Documentation [How to use it?]

### Linked lists are best created by using a Class...take a look at this example to get a feel of how it's structured with a class...

```
class linked_list():

    class Node():

        def __init__(self):

            self.next = None
            self.prev = None
            self.data = 'Data'


    def __init__(self):

        self.head = None
        self.tail = None
        
     def insert_head(self, value):
        """
        Insert a new node at the front, the head, of the linked list. 
        """
        new_node = linked_list.Node(value)  
        
        if self.head is None:
            
            self.head = new_node
            self.tail = new_node
            
        else:

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
```
### This is the bare bones of a linked list. The most important documentation to know is how the list is made. First the linked list class is created. Inside of that class is a nested class representing the Node. The node has 3 attributes that represent both pointers and the data itself. (data, next, and previous). The linked list is initialized with the head and the tail, which will point to the nodes inserted there. Finally, we have the insert_head function. The linked_list class will have several functions which cover the entire breadth of capabilities, such as removing, inserting, iterating, etc. But to keep things simple we'll just look at the insert_head functions to get an idea of how all these elements play together...

### 

### Common operations assosciated with the Queue...
```
Adding (Enqueue):  
Removing (Dequeue):    
Find size (Size):      
``` 


# Implementation [When to use it?]:

### A linked list 

Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(n)  |  O(n)  |   O(1)    |    O(1)  |

# Example:
### Let's see what this looks like with an example problem.

### Scenario: 
```
```
### Example Notes

# Practice:

### Try this practice by implementing a linked list yourself...

### Scenario: .....

```
CODE
```

## [Click here for the solution](Solution link)

## Key Takeaways:

> Takeaway 1

> Takeaway 2

> Takeaway 3

