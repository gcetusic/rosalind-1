#!/usr/bin/python

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

with open('rosalind_rna.txt') as f:
    t = f.read()

rna = t.replace('T', 'U')

with open('02_rna.txt', 'w') as f:
    f.write(rna)
