#!/usr/bin/python

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the
# GC-content of that string.

with open('rosalind_gc.txt') as f:
    dna_strings = f.read()

dna_strings = dna_strings.split('>')
highest_gc = 0
highest_gc_id = ''
i = 1
n = len(a)

while i < n:
    dna_string = dna_strings[i]
    id = dna_string[:13]
    dna_string = dna_string[14:].strip('\n')
    gc = (dna_string.count('G') + dna_string.count('C')) / float(len(dna_string)) * 100
    if gc > highest_gc:
        highest_gc = gc
        highest_gc_id = id
    i += 1

answer = '%s\n%s' % (highest_gc_id, highest_gc)

with open('05_gc.txt', 'w') as f:
    f.write(answer)
