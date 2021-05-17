# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

# Function Description

# Complete the function rotLeft in the editor below.

# rotLeft has the following parameter(s):

# int a[n]: the array to rotate
# int d: the number of rotations
# Returns

# int a'[n]: the rotated array
# Input Format

# The first line contains two space-separated integers  and , the size of  and the number of left rotations.
# The second line contains  space-separated integers, each an .

# Constraints

# Sample Input

# 5 4
# 1 2 3 4 5
# Sample Output

# 5 1 2 3 4
# Explanation





#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here

    n = len(a)
    for i in range(d):
        if  n in range(1, 10**5) and d in range(1, n+1) and filter(lambda x: x in range(1, 10**6), a):
            temp = a.pop(0)
            a.append(temp)
    return a    

if __name__ == '__main__':
    a = [1,2,3,4,5]
    d = 4

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
