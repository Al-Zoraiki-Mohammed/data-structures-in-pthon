"""Implementation of Stack data structure from scratch"""


class Node:
    """Represents a node in a Stack 
    with a data and next values.
"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    """Representing a linked list data structure."""
    def __init__(self):
        self.top = None

    def push(self, data):
        """Add an element to the top of the stack"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove the last element from the stack"""
        if self.top is None:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        """Get the value of the last element of the stack"""
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data

    def print_stack(self):
        """Print the elements of the stack"""
        if self.top is None:
            print('empty stack')
        else:
            iterator = self.top
            stack_str = ''
            while iterator:
                stack_str += f'|{str(iterator.data)}|\n'
                iterator = iterator.next
            print(stack_str)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.print_stack()
    stack.push(2)
    stack.print_stack()
    stack.push(3)
    stack.print_stack()
    stack.push(4)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.push(5)
    stack.print_stack()
    print(stack.peek())
