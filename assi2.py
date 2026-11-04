
stack = []

# 1. PUSH
def push():
    value = int(input("Enter element: "))
    stack.append(value)
    print("Element pushed successfully")


# 2. POP
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Deleted element:", stack.pop())


# 3. DISPLAY
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])


# 4. REVERSE STRING USING STACK
def reverse_string():
    string = input("Enter a string: ")
    temp = []

    for ch in string:
        temp.append(ch)

    rev = ""
    while len(temp) > 0:
        rev = rev + temp.pop()

    print("Reversed string:", rev)


# 5. REVERSE STACK USING ANOTHER STACK
def reverse_stack():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        temp = []

        while len(stack) > 0:
            temp.append(stack.pop())

        while len(temp) > 0:
            stack.append(temp.pop())

        print("Stack reversed successfully")


# MAIN PROGRAM
while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using Another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        reverse_string()

    elif choice == 5:
        reverse_stack()

    elif choice == 6:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
