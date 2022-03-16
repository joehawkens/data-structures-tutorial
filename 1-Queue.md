# Queue [What is it?]

### Queues structure data the same way cars line up in a drive-through. To enter (insert) you go in from the back. And to exit (remove) you leave from the front.

![A Queue compared to a line of people](https://github.com/joehawkens/data-structures-final/blob/main/Assets/QueueDiagram.PNG?raw=true)

## Documentation [How to use it?]

### In the Python programming language, a Queue is implemented as a list, so if you wanted to make a Queue you'd simply make a list...
```
queue = []
```
### Common operations assosciated with the Queue...
```
Adding (Enqueue):      queue.append(item)
Removing (Dequeue):    queue.remove[0] OR queue.pop(0)    
Find size (Size):      size = len(queue)
``` 


## Implementation [When to use it?]:

### You implement Queues when the way data is ordered is important. You can use other Data Structures to accomplish this task, but they wouldn't be as efficient. As far as Big-O notation goes, Insertion and Deletion with a Queue boasts an impressive O(1). This is because there's only one space to insert (the back) and one place to remove (the front).

Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(n)  |  O(n)  |   O(1)    |    O(1)  |

# Example:
### Let's see what this looks like with an example problem.

### Scenario: The IT department at BYUI needs a software application that lets them recieve help desk tickets from locations around campus in real time. You want to ensure that each ticket is served in the order they are recieved, so you decide to implement the Queue data structure into the design...
```
class Queue():

    def __init__(self):

        self.tickets = []


    def submit_helpdesk_ticket(self, location): #A function that recieves help desk tickets and assigns them a spot in the queue.

        self.tickets.append(location)


    def show_helpdesk_tickets(self):

        return self.tickets


    def show_next_ticket(self):

        return self.tickets.pop(0)


ticket_object = Queue()

#TESTS ===============
ticket_object.submit_helpdesk_ticket("STC111") # The first ticket issued.
ticket_object.submit_helpdesk_ticket('ROM201')
ticket_object.submit_helpdesk_ticket('STC207')
ticket_object.submit_helpdesk_ticket('KIM333')
ticket_object.submit_helpdesk_ticket('MC107') # The last ticket issued.

print('====================================\n')
print('The next location that needs assistance: ')
print(ticket_object.show_next_ticket()) #Shows the first ticket in Queue.


print('The following locations need assistance:') #Shows the rest of the tickets ini Queue.
print(ticket_object.show_helpdesk_tickets())
print('\n====================================')
# Output: 
The next location that needs assistance:
STC111
The following locations need assistance:
['ROM201', 'STC207', 'KIM333', 'MC107']

Notice the placement of 'STC111' and 'MC107'
```
### Whenever a help desk ticket is issued through the submit_helpdesk_ticket() function it is added to a Queue (list). Then this list is displayed in the order they were recieved. In the tests you can see 'STC111' and 'MC107' were the first and last tickets issued, in the output you can see they are the first and last elements in the list. The first ticket is being shown by the show_next_ticket() function, which grabs the first in the Queue and displays it.

# Practice:

### Scenario: You work for a phone company that plans on releasing a new Smartphone soon. They usually have enough supply to meet demand, however, due to the global semiconductor shortage they know they'll run out as soon as they release. Because of this, they've started a preorder campaign so customers can sign up as shipments are resupplied.
### However, the programmer that created the backend code for preorders used a dictionary to order the data instead of a list. Although this can work as a solution this makes the operations inefficient as a dictionary has a speed of O(n) for Insertion and Deletion, as opposed to O(1) for Queues.

```
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

class Queue():

    def __init__(self):

        self.queued_customers = []

    def add_values_into_queue(self, dictionary): #Transfer existing customers from dictionary into the queue through this function...

        pass

    def add_customer_queue(self, name): #Let this function add future customers into the Queue.

        pass

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

print(show_customers()) 
#Expected output: 
['Rob', 'Kelly', 'Anna', 'Katie', 'Peter', 'Joshua', 'Karen', 'Ignacio', 'Johann', 'Frank', 'Derrin', 'Sarah', 'Jake', 'Meagan', 'Richard', 'Manny', 'Sam', 'Matthew', 'Maria', 'Jessica', 'Shelby', 'Ryan', 'Louis', 'Reggie', 'Dominic', 'Lola']


#==================================================================
```

## Solution: !(https://github.com/joehawkens/data-structures-final/blob/main/Code/queue_solution.py)

## Key Takeaways:

> In the Python programming language, a Queue is implemented as a list.

> How to know when to implement Queues? You should consider implementing Queues when the way data is ordered takes priority in a problem.

> Queues have fast speeds when it comes to adding and removing elements.
