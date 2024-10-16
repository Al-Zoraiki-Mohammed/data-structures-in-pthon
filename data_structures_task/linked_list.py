"""Implementation of LinkedList data structure from scratch"""


class Node:
    """Represents a node in a LinkedList 
    with a data and next values.
"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """Representing a linked list data structure."""
    def __init__(self):
        self.head = None

    def prepend(self, data):
        """add an element to the beginning of the list"""
        self.head = Node(data, self.head)

    def append(self, data):
        """add an element to the end of the list"""
        if self.head is None:
            self.head = Node(data, None)
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next

            # when reach the end, new node should be created
            iterator.next = Node(data, None)

    def get_len(self):
        """to get the length of the linked list"""
        counter = 0
        iterator = self.head
        while iterator:
            counter += 1
            iterator = iterator.next
        return counter

    def delete(self, idx):
        """delete the element by index"""
        if idx < 0 or idx >= self.get_len():
            raise Exception(f'{idx} is an invalid index')

        if idx == 0:
            self.head = self.head.next
            return

        counter = 0
        iterator = self.head
        while iterator:
            if counter == idx - 1:
                if iterator.next.next is None:
                    iterator.next = None
                else:
                    iterator.next = iterator.next.next
                break

            iterator = iterator.next
            counter += 1

    def insert(self, data, idx):
        """insert the element at a specific index with the elements shifted to the right"""
        if idx < 0 or idx > self.get_len():
            raise Exception(f'{idx} is an invalid index')

        if idx == 0:
            self.prepend(data)
            return

        counter = 0
        iterator = self.head

        while iterator:
            if counter == idx - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break
            iterator = iterator.next
            counter += 1

    def lookup(self, value):
        """find the index of the element by value (the first one found)"""
        iterator = self.head
        index = 0
        while iterator:
            if iterator.data == value:
                return index
            iterator = iterator.next
            index += 1
        return -1

    def print_linked_list(self):
        """Print the liked list elements to the std output"""
        if self.head is None:
            print('empty linked list')
        else:
            iterator = self.head
            ll_str = ''

            while iterator:
                ll_str += f'|{str(iterator.data)}| --> '
                iterator = iterator.next

            print(ll_str[:-4])


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.prepend(7)
    linked_list.append(3)
    linked_list.prepend(70)
    linked_list.append(30)
    linked_list.print_linked_list()
    linked_list.delete(1)
    linked_list.print_linked_list()
    linked_list.insert(77, 2)
    linked_list.print_linked_list()
    print(linked_list.lookup(70))
    print(linked_list.lookup(100))  # Output: -1 (Value not found)
