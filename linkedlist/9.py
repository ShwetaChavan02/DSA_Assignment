# write a function to delete first and last node of a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_first(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head

            while temp.next.next is not None:
                temp = temp.next

            temp.next = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

ll.display()

ll.delete_first()
ll.display()

ll.delete_last()
ll.display()
