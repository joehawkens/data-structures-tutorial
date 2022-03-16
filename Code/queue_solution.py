#========================================================SOLUTION===========================================================

#Scenario: Previous programmer didn't integrate a Queue structure into the preorder process...Instead they used a dictionary.
#Implement the Queue by doing the following:
#       1. Transfer existing customers from the dictionary into a list.
#       2. Create a funciton that can add future customers into the Queue.

#=======================================================DICTIONARY==========================================================

customers = {

    #number:name
    #number represents their place in the Queue. (1 = first, 20 = last, etc.)

    1:'Rob',
    2:'Kelly',
    3:'Anna',
    4:'Katie',
    5:'Peter',
    6:'Joshua',
    7:'Karen',
    8:'Ignacio',
    9:'Johann',
    10:'Frank',
    11:'Derrin',
    12:'Sarah',
    13:'Jake',
    14:'Meagan',
    15:'Richard',
    16:'Manny',
    17:'Sam',
    18:'Matthew',
    19:'Maria',
    20:'Jessica'

}


def add_customer_to_dictionary(name): #Adds customer to dictionary.

    amount = len(customers) + 1
    customers[amount] = name

#==================================QUEUE===========================================

class Queue():

    def __init__(self):

        self.queued_customers = []

    def add_values_into_queue(self, dictionary):

        for key in dictionary:

            value = dictionary.get(key)
            self.queued_customers.append(value)


    def add_customer_queue(self, name):

        self.queued_customers.append(name)

    def show_customers(self):

        return self.queued_customers




#=====TESTS========================================================
new_queue = Queue() #Instantiates the Queue object.

add_customer_to_dictionary("Shelby")#Adds a customer to the dictionary.
add_customer_to_dictionary("Ryan")
add_customer_to_dictionary("Louis")

new_queue.add_values_into_queue(customers)
new_queue.add_customer_queue('Reggie')
new_queue.add_customer_queue('Dominic')
new_queue.add_customer_queue('Lola')

print(new_queue.show_customers()) #Should return the 20 customers from the dictionary and the three added above (last).
#Output:
#['Rob', 'Kelly', 'Anna', 'Katie', 'Peter', 'Joshua', 'Karen', 
# 'Ignacio', 'Johann', 'Frank', 'Derrin', 'Sarah', 'Jake', 
# 'Meagan', 'Richard', 'Manny', 'Sam', 'Matthew', 'Maria', 
# 'Jessica', 'Shelby', 'Ryan', 'Louis', 'Reggie', 'Dominic', 'Lola']

#==================================================================