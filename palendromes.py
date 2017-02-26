import re
from itertools import permutations


def clean_name(n):
    return re.sub("[\W_]+", '', n).lower()


def is_palindrome(n):
    return n == n[::-1]


Dwarfs = ["Gimli", "Fili", "Ilif", "Ilmig", "Mark"]
dwarfs = [clean_name(d) for d in Dwarfs]

for d in dwarfs:
    if dwarfs.count(d) != 1:
        raise Exception('Duplicate name not supported: '+d)

for i in range(1, len(dwarfs)+1):
    for sequence in permutations(dwarfs, i):
        if is_palindrome("".join(sequence)):
            print " ".join([Dwarfs[dwarfs.index(d)] for d in sequence])
