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
