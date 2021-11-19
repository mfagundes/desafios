"""
Task description
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].

Results: https://app.codility.com/demo/results/trainingASDK5J-9MN/
        https://app.codility.com/demo/results/trainingYVBC7P-SD9/

Time Complexity: O(N)
Reference: https://stackoverflow.com/questions/48030130/codility-tape-equilibrium-training-using-python
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import accumulate

def solution(A):
    # write your code in Python 3.6
    array_sum = sum(A)
    accum = list(accumulate(A[:-1]))
    res = float('inf')

    for left in accum:
        """
        right = array_sum - left =>
        left - right = left - (array_sum - left) =>
        left - right = 2 * left - array_sum
        res = min([abs(left - right), res])
        """
        res = min([abs(2*left - array_sum), res])

    return res