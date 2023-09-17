
# the key to the quicksort algorithm is the partitioning
# which rearranges the subarray array[p..r] in place.
# p and r represent the index of the first and last element
# of the current partition
def partition(array, p, r):
    # set an element as the pivot element around which to
    # partition the array
    x = array[r]
    i = p - 1
    # loop over the partition, from the leftmost element
    # to the rightmost, excluding the pivot element
    for j in range(p, r):
        # if the element is smaller than the pivot element
        # flip this condition to make it sort decending
        if array[j] <= x:
            # increment the left boundary
            i += 1
            # and move the element to the left of the boundary
            # this moves smaller elements to the left side of the partition
            array[i], array[j] = array[j], array[i]
    # this places the pivot element at its correct positon within the partition
    array[i+1], array[r] = array[r], array[i+1]
    # return the position of the pivot. elements to the left are smaller
    # and elements to the right are larger than the pivot.
    return i + 1


# quicksort has worst case time complexity of O(n^2) but the average
# time complexity is O(n log n)
def quicksort(array, p, r):
    if p < r:  # make sure that p is to the left of r
        # call partition, which will return the position of the pivot element
        q = partition(array, p, r)
        # call quicksort recursively on both the left and right partition
        quicksort(array, p, q-1)
        quicksort(array, q + 1, r)


a = [1, 4, 6, 99, 7, 2, 7465, 23, 63, -3]
print(a)
quicksort(a, 0, len(a)-1)
print(a)
