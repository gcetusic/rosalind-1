#!/usr/bin/python

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

with open('rosalind_revc.txt') as f:
    s = f.read()

from string import maketrans

in_table = 'TGAC'
out_table = 'ACTG'
trans_table = maketrans(in_table, out_table)

sc = s[::-1].strip().translate(trans_table)

with open('03_revc.txt', 'w') as f:
    f.write(sc)
