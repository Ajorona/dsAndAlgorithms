unsorted = [5, 3, 8, 9, 1, 7, 0, 2, 6, 4]

def splitList(li):
    splitIndex = len(li)/2
    return li[splitIndex:], li[:splitIndex]

def mergeSort(li):
        if len(li) == 1:
            print li
            return li
        else:
            a, b = splitList(li)
            a = mergeSort(a)
            b = mergeSort(b)
            print a, b
        return merge(a, b)

def merge(a, b):
    c = []
    while ((len(a) != 0) and len(b) != 0) :
        if  a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])

    while (len(a) != 0) :
        c.append(a[0])
        a.remove(a[0])
    while (len(b) != 0):
        c.append(b[0])
        b.remove(b[0])
    return c


print mergeSort(unsorted)