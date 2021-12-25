# Find subsequence with greater sum
This question was proposed in the Welcome To The Django Forum

## Question

Create a program to find the continuous sub-sequence inside array A with the greatest sum:

Example 1:
- Input: [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
- Output: 13

In this first example, the subarray [5, 2, 1, 4, -7, 8] is the largest sum continuous sequence 
contained within the array and the sum of this array is 13

Example 2:
- Input: [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
- Output: 8

In this second example, the subarray [5, -1, 2, 1, 1] is the largest-sum continuous 
sequence contained within the array and the sum of these numbers is 8.

Your program only needs to display the VALUE of the largest sum, 
it is not necessary to display the array in question.

### My solution
I thought about the problem graphically. As it asks for a continuous sequence, 
we don't need to focus on all the possibilities, but on the “steps” that the sum takes. 
I used numpy's cumsum method, so I can see every “step” it takes.

There is a "implicit 0" in the beginning of the array, so the first number is like a movemnt
from the position 0 to that number.

**UPDATED: to remove the dependency to Numpy I decided to use a simple loop**

If in these steps the value is never negative, then the highest value will be the maximum of the cumsums array.

But, what about when in any steps it turns negative?

In this case I found the lowest value in the list of cumulative sum (as it is a negative number, it will be 
the highest absolute velue), and subtracted it from all the values (subtracting a negative number
is the same of adding its positive value).

Graphically speaking, I shifted all the steps to zero, so the lowest value turned to 0. 

Example: Array = [6, -8, 7, 2, -3]

```
    0
    |----->   step 1: +6   || total cumsum: +6
  <-|-----    step 2: -8   || total cumsum: -2
   -|---->    step 3: +7   || total cumsum: +5
    |.....->  step 4: +2   || total cumsum: +7
    |...<--   step 5: -3   || total cumsum: +4
```

Here, the result should be 9, from the subsequence [6, -8, 7, 2]. However, as the steps moved 
to a negative position, I shifted all steps in order to the last position is 0. 
As the furthest position was -2, all moves must be shifted by +2:

```
   0
   |------->   shifted position 1: +8
   |<------    shifted position 2: 0
   |------>    shifted position 3: +7
   |.......->  shifted position 4: +9
   |......<--  shifted position 5: +6
```

**Corner case: all numbers negatives**

After testing this solution, a question arised: and if all the numbers in the array are negatives?

The question states that we must find the highest sum of a sequence, but does not state the minimun
lenght of the sequence. So, I assumed that the lenght of the sequence could be 1 (eg. [-2]).

In the case of only negative values, any sum of sequential numbers will be lower than the prior one.
With that in mind, I assumed the right answer should be the highest value of the array, as it
alone would be the "highest sum" of a sequence of lenght 1