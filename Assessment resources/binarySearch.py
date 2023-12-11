# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [2, 4, 5, 8, 11, 15, 28, 33, 39, 42, 57, 64, 68, 72, 74, 75, 79, 81, 85, 88, 95, 100, 150, 245, 265, 278, 335]
x = 85
# x = 44
result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

   
   
   
   
   
   
   
    import time

"""start = time.time()

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
"""