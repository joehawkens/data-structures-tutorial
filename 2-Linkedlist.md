# Linked List [What is it?]

### A linked list structures data inside nodes that connect to each other through pointers. If you've ever played with a Barrel of Monkeys, the idea is very similar. A monkey represents a node of data and the arms of the monkey represents the pointers of the node, "pointing" or referencing to the next and previous nodes. Each node can only point to the one behind them and the one in front of them, much like how a monkey can only connect to two others maximum. The head and tail of the linked list is where you're able to access the data within the structure, giving you a starting point that references down the line toward the end or the front. - Also Monkeys have tails too, but that has nothing to do with what we're talking about.

![Photo](https://github.com/joehawkens/data-structures-final/blob/main/Assets/LinkedlistDiagram.PNG)

# Documentation [How to use it?]

### Linked lists are best created by using a class...take a look at this example to get a feel of how it's structured with a class...

``` Python
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
### This is the bare bones of a linked list. The most important documentation to know is how the list is made. First the linked list class is created. Inside of that class is a nested class representing the Node. The node has 3 attributes that represent both pointers and the data itself. (data, next, and previous). The linked list is initialized with the head and the tail, which will point to the nodes inserted there. Finally, we have the insert_head function. The linked_list class will have several functions which cover the entire breadth of capabilities, such as removing, inserting, iterating, etc. But to keep things simple I've only added the insert head function for you to get a feel of how all these elements interact.


### Common operations associated with the Queue...

```
Insert Tail/Head:      linked_list.append(value) or linked_list.appendleft(value)
Remove Tail/Head:      linked_list.pop(0) or linked_list.pop()
Insert Node:           insert(i, value) - Insert value after i
Remove Node:           del linked_list(value)
Replace Node:          linked_list.replace(value)
Find size (Size):      len(linked_list)
``` 


# Implementation [When to use it?]:

Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(n)  |  O(n)  |   O(1)    |    O(1)  |
 
### Linked Lists are organized non-contiguously in memory. This means that they are randomly assigned open slots of memory, instead of in sequence, this provides the benefit of saving space within memory. And because they are randomly assigned within memory, Insertion and Deletion are constant time O(1) because inserting won't disrupt neighboring nodes and require shifting the data over 1 space like arrays do. This can be especially helpful when you need to have your data stored and be easily referenced.


# Example:
### Now that we know Linked lists contain data points that are easily removed and inserted, let's look at a real world example of this. Think of a text editor on a computer and how each letter in such a document is referencing the next and followed by the previous. It sounds a lot like a linked list. 

### Scenario: 
``` Python
``` 
### Example Notes




# Practice:

### Try this practice by implementing a linked list yourself...

### Scenario: You work for a prestigious university that only accepts 15 students at any given time. Because of the difficulty of classes, some students drop out late into their career. This is fine, however, on the student database, each student is registered into a fixed-size array, which means that every time an upper class student drops out, it shifts existing students over 1 space in the lineup. And since student ID numbers are their spot inside this array, it's made it a nightmare for the student records office in assigning student ID's. Now they're assigning you to change the student database into a linked list instead of an array to help organize them be more organized.

``` Python
#We need to add the students from the array into the linked list. To do this follow these steps:
#   1. Add the first student at the head.
#   2. Add the proceeding students at the tail.



# Student database (fixed array)
# students[0] = Rob - Student ID = 0
# students[1] = Cher - Student ID = 1
# students[14] = Mariah - Student ID = 14

students = ["Rob", "Cher", "Michael", "Arianna", "Taylor", "Kanye", "Selena", "Marshal", "Jimi", "Bob", "Whitney", "David", "Paul", "Aretha", "Mariah"]


class linked_list():

    class Node():

        def __init__(self, value):

            self.next = None
            self.prev = None
            self.data = value


    def __init__(self):

        self.head = None
        self.tail = None



    def insert_head(self, value):
        """
        Insert a new node at the front, the head, of the linked list. 
        """



    def insert_tail(self, value):
        """
        Insert a new node at the back, the tail, of the linked list.
        """


    def go_forward(self):
    
        current = self.head
       
        while current is not None:
            
            print(current.data)
            current = current.next




#======================================
student_data = linked_list() #Creates the linked list.
# =============== TESTS ===============
student_data.insert_head('Rob')
student_data.insert_tail('Cher')
student_data.insert_tail('Michael')
student_data.insert_tail('Arianna')
student_data.insert_tail('Taylor')
student_data.insert_tail('Kanye')
student_data.insert_tail('Selena')
student_data.insert_tail('Marshal')
student_data.insert_tail('Jimi')
student_data.insert_tail('Bob')
student_data.insert_tail('Whitney')
student_data.insert_tail('David')
student_data.insert_tail('Paul')
student_data.insert_tail('Aretha')
student_data.insert_tail('Mariah')
#======================================
print(student_data.go_forward())
# Expected output:
'''
Rob
Cher
Michael
Arianna
Taylor
Kanye
Selena
Marshal
Jimi
Bob
Whitney
David
Paul
Aretha
Mariah
'''
#======================================
```

## [Click here for the solution](https://github.com/joehawkens/data-structures-final/blob/main/Code/linked_list_solution.py)

## Key Takeaways:

> Linked lists are useful for manipulating individual data points (Nodes) without disrupting the location of other Nodes in the structure.

> Linked lists are stored non-contiguously in memory, which saves space in memory if there is large input.

> Linked lists are extremely effective when you need to do a lot of insertions/removals.

