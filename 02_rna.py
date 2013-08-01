#!/usr/bin/python

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

input = open('rosalind_rna.txt', 'r')
t = input.read()
input.close()

rna = t.replace('T', 'U')

output = open('02_rna.txt', 'w')
output.write(rna)
output.close()
