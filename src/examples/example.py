# MERGESORT
​
[2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
​
# (base case) If the array is empty or length 1, return
​
# Split the arrays into half
arr1 = [2, 0, 1, 3, 6]
arr2 = [9, 8, 5, 7, 4]
​
# Sort each half
arr1 = [0, 1, 2, 3, 6]
arr2 = [4, 5, 7, 8, 9]
​
# Merge them back together
# Compare the first values of each array, add smaller of the 2 to result
merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def fib(n):
    # base case
    if n <= 2:
        return 1
    # Recursive call, should move toward base case
    return fib(n-1) + fib(n-2)


def foo(n):
    if n <= 1:
        return 1
