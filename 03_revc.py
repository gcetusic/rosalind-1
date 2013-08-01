#!/usr/bin/python

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

input = open('rosalind_revc.txt', 'r')
s = input.read()
input.close()

from string import maketrans

in_table = 'TGAC'
out_table = 'ACTG'
trans_table = maketrans(in_table, out_table)

sc = s[::-1].strip().translate(trans_table)

output = open('03_revc.txt', 'w')
output.write(sc)
output.close()
