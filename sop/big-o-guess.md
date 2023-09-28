# guess big o base on the n

https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4725/

## n < 10:

backtracking or any brute-force

## 10 < n <= 20:

most algorithms that are correct will probably be fast enough.
Consider backtracking and recursion.

## 20 < n <= 100:

If you come up with a brute force solution
try to improve on those steps using tools like hash maps or heaps.

## 100 < n <= 1000:

`O(n^2)` is usually the expected/optimal time complexity in this range
and it might not be possible to improve.

## 1000 < n < 100_000:

`n<=10^5` is the most common constraint you will see on LeetCode
In this range, the slowest acceptable common time complexity is `O(nlogn)`
although a linear time approach `O(n)` is commonly the goal.

In this range, ask yourself if sorting the input or using a heap can be helpful.
If not, then aim for an `O(n)`

-   Hash map
-   A two pointers implementation like sliding window
-   Monotonic stack
-   Binary search
-   Heap
-   A combination of any of the above

## 100_000 < n < 1_000_000:

It will likely require a time complexity of `O(n)`
`O(nlogn)` is usually safe as long as it has a small constant factor.
You will very likely need to incorporate a hash map in some way.

## n > 1_000_000:

`O(logn)` or `O(1)`

![](find-solution-flowchart.png)

-   input is array or string
    -   if sorted
        -   binary search
        -   two pointers
    -   if not sorted
        -   all of something
            -   backtrack
        -   number of ways to do something, max/min possible of something, is something possible
            -   decisions depends on previous decisions
                -   dynamic programming
            -   decisions does not depends on previous decisions
                -   greedy
                    -   possible and impossible are two infinite zones
                        -   binary search
                -   not necessarily greedy
                    -   sub-array or substrings
                        -   sliding window or counting hash map
                    -   continuously finding max/min element
                        -   max/min continuously remove
                    -   sliding window fashion
                        -   monotonic queue
        -   prefix matching
            -   trie
        -   string building, distance between elements
            -   monotonic stack
        -   finding specific element
            -   hash maps

# find solution flowchart

-   Pattern 1: If the given input is a sorted (array, list, or matrix), then we will be
    using a variation of Binary Search or a Two Pointers strategy
-   Pattern 2: If we are dealing with top/maximum/minimum/closest 'k'
    elements among 'n' elements, we will be using a Heap
-   Pattern 3: If we need to try all combination (or permutations) of
    the input, we can either use recursive Backtracking or iterative
    Breadth-First Search.
-   Pattern 4: Most of the questions related toTrees or Graphs can be
    solved either through Breadth-First Search or Depth-First Search.
-   Pattern 5: Every recursive solution can be converted to an iterative solution using a stack.
-   Pattern 6: If for a problem, there exists a brute-force solution in O(n2) time and 0(1) space,
    there must exist two other solutions:
    -   (1) Using a Map or a set for O(n) time and O(n) space,
    -   (2) Using sorting for O(n log n) time and 0(1) space.
-   Pattern 7: If the problem is asking for optimization (e.g., maximization or minimization), we
    will need to use Dynamic Programming to solve it.
-   Pattern 8: If we need to find some common substring among a set of strings, we
    will be using a HashMap or a Trie.
-   Pattern 9: If we need to search among a bunch of strings, Trie will be
    the best data structure.
-   Pattern 10: If the problem involves a LinkedList and we
    can't use extra space, then use Fast & Slow Pointer approach.
