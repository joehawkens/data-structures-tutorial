
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


    def insert_tail(self, value):
        """
        Insert a new node at the back, the tail, of the linked list.
        """

        new_node = linked_list.Node(value)  
        
        if self.head is None:

            self.head = new_node
            self.tail = new_node

        else:

            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        """ 
        Remove the first node from the linked list.
        """

        if self.head == self.tail:

            self.head = None
            self.tail = None

        elif self.head is not None:

            self.head.next.prev = None
            self.head = self.head.next

    def remove_tail(self):
        """
        Remove the last node from the linked list.
        """
        
        self.tail.prev.next = None
        self.tail = self.tail.prev

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

    def replace(self, old_value, new_value):

        """
        Replaces a specified node with a new value given by the user.
        """
        
        curr = self.head

        while curr is not None:

            if curr.data == old_value and curr == self.head:

                curr.data = new_value

            elif curr.data == old_value and curr == self.tail:

                curr.data = new_value

            elif curr.data == old_value:

                
                curr.data = new_value
            
            else:

                curr = curr.next

    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        curr = self.tail  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev # Go forward in the linked list

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list