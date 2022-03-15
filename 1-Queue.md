Completed example code problem
Incomplete example code w/ tests

#### Data structures are a way to structure data. Some Data Structures work better than others depending on the problem you're solving.


# Queue [What is it?]

### Queues structure data the same way cars line up in a drive-through. To enter (insert) you go in from the back. And to exit (remove) you exit from the front.

![A Queue compared to a line of people](https://github.com/joehawkens/data-structures-final/blob/main/Assets/QueueDiagram.PNG?raw=true)

## Documentation [How to use it]

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


## Implementation [When to use it]:

### This data strucutre is effective when you need to make a "line" in a Software application. You can use other Data Structures to accomplish this task, but they wouldn't be as efficient. As far as Big-O notation goes, the Queue reigns king in Insertion and Deletion with a speed of O(1). This is because there's only one space to insert (the back) and one place to remove (the front).

Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(n)  |  O(n)  |   O(1)    |    O(1)  |

## [Example]:
### Let's see what this looks like with an example problem.

### Scenario: The IT department at your University needs to a software application that lets them recieve help desk tickets around campus in real time. You want to ensure that each ticket is served in the order they are recieved, so you decide to implement the Queue data strucutre into the design...

```
tickets = []


def submit_helpdesk_ticket(problem): #A function that recieves help desk tickets and assigns them a spot in the queue.

    tickets.append(problem)


def show_helpdesk_tickets():

    return tickets


#TESTS ===============
submit_helpdesk_ticket('server_12') # The first ticket issued.
submit_helpdesk_ticket('server_6')
submit_helpdesk_ticket('server_30')
submit_helpdesk_ticket('server_1')
submit_helpdesk_ticket('server_19') # The last ticket issued.

print('====================================\n')
print('The following servers need repairs:')
print(show_helpdesk_tickets())
print('\n====================================')
# Output: ['server_12', 'server_6', 'server_30', 'server_1', 'server_19'] 
# Notice the placement of server_12 and server_19.
```
### Whenever a help desk ticket is issued through the submit_helpdesk_ticket() function it is added to a Queue (list). Then this list is displayed in the order they were recieved. In the tests you can see server 12 and server 19 were the first and last tickets issued, in the output you can see they are the first and last elements in the list (as expected).



## Apply what you've learned [Practice]:
### Now let's try to apply what you've learned.

### Scenario: 
