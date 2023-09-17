
# see datastructures/heap for explanation
def maxHeapify(array: list, heapSize: int, i: int):
    left = 2*i + 1
    right = 2*i + 2

    if left < heapSize and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right < heapSize and array[right] > array[largest]:
        largest = right
    if largest != i:
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        maxHeapify(array, heapSize, largest)


# see datastructures/heap for explanation
def buildMaxHeap(array):
    heapsize = len(array)
    for i in range((len(array)//2)-1, -1, -1):
        maxHeapify(array, heapsize, i)


# heapsort will sort in incremental order when called on a max-heap
# and in decrementing order when called on a min-heap. It runs in
# O(n log n) time complexity
def heapsort(array):
    buildMaxHeap(array)
    heapsize = len(array)
    print(array)  # this is the tree in array form
    # looping backwards from the last element to the second element
    for i in range(len(array)-1, 1, -1):
        # move the root node (largest) to the end of the array
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        # remove the last element in the array from the tree
        heapsize -= 1
        # and maxheapify the tree again.
        maxHeapify(array, heapsize, 0)


a = [1, 32, 53, 654, 12, 6, 3, 1, 32, 53,
     654, 12, 6, 3, 1, 32, 53, 654, 12, 6, 3]
print(a)
heapsort(a)
print(a)
