
class linked_list():

    class Node():

        def __init__(self):

            self.next = None
            self.prev = None
            self.data = 'Data'


    def __init__(self):

        self.head = None
        self.tail = None
        self.size = len(linked_list)


    def remove(self, value):
        """
        Remove the first node that contains the inputted value.
        """

        curr = self.head

        while curr is not None:

            if curr.data == value and curr == self.head:

                self.head.next.prev = None
                self.head = self.head.next
                break

            elif curr.data == value and curr == self.tail:

                self.tail.prev.next = None
                self.tail = self.tail.prev
                break

            elif curr.data == value:

                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                break
            
            else:

                curr = curr.next