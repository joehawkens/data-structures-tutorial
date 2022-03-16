tickets = []


def submit_helpdesk_ticket(location): #A function that recieves help desk tickets and assigns them a spot in the queue.

    tickets.append(location)


def show_helpdesk_tickets():

    return tickets


#TESTS ===============
submit_helpdesk_ticket('STC111') # The first ticket issued.
submit_helpdesk_ticket('ROM201')
submit_helpdesk_ticket('STC207')
submit_helpdesk_ticket('KIM333')
submit_helpdesk_ticket('MC107') # The last ticket issued.

print('====================================\n')
print('The following servers need repairs:')
print(show_helpdesk_tickets())
print('\n====================================')
# Output: ['STC111', 'ROM201', 'STC207', 'KIM333', 'MC107']
# Notice the placement of 'STC111' and 'MC107'



