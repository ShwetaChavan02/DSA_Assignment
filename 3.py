#count even and odd numbers
# write a program to accept n integers into an array and count and display 
# the numbers of even and odd elements present in the array

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

even = 0
odd = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)