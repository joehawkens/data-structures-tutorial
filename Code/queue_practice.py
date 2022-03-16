#Scenario: Previous programmer didn't integrate a Queue structure into the order process...Instead he used a dictionary.
#Implement the Queue by adding the customers to the queue from the Dictionary and 

queue = []

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


def add_customer_to_queue():

    pass


#=====TESTS========================================================
add_customer_to_dictionary("Shelby")#Adds a customer to the dictionary.
add_customer_to_dictionary("Ryan")
add_customer_to_dictionary("Louis")



#=====TESTS========================================================


