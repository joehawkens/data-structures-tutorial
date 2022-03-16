
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
print('The next location that needs assistance: ') #Shows the first ticket in Queue.
print(ticket_object.show_next_ticket())


print('The following locations need assistance:')
print(ticket_object.show_helpdesk_tickets())
print('\n====================================')
# Output: ['STC111', 'ROM201', 'STC207', 'KIM333', 'MC107']
# Notice the placement of 'STC111' and 'MC107'