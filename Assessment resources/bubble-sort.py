def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", my_list)

bubble_sort(my_list)

print("Sorted List:", my_list)

# Import time module
import time

# record start time
start = time.time()

# define a sample code segment
a = 0
for i in range(1000):
	a += (i**100)

# record end time
end = time.time()

# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
	(end-start) * 10**3, "ms")
