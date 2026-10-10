# remove dulicate elements
# write a program to accept n integers into an array and create a new array containing
# only the unique elements, removing all duplicate values

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

new_arr = []

for i in range(n):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])

print("Original array:", arr)
print("Array after removing duplicates:", new_arr)