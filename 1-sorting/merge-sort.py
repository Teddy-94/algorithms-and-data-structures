# Merge sort is a recursive sorting algorithm, that divides
# the array into two halves until it tries
# to call mergeSort on a subarray of size 1


# it has time complexity of O(n log n) and space of O(n)

# the params p, q, and r are indices into array such
# that p < q < r.

def mergeSort(array):
    # if we are trying to sort an array of len < 1
    # we are done and the array should be sorted
    if len(array) > 1:

        # python makes splitting the array
        # into the two subarrays trivial
        r = len(array) // 2
        L = array[:r]
        R = array[r:]

        # sort the halves
        mergeSort(L)
        mergeSort(R)

        # initialize steppers for each array
        i = j = k = 0
        while (i < len(L) and j < len(R)):
            # if the left element is smaller or equal
            # insert it into the main array
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            # else pick the right element
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # when we have run out of elements in either L or R
        # put the rest of the elements into array
        while (i < len(L)):
            array[k] = L[i]
            i += 1
            k += 1
        while (j < len(R)):
            array[k] = R[j]
            j += 1
            k += 1


A = [1, 99, 2, -3, 234, 3, 4]
print(A)
mergeSort(A)
print(A)
