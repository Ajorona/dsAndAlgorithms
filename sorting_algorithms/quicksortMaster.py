import random

with open("array.txt", 'rw+') as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [int(x) for x in content]

def DCQS(Array):
    l = 0
    r = len(Array) - 1
    random.seed(None)
    return QuickSort(Array, l, r)

# partition returns l and r for each unsorted subArray
def partition(A, l, r, p):
    A[l], A[p] = A[p], A[l]
    i = l + 1
    j = l + 1
    while j <= (r):
        if (A[j] < A[l]):
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1

    if (i == l + 1):
        newParams = l, l, i, r
    elif (i == r + 1):
        A[i - 1], A[l] = A[l], A[i - 1]
        newParams = l, i - 2, r, r
    else:
        A[i - 1], A[l] = A[l], A[i - 1]
        newParams = l, i - 2, i, r
    return newParams


def QuickSort(A, left, right):
    if left == right:
        return None
    p = random.randint(left, right)
    L1, R1, L2, R2 = partition(A, left, right, p)
    QuickSort(A, L1, R1)
    QuickSort(A, L2, R2)

# unsorted, sort, sorted

DCQS(content)

print "Sorted array is: %s" % content
