
often taken for granted, finding the min and max values, as well as statistics like average and median are algorithmic operations.


## min and max

finding the min and max values are done by keeping track of the smallest/largest value seen so far, and looping over the array, checking each element against the smallest/largest. this will always require O(n-1) comparisons. if we need to find both the min and max, this can be done with at most 3 [ n / 2 ] comparisons, by keeping track of both the min and the max value and comparing against both as we traverse the array.


## randomized select 

if we want to pick the n:th smallest/largest item from an array, we can use a select algorithm which improves the time complexity over using a sorting algorithm and then picking the n:th element from the resulting array. If the elements in the array are distinct, select runs with time complexity of O(n), which is a big improvement over the selection algorithms
