Big-O speed complexity
Completed example code problem
Incomplete example code w/ tests

#### Reminder: Data structures are a way to structure data. Some forms work better than others depending on the problem you're trying to solve.


# Queues

### Queues can be thought of as a line at a fast food drive-through. Where the cars represent the data being structured. Each car is served when they reach the order window (the front). When data is added to this structure, it is added in the back of the line, exactly the same way as a drive-through.

![Comparing Queues to a real world situation](https://github.com/joehawkens/data-structures-final/blob/main/Assets/QueueDiagram.PNG?raw=true)

## Purpose:

### This data strucutre is effective when you need to make a line in Software. But what would that look like? Let's say a phone company decides to release a new smartphone at midnight, the demand for this phone is very high, but unfortunately, there's only limited supply due to a battery shortage (only 500 available). The company is expecting way more orders than there are supplies, so how do they choose who gets a phone and who doesn't? The same way a fast food drive-through chooses who's order is going to be cooked. A queue! (a line). That way, instead of deciding on behalf of thousands of customers, you let them decide for themselves if they're going to stay up until midnight and make a pre-order to get a spot in the queue. In software you make a program that takes orders(data) and inserts them into a queue based on the time they made the order. When the first 500 orders are made, you can assign each one based off their position in the queue. It would look a little something like this:

```
def smartphone_queue():

    customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] - Represents 20 customers
    smartphone_orders = [] - Represents a list of customers that made pre-orders


    This for loop 
    for customer in random_customers:

        fast_customer = random.choice(random_customers) 
        random_customers.remove(fast_customer)
        smartphone_orders.append(fast_customer) 



    return smartphone_orders


# Output: [14, 15, 16, 9, 19, 1, 11, 10, 6, 18] 

This represents the customers that stayed up late to make sure
they can process a pre-order before anyone else.

```


## Apply what you learned:
