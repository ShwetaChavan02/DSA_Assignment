# write a function to find the middle node and then delete it of a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Delete middle node
    def del_middle(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

    # Display linked list
    def print(self):
        temp = self.head
        print("List elements are:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Create linked list
ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)
ll.head.next.next.next.next = Node(50)

print("Before deletion:")
ll.print()

ll.del_middle()

print("After deleting middle node:")
ll.print()