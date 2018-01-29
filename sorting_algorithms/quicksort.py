import random

# This is my implementation of the QuickSort Algorithm using a
# pseudorandom pivot for an expected runtime O(n) = n*log(n)
# notes on variables:
# A is a sublist length n of some list
# l is the leftmost sublist index inclusive
# r is the rightmost sublist index inclusive
# edgecase 1: every element less than pivot.
# maximum swaps occur and base case is
# hit. No > than array. Return None in recursion
# edgecase 2: every element greater than pivot.
# no swaps occur and there is no < than array.


# Divide and Conquer, QuickSort
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
    elif (A[i] < A[l]):
        A[i], A[l] = A[l], A[i]
        newParams = l, i - 1, i + 1, r
    elif (A[i] > A[l]):
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
print "Unsorted array is: %s \n" % testArray

DCQS(testArray)

print "Sorted array is: %s" % testArray
