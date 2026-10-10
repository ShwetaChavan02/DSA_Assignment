# find the smallest and the largest element
# write a program to accept N integeres into and array and find and display 
# the largest, second largest element, smallest element, second smallest element present in array
# without sorting the array

arr = [10, 3, 45, 6, 8, 23, 42, 56, 30]

max = min = arr[0]
smax = smin = arr[0]

for num in arr:
    if num > max:
        smax = max
        max = num
    elif num > smax and num != max:
        smax = num

    if num < min:
        smin = min
        min = num
    elif num < smin and num != min:
        smin = num

print("Maximum : ", max)
print("Second Maximum : ", smax)
print("Minimum : ", min)
print("Second Minimum : ", smin)