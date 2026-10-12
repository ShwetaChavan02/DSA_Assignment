# write a function to concatenate two singly linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = list2.head

    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# First linked list
ll1 = LinkedList()
ll1.head = Node(10)
ll1.head.next = Node(20)
ll1.head.next.next = Node(30)

# Second linked list
ll2 = LinkedList()
ll2.head = Node(40)
ll2.head.next = Node(50)

print("First list:")
ll1.print()

print("Second list:")
ll2.print()

# Concatenate lists
ll1.concatenate(ll2)

print("After concatenation:")
ll1.print()