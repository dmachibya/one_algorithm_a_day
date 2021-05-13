"""
Insertion Sort Algorithm
When to use this Algorithm
- when the array is small
- Input elements are somehow sorted.
"""
def insertionSort(alist):
    for i in range(0, len(alist)-1):
        if alist[i]>alist[i+1]:
            temp = alist[i]
            temp2 = alist[i+1]
            alist[i+1] = temp
            alist[i] = temp2

            for i in range(i, 0, -1):
                if(alist[i]<alist[i-1]):
                    temp = alist[i]
                    temp2 = alist[i-1]
                    alist[i-1] = temp
                    alist[i] = temp2

    return alist

print(insertionSort([4,2,5,1,0]))