#!/usr/bin/env python

# Euler https://projecteuler.net/problem=1
#
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Create a result array
result = []

# Iterate over range 0 .. 1000
for val in range(0, 1000):
    # if it's divisibale by 3 added it result
    if val % 3 == 0:
        result.append(val)
    elif val % 5 == 0:      # Else if it's divisibale by 5
        result.append(val)

# Sum the result array and print
print sum(result)
