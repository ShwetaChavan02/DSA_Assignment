# Assignment 3 :
# Q. 1 Hospital Emergency Management 
# Develop a Python program to manage patients in a hospital using a Priority Queue 
# Requirements:
# 1. Accept patient ID, patient name and priority 
# 2. Priority 1 represents Critical, 2 represents Serious and 3 
# represents Normal 
# 3. Patients with higher priority must be treated first 
# Write the following functions 
# 1. Add Patient (enqueue) 
# 2. Display the next patient to be treated. (display_next) 
# 3. Remove a patient from the queue after treatment. (dequeue) 
# 4. Display all waiting patients in priority order(display_all)

patients = []

# 1. Add Patient (Enqueue)
def enqueue():
    pid = int(input("Enter Patient ID: "))
    name = input("Enter Patient Name: ")
    priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

    if priority < 1 or priority > 3:
        print("Invalid Priority!")
        return

    patient = [pid, name, priority]
    patients.append(patient)

    patients.sort(key=lambda x: x[2])

    print("Patient added successfully!")


# 2. Display Next Patient
def display_next():
    if len(patients) == 0:
        print("Queue is empty!")
    else:
        print("Next Patient to be treated:")
        print("ID:", patients[0][0])
        print("Name:", patients[0][1])
        print("Priority:", patients[0][2])


# 3. Remove Patient (Dequeue)
def dequeue():
    if len(patients) == 0:
        print("Queue is empty!")
    else:
        patient = patients.pop(0)
        print("Treated Patient:", patient[1])


# 4. Display All Patients
def display_all():
    if len(patients) == 0:
        print("Queue is empty!")
    else:
        print("\nWaiting Patients:")
        for patient in patients:
            print("ID:", patient[0],
                  "Name:", patient[1],
                  "Priority:", patient[2])


# Main Program
while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        display_next()
    elif choice == 3:
        dequeue()
    elif choice == 4:
        display_all()
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
