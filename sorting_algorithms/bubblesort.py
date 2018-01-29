Array = [9,8,7,6,5,4,3,2,1]


def bubbleSort(a):
    count = 1
    a.append('end')
    while count > 0:
        count = 0
        for i in xrange(len(a)):
            if a[i+1] is 'end':
                break
            elif a[i+1] < a[i]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                count += 1
                
    return a


sortedArray = bubbleSort(Array)

print sortedArray