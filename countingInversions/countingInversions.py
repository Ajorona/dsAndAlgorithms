def getInput():
    with open("input.txt", 'r') as f:
        input = f.readlines()
    input = [x.strip() for x in input]
    input = [int(x) for x in input]
    return input


def listSplit(arr, length):
    mid = length / 2
    A = arr[0:mid]
    B = arr[mid:]
    return A, B


def mergeCount(L, R):
    c = []
    count = 0
    i = j = 0
    while (i < len(L) and j < len(R)):
        if L[i] < R[j]:
            c.append(L[i])
            i += 1
        else:
            c.append(R[j])
            count = count + (len(L) - i)
            j += 1
    c.extend(L[i:])
    c.extend(R[j:])
    return c, count


def sortCount(arr):
    length = len(arr)
    if length == 1:
        return arr, 0
    else:
        A, B = listSplit(arr, length)
        arrA, countX = sortCount(A)
        arrB, countY = sortCount(B)
        arrC, countZ = mergeCount(arrA, arrB)
        return arrC, countX + countY + countZ


def Main():
    input = getInput()
    Array, Count = sortCount(input)
    print "There are %d inversions in the list. \n" % Count


Main()
