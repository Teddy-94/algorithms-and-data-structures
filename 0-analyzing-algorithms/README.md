When analyzing algorithms the most common use is big O notation. The two main aspects we are interested in are Size and Running time. These are most ofen examined and presented as how they both relate to the size of the input. 

## Input Size

The presentation of the input size depends on the input the algorithm takes.

- Arrays or similar: In most problems, the most natural measure of input size is the number of items in the input. For example, the number of items in an array.
- Graphs: If the input is a graph, the input size is well described by the number of vertices and the number of edges.
- Numerical operations: For many other problems, the best input size description is the total number of bits required to represent the input in ordinary binary notation.

## Running Time

The running time of an algorithm is the number of "primitive steps" executed. 

It is common to focus on only finding the worst case running time of an algorithm, for any input, since this provides an upper bound. 

Finally, when analyzing the running time, it is often the order of growth as the input size increases that is studied.
This leads to it being most common to only provide the leading term of a formula, and to discard the leading terms constant coefficient.

Running time is presented using O(n) notation, usually presented as "The time complexity is O of n...". In the Algorithms book, and presumably in formal settings O is actually the greek letter theta, and O(n) is pronounced "theta of n"


### Some common running times

See the wikipedia page for [Analysis of algorithms](https://en.wikipedia.org/wiki/Analysis_of_algorithms) for more information.

In gross simplification, in the middle is linear time complexity O(n), each additional item in a list will increase the time by 1 unit.

Then we have two extremes, very bad, and very good.
The very bad complexities are from least worst to worst worst: O(n log n), O(n^2), O(2^n), and the worst, O(n!)

the best are: O(root(n)), O(log n), and O(1).
