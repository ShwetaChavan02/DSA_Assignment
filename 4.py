# search an element
# write a program to accept n integers into an array and search for a given number 
# display an aprropriate message indicating whether the number is present in the array
# or not and also display its position

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

num = int(input("Enter number to search: "))

found = 0

for i in range(n):
    if arr[i] == num:
        print("Number is present at position", i + 1)
        found = 1

if found == 0:
    print("Number is not present in the array")