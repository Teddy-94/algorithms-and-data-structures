# see quicksort for explanation of partitioning
def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i + 1


# returns the i:th smallest or largest item from an array
def select(array, p, r, i):
    # if the array only has one element
    if p == r:
        return array[p]
    # otherwise partition, which returns the index
    # of the pivot element
    q = partition(array, p, r)
    # k = the number of elements in subarray array[p..q]
    k = q - p + 1
    # the selected number i is the pivot
    if i == k:
        return array[q]
    # if it is not the pivot element, then check if it is in
    # the left or right subarray, and recursively call select on that
    elif i < k:
        return select(array, p, q-1, i)
    else:
        return select(array, p, q+1, i-k)


a = [12, 5432, 654, 65, 72, 3, 65, 7]
x = 0
print(select(a, 0, len(a)-1, x))
