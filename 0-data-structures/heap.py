
# each call to maxheapify gives it an array, a heapsize and an index
# maxHeapify makes sure that the given root node, its left and right
# node are in the correct order. The node at i should be larger than
# both the left and right node.
def maxHeapify(array: list, heapSize: int, i: int):
    # given the index for a node, we can find the left and right node
    left = 2*i + 1
    right = 2*i + 2

    # to make this a min-heap, simply flip this condition
    # array[left] > array[i] and array[right] > array[largest]
    # to become array[left] < array[i] and array[right] < array[largest]

    # if the left node is larger than the given node
    # it is the biggest node so far.
    if left < heapSize and array[left] > array[i]:
        largest = left
    else:
        largest = i
    # if the right node is larger than the largest node so far
    if right < heapSize and array[right] > array[largest]:
        largest = right
    # if the largest node is not the given node
    if largest != i:
        # put the largest node at index i
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        # and recursively call maxHeapify on the node that
        # was replaced
        maxHeapify(array, heapSize, largest)


def buildMaxHeap(array):
    heapsize = len(array)

    # In a heap, all leaf nodes are in the second half of the heap
    # so dividing the len by 2 and subtracting 1 gives us the final
    # non-leaf node. This loop goes from the last non leaf node to
    # the root node.
    for i in range((len(array)//2)-1, -1, -1):
        # call maxHeapify
        maxHeapify(array, heapsize, i)


def insert(array, element):
    if (len(array) == 0):
        array.append(element)
    else:
        array.append(element)
        for i in range((len(array)//2)-1, -1, -1):
            maxHeapify(array, len(array), i)


def delete(array, element):
    i = 0
    for i in range(0, len(array)):
        # find the element to delete
        if element == array[i]:
            break

    # swap it with the last element in the tree
    temp = array[i]
    array[i] = array[len(array)-1]
    array[len(array)-1] = temp

    # remove it
    array.remove(element)
    # max-heapify it
    for i in range((len(array)//2)-1, -1, -1):
        maxHeapify(array, len(array), i)


def printHeap(array, i, n, level=0):
    if i < n:
        print("   " * level + str(array[i]))
        printHeap(array, 2 * i + 1, n, level + 1)
        printHeap(array, 2 * i + 2, n, level + 1)


A = [1, 32, 53, 654, 12, 6, 3]
print(A)
buildMaxHeap(A)
print(A)
printHeap(A, 0, len(A))
insert(A, 432)
insert(A, -43)
insert(A, 99)
insert(A, 1)
printHeap(A, 0, len(A))
delete(A, 99)
print("######################")
printHeap(A, 0, len(A))
delete(A, 432)
print("######################")
printHeap(A, 0, len(A))
