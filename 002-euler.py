#!/usr/bin/env python
# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

fib = 1     # set up necessary variables
fib2 = 2
temp = 0
total = 0

while temp <= 4000000:      # set up loop to keep number below 4000000
    temp = fib2
    if temp % 2 == 0:       # check that number is even
        total += temp       # add temp to total
    temp = fib + fib2       # Setup fibbonacci sequence
    fib = fib2
    fib2 = temp
print(total)        # print out the total even fibbonacci numbers
