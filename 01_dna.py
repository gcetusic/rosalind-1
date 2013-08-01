#!/usr/bin/python

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of
# times that the symbols 'A', 'C', 'G', and 'T' occur in s.

input = open('rosalind_dna.txt', 'r')
s = input.read()
input.close()

answer = str(s.count('A')) + ' ' + str(s.count('C')) + ' ' + str(s.count('G')) \
       + ' ' + str(s.count('T'))

output = open('01_dna.txt', 'w')
output.write(answer)
output.close()
