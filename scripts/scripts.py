
''' Introduction '''
#Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n >= 1 and n <= 100:    
        if n % 2 != 0:
            print("Weird")
        else:
            if (n >= 2 and n <= 5) or (n > 20):
                print("Not Weird")
            else:
                print("Weird")

# Arithmetic Operators 

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

# Loops

if __name__ == '__main__':
    n = int(input())

    if n >= 0 and n <= 20:
        for n in range(0, n):
            print(n**2)

# Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here

    if year >= 1900 and year <= 10**5:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                leap = False
            else:
                leap = True

    return leap

# Print function

if __name__ == '__main__':
    n = int(input())

def count_digits(num):
    
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num/10)
    

max_exp = 0
for i in range(1,n+1):
    num_digits = count_digits(i)
    max_exp += num_digits


