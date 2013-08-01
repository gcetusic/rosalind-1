#!/usr/bin/python

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months if
# we begin with 1 pair and in each generation, every pair of reproduction-age
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

input = open('rosalind_fib.txt', 'r')
args = input.read()
input.close()

args = args.split(' ')
n = int(args[0])
k = int(args[1])
# Save values to not count the same again
saved_values = [0] * (n-1)

def fib(n):
    if n < 3:
        return 1
    else:
        if saved_values[n-1] != 0:
            return saved_values[n-1]
        else:
            saved_values[n-2] = fib(n-1)
            return fib(n-1) + k * fib(n-2)

rabbits = fib(n)

output_file = open('04_fib.txt', 'w')
output_file.write(str(rabbits))
output_file.close()
