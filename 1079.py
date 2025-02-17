"""
1079. Letter Tile Possibilities

Example 1:
Input: tiles = "AAB"
Output: 8

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1
"""
import math
from itertools import permutations

from numpy.random import permutation


# =========== SOLUTION =========== #

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        for i in range(1, len(tiles) + 1):
            ans += len(set(permutations(tiles, i)))

        return ans


# =========== TEST =========== #

solution = Solution()
print(solution.numTilePossibilities("AAB"))