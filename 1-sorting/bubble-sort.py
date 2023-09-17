# Bubble sort runs at worst and average time of O(n^2) with space of O(1)

def bubbleSort(array):
    # for each element int the array
    for i in range(len(array)):

        # easy optimisation to let us stop checking early
        # without this check, every comparison is always made
        # even if the array is already sorted.
        swapped = False

        # for each element after element[i]
        for j in range(0, len(array) - i - 1):
            # compare the current element with the element ahead
            # to reverse flip > to <
            if array[j] > array[j + 1]:
                # swap the positions of elements j and j+1
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                # set swapped to true
                swapped = True

        # if we managed to check the entire array wihout making a swap
        # the array is sorted and we can break
        if not swapped:
            break


A = [5, 25, 4, 63, 1, 3, 235, -9]
print(A)
bubbleSort(A)
print(A)
