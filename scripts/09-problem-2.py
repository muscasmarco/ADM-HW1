''' Problem 2 '''

# Birthday Cake Candles

def birthdayCakeCandles(ar):

    count = 0
    max_height = max(ar)
    for i in range(len(ar)):
        if ar[i] == max_height:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# kangaroo

def kangaroo(x1, v1, x2, v2):
    x1, v1, x2, v2 = float(x1), float(v1), float(x2), float(v2)

    if v2 == v1 and x1 != x2:
        return 'NO'
    if v2 == v1 and x1 == x2:
        return 'YES'
        
    int_part = (x1 - x2)//(v2 - v1)

    if (x1 - x2)/(v2 - v1) < 0.0:
        return 'NO'

    if ((x1 - x2)/(v2 - v1) - float(int_part)) == 0.0:
        return 'YES'

    return 'NO'

# recursive digit sum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):

    if k != 0:
        s = sum(map(int, list(n)))
        s *= k
        k = 0
        return superDigit(str(s), 0)

    s = sum(map(int, list(n)))
    if len(str(s)) > 1:
        return superDigit(str(s), 0)
    else:
        return sum(map(int, list(n)))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

