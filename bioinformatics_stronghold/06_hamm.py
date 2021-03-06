#!/usr/bin/python

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

with open('rosalind_hamm.txt') as f:
    args = f.read()

args = args.split("\n")
s = args[0]
t = args[1]
i = 0
n = len(s)
answer = 0

while i < n:
    if s[i] != t[i]:
        answer += 1
    i += 1

with open('06_hamm.txt', 'w') as f:
    f.write(str(answer))
