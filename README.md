# HMH palendromes example
PROBLEM:

Five Dwarves (Gimli Fili Ilif Ilmig and Mark) met at the Prancing Pony and played a word game to determine which combinations of their names resulted in a palindrome. Write a program that prints out all of those combinations.

SOLUTION:

This code cleans input names. Then checks all permutations for palindromes. Duplicate names are not supported they cause repeated answers and are beyond the scope of the problem. To improve performance the permutation order can be rearanged so that the code can detect groups of wrong palendromes faster by testing first and last letters. However, performance may be out of scope for this small problem.
