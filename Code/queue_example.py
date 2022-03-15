
tickets = []


def submit_helpdesk_ticket(problem): #A function that recieves help desk tickets and assigns them a spot in the queue.

    tickets.append(problem)


def show_helpdesk_tickets():

    return tickets


#TESTS ===============
submit_helpdesk_ticket('server_12')
submit_helpdesk_ticket('server_6')
submit_helpdesk_ticket('server_30')
submit_helpdesk_ticket('server_1')
submit_helpdesk_ticket('server_19')

print('====================================\n')
print('The following servers need repairs:')
print(show_helpdesk_tickets())
print('\n====================================')

#Expected output: ['server_12', 'server_6', 'server_30', 'server_1', 'server_19']
#=====================



