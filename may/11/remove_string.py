"""
Remove string from an array with numbers and strings
"""

def remove_string(array):
    new_array = []
    for i in range(0, len(array)-1):
        try:
            array[i]/2
            new_array.append(array[i])
        except TypeError as e:
            pass
    return new_array



print(remove_string([1,2,"a", 5, "c"]))