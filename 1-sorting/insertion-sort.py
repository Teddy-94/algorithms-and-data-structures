# Insertion sort runs at worst and average case time of O(n^2) with space O(1)

def insertionSort(array: list[int]):
    # We start at index 1
    for i in range(1, len(array)):
        # Take the element
        element = array[i]
        # Look back one index
        j = i - 1

        # while j is inbounds, and element at prev index is larger than element
        while (j >= 0) and (array[j] > element):  # To reverse flip the > to <
            # Move the element back one space
            array[j + 1] = array[j]
            # and look back one more index
            j = j - 1
        # if we are outside of the loop, place element here
        print(i, j+1)
        array[j + 1] = element
    return array


A = [5, 25, 4, 63, 1, 3, 235]
print(A)
insertionSort(A)
print(A)
