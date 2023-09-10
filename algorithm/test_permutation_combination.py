import math
from itertools import combinations, permutations

# permutation
# nPr = n! / (n-r)!
# 5P2 = 5! / (5-2)! = 5! / 3! = 5 * 4 = 20
assert len(list(permutations(range(5), 2))) == 20 == math.perm(5, 2)
assert list(permutations(range(3), 2)) == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# combination
# nCr = n! / (n-r)! / r!
# 5C2 = 5! / (5-2)! / 2! = 5! / 3! / 2! = 5 * 4 / 2 = 10
assert len(list(combinations(range(5), 2))) == 10 == math.comb(5, 2)
assert list(combinations(range(3), 2)) == [(0, 1), (0, 2), (1, 2)]
