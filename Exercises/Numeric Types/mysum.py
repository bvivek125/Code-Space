#!/usr/bin/env python
from __future__ import print_function, unicode_literals 

### Exercise 2 ###

'''The challenge here is to write a mysum function that does the same thing as the built-in sum function. However, instead of taking a single sequence as a parameter, it should take a variable number of arguments'''

# Hints

'''
1. Use splat operator (*args) to invoke a function with variable number of arguements
2. Numbers will be a tuple [Assumption: arguements are of same type]
3. Set output variable to 0 at the start of function & add invidual numbers to it in a for loop
4. If you have an iterable object and want to pass its elements to a function, just preface it with * in the function call
5. Functions can accept a variable number of positional arguments by using *args in the def statement.
6. You can use the items from a sequence as the positional arguments for a function with the * operator.'''

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(*[10,20,30,40]))