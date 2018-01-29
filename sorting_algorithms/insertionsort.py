
unsorted = [10,9,8,7,6,5,4,3,2]

def insertionSort(li):
    i = 0
    for num in xrange(len(li)):
        j = i
        while (j > 0 and (li[j] < li[j - 1])):
            temp = li[j-1]
            li[j-1] = li[j]
            li[j] = temp
            j += -1
        i += 1
        
    return unsorted 

sorted = insertionSort(unsorted)

print sorted
