#!/usr/bin/python

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of
# times that the symbols 'A', 'C', 'G', and 'T' occur in s.

with open('rosalind_dna.txt') as f:
    s = f.read()

answer = '%s %s %s %s' % (s.count('A'), s.count('C'), s.count('G'), s.count('T'))

with open('01_dna.txt', 'w') as f:
    f.write(answer)
