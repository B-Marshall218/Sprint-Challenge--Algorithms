# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
Polynomial O(n^3) because the the runtime will grow at a higher rate than the input. when a = 2 then n = 3 until they equal each other then maybe it would become Linear O(n)?   

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
This is Polynomial O(n^2) because there is a for loop and you are adding the outside loops O(n) as well as the inner while loop's O(n) so that would give you O(n^2)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Logrithmic O(log n) since your output would descrease by 1 everytime the run time should be a little slower than the input each time. 
## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

binary search tree 

chose a starting point in the middle floor. If the floor ends up being your target then return floor number. If the egg breaks go down one floor, if it doesnt break go up one floor. The target is the highest floor without the egg breaking. This recursive approach would be Logarithmic O(log n) because the output is getting smaller and smaller with each iteration. 