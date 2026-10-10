# reverse the array
# write a program to accept n integeres into an array and display the elements
# in reverse order without changing the original array

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

print("Original array:", arr)

print("Reverse array:")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")