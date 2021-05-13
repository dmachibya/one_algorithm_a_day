"""
Binary search Algorithm

When to use this algorithm
- When we have a sorted list
- when the list is large
"""

#looping approach - Most appropriate for python
def binary_search(array, target):
    first = 0
    global last

    last  = (len(array)-int(1))

    midpoint = -1

    while midpoint != 0 or midpoint != len(array):
        midpoint = last//2
        print("looping: "+str(last))
        if(array[midpoint] == target):
            return midpoint
        else:
            if(midpoint > target):
                first = midpoint
            else:
                last = midpoint
            print("first: "+str(first), "last: "+str(last))
    return None


def verify(algorithm):
    if(algorithm == None):
        print("Element not found")
    else:
        print("Element found at index: "+algorithm)


verify(binary_search([1,2,3,4,5,6,7,8], 3))