import re
from itertools import permutations


def clean_name(n):
    return re.sub("[\W_]+", '', n).lower()


def is_palindrome(n):
    return n == n[::-1]


Dwarves = ["Gimli", "Fili", "Ilif", "Ilmig", "Mark"]
dwarves = [clean_name(d) for d in Dwarves]  # clean input

for d in dwarves:  # check input
    if dwarves.count(d) != 1:
        raise Exception('Duplicate name not supported: '+d)

for i in range(1, len(dwarves)+1):  # all lengths
    for sequence in permutations(dwarves, i):  # all orders
        if is_palindrome("".join(sequence)):
            print " ".join([Dwarves[dwarves.index(d)] for d in sequence])

