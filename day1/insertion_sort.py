#insertion sort algorithm

def insertion_sort(items):
    output = []
    for i in items:
        n = i + 1

        if n == 5:
            n = 4
        for j in range(0,i):
            if items[n] > items[i]:
                temp = items[i]
                items[n] = temp
                items[i] = items[n]
    return items
