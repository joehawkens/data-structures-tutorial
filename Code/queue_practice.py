#Scenario: Previous programmer didn't integrate a Queue structure into the preorder process...Instead they used a dictionary.
#Implement the Queue by doing the following:
#       1. Transfer existing customers from the dictionary into a list.
#       2. Create a funciton that can add future customers into the Queue.

#===================================DICTIONARY===========================================

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


queue = []

def add_values_into_queue(dictionary): #Transfer existing customers from dictionary into the queue through this function...

    pass

def add_customer_queue(name): #Let this function add future customers into the Queue.

    pass

def show_customers():

    return queue




#=====TESTS========================================================
add_customer_to_dictionary("Shelby")#Adds a customer to the dictionary.
add_customer_to_dictionary("Ryan")
add_customer_to_dictionary("Louis")

add_values_into_queue(customers)
add_customer_queue('Reggie')
add_customer_queue('Dominic')
add_customer_queue('Lola')

print(show_customers()) #Should return the 20 customers from the dictionary and the three added above (last).
#==================================================================