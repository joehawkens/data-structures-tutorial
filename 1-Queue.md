Completed example code problem
Incomplete example code w/ tests

#### Data structures are a way to structure data. Some Data Structures work better than others depending on the problem you're solving.


# Queue [What is it?]

### Queues can be thought of as a line of customers at a grocery store. Where the customers represent the data being structured. When something is added, it starts in the back.
### Each customer is served when they reach the checkout counter (the front) and is then removed from the Queue.

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

### This data strucutre is effective when you need to make a "line" in a Software application. You can use other Data Structures to accomplish this task, but they simply wouldn't be as fast or effective. As far as Big-O notation goes, the Queue reigns king in Insertion and Deletion with a speed of O(1). This is because there's only one space to insert (the back) and one place to remove (the front).

Access | Search | Insertion | Deletion |
-------|--------|-----------|----------|
 O(n)  |  O(n)  |   O(1)    |    O(1)  |

## [Example]:
### Let's see what this looks like with an example problem.

### Scemario: You're creating a program that manages help desk tickets for the IT department. You want to ensure that each ticket is served in the order they are recieved, so you decide to implement the Queue data strucutre in your program...

```
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


```
## Apply what you learned [Practice]:
