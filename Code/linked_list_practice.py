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