import re
from itertools import permutations


def clean_name(n):
    return re.sub("[\W_]+", '', n).lower()


def is_palindrome(n):
    return n == n[::-1]


Dwarves = ["Gimli", "Fili", "Ilif", "Ilmig", "Mark"]
dwarves = [clean_name(d) for d in Dwarves]

for d in dwarves:
    if dwarves.count(d) != 1:
        raise Exception('Duplicate name not supported: '+d)

for i in range(1, len(dwarves)+1):
    for sequence in permutations(dwarves, i):
        if is_palindrome("".join(sequence)):
            print " ".join([Dwarves[dwarves.index(d)] for d in sequence])

