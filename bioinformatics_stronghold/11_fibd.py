#!/usr/bin/python

# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th
# month if all rabbits live for m months.

with open('rosalind_fibd.txt') as f:
    args = f.read()

args = args.split(' ')
n = int(args[0])
m = int(args[1])
# Save values to not count the same again
saved_values = [0] * (n-1)

def fib(n):
    if n < 0:
        return 0
    elif n < 3:
        return 1
    else:
        if saved_values[n-1] != 0:
            return saved_values[n-1]
        else:
            saved_values[n-2] = fib(n-1)
            return fib(n-1) + fib(n-2) - fib(n-1-m)

rabbits = fib(n)

with open('11_fibd.txt', 'w') as f:
    f.write(str(rabbits))
