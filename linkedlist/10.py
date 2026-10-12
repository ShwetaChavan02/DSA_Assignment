# write a function to delete alternate nodes of a singly linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def delfirst_last(self):
        temp = None

    def del_altername(self):
        prev = self.head

        if prev is None:
            return

        temp = self.head.next

        while prev and temp:
            prev.next = temp.next
            temp = None  # removes the link to the node

            prev = prev.next

            if prev:
                temp = prev.next

    def print(self):
        temp = self.head
        print("List elements are:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)
ll.head.next.next.next.next = Node(50)

print("Before deleting alternate nodes:")
ll.print()

ll.del_altername()

print("After deleting alternate nodes:")
ll.print()