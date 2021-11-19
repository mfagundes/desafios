"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].

Result: https://app.codility.com/demo/results/trainingYP7QGD-W94/
Score: 63%
Correctness: 100%
Performance: 20%
Time complexity: O(N**2)
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    # leaves_path = [1,2,3,4,5]
    # leaves_path = [leaf for leaf in range(1, X + 1)]
    # leaves_fallen = set()
    path_sum = sum(range(1, X+1))
    fallen_sum = 0
    time_elapsed = 0
    for leaf in A:
        time_elapsed += 1
        leaves_fallen.add(leaf)
        if list(leaves_fallen) == leaves_path:
            return sec
    return -1


def solution_old(X, A):
    # write your code in Python 3.6
    # leaves_path = [1,2,3,4,5]
    leaves_path = [leaf for leaf in range(1, X + 1)]
    leaves_fallen = set()
    for sec, leaf in enumerate(A):
        leaves_fallen.add(leaf)
        if list(leaves_fallen) == leaves_path:
            return sec
    return -1
