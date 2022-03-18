# Linked List [What is it?]

### A linked list structures data inside nodes that connect to each other through pointers. If you've ever played with a Barrel of Monkeys, the idea is very similar. A monkey represents a node of data and the arms of the monkey represents the pointers of the node, "pointing" or referencing to the next and previous nodes. Each node can only point to the one behind them and the one in front of them, much like how a monkey can only connect to two others maximum. The head and tail of the linked list is where you're able to access the data within the structure, giving you a starting point that references down the line toward the end or the front. - Also Monkeys have tails too, but that has nothing to do with what we're talking about.

![Photo](https://github.com/joehawkens/data-structures-final/blob/main/Assets/LinkedlistDiagram.PNG)

# Documentation [How to use it?]

### Linked lists are best created by using classes...take a look at this example to get a feel of how it's structured with a class...

``` Python
class linked_list():
    
    def __init__(self):

        self.head = None
        self.tail = None


    class Node():

        def __init__(self, value):

            self.next = None
            self.prev = None
            self.data = value
            
        
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
### This is the bare bones of a linked list. The most important documentation to know is how the list is initialized. First the linked list class is created. Inside of that class is a nested class representing the Node. The Node has 3 attributes that represent both pointers and the data itself. (data, next, and previous). The linked list is initialized with the head and the tail, which will point to the nodes inserted there. Finally, we have the insert_head function. The linked_list class will have several functions which cover the entire breadth of capabilities, such as removing, inserting, iterating, etc. But to keep things simple I've only added what makes up the linked list, rather than what it's able to do.


### Other common operations associated with the Linked list include...

```
Insert Tail/Head:      linked_list.insert_head() or linked_list.insert_tail()
Remove Tail/Head:      linked_list.remove_head() or linked_list.remove_tail()
Insert Node:           linked_list.insert(x, value) - Inserts value after node "x"
Remove Node:           linked_list.remove(value)
Find size (Size):      len(linked_list)
``` 


# Implementation [When to use it?]:
-------|--------|-----------|----------|
Big-O 
-------|--------|-----------|----------|
Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(n)  |  O(n)  |   O(1)    |    O(1)  |
 
### Linked Lists are organized non-contiguously in memory. This means that they are randomly assigned open slots of memory, instead of in sequence, this provides the benefit of saving space within memory. And because they are randomly assigned within memory, Insertion and Deletion are constant time O(1) because inserting won't disrupt neighboring nodes and require shifting the data over 1 space like arrays do. 


# Example:
### As mentioned previously, Linked lists are capable of much more than just inserting at the head. They can insert at the tail, in the middle, Nodes can be removed, replaced, etc. But for the sake of simplicity let's take a deeper look at just one of these operations, the remove Node operation. In this example code we loop through the linked list starting at the head. There are 4 conditionals this runs off of. If the value matches the head, it will insert at the head, the same goes for the tail and a value in the middle. But if none of the values match it will change the "curr" variable to curr.next, which would be the previous of the next node - and on that node all the conditionals will run through again. This process repeats until a match is found. Then the Node will be removed. This is to help show you how the linked list would be iterated in order to remove a node and to get another example of an opeartion performed by the data structure.

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
        self.size = len(linked_list)


    def remove(self, value):
        """
        Remove the first node that contains the inputted value.
        """

        curr = self.head

        while curr is not None:

            if curr.data == value and curr == self.head:

                self.head.next.prev = None
                self.head = self.head.next
                break

            elif curr.data == value and curr == self.tail:

                self.tail.prev.next = None
                self.tail = self.tail.prev
                break

            elif curr.data == value:

                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                break
            
            else:

                curr = curr.next
``` 
# Practice:

### Now that you've seen examples from above, try this practice by implementing a linked list yourself...

### Scenario: You work for a prestigious university that only accepts 15 students at any given time. Each student is assigned a student ID based on their position in this lineup. Because of the difficulty of classes, some students drop out late into their career. This is fine, however, on the student database, each student is registered into a fixed-size array, which means that every time an upper class student drops out, it shifts existing students over 1 space in the lineup. And since student ID numbers are their spot inside this array, it's made it a nightmare for the student records office in assigning student ID's. Now they're assigning you to change the fixed array into a linked list to help them be more organized.

### A linked list has already been created and called to put all 15 students inside of the linked list. The only thing missing is implementing the insert_head and insert_tail functions. Add code to these functions to finish implementation.

``` Python

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

> Linked lists are stored non-contiguously in memory, which saves space in memory if there is large input of data that needs to be stored.

> Linked lists 

