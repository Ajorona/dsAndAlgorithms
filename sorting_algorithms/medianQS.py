with open("array.txt", 'rw+') as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [int(x) for x in content]


def DCQS(Array):
    l = 0
    r = len(Array)
    return QuickSort(Array, l, r)


def partition(A, l, r):
    left = l
    right = r - 1
    mid = l + (r-l+1)/2 - 1 

    if((A[left] < A[mid] < A[right]) or (A[right] < A[mid] < A[left])):
        A[left], A[mid] = A[mid], A[left]

    elif((A[mid] < A[left] < A[right]) or (A[right] < A[left] < A[mid])):
        pass

    elif((A[left] < A[right] < A[mid]) or (A[mid] < A[right] < A[left])):
        A[l], A[right] = A[right], A[l]

    i = l + 1
    j = l + 1

    while j < r:
        if (A[j] < A[l]):
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1
    A[i - 1], A[l] = A[l], A[i - 1]
    newParams = l, i - 1, i, r
    return newParams


def QuickSort(A, left, right):
    count = 0
    if left < right:
        count = right - left - 1
        L1, R1, L2, R2 = partition(A, left, right)
        lc = QuickSort(A, L1, R1)
        rc = QuickSort(A, L2, R2)
        return count + lc + rc
    else:
        return 0


total = DCQS(content)

print total
