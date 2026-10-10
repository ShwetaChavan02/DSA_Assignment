#Ass1: Create a Singly Linear Linked List with following operations
#Create Linked List
#Traverse and print the node values
#Insert node at a specific position
#Find Middle node and print its value
#Delete node
#Reverse list
#Calculate the sum of every two consecutive node values.
#Constraints:
#Time limit: 2000 ms
#Memory limit: 256 MB

# Create Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

n1 = Node(10)
head = n1

n2 = Node(20)
n1.next = n2

n3 = Node(30)
n2.next = n3

#Traverse and print the node values

temp = head

while temp is not None:
    print("The node value after traversing the list is:", temp.data)
    temp = temp.next

#Insert node at a specific position

new_node = Node(11)

temp = head

for i in range(1 - 1):
    temp = temp.next

new_node.next = temp.next
temp.next = new_node

#Find Middle node and print its value

slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

print("The middle node value is:", slow.data)

#Delete node

temp = head

while temp.next is not None:
    if temp.next.data == 20:
        temp.next = temp.next.next
        break
    temp = temp.next

#Reverse list

previous = None
current = head

while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

head = previous

#Calculate the sum of every two consecutive node values.

temp = head

while temp is not None and temp.next is not None:
    print("The sum of two consecutive node values is:", temp.data + temp.next.data)
    temp = temp.next.next

