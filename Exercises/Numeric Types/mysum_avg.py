### Exercise 2a ###

'''Write a function that takes a list of numbers. It should return the average (i.e., arithmetic mean) of those numbers.'''

#!/usr/bin/env python 

def mysum(*numbers):
    output=0
    for number in numbers:
        output += number
    return output/len(numbers)
print(mysum(*[10,20,30,40]))