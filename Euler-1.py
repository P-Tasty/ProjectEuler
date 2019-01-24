import math

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

#With first 4 numbers given we'll start with 9
x = 9

#Create an array of existing numbers
mults=[3, 5, 6, 9]

#Check for every multiple of 3 & 5
while (x < 999):
    x = x + 1
    if (x % 5 == 0) or (x % 3 == 0):
        mults.append(x);
        print x
z = 0

#Find the sum of multiples
for y in mults:
    z = z + y

#Print sum of multiples
print z
