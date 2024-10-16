"""Implementation of Queue data structure from scratch"""


class Node:
    """Represents a node in a Queue 
    with a data and next values.
"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    """Representing a queue data structure."""
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        """Add an element to the end of the queue"""
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.front is None:
            raise Exception("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        """Get the value of the element at the front of the queue"""
        if self.front is None:
            raise Exception("Queue is empty")
        return self.front.data

    def print_queue(self):
        """Print the elements of the queue"""
        if self.front is None:
            print('empty queue')
        else:
            iterator = self.front
            queue_str = ''

            while iterator:
                queue_str += f'|{str(iterator.data)}| '
                iterator = iterator.next

            print(queue_str[::-1])


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.print_queue()
    queue.enqueue(2)
    queue.print_queue()
    queue.enqueue(3)
    queue.print_queue()
    queue.enqueue(4)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.enqueue(5)
    queue.print_queue()
    print(queue.peek())
