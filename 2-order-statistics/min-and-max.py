
def minAndMax(array):
    min = array[0]
    max = array[0]
    for i in range(len(array)-1):
        if min > array[i]:
            min = array[i]
        if max < array[i]:
            max = array[i]
    return (min, max)


print(minAndMax([1, 4, 6, 73, 8, 51]))
