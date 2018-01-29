 
unsorted = [10,9,8,7,6,5,4,3,2]

#lowest excludes loop invariant

def selectionSort(arr):
    unsorted.append('end')
    for i in xrange(len(arr) - 1):
        place = i
        lowest = i
        for j in xrange(len(arr)):
                if arr[j] is 'end':
                    temp = arr[place]
                    arr[place] = arr[lowest]
                    arr[lowest] = temp
                elif arr[j] <= arr[place]:
                        lowest = j
    return arr


print selectionSort(unsorted)