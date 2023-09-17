# Sorting

Sorting is one of the core problems in algorithms, and many other algorightms use sorting as a key subroutine.

The sorting algorithms we are looking at here are going to be:

- Algorithm,     worst case,    average
- Insertion Sort, O(n^2),       O(n^2)
- Bubble Sort,  O(n^2),         O(n^2)
- Merge sort,   O(n lg n),      O(n lg n) 
- Heapsort,     O(n lg n),      O(n lg n)
- Quicksort,    O(n^2),         O(n lg n)


- Counting sort, O(k + n),      O(k + n)
- Radix sort,   O(d(n + k)),    O(d(n + k))
- Bucket sort,  O(n^2),         O(n)


## Insertion sort

Insertion sort works much like how a person sorts a hand of cards. It takes a list as input and sorts it in place. Its fast and simple for sorting a small number of elements.


## Bubble sort

similar to insertion sort its a simple sorting algo, but it also has O(n^2) time complexity. Like bubbles in water, the elements bubble up to the top when sorted.


## Merge sort

Merge sort is a recursive algorithm that works by continuously dividing the input array untill it cannot be split anymore, then it merges the subarrrays so that they are sorted. n log n time complexity is much faster for large sets thatn n squared, but having a larger constant, insertion sort can be faster for small n. Also, unlike insertion sort, merge sort does not sort in place.


## Heapsort

Heapsort utilizes a heap datastrucutre in order to sort n elements in place in O(n log n) time complexity. Heapsort called on a max-heap will sort in increasing order, and vice versa.


## Quicksort

Quicksort also sorts n elements in place but worst case time complexity is O(n^2), but the "expected" running time is O(n log n). In practice quicksort generally outperforms heapsort, and is a popular algorithm for sorting large arrays. It is also a recursive algorithm.

The quicksort algorithm uses a partitioning routine, which is the key to the effectivenes of quicksort. It selects an element in the array and uses that element to roughly sort each partition. The time complexity depends on how well the partition routine happens to divide the array. In the worst case the pivot element is the largest or smallest element, in each subdivision. In the best case the pivot element is in the middle of the array. The average case is much closer to the best case than the worst case.

In order to make the worst case less likely, a randomized approach can be used. The only change we have to make is to select the pivot element at random.
