#!/usr/bin/env python 
from __future__ import print_function, unicode_literals
 
### Exercise 2a ###

'''The built-in version of sum takes an optional second argument, which is used as the starting point for the summing. (That’s why it takes a list of numbers as its first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns 10, because 1+2+3 is 6, which would be added to the starting value of 4. Reimplement your mysum function such that it works in this way. If a second argument is not provided, then it should default to 0. Note that while you can write a function in Python 3 that defines a parameter after *args, I’d suggest avoiding it and just taking two arguments--a list and an optional starting point.'''

''' Issues:
1. The first issue is that the variable arguments are always turned into a tuple before they are passed to your function. This means that if the caller of your function uses the * operator on a generator, it will be iterated until it’s exhausted. The resulting tuple will include every value from the generator, which could consume a lot of memory and cause your program to crash.
2. The second issue with *args is that you can’t add new positional arguments to your function in the future without migrating every caller. If you try to add a positional argument in the front of the argument list, existing callers will subtly break if they aren’t updated.'''



def mysum(start,/,*numbers):
    output=0
    if start:
        output=start
        print(f'Starting point is: {start}')
    else:
        start=0
        print(f'Starting point is: {start}')
    for number in numbers:
        output += number
    return output
print(mysum(4,*[10,20,30,40]))