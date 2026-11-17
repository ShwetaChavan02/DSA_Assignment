# Assignment 2 (Q2) : DSA
# Q. 2 Write a program to perform the following operations on a Linear Queue
# Enqueue an element into the queue
# Dequeue an element from the queue
# Display
# Reverse the queue using stack
# Merge two queues into one.
# Check if two queues are identical

queue = []

# 1. ENQUEUE
def enqueue():
    value = int(input("Enter element: "))
    queue.append(value)
    print("Element inserted successfully")


# 2. DEQUEUE
def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))


# 3. DISPLAY
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:")
        for i in queue:
            print(i)


# 4. REVERSE QUEUE USING STACK
def reverse_queue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        stack = []

        while len(queue) > 0:
            stack.append(queue.pop(0))

        while len(stack) > 0:
            queue.append(stack.pop())

        print("Queue reversed successfully")


# 5. MERGE TWO QUEUES
def merge_queue():
    q2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        value = int(input("Enter element: "))
        q2.append(value)

    merged = queue + q2

    print("Merged queue:", merged)


# 6. CHECK TWO QUEUES ARE IDENTICAL
def identical_queue():
    q2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        value = int(input("Enter element: "))
        q2.append(value)

    if queue == q2:
        print("Both queues are identical")
    else:
        print("Queues are not identical")


# MAIN PROGRAM
while True:

    print("\n--- LINEAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        reverse_queue()

    elif choice == 5:
        merge_queue()

    elif choice == 6:
        identical_queue()

    elif choice == 7:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
