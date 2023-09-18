One important thing to consider is how the data is stored, because the data structure will affect the time and space required for the algorithm.

## Datastructures and their worst case time complexity

- Datastructure,    access, search, insert, delete
- Array,            O(1),   O(n),   O(n),   O(n)
- Stack,            O(n),   O(n),   O(1),   O(1)
- Queue,            O(n),   O(n),   O(1),   O(1)

- Singly liked list,  O(n),   O(n),   O(1),   O(1)
- Doubly linked list, O(n),   O(n),   O(1),   O(1)

- Hash table,         O(n),   O(n),   O(n),   O(n)

- Binary Tree,        O(n),   O(n),   O(n),   O(n)
- Binary Search Tree, O(n),   O(n),   O(n),   O(n)
- B tree,           O(lg n), O(lg n), O(lg n), O(lg n),

## Note on average time complexity

Arrays, Stacks, Queues, and linked lists all have the same average time complexity as their worst time complexity. 

Hash tabels have average operations time complexity of O(1)

Trees have average time complexities of O(log n)

All of these have space complexity O(n)


### Heap
the heap datastructure is an array object that can be viewed as an almost complete binary tree. each node in the tree corresponds to an element of the array. There are two kinds of heaps: max-heap and min-heap.

In a max-heap, the parent of a node is always larger or equal to the node. in a min-heap the parent of a node is smaller or equal to the node.

In order to maintain the max heap property, we use the max-heapify procedure. This takes O(lg n) time.

A max-heap can be created from an array by using max-heapify in a botton up manner. A heap can be built in O(n) time.

The children of a parent node at index i are stored at index 2i+1 and 2i+2 respectively. Thus the child nodes of the node at index 3 would be stored at index 7 and 8 respectively. The parent for node at index i can be found by dividing i with 2. These operations can be done by by bitshifting.

One very common usage of a heap is as a priority queue


## Stack 

In a stack, the element deleted is the element most recently inserted. Stacks operate on a LIFO basis. Insert and delete on a stack are often called push and pop.

A stack can be implemented using an array and keeping track of the last added element. Often denoted top. When top = 0, the stack is empty.


## Queue

In a queue, the element deleted is the element first inserted. Queues operate on a FIFO basis. Insert and delete in a queue are often called enqueue and dequeue.

A queue is also an array structure, where we keep track of its head and tail. The tail indexes the position where the next enqueued item will be placed. The head indexes the next item that will be dequeued. Since the tail points to an empty index, the last item in the queue has index tail-1. When head = tail, the queue is empty


## Linked Lists

A linked list is a data structure where each element is arranged in a linear order, but unlike an array, the order is not determined by the array indices. Instead the order is determined by pointers in each object.

A linked list can either be doubly linked, or singly  linked. Each element in a doubly linked list contains three attributes: the key, a pointer to the previous element, and a pointer to the next element. If element.prev is null, the element is the head of the list. If element.next is null, the element is the tail of the linked list. Is singly linked lists, the elements don't have  the prev pointer.

If the linked list is sorted, the linear order of the list corresponds to the linear order of the keys in the elements.

In a circular linked list, the prev pointer of the head points to the tail element of the list, and the next pointer of the tail element points to the head.

## Binary search tree

TODO

## Red-Black Tree

TODO
