"""
Linear search algorithm

When to use this Algorithm
- When searching a short array which may be unsorted.
"""

#algorithm function
def linear_search(array, target):
    for i in range(0, len(array)):
        if(array[i] == target):
            return i
    return None


#testing function
def verify(algorithm):
    if(algorithm) == None:
        print("Element not found")
    else:
        print("Element found at index: "+str(algorithm))

verify(linear_search([1,2,45,67,5,9], 2))