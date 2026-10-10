# calculate array sum
# write a program to acept N integers into an array 
# and calculate and display the sum of all the elements
# accept enumber of elements in an array and do its sum

n = int(input("Enter number of elements in an array: "))
arr = [0] * n
for i in range(n):
    arr[i] = int(input("Enter element in arry: "))
sum = 0
for i in range(n):
    sum = sum + arr[i]
print("Sum =", sum)