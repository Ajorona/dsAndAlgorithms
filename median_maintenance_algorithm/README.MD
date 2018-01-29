Median Maintenance Algorithm in Java with Dynamic Minimum and Maximum Heap

The median maintenance algorithm receives as input a stream of integers line-by-line from a text file.
It outputs the sum modulo 10,000 of the input stream median caputured at each input step n for a file
with n lines of single integer input. (i.e. For all integers 1 through 10,000 the median n/2 (if even)
or ceiling(n/2) (if odd) is captured in an array). This array is summed and to truncate the size of the
result, % 100000 is applied. This is a demonstration of how to build a minimum heap, how to build a 
maximum heap, and how to use a simple algorithm with dynamic data structures.

