# Patti (Patricia) Elfers-Wygand
# CSCI 77800 Fall 2022
# helped by Alana Robinson
# consulted: w3schools.com, Replit.com, guides.codepath.com/compsci/Binary-Search#iterative-binary-search, programiz.com

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


array = [3, 14, 15, 6, 7, 18, 2, 0, 9]
x = 3
#x = 0
#x = 13

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
